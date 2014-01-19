# Build Docker Image
FROM angelrr7702/ubuntu-13.10

MAINTAINER Bernard McKeever dregin@gmail.com

# Weechat
RUN apt-get install -y python2.7 weechat-curses
# TODO: Probably need to create the .weechat directory manually since weechat won't have run yet
ADD weechat-serf.py /.weechat/python/autoload/weechat-serf.py

# Serf
RUN apt-get install -y wget unzip
RUN wget https://dl.bintray.com/mitchellh/serf/0.3.0_linux_amd64.zip -P /var/tmp/
RUN unzip /var/tmp/0.3.0_linux_amd64.zip -d /usr/bin/

# Supervisor
RUN apt-get install -y supervisor
RUN mkdir /var/log/supervisor
ADD supervisor.conf /etc/supervisor/conf.d/supervisord.conf