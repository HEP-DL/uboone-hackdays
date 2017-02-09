pip install --upgrade pip
pip install packaging
pip install appdirs
pip install notebook
pip install protobuf
echo "COPYING JUPYTER CONFIG"
if [ ! -d ~/.jupyter ]; then
  mkdir ~/.jupyter
fi
cp jupyter_notebook_config.py ~/.jupyter/.