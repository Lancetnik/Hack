python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. websockets.proto

sed -i "s/import websockets_pb2/from . import websockets_pb2/" "websockets_pb2_grpc.py"