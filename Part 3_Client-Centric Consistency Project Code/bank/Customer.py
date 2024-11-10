import grpc
import bankService_pb2
import bankService_pb2_grpc

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = {"id": id, "balance": []}
        # pointer for the stub
        self.stub = None
        # Initialize the write set
        self.writeSet = []

    # Create the Customer stub
    def createStub(self):
        # Create a gRPC channel to connect to the Bank (Branch) server
        hostId = 50000 + self.id
        channel = grpc.insecure_channel(f'localhost:{hostId}')
        # Create a gRPC stub for the Bank (Branch) service
        self.stub = bankService_pb2_grpc.BankServiceStub(channel)

    def addWriteSet(self, write_id):
        # Add a new write ID to the write set
        if write_id not in self.writeSet:
            self.writeSet.append(write_id)

    # Send out the events to the Bank
    def executeEvents(self):
        if self.stub is not None:
            for event in self.events:
                # print(f"Customer {self.id} - Sending event: {event}")
                # Create a gRPC request message
                if event['interface'] != 'query':
                    request = bankService_pb2.CustomerRequest(
                        customer_id = int(self.id),
                        event = str(event['interface']),
                        amount = int(event['money'])
                    )
                else:
                    request = bankService_pb2.CustomerRequest(
                        customer_id = self.id,
                        event = event['interface'],
                        amount = 0
                    )
                # Include the write set in the request
                request.write_set.extend(self.writeSet)

                # Send the request to the Bank (Branch) server and get the response
                response = self.stub.MsgDelivery(request)
                if response.success and hasattr(response, 'write_id'):
                    self.addWriteSet(response.write_id)  # Update write set only for successful operations

                if event['interface'] == 'query':
                    self.recvMsg["balance"] = int(response.message)




