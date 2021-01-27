import pika, json, django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product


rabbit_mq = os.environ.get('AMQ_URL')
params = pika.URLParameters(rabbit_mq)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id_t = json.loads(body)
    print(id_t)
    product = Product.objects.get(id=id_t)
    print(product)
    product.likes = product.likes + 1
    product.save()
    print('Product likes saved!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()