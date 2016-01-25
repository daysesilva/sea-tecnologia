sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

sudo apt-get install -y git python-pip python-dev postgresql postgresql-server-dev-9.3
	
sudo apt-get autoremove -y
sudo apt-get autoclean -y

sudo -H pip install --upgrade pip

cd /vagrant 
sudo pip install -r requirements.txt
