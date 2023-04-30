import asyncio
from dataclasses import dataclass, field
import json
import random
import datetime

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic
from faker import Faker

faker = Faker()

BROKER_URL = "PLAINTEXT://localhost:9092"
TOPIC_NAME = "Test"


@dataclass
class Purchase:
    username: str = field(default_factory=faker.user_name)
    currency: str = field(default_factory=faker.currency_code)
    amount: int = field(default_factory=lambda: random.randint(100, 200000))

    def serialize(self):
        """Serializes the object in JSON string format"""
        return json.dumps(
                {
                        "username": self.username,
                        "currency": self.currency,
                        "amount"  : self.amount,
                }
        )

async def produce_sync(topic_name):
    """Produces data synchronously into the Kafka Topic"""
    p = Producer({"bootstrap.servers": BROKER_URL})
    iter_count = 0
    while True:
        if iter_count < 100:
            p.produce(topic_name, Purchase().serialize())
            p.flush()
            #chage sync and async with flush: flush ~sync
            await asyncio.sleep(0.001)
        else:
            break
        iter_count += 1

def main():
    start_time = datetime.datetime.utcnow()
    asyncio.run(produce_sync(TOPIC_NAME))
    print((datetime.datetime.utcnow()-start_time).microseconds)

if __name__ == "__main__":
    main()