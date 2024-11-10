import grpc
import bankService_pb2
import bankService_pb2_grpc

class Branch(bankService_pb2_grpc.BankServiceServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = []
        # a list of received messages used for debugging purpose
        self.recvMsg = []
        # a list to store all write events
        self.writeSet = []
        # Initialize the write ID counter
        self.write_id_counter = 0


        # Iterate the processID of the branches
        for branch_id in branches:
            if branch_id != self.id:
                # Create a gRPC channel to the branch
                hostId = 50000 + branch_id
                channel = grpc.insecure_channel(f'localhost:{hostId}')
                # Create a stub for communication with the branch
                stub = bankService_pb2_grpc.BankServiceStub(channel)
                self.stubList.append(stub)

    # Generate a unique write ID
    def generate_write_id(self):
        self.write_id_counter += 1
        return self.write_id_counter % 2147483647  # Ensuring it doesn't exceed int32 range

    def updateWriteSet(self, write_set):
        # Update the branch's WriteSet with new write IDs
        self.writeSet = list(set(self.writeSet).union(set(write_set)))

    def checkWriteSet(self, customer_write_set):
        # Check if all customer's writes are reflected in the branch's WriteSet
        return all(item in self.writeSet for item in customer_write_set)

    def Query(self):
        response = bankService_pb2.ResponseMessage()
        response.success = True
        response.message = str(self.balance)
        return response

    def Withdraw(self, request, context):
        # Update and check WriteSet before processing
        self.updateWriteSet(request.write_set)
        if not self.checkWriteSet(request.write_set):
            return bankService_pb2.ResponseMessage(success=False, message="Write operations not yet propagated")

        response = bankService_pb2.ResponseMessage()
        response.write_id = self.generate_write_id() # Function to generate a unique write ID
        if self.balance >= request.amount:
            self.balance -= request.amount
            response.success = True
            response.message = "success"
        else:
            response.success = False
        return response

    def Deposit(self, request, context):
        # Update and check WriteSet before processing
        self.updateWriteSet(request.write_set)
        if not self.checkWriteSet(request.write_set):
            return bankService_pb2.ResponseMessage(success=False, message="Write operations not yet propagated")

        response = bankService_pb2.ResponseMessage()
        response.write_id = self.generate_write_id() # Function to generate a unique write ID
        self.balance += request.amount
        response.success = True
        response.message = "success"
        return response

    def Propagate_Withdraw(self, request, context):
        for stub in self.stubList:
            if stub != self.id:
                try:
                    response = stub.Withdraw(request, timeout = 10.0)
                except grpc.RpcError as e:
                    print("RPC error in branches propagations.", e.details())

    def Propagate_Deposit(self, request, context):
        for stub in self.stubList:
            if stub != self.id:
                try:
                    response = stub.Deposit(request, timeout = 10.0)
                except grpc.RpcError as e:
                    print("RPC error in branches propagations.", e.details())

    def MsgDelivery(self,request, context):
        # Implement the logic for MsgDelivery to process requests from clients
        # For example, update the balance based on client requests and return a response
        response = bankService_pb2.ResponseMessage()
        if request.event == "deposit":
            response = self.Deposit(request,context)
            self.Propagate_Deposit(request,context)
        elif request.event == "withdraw":
            response = self.Withdraw(request,context)
            self.Propagate_Withdraw(request,context)
        elif request.event == "query":
            response = self.Query()
        else:
            response.success = False
            response.message = "Invalid event."
        self.recvMsg.append(response.message)
        return response









