import grpc

from message import message_pb2,message_pb2_grpc

SERVER_ADDRESS = '0.0.0.0'
PORT = 8080

def generate_messages():
        msg=message_pb2.Chatmessage(
        message="hello from client2",
        type=1,
        data=bytes(0),
        lat=12.971599,
        long=77.594566,
        chat_id="mainchatid",
        source_id="client1sourceid",
        destination_id="serverid",
        source_device_id="client2 device id",
        source_device_time="client2time",
        source_device_os="macos2",
        source_device_os_version="13.0"
        )
        for _ in range(0, 10):
                chat_item=msg
                print("chat_item %s" % chat_item)
                yield chat_item

def messageChat(stub):
        responses = stub.messageChat(generate_messages())
        for response in responses:
                print("response=>",response)
       


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        print("channel==>",channel)
        stub = message_pb2_grpc.chatStub(channel)
        print("===sending message===>>")
        messageChat(stub)



if __name__ == '__main__':
#     logging.basicConfig()
    run()