FROM ubuntu:20.04
RUN apt-get update && apt-get -y install python3 python3-pip socat
RUN ln -s /usr/bin/python3 /usr/bin/python & ln -sf /usr/bin/pip3 /usr/bin/pip
COPY wordleswithdads.py .
COPY jokes.txt .
COPY flag.txt .
EXPOSE 34345
CMD socat TCP-LISTEN:34345,reuseaddr,fork EXEC:"python -u wordleswithdads.py"
