import grpc
import LogicalClock_pb2
import LogicalClock_pb2_grpc
import logging
from Event import Event
from event_logger import log_event


class Branch(LogicalClock_pb2_grpc.LogicalClockServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the dictionary of Client stubs to communicate with the branches, with their associated branch id as keys
        self.stubList = {}
        # a list of received messages used for debugging purpose
        self.recvMsg = {'id': id, 'type': 'branch', 'events':[]}
        # initial logical clock
        self.clock = 0
        # initial events which can be stored to Event


        # iterate the processID of the branches
        for branch_id in branches:
            if branch_id != self.id:
                # Create a gRPC channel to the branch
                hostId = 50000 + branch_id
                channel = grpc.insecure_channel(f'localhost:{hostId}')
                # Create a stub for communication with the branch
                stub = LogicalClock_pb2_grpc.LogicalClockStub(channel)
                self.stubList[branch_id] = stub

    def RecvRequest(self, request,context):
        # Update logical clock based on the received request
        self.clock = max(self.clock, request.clock) + 1
        response = LogicalClock_pb2.Response()
        # Update the request clock stamp to match the current local clock of the branch
        request.clock = self.clock
        # Update request type to be branch
        request.type = 'branch'
        self.recvMsg['events'].append({"customer-request-id": request.customer_request_id,
                                       "logical_clock": request.clock,
                                   "interface": request.interface,
                                    "comment": "event_recv from " + request.type + " " + str(request.sender_id)})
        event = Event(self.id, request.customer_request_id, request.type, request.clock, request.interface,
                      "event_recv from " + request.type + " " + str(request.sender_id))
        log_event(event.to_dict())
        return response

    # Propagate the message to all the other branches
    def PropagateToBranches(self, request, context):
        response = LogicalClock_pb2.Response()
        # Update the request interface to be 'propogate_'+Request.interface
        request.interface = 'propogate_' + request.interface
        for branch_id, stub in self.stubList.items():
            # Increment logical clock before propagating
            self.clock += 1
            # Update the request clock
            request.clock = self.clock
            # Update the request sender to be the current branch
            request.sender_id = self.id
            # Update the request type to be 'branch'
            request.type = 'branch'
            # Propagate the request to all other branches
            try:
                stub.RecvRequest(request)
            except grpc.RpcError as e:
                logging.error(f'gRPC error: {e}')
            self.recvMsg['events'].append({"customer-request-id": request.customer_request_id,
                                           "logical_clock": request.clock,
                                           "interface": request.interface,
                                           "comment": "event_sent to " + request.type + " " + str(branch_id)})
            event = Event(self.id, request.customer_request_id, request.type, request.clock,
                          request.interface, "event_sent to " + request.type + " " + str(branch_id))
            log_event(event.to_dict())

        return response

    def MsgDelivery(self,request, context):
        response = self.RecvRequest(request, context)
        self.PropagateToBranches(request, context)
        return response

