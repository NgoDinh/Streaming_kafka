import faust
import asyncio

app = faust.App("hello-world-faust", broker="kafka://localhost")
topic = app.topic("udacity.ex.topic_faust")

@app.agent(topic)
async def clickevent(events):
    async for mess in events:
        print(mess)


if __name__ == "__main__":
    asyncio.run(app.main())
    # app.main()
    