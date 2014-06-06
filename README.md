docker-serf-irc
===================

Serf Cluster message propogation visualised through messages to an IRC channel.

This setup will automatically join docker nodes to a serf cluster.

The IRC Bots currently connect to irc.freenode.net/#serf-test - this can be changed simply enough in the code. I'll make configuration a little easier in the future.

## Use
- Join the channel the bots have been configured to use.
- Use the following to send a message to the cluster and see the message spread through the nodes:

`botname: message for cluster`

- As each of the clustered bots receives the message through serf, they will send it back to the channel allowing you to see the message propogate through the cluster in real time.

## Run
### Build the docker image
`sudo docker build -t dregin/serf-irc .`

### Run the first docker image
`sudo docker run --name serf1 -d -t dregin/serf-irc`

### Run the second docker image, linking it to the first
`sudo docker run --link serf1:child -d -t dregin/serf-irc`

All later images can be linked to the same image - A single point of contact allows nodes establish a connection between each other \o/

**Fun Exercise**: Stop the first image to see if the cluster remains intact!
