apt update
apt install -y firejail
apt install -y python3 python3-pip

apt install -y gcc # for C

# python3 -m pip install poetry

# python3 -m poetry config virtualenvs.in-project false
# python3 -m poetry install

python3 -m pip install -r requirements.txt # for very small instances

python3 -m pip install pytest
# change based on python version
python3 -m pytest /usr/local/lib/python3.8/dist-packages/executioner/