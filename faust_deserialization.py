from dataclasses import asdict, dataclass
import json
import faust

#define schema of mess
@dataclass
class users(faust.Record):
    user_id: int
    user_name: str
    user_address: str
    platform: str
    signup_at:str

app = faust.App("sample2", broker="kafka://localhost:9092") #setup app
users_topic = app.topic(#set up topic
    "udacity.ex.topic_faust",
    key_type=str,
    value_type=users, #schema had been push here.
)

@app.agent(users_topic) #decorater a function with app.agent
async def clickevent(us):
    async for ce in us:
        print(json.dumps(asdict(ce), indent=2))


if __name__ == "__main__":
    app.main()