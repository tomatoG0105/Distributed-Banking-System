
import grpc
import LogicalClock_pb2
import LogicalClock_pb2_grpc
from Event import Event
from event_logger import log_event

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = {'id': id, 'type': 'customer', 'events':[]}
        # pointer for the stub
        self.stub = None
        # initial logical clock
        self.clock = 0
        # initial events which can be stored to Event

    def createStub(self):
        # Create a gRPC channel to connect to the Bank (Branch) server
        hostId = 50000 + self.id
        channel = grpc.insecure_channel(f'localhost:{hostId}')
        # Create a gRPC stub for the Bank (Branch) service
        self.stub = LogicalClock_pb2_grpc.LogicalClockStub(channel)

    def executeEvents(self):
        if self.stub is not None:
            for event in self.events:
                self.clock += 1
                # Create a gRPC request message
                request = LogicalClock_pb2.Request(
                    sender_id = self.id,
                    type = 'customer',
                    customer_request_id = event['id'],
                    interface = event['interface'],
                    money = event['money'],
                    clock = self.clock
                )
                # Send the request to branch
                response = self.stub.MsgDelivery(request)
                # Append the message to customer
                self.recvMsg['events'].append({"customer-request-id": request.customer_request_id,
                                               "logical_clock": request.clock,
                                               "interface": request.interface,
                                               "comment": "event_sent from " + request.type + " " + str(request.sender_id)})
                event = Event(self.id, request.customer_request_id, request.type, request.clock,
                              request.interface, "event_sent from " + request.type + " " + str(request.sender_id))
                log_event(event.to_dict())
