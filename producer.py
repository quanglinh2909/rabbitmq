import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='my_topic_exchange', exchange_type=ExchangeType.topic)

message_payments_service = "Payment service: Payment has been processed"
channel.basic_publish(exchange='my_topic_exchange', routing_key='user.europe.payments', body=message_payments_service)
print(f" [x] Sent {message_payments_service}")

business_order_message = "Business order: Order has been processed"
channel.basic_publish(exchange='my_topic_exchange', routing_key='business.europe.order', body=business_order_message)
print(f" [x] Sent {business_order_message}")

connection.close()