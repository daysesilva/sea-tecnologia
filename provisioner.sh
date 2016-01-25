sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

sudo apt-get install -y git python-pip python-dev postgresql postgresql-server-dev-9.3

sudo apt-get autoremove -y
sudo apt-get autoclean -y

sudo -H pip install --upgrade pip

cd /vagrant
sudo pip install -r requirements.txt

sudo -u postgres createdb sea
sudo -u postgres psql <<< "CREATE USER vagrant WITH PASSWORD 'vagrant';"
sudo -u postgres psql <<< 'GRANT ALL PRIVILEGES ON DATABASE "sea" to vagrant;'

echo "export DATABASE_URL='postgres://vagrant:vagrant@localhost/sea'" >> ~/.bashrc
echo "cd /vagrant" >> ~/.bashrc