import pika, json
import os


rabbit_mq = os.environ.get('AMQ_URL')
params = pika.URLParameters(rabbit_mq)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)