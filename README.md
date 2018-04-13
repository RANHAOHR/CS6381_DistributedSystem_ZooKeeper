# CS6381_DistributedSystem_ZooKeeper
The package builds a small layer of middleware on top of XPUB/XSUB and Zookeeper(Kazoo) to support ANONYMITY, OWNERSHIP_STRENGTH and HISTORY. This package is based on the Pub/Sub middleware from Assignment#1, build for CS6381 Distributed System Assignment#3.

## Collaborators

Ran Hao (rxh349@case.edu) Xiaodong Yang (xiaodong.yang@vanderbilt.edu)

- Please contact us if there is any problem
## Dependences
- Java: sudo add-apt-repository ppa:webupd8team/java ; sudo apt update ; sudo apt install oracle-java9-installer ;  sudo apt-get install openjdk-9-jre-headless
- Zookeeper: Download the Zookeeper package from official website: http://www.gtlib.gatech.edu/pub/apache/zookeeper/ ; Uncompress: tar xvzf zookeeper-'version'.tar.gz
- Kazoo: pip install Kazoo

## Before running the server node:
- First go to the zookeeper directory and `cd /bin` then run the zookeeper servers by : `./zkServer.sh start`
- Then run `python zookeeper_server.py`

## Run publishers by ("zipcode" is the topic here):
- Go to the package directory
- `python publisher.py "ownership(default 2)" "zipnode(default 10001)" "address of zookeeper server"`

## Run subscriber by:
- Go to the package directory
- `python subscriber.py "zipnode(default 10001)" "address of zookeeper server"`

## When running additional subscribers, if want to receive HISTORY massage, run:
`python subscriber.py "zipnode(default 10001)" "address of the broker node" "port(for receiving HISTORY)"`
- In the zookeeper server, press `Enter` to send the HISTORY and start the communication. Please wait until "Sent HISTORY" message shows to send history to the next subscriber
