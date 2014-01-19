'''
SCRIPT_NAME    = "serf_node"
SCRIPT_AUTHOR  = "Bernard <dregin@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "A POC for serf cluster messaging"
'''

#from Mind import Mind

### Default Settings ###
settings = {
            'server_name' : 'shitebuzz'
            }

try:
    import weechat as w
    WEECHAT_RC_OK = w.WEECHAT_RC_OK
    import_ok = True

except:
    print "This script must be run under WeeChat."
    print "Get WeeChat now at: http://www.weechat.org/"
    import_ok = False
 
class Message():
    def __init__(self, sender, message_string):
        arguments = message_string.split(' ')
        self.sender = sender     
        self.type = arguments[0]
        self.receiver = arguments[1]
        self.command = arguments[2]
        self.parameters = arguments[3]
        self.other = arguments[4]
           
def talk_callback(data, buffer, date, tags, displayed, highlight, prefix, message):
    '''   
    w.prnt('', 'data: %s' % data)
    w.prnt('', 'buffer: %s' % buffer)
    w.prnt('', 'date: %s' % date)
    w.prnt('', 'tags: %s' % tags)
    w.prnt('', 'displayed: %s' % displayed)
    w.prnt('', 'highlight: %s' % highlight)
    w.prnt('', 'prefix: %s' % prefix)
    w.prnt('', 'message: %s' % message)
    '''
    incoming = Message(prefix, message)
    if incoming.receiver == "all" or incoming.receiver == w.info_get("irc_nick", server_name):           #Only react if the master is talking to me OR ALL bots
        w.prnt('', '%s told %s to /%s %s' % (incoming.sender, incoming.receiver,incoming.command, incoming.parameters))
#    mind = Mind()
#    mind.decide(incoming)
#    if "mas" in incoming.sender:                                                                        #Only accept commands from specific user nick
#        if incoming.type == "bot":
#            if incoming.receiver == "all" or incoming.receiver == w.info_get("irc_nick", server_name):           #Only react if the master is talking to me OR ALL bots
#                w.prnt('', '%s told %s to /%s %s' % (incoming.sender, incoming.receiver,incoming.command, incoming.parameters))
#                if incoming.command == "nick": w.command('', '/nick %s' % incoming.parameters)
                
    return 1
        
if __name__ == '__main__' and import_ok and w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC,'', ''):
    for opt, val in settings.iteritems():
        if not w.config_is_set_plugin(opt):
            w.config_set_plugin(opt, val)
    
    server_name = w.config_get_plugin('server_name')
    
    w.prnt('', "Loaded Bot Slave")
    w.prnt('', "My name is %s" % w.info_get("irc_nick", server_name))
    
    talk_hook = w.hook_print("", "", "", 1, "talk_callback", server_name)