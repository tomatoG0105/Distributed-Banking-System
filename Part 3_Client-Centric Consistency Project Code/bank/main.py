from Customer import Customer
from Branch import Branch
import json
import grpc
import bankService_pb2
import bankService_pb2_grpc
from concurrent import futures


if __name__ == "__main__":
    def execution(file):
        balanceSheet = {}
        customerList = []
        branch_servers = []
        branches = []

        with open(file, 'r') as file:
            customer_data = json.load(file)

        # Initialize branches
        for data in customer_data:
            if data['type'] == 'branch':
                balanceSheet[data['id']] = data['balance']
                branches.append(data['id'])

        # Start branch servers
        for data in customer_data:
            if data['type'] == 'branch':
                server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
                branch = Branch(data['id'], balanceSheet[data['id']], branches)
                bankService_pb2_grpc.add_BankServiceServicer_to_server(branch, server)
                hostId = 50000 + data['id']
                server.add_insecure_port(f'localhost:{hostId}')
                server.start()
                branch_servers.append(server)

        for data in customer_data:
            if data['type'] == 'customer':
                customer_id = data['id']
                customer = Customer(customer_id, data['events'])
                customer.createStub()
                customerList.append(customer)

        for customer in customerList:
            customer.executeEvents()

        for server in branch_servers:
            server.stop(0)

        for customer in customerList:
            print(customer.recvMsg)

    # Execute Monotonic Write input:
    print('Monotonic Write Output:')
    execution('mono_input.json')

    # Execute Read Your Write input:
    print('Read Your Write Output:')
    execution('read_your_write_input.json')