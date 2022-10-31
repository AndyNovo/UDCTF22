FROM ubuntu:20.04
RUN apt-get update && apt-get -y install socat python
COPY future.py .
EXPOSE 34345
CMD socat TCP-LISTEN:34345,reuseaddr,fork EXEC:"python -u future.py"
