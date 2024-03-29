import pika
import uuid

def on_message_received(ch, method, properties, body):
    print(f"Message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

reply_queue = channel.queue_declare(queue='', exclusive=True)
channel.basic_consume(queue=reply_queue.method.queue, on_message_callback=on_message_received, auto_ack=True)

channel.queue_declare(queue='request-queue')

message = 'can I reaquest a reply?'
cor_id = str(uuid.uuid4())
print(f"Sending resquest: {cor_id}")
channel.basic_publish(exchange='', routing_key='request-queue',
                      properties=pika.BasicProperties(
                          reply_to=reply_queue.method.queue,
                            correlation_id=cor_id),
                        body=message)

print("Starting Client")
channel.start_consuming()