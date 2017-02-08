FROM kwierman/hep-dl

# Install the remaining dependencies
RUN apt-get install -y wget
RUN pip install jupyter

# Now Download the data
RUN wget ec2-54-213-91-246.us-west-2.compute.amazonaws.com/train.root /data/.
RUN wget ec2-54-213-91-246.us-west-2.compute.amazonaws.com/test.root /data/.

# And Download the models
RUN wget ec2-54-213-91-246.us-west-2.compute.amazonaws.com/*.h5 /models/.
RUN wget ec2-54-213-91-246.us-west-2.compute.amazonaws.com/*.cfg /models/.
RUN wget ec2-54-213-91-246.us-west-2.compute.amazonaws.com/*.prototxt /models/.

CMD /bin/bash