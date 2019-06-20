FROM python:alpine3.7

COPY main.py pynado.py requirements.txt /

WORKDIR /

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]