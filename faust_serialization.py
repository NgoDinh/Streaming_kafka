
from dataclasses import asdict, dataclass
import json
import faust

# create two class: one for raw data and another to transformed data
@dataclass
class users(faust.Record):
    user_id: int
    user_name: str
    user_address: str
    platform: str
    signup_at:str


@dataclass
class usersSerialization(faust.Record):
    user_name: str
    signup_at:str

# create two topic for get and push transformed data
app = faust.App("sample3", broker="kafka://localhost:9092") #setup app
users_topic = app.topic(#set up topic
    "udacity.ex.topic_faust",
    key_type=str,
    value_type=users, #schema had been push here.
)

ser_user_topic = app.topic(
    "udacity.ex.topic_faust_ser",
    key_type=str,
    value_type=usersSerialization,
)
# for each user get from user topic will be filter out and just get user name and signup at then send it to another topic
@app.agent(users_topic)
async def clickevent(uss):
    async for us in uss:
        sanitized = usersSerialization(
            user_name=us.user_name,
            signup_at=us.signup_at
        )
        await ser_user_topic.send(key=sanitized.user_name, value=sanitized)

if __name__ == "__main__":
    app.main()