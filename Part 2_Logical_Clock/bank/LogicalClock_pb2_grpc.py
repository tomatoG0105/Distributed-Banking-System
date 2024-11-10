# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import LogicalClock_pb2 as LogicalClock__pb2


class LogicalClockStub(object):
    """The bank service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MsgDelivery = channel.unary_unary(
                '/LogicalClock.LogicalClock/MsgDelivery',
                request_serializer=LogicalClock__pb2.Request.SerializeToString,
                response_deserializer=LogicalClock__pb2.Response.FromString,
                )
        self.RecvRequest = channel.unary_unary(
                '/LogicalClock.LogicalClock/RecvRequest',
                request_serializer=LogicalClock__pb2.Request.SerializeToString,
                response_deserializer=LogicalClock__pb2.Response.FromString,
                )
        self.PropagateToBranches = channel.unary_unary(
                '/LogicalClock.LogicalClock/PropagateToBranches',
                request_serializer=LogicalClock__pb2.Request.SerializeToString,
                response_deserializer=LogicalClock__pb2.Response.FromString,
                )


class LogicalClockServicer(object):
    """The bank service definition.
    """

    def MsgDelivery(self, request, context):
        """Method to send a request from customer to branch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecvRequest(self, request, context):
        """Method to receive the request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateToBranches(self, request, context):
        """Method to propagate the request to other branches
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogicalClockServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=LogicalClock__pb2.Request.FromString,
                    response_serializer=LogicalClock__pb2.Response.SerializeToString,
            ),
            'RecvRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.RecvRequest,
                    request_deserializer=LogicalClock__pb2.Request.FromString,
                    response_serializer=LogicalClock__pb2.Response.SerializeToString,
            ),
            'PropagateToBranches': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateToBranches,
                    request_deserializer=LogicalClock__pb2.Request.FromString,
                    response_serializer=LogicalClock__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LogicalClock.LogicalClock', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LogicalClock(object):
    """The bank service definition.
    """

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LogicalClock.LogicalClock/MsgDelivery',
            LogicalClock__pb2.Request.SerializeToString,
            LogicalClock__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecvRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LogicalClock.LogicalClock/RecvRequest',
            LogicalClock__pb2.Request.SerializeToString,
            LogicalClock__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateToBranches(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LogicalClock.LogicalClock/PropagateToBranches',
            LogicalClock__pb2.Request.SerializeToString,
            LogicalClock__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
