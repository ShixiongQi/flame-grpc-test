# Basic gRPC in Python

Contains a minimal working example for rolling gRPC in Python.

## Quickstart

```shell
git clone https://github.com/ShixiongQi/flame-grpc-test
cd basic-grpc-python
pip3 install -r requirements.txt
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
python3 server.py
python3 client.py
```

## File reference
```
basic-grpc-python/
├── calculator.py          # module containing a function
|
├── calculator.proto       # protobuf definition file
|
├── calculator_pb2_grpc.py # generated class for server/client
├── calculator_pb2.py      # generated class for message
|
├── server.py              # a server to expose the function
└── client.py              # a sample client
```
