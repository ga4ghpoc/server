# GA4GH API PoC #

This Proof-of-Concept (PoC) aims to provide instructions to set up server for a limited evaluation exercise.

- **Please never run this in a production environment** (where you store confidential customer data) or in the same network with production servers.

## Infrastructure requirements ##

### Networking ###
The recommended network setup for the PoC is the following:

- Network layer 3 addressing (simple addresses) for the machine. E.g.: 192.168.X.X network. DHCP and DNS should be available by default.
- A public IP address is required with port forwarding enabled (inbound - towards the machine). The public IP address can be anything, as long as it's reachable from all other participants.
- The target port (**8000** by default) needs to be allowed for inbound/outbound to all participant addresses.
- The machine needs at least NAT-based internet access to download components for the purposes of following these instructions (HTTP+HTTPS+FTP)

### Hardware ###
The required hardware setup for the PoC is the following:

- A Virtual Machine to act as a Docker host
	- **RAM**: 512 MB or more
	- **CPU**: 1 core @ 1 GhZ (or more)
	- **Disk**: 30 GB space on a single disk
	- **Network**: to handle up to 512Kbps traffic (minimal load)
- Operating System: Ubuntu 14.04 LTS x64 (or newer) with all the latest security updates applied
- Docker: Docker Engine/Client 1.12.1 (or newer)

## Setup steps ##
Follow the below steps to get the PoC environment up and running
### VM Setup ###
Once your VM is up and running, execute the following commands to install the Docker engine (run these commands with an admin user on the VM - *the account must be part of sudoers* - e.g. **ubuntu** by default):

    sudo curl -fsSL https://get.docker.com/ | sh
    sudo usermod -aG docker $(whoami)
    sudo service docker restart

### Preparing Sample Data (To Test Set-up) ###

In order to test the set-up of this installation, we detail some sample data. Further instructions will be provided to specify the data to be used in the actual PoC exercise. 

Once logged in to the VM you will need to pick a folder where you want to store sample data. Make sure you have permissions to write that folder before you decide on it. If you are unsure where you are in the file system, you can run the `pwd` command to see what the full path is.

Once the folder is created download the sample data with the following command:

    wget https://github.com/ga4ghpoc/server/raw/master/ga4gh_sample_data.tar

extract it to the target folder with (substitute /the/target/path with what you want it to be):

	tar xvf ga4gh_sample_data.tar -C /the/target/path

This command will also result in the creation of the 'ga4gh-data' subfolder under the target path.
Default permissions on the folders are 777 (public) and owned by root:root. This should be left as-is for the container to function ok.

#### Fixing folder permissions (optional) ####

In case permissions are wrong on the ga4gh-data folder these commands can be run any time to fix them:

    sudo chown -R root:root /the/target/path/ga4gh-data
	sudo chmod -R 0777 /the/target/path/ga4gh-data

### Run the GA4GH API Server (as a Docker container) ###

At this point you will have all the prerequisites in place:

- The host VM is also Docker host
- The sample data folder is available on the host

You can start the container with the following command:

    docker run -e GA4GH_DATA_SOURCE=/data -v /the/target/path/ga4gh-data:/data -d -p MYPORT:80 --name ga4gh_server ga4ghapi/server:latest

- We must pass the full path to folder which contains sample data e.g. **/tmp/data/ga4gh-data** or **/home/ubuntu/ga4gh-data**
- We must specify a port to which we expose the server [MYPORT] e.g **8000:80**

Example command:

    docker run -e GA4GH_DATA_SOURCE=/data -v /home/ubuntu/ga4gh-data:/data -d -p 8000:80 --name ga4gh_server ga4ghapi/server:latest

The command will trigger the following actions:

1. It will download the Docker image for the ga4gh server from Docker Hub (http traffic) if not available locally
2. It will mount the sample data folder to the container to path /data within the container
3. It will start the container and kick off the API

**The API server with the sample data is ready to use at this point.**

## Testing the API Server ##

To test whether the API is running correctly use this command from a linux machine that has direct connection to the VM host running the container (keep in mind that if you used a port other than 8000 you will need to change the command):

	curl --data '{}' --header 'Content-Type: application/json' http://VMS_IP_ADDRESS:8000/ga4gh/datasets/search

The expected response for this should be:

	{"nextPageToken": "", "datasets": [{"info": {}, "description": "", "id": "WyIxa2ctcDMtc3Vic2V0Il0", "name": "1kg-p3-subset"}]}

You can find the API reference (what commands and methods are supported) on:

	http://VMS_IP_ADDRESS:8000/ga4gh/

Because the VM has the container port forwarded to 8000 by default, if you target the VM's IP address with any browser and load up the above page resource, it will get to the container and you will see the API reference page.

### Restarting the container ###

If you need to stop the container or VM it is running on, the following steps are needed to restart.

Do the following commands to restart the container on the host as it is prone to get stuck with a PID error on restart (mind the port and path if you are using another):

	docker kill ga4gh_server
    docker rm ga4gh_server
	docker run -e GA4GH_DATA_SOURCE=/data -v /home/ubuntu/ga4gh-data:/data -d -p 8000:80 --name ga4gh_server ga4ghapi/server:latest

### Adding data to the PoC ###

To add data (e.g .fa.gz files) to be served via the api server, place files to `.../ga4gh-data/tmp/` folder you created. 

You can run the following commands from the host VM.

Add data [datasets, variants, references] – specify full path to the file. 

	docker exec -ti ga4gh_server ga4gh_repo list /data/repo.db

	docker exec -ti ga4gh_server ga4gh_repo add-referenceset /data/repo.db -r /data/tmp/GRCh37-subset.fa.gz --name GRCh37

	docker exec -ti ga4gh_server ga4gh_repo add-ontology /data/repo.db /data/tmp/so-xp.obo -r -n so-xp

	docker exec -ti ga4gh_server ga4gh_repo add-variantset /data/repo.db 1kg-p3-subset /data/tmp/chr1.vcf.gz /data/tmp/chr2.vcf.gz -n phase1-subset -R G RCh37
	
	[...]

More information on Data repository and supported methods:

- http://ga4gh-reference-implementation.readthedocs.io/en/latest/configuration.html#data-repository

## Dry-run Installation (Optional) ##

If you wish to dry-run the installation deploying it to the VM used for the PoC, you can try it with Vagrant with VirtualBox (install them first). Note that this is an option step and is not a substitute for the full set-up described above.

First, clone the git repository to your machine and cd into the folder.

	vagrant up

Once the machine is up, you can reach the test environment on

	http://localhost:9001

Make sure you use the `9001` port number when making API calls to test machine!
When you are done testing, you can destroy the VM with

	vagrant destroy

from the git repository folder.