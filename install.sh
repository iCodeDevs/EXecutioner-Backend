sudo apt update
sudo apt install firejail
sudo apt install python3 python3-pip

sudo apt install gcc # for C

python3 -m pip install poetry

python3 -m poetry config virtualenvs.in-project true
python3 -m poetry install

python3 -m poetry add pytest
# change based on python version
python3 -m poetry run pytest .venv/lib/python3.8/site-packages/executioner/