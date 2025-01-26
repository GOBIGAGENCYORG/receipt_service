import pika
import pydantic
import json

from settings import settings
from logger import LoggingProvider


class QueueManager(LoggingProvider):
    def __init__(self):
        super().__init__()
        self.debug("Initialization starts")
        self._rabbitmq_host = settings.rabbitmq_host
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.rabbitmq_host)
        )
        self.debug("Initialized")

    def _declare_queue(
        self, channel: pika.adapters.blocking_connection.BlockingChannel, queue: str
    ):
        self.debug(f"Initializing queue {queue}")
        channel.queue_declare(queue=queue)

    def send(self, queue: str, data_object: pydantic.BaseModel):
        self.debug(f"Sending message")
        channel = self._connection.channel()
        self._declare_queue(channel, queue)
        channel.basic_publish(
            exchange="", routing_key=queue, body=json.dumps(data_object.model_dump())
        )
        channel.close()
        self.debug("Message sent")

    def start_consume(self, queue: str, callback: callable):
        self.debug(f"Start consuming messages from queue {queue}")
        channel = self._connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=False)
        channel.start_consuming()
        self._connection.close()

    def close(self):
        self.debug("Closing QueueManager")
        self._connection.close
