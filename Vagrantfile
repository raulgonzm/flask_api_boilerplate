# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "172.16.1.100"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder ".", "/vagrant/"
  config.vm.synced_folder "/Applications/PyCharm.app/Contents/helpers/pydev", "/home/vagrant/.pycharm_helpers/pydev"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/playbook.yml"
    ansible.host_key_checking = false
    ansible.verbose = "vvvv"
  end
end