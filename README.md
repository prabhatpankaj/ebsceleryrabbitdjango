#Setting up RabbitMQ
Although there are various choices for messaging broker with two most popular being Redis and rabbitMQ,  rabbitMQ works best with celery. You can read more about brokers (http://docs.celeryproject.org/en/latest/getting-started/brokers/ )

Install rabbitmq using the following command
```
sudo apt-get install rabbitmq-server
```

Once the installation is complete, create user, add a virtual host and set desired permissions.
```
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

celery -A mysite beat -l info

```
