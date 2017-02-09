#establish current directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#download the data
rsync ec2-54-213-91-246.us-west-2.compute.amazonaws.com/data.tar.gz /tmp/data.tar.gz
#untar
tar /tmp/data.tar.gz -C $DIR/data
#download trained network
#untar