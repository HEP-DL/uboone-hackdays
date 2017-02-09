pip install --upgrade pip
pip install packaging
pip install appdirs
pip install notebook
pip install protobuf
pip install pandas
pip install lmdb
echo "COPYING JUPYTER CONFIG"
if [ ! -d ~/.jupyter ]; then
  mkdir ~/.jupyter
fi
cp jupyter_notebook_config.py ~/.jupyter/.