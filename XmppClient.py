import xmpp

def send_xmpp_message(username, password, to, message):
    jid = xmpp.protocol.JID(username + "@forgeservicelab.fi")
    jabber = xmpp.Client(jid.getDomain(), debug=[])
    jabber.connect(server=("xmpp.forgeservicelab.fi", 5222))
    jabber.auth(jid.getNode(), password)
    ret = jabber.send(xmpp.Message(to, message))
    if ret != "1":
        return "True"
    else:
        return ret 
