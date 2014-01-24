docker-serf-weechat
===================

Docker running serf posting messages through IRC using the ii IRC

## Run
### Build the docker image
`sudo docker build -t dregin/serf-irc .`

### Run the first docker image
`sudo docker run -name serf1 -d -t dregin/serf-irc`

### Run the second docker image, linking it to the first
`sudo docker run -link serf1:child -d -t dregin/serf-irc`

