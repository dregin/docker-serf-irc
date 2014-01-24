#! /usr/bin/python2.7
import threading, Queue, subprocess, sys, socket, time,os

tailq = Queue.Queue(maxsize=10) # buffer at most 100 lines
irc_nick = "a" + socket.gethostname()
# irc_nick = "blah123123"
def tail_incoming(channel_dir):
	out_file = channel_dir + "/out"
	while not os.path.exists(out_file):
		continue
	p = subprocess.Popen(["tail", "-f", "-n", "0", out_file], stdout=subprocess.PIPE)
	while 1:
		line = p.stdout.readline()
		tailq.put(line)
		if not line:
			break
		
if __name__ == '__main__':
	server_dir=sys.argv[1]

	f = open(server_dir + '/in','w')
	f.write('/j #serf-test\n')
	f.close()
	time.sleep(3)
	channel_dir=server_dir + "/#serf-test"
	threading.Thread(target=tail_incoming, args=(channel_dir,)).start()
	print("irc_nick: %s") % irc_nick
	while 1:
		irc_line = tailq.get().replace('\n','')
		print("irc_line: %s, irc_nick: %s") % (irc_line, irc_nick)
		# Check for highlight
		if irc_nick + ": " in irc_line:
			# Parse for message
			message = irc_line.split(irc_nick + ": ", 1)[1] + "\n"
			print(message)
			f = open(channel_dir + '/in','w')
        		f.write(irc_line)
        		f.close()
			# serf event serf-irc "MESSAGE"
			subprocess.call(["serf", "event", "serf-irc", message])
