# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "shell", path: "provisioner.sh", privileged: false 
  # essa linha de baixo sรณ deve ser executada no windows
  config.ssh.insert_key = false
  config.vm.network :forwarded_port, guest: 5000, host: 5000
end
