# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"
  config.vm.network 'forwarded_port', guest: 80, host: 80

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    sudo curl -fsSL https://get.docker.com/ | sh
    sudo usermod -aG docker vagrant
    sudo service docker restart
    cd /home/ubuntu
    wget https://github.com/ga4ghpoc/server/raw/master/ga4gh_sample_data.tar
    tar xvf ga4gh_sample_data.tar -C /home/ubuntu
    sudo chown -R root:root /home/vagrant/ga4gh-data
    sudo chmod -R 0777 /home/vagrant/ga4gh-data
    docker run -e GA4GH_DATA_SOURCE=/data -v /home/vagrnat/ga4gh-data:/data -d -p 80:80 --name ga4gh_server ga4ghapi/server:latest
  SHELL
end
