apt update
apt install -y firejail python3 python3-pip gcc

python3 -m pip install -r requirements.txt # for very small instances

# change based on python version
python3 -m pytest --disable-warnings /usr/local/lib/python3.8/dist-packages/executioner/
# folder made using service is root owned
mkdir playground