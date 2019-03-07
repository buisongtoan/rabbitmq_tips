"""
**
** Author: Toan Bui <buisongtoan@outlook.com>
**
** Version: 1.1 Last update: 2019-03-01 18:00
"""
import requests
import json
import pprint
import argparse


def call_rabbitmq_api(host, port, path, user, passwd):
    url = 'http://%s:%s/%s' % (host, port, path)
    r = requests.get(url, auth=(user, passwd))
    return r


def get_queue_name(queues):
    r = []
    for queue in queues:
        if 'name' in queue:
            r.append(queue["name"])
    return r


def check_synchronised_slave_nodes(queues):
    count = 0
    for queue in queues:
        if 'synchronised_slave_nodes' in queue:
            if len(queue['synchronised_slave_nodes']) == 0:
                count += 1
    return count


def check_partitions(nodes):
    """If count > 0 => cluster is partition"""
    count = 0
    for node in nodes:
        if 'partitions' in node:
            if len(node['partitions']) > 0:
                count += 1
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='vcdn monitor tools')
    parser.add_argument('-u', '--user', required=True,
                        action='store',
                        help='rabbitmq user')
    parser.add_argument('-p', '--password', required=True,
                        action='store',
                        help='rabbitmq user')
    parser.add_argument('-H', '--host', required=True,
                        action='store',
                        help='rabbitmq host')
    parser.add_argument('-P', '--port', required=True,
                        action='store',
                        help='rabbitmq port')
    parser.add_argument('--check_partition', required=False,
                        action='store_true',
                        help='check rabbitmq cluster network partition')
    parser.add_argument('--check_synchronnised_slave_node', required=False,
                        action='store_true',
                        help='check rabbitmq HA synchronnised slave node')

    args = parser.parse_args()
    if args.check_partition:
        uri = 'api/nodes'
        res = call_rabbitmq_api(args.host, args.port, uri, args.user, args.password)
        # pprint.pprint(res.json())
        if check_partitions(res.json()):  # network parttion
            print(1)
        else:
            print(0)
    if args.check_synchronnised_slave_node:
        uri = 'api/queues'
        res = call_rabbitmq_api(args.host, args.port, uri, args.user, args.password)
        if check_synchronised_slave_nodes(res.json()):  # not synchronnised slave node
            print(1)
        else:
            print(0)
