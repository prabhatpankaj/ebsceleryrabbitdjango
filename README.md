#Setting up RabbitMQ in ubuntu 16.04
Although there are various choices for messaging broker with two most popular being Redis and rabbitMQ,  rabbitMQ works best with celery. You can read more about brokers (http://docs.celeryproject.org/en/latest/getting-started/brokers/ )

Install rabbitmq using the following command
```
sudo apt-get install rabbitmq-server
```

Once the installation is complete, create user, add a virtual host and set desired permissions.
```
sudo rabbitmq-server
sudo rabbitmqctl add_user myuser mypassword
sudo rabbitmqctl add_vhost myvhost
sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
```
Now start the rabbitmq-server using this command
```
sudo rabbitmq-server
```
To run it in background, use the detached flag
```
sudo rabbitmq-server -detached

```
Now run this in your manage.py directry using virtualenvinonment 
```
celery -A celerydjango worker -l info

celery -A celerydjango beat -l info

```
# for setting up django project on ubuntu replace os.environ[] value to actual value . 
# for setting up django project in elasticbeanstalk update these values to Software Configuration. 

```
'NAME': os.environ['RDS_DB_NAME'],
'USER': os.environ['RDS_USERNAME'],
'PASSWORD': os.environ['RDS_PASSWORD'],
'HOST': os.environ['RDS_HOSTNAME'],
'PORT': os.environ['RDS_PORT'],
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

```
