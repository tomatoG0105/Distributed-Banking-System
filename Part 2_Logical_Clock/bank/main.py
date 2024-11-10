import time
from Customer import Customer
from Branch import Branch
from Event import Event
import json
import grpc
import LogicalClock_pb2
import LogicalClock_pb2_grpc
from concurrent import futures
from event_logger import events_log

if __name__ == "__main__":
    balanceSheet = {}
    customerList = []
    branch_servers = []
    branch_IDs = []
    branches = []
    requests = []

    with open('sample_input.json', 'r') as file:
        data_list = json.load(file)

    for data in data_list:
        if data['type'] == 'branch':
            balanceSheet[data['id']] = data['balance']
            branch_IDs .append(data['id'])

    for data in data_list:
        if data['type'] == 'branch':
            server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
            branch = Branch(data['id'], balanceSheet[data['id']], branch_IDs )
            branches.append(branch)
            LogicalClock_pb2_grpc.add_LogicalClockServicer_to_server(branch, server)
            hostId = 50000 + data['id']
            server.add_insecure_port(f'localhost:{hostId}')
            server.start()
            branch_servers.append(server)

    for data in data_list:
        if data['type'] == 'customer':
            customer_id = data['id']
            customer = Customer(customer_id, data['events'])
            customer.createStub()
            customerList.append(customer)

    for customer in customerList:
        customer.executeEvents()

    for server in branch_servers:
        server.stop(0)

    print('Part 1: List all the events taken place on each customer:')
    for customer in customerList:
        print(customer.recvMsg)
    print('')  # Leave a blank line after each part

    print('Part 2: List all the events taken place on each branch:')
    for branch in branches:
        print(branch.recvMsg)
    print('')  # Leave a blank line after each part

    print('Part 3: List all the events (along with their logical times) triggered by each customer Deposit/Withdraw request:')
    sorted_events = sorted(events_log, key=lambda x: (x['customer_request_id'], x['logical_clock']))
    for event in sorted_events:
        print(event)

