import grpc
import test_pb2
import test_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')  # Подключение к серверу
    stub = test_pb2_grpc.TestServiceStub(channel)

    # Пример вызова метода generate
    request = test_pb2.GenerateRequest(
        id=1,
        capibara_format='example_format',
        capibara_slang='example_slang',
        capibara_phrases=['phrase1', 'phrase2', 'phrase1']
    )
    response = stub.generate(request)
    print("generate response:", response)

    # Пример вызова метода statement
    statement_request = test_pb2.StatementRequest(id=1)
    statement_response = stub.statement(statement_request)
    print("statement response:", statement_response)

    # Пример вызова метода statementSlang
    statement_slang_request = test_pb2.StatementSlangRequest(capibara_slang='example_slang')
    statement_slang_response = stub.statementSlang(statement_slang_request)
    print("statementSlang response:", statement_slang_response)

if __name__ == '__main__':
    run()