
from dataclasses import asdict, dataclass
import random
import faust

# create two class: one for raw data and another to transformed data
@dataclass
class users(faust.Record):
    user_id: int
    user_name: str
    user_address: str
    platform: str
    signup_at:str
    score: int = 0


@dataclass
class usersSerialization(faust.Record):
    user_name: str
    platform:str
    score: int

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

# add processor
def add_score(user):
    user.score = random.randint(1, 100)
    return user

# for each user get from user topic will be filter out and just get user name and signup at then send it to another topic
@app.agent(users_topic)
async def clickevent(uss):
    # add a processor to add one more column here
    uss.add_processor(add_score)
    async for us in uss.filter(lambda x: x.platform != 'Mobile'):
        # can add filter here
        # uss.filter(lambda x: x.attribute condition):
        sanitized = usersSerialization(
            user_name=us.user_name,
            platform=us.platform,
            score=us.score
        )
        await ser_user_topic.send(key=sanitized.user_name, value=sanitized)

if __name__ == "__main__":
    app.main()