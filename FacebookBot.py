from fbchat import log, Client,Message

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
       
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        reply = "I am currently unavailable, but I will contact you shortly. "

        # If you're not the author, echo
        if author_id != self.uid:
           self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
        self.markAsDelivered(author_id, thread_id)

client = EchoBot("Login", "Password")
    
client.listen()
