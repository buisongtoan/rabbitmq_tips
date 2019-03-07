# rabbitmq_tips


### Monitoring

```
$python3 rabbitmq_api.py -u <RABBIT-USER> -p <RABBIT-PASSWORD> -H <MANAGEMENT-HOST> -P <MANAGEMENT-PORT> --check_partition
$python3 rabbitmq_api.py -u <RABBIT-USER> -p <RABBIT-PASSWORD> -H <MANAGEMENT-HOST> -P <MANAGEMENT-PORT> --check_synchronnised_slave_node
$python3 rabbitmq_api.py --help
```