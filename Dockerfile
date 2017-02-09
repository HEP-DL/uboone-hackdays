FROM kwierman/hep-dl

CMD "sh" "-c" "echo nameserver 8.8.8.8 > /etc/resolv.conf"

# Install the remaining dependencies
RUN apt-get update
RUN apt-get install -y wget
RUN pip install --upgrade pip
RUN pip install notebook

RUN mkdir /data
RUN mkdir /notebooks
RUN mkdir /models

CMD /bin/bash