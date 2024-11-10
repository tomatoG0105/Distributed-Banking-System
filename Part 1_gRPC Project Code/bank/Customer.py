import grpc
import bankService_pb2
import bankService_pb2_grpc
import time
import json
import threading

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = {"id": id, "recv": []}
        # pointer for the stub
        self.stub = None

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        # Create a gRPC channel to connect to the Bank (Branch) server
        hostId = 50000 + self.id
        channel = grpc.insecure_channel(f'localhost:{hostId}')
        # Create a gRPC stub for the Bank (Branch) service
        self.stub = bankService_pb2_grpc.BankServiceStub(channel)

    # TODO: students are expected to send out the events to the Bank
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
                # Send the request to the Bank (Branch) server and get the response
                response = self.stub.MsgDelivery(request)
                if event['interface'] != 'query':
                    self.recvMsg["recv"].append({"interface": event['interface'], "result": response.message})
                else:
                    self.recvMsg["recv"].append({"interface": "query", "balance": int(response.message)})



