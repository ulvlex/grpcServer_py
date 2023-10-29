# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.generate = channel.unary_unary(
                '/test.TestService/generate',
                request_serializer=test__pb2.GenerateRequest.SerializeToString,
                response_deserializer=test__pb2.GenerateResponse.FromString,
                )
        self.statement = channel.unary_unary(
                '/test.TestService/statement',
                request_serializer=test__pb2.StatementRequest.SerializeToString,
                response_deserializer=test__pb2.StatementResponse.FromString,
                )
        self.statementSlang = channel.unary_unary(
                '/test.TestService/statementSlang',
                request_serializer=test__pb2.StatementSlangRequest.SerializeToString,
                response_deserializer=test__pb2.StatementSlangResponse.FromString,
                )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def statement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def statementSlang(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'generate': grpc.unary_unary_rpc_method_handler(
                    servicer.generate,
                    request_deserializer=test__pb2.GenerateRequest.FromString,
                    response_serializer=test__pb2.GenerateResponse.SerializeToString,
            ),
            'statement': grpc.unary_unary_rpc_method_handler(
                    servicer.statement,
                    request_deserializer=test__pb2.StatementRequest.FromString,
                    response_serializer=test__pb2.StatementResponse.SerializeToString,
            ),
            'statementSlang': grpc.unary_unary_rpc_method_handler(
                    servicer.statementSlang,
                    request_deserializer=test__pb2.StatementSlangRequest.FromString,
                    response_serializer=test__pb2.StatementSlangResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.TestService/generate',
            test__pb2.GenerateRequest.SerializeToString,
            test__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def statement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.TestService/statement',
            test__pb2.StatementRequest.SerializeToString,
            test__pb2.StatementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def statementSlang(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.TestService/statementSlang',
            test__pb2.StatementSlangRequest.SerializeToString,
            test__pb2.StatementSlangResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
