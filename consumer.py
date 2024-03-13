import pika
import time
import random
def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f" [x] {body}: {processing_time}s")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f" [x] Done processing")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()