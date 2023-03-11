import grpc
import argparse

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', action='store', type=str, default='localhost')
parser.add_argument('-p', '--port', action='store', type=str, default='50051')
parser.add_argument('-u', '--url', action='store', type=str)
args = parser.parse_args()

aggregator_url = 'http://flame-aggregator.flame.example.com'

# open a gRPC channel
if args.url == '':
	print("Creating gRPC channel without options")
	channel = grpc.insecure_channel(f'{args.ip}:{args.port}')
else:
	print(f"Creating gRPC channel with customized authority header: {aggregator_url}")
	channel = grpc.insecure_channel(f'{args.ip}:{args.port}', options=[(('grpc.default_authority', aggregator_url))])

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)