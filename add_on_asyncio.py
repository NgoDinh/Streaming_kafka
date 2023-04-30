import asyncio
import time
import datetime

# async def hello():
#     print('Hello ...')
#     await asyncio.sleep(2)
#     print('... World!')

# async def main():
#     start_time = datetime.datetime.utcnow()
#     await asyncio.gather(hello(), hello())
#     print((datetime.datetime.utcnow()-start_time).microseconds)

# asyncio.run(main())

def hello():
    print('Hello ...')
    time.sleep(2)
    print('... World!')

def main():
    start_time = datetime.datetime.utcnow()
    hello()
    hello()
    print((datetime.datetime.utcnow()-start_time).microseconds)
if __name__ == '__main__':
    main()