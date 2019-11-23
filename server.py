from concurrent import futures
import time
import logging

import grpc

# import message.message_pb2 as message_pb2
# import message.message_pb2_grpc as message_pb2_grpc 

# from .message import message_pb2
# from message import message_pb2
import message.message_pb2 as message_pb2
import message.message_pb2_grpc as message_pb2_grpc

class chatServicer(message_pb2_grpc.chatServicer):
    """Provides methods that implement functionality of route guide server."""

    # def __init__(self):
        # self.db = {}
    def generate_messages(self):
        chatMessaage= message_pb2.Chatmessage(
        message="hello from server",
        type=1,
        data=bytes(0),
        lat=12.971599,
        long=77.594566,
        chat_id="mainchatid",
        source_id="serversourceid",
        destination_id="destinationid",
        source_device_id="server device id",
        source_device_time="servertime",
        source_device_os="macos",
        source_device_os_version="12.0"
        )
        return chatMessaage

    def messageChat(self,request,contex):
        chatMessaage= message_pb2.Chatmessage(
        message="hello from server",
        type=1,
        data=bytes(0),
        lat=12.971599,
        long=77.594566,
        chat_id="mainchatid",
        source_id="serversourceid",
        destination_id="destinationid",
        source_device_id="server device id",
        source_device_time="servertime",
        source_device_os="macos",
        source_device_os_version="12.0"
        )
        
        print("msg==>>",request)

        return chatMessaage



def serve():
    # with open('server.key', 'rb') as f:
    #     private_key = f.read()
    # with open('server.crt', 'rb') as f:
    #     certificate_chain = f.read()
    # server_credentials = grpc.insecure_channel()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_chatServicer_to_server(
        chatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server is up and wait_for_termination.............")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()