import traceback

import grpc
from concurrent import futures
import test_pb2
import test_pb2_grpc
import psycopg2
import io
import pandas

class TestService(test_pb2_grpc.TestServiceServicer):

    HOST = "localhost"
    DATABASE = "testDB"
    USER = "postgres"
    PASSWORD = "123"
    TABLE = "data"
    def generate(self, request, context):
        print("Received generate request")
        try:
            # Извлекаем данные из Protobuf-запроса
            id = request.id
            capibara_format = request.capibara_format
            capibara_slang = request.capibara_slang
            capibara_phrases = request.capibara_phrases

            # Убираем дубликаты из capibara_phrases с помощью множества
            unique_phrases = list(set(capibara_phrases))

            # подключение к БД
            connectionDB = self.connectToDB()
            cur = connectionDB.cursor()

            # Проверяем наличие записи с данным id
            cur.execute("SELECT id, capibara_phrases FROM {} WHERE id = %s".format(self.TABLE), (id,))
            existing_record = cur.fetchone()

            if existing_record:
                # Если запись существует, обновляем все поля
                cur.execute(
                    "UPDATE {} SET capibara_format = %s, capibara_slang = %s, capibara_phrases = %s WHERE id = %s".format(self.TABLE),
                    (capibara_format, capibara_slang, unique_phrases, id)
                )
            else:
                # Если запись не существует, вставляем новую запись
                cur.execute(
                    "INSERT INTO {} (id, capibara_format, capibara_slang, capibara_phrases) VALUES (%s, %s, %s, %s)".format(self.TABLE),
                    (id, capibara_format, capibara_slang, list(unique_phrases))
                )

            connectionDB.commit()
            cur.close()
            connectionDB.close()
            response = test_pb2.GenerateResponse(success=True)
        except Exception as e:
            print(f"Error in generate method: {e}")
            response = test_pb2.GenerateResponse(success=False)

        print("Sending generate response")
        return response

    def statement(self, request, context):
        print("Received statement request")

        try:
            id = request.id

            connectionDB = self.connectToDB()

            # Выполняем запрос к базе данных для получения данных по id
            cur = connectionDB.cursor()
            cur.execute("SELECT * FROM {} WHERE id = %s".format(self.TABLE), (id,))

            # Получаем результаты запроса в виде списка кортежей
            rows = cur.fetchall()

            # Если есть записи, создаем XLSX-файл
            if rows:
                # Создаем DataFrame из результатов запроса
                df = pandas.DataFrame(rows, columns=["id", "capibara_format", "capibara_slang", "capibara_phrases"])

                # Создаем XLSX-файл
                output = io.BytesIO()
                writer = pandas.ExcelWriter(output, engine="xlsxwriter")
                df.to_excel(writer, sheet_name="Sheet1", index=False)
                writer.close()

                # Возвращаем XLSX-файл в Protobuf-ответе
                response = test_pb2.StatementResponse(status=True, file_data=output.getvalue())
            else:
                # Если записей не найдено, устанавливаем status=False
                response = test_pb2.StatementResponse(status=False, file_data=b"")

            cur.close()
            connectionDB.close()
        except Exception as e:
            print(f"Error in statement method: {e}")
            response = test_pb2.StatementResponse(status=False, file_data=b"")

        print("Sending statement response")
        return response

    def statementSlang(self, request, context):
        print("Received statementSlang request")
        try:
            capibara_slang = request.capibara_slang

            connectionDB = self.connectToDB()

            # Выполняем запрос к базе данных для получения данных
            cur = connectionDB.cursor()
            cur.execute("SELECT * FROM {} WHERE capibara_slang = %s".format(self.TABLE), (capibara_slang,))

            # Получаем результаты запроса в виде списка кортежей
            rows = cur.fetchall()

            # Если есть записи, группируем их и создаем XLSX-файл
            if rows:
                # Создаем DataFrame из результатов запроса
                df = pandas.DataFrame(rows, columns=["id", "capibara_format", "capibara_slang", "capibara_phrases"])

                # Группируем записи по capibara_slang
                grouped_data = df.groupby("capibara_slang")

                # Создаем XLSX-файл
                output = io.BytesIO()
                writer = pandas.ExcelWriter(output, engine="xlsxwriter")
                for name, group in grouped_data:
                    group.to_excel(writer, sheet_name=name, index=False)
                writer.close()

                # Возвращаем XLSX-файл в Protobuf-ответе
                response = test_pb2.StatementSlangResponse(status=True, file_data=output.getvalue())
            else:
                # Если записей не найдено, устанавливаем status=False
                response = test_pb2.StatementSlangResponse(status=False, file_data=b"")

            cur.close()
            connectionDB.close()
        except Exception as e:
            print(f"Error in statementSlang method: {e}")
            response = test_pb2.StatementSlangResponse(status=False, file_data=b"")

        print("Sending statementSlang response")
        return response

    def connectToDB(self):
        # Подключение к БД PostgreSQL
        connectionDB = psycopg2.connect(
            host= self.HOST,
            database= self.DATABASE,
            user= self.USER,
            password= self.PASSWORD
        )

        return connectionDB

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    server.add_insecure_port('[::]:50051')  # Порт для gRPC
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()