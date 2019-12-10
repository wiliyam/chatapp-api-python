#use grpc install pyton
FROM python:3.7

RUN python -m pip install --upgrade pip

RUN python -m pip install grpcio

RUN python -m pip install grpcio-tools

# RUN mkdir /chatapp

WORKDIR chatapp

# ARG gitpassword

# RUN git clone https://github.com/wiliyam/chatapp-api-python.git/.

# RUN git pull

CMD ["python","-u","server.py"]

