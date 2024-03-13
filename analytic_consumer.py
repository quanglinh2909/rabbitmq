import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f" [x] Analytic Service: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='analytics_only')
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='both')


channel.basic_consume(queue=queue.method.queue, on_message_callback=on_message_received, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()