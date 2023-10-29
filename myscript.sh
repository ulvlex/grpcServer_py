#!/bin/bash
python -m venv venv
venv\Scripts\activate
pip install grpcio protobuf
pip install grpcio-tools
pip install XlsxWriter
pip install psycopg2
pip install pandas
