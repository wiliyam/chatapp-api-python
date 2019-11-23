#use grpc install pyton
FROM grpc/python

RUN mkdir /chatapp

WORKDIR chatapp

ARG gitpassword

RUN git clone https://github.com/wiliyam/chatapp-api-python.git/.

RUN git pull

CMD ["python","server.py"]

