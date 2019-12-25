# rabbitmq_tips


### Monitoring

```
$python3 rabbitmq_api.py -u <RABBIT-USER> -p <RABBIT-PASSWORD> -H <MANAGEMENT-HOST> -P <MANAGEMENT-PORT> --check_partition
$python3 rabbitmq_api.py -u <RABBIT-USER> -p <RABBIT-PASSWORD> -H <MANAGEMENT-HOST> -P <MANAGEMENT-PORT> --check_synchronnised_slave_node
$python3 rabbitmq_api.py --help
```

### Link

##### Client lib

https://medium.com/python-pandemonium/building-robust-rabbitmq-consumers-with-python-and-kombu-part-1-ccd660d17271?

https://medium.com/python-pandemonium/building-robust-rabbitmq-consumers-with-python-and-kombu-part-2-e9505f56e12e

https://github.com/Skablam/kombu-examples

##### Summit

https://www.youtube.com/watch?v=ez9kQEhHsnc

##### Other

https://www.rabbitmq.com/resources/specs/amqp0-9-1.pdf

https://www.rabbitmq.com/heartbeats.html

https://www.rabbitmq.com/networking.html

https://www.rabbitmq.com/configure.html
