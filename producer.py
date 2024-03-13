import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
message = f"Hello World"
channel.basic_publish(exchange='routing', routing_key='analytics_only', body=message)
channel.basic_publish(exchange='routing', routing_key='both', body=message)
print(f" [x] Sent {message}")

connection.close()