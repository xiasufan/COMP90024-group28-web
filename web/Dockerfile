FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
 
RUN mkdir -p /app/cccweb
 
WORKDIR /app/cccweb
 
ADD . /app/cccweb

RUN pip install -r requirements.txt --proxy=http://wwwproxy.unimelb.edu.au:8000/