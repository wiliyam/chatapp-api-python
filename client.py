import grpc

from message import message_pb2,message_pb2_grpc
import random

SERVER_ADDRESS = '13.233.6.179'
PORT = 50051

def generate_messages():
        msg=message_pb2.Chatmessage(
        message="hello from client1",
        type=1,
        data=bytes(0),
        lat=12.971599,
        long=77.594566,
        chat_id ="mainchatid",
        source_id="client1sourceid",
        destination_id="serverid",
        source_device_id="client1 device id",
        source_device_time="client1time",
        source_device_os="macos1",
        source_device_os_version="12.0"
        )
        return msg

def messageChat(stub):
        # msg=message_pb2.Chatmessage(
        # message="hello from client1",
        # type=1,
        # data=bytes(0),
        # lat=12.971599,
        # long=77.594566,
        # chat_id="mainchatid",
        # source_id="client1sourceid",
        # destination_id="serverid",
        # source_device_id="client1 device id",
        # source_device_time="client1time",
        # source_device_os="macos1",
        # source_device_os_version="12.0"
        # )
        random.seed(5)
        topic=random.randint(100, 999)
        msg=input("typing...topic={}\n".format(topic))
        message=message_pb2.Chatmessage(message=msg,
        type=0,id=topic)
        responses = stub.messageChat(message)
        
        print("response=>",responses)

        # return msg
       


def run():

#     ca_cert = 'server.crt'
#     root_certs = open(ca_cert).read()
# #     print(root_certs)
#     credentials = grpc.ssl_channel_credentials(bytes(root_certs,'utf-8'))
    #create secure channle
    channel = grpc.insecure_channel('{}:{}'.format(SERVER_ADDRESS,PORT))
    stub = message_pb2_grpc.chatStub(channel)
    print("===sending message===>>")
    messageChat(stub)

#     with grpc.insecure_channel('localhost:50051') as channel:
#         print("channel==>",channel)
#         stub = message_pb2_grpc.chatStub(channel)
#         print("===sending message===>>")
#         messageChat(stub)



if __name__ == '__main__':
#     logging.basicConfig()
    run()