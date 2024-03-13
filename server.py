import pika
import uuid

def on_message_received(ch, method, properties, body):
    print(f"Message: {properties.correlation_id} - {body }")
    ch.basic_publish(exchange='', routing_key=properties.reply_to,
                     body=f"Reply to {properties.correlation_id}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

reply_queue = channel.queue_declare(queue='request-queue')
channel.basic_consume(queue="request-queue", on_message_callback=on_message_received, auto_ack=True)

channel.queue_declare(queue='request-queue')


print("Starting Server")
channel.start_consuming()