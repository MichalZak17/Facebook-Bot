import fbchat as Facebook

class EchoBot(Facebook.Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
       
        Facebook.log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        REPLAY = "I am currently unavailable, but I will contact you shortly. "

        if author_id != self.uid:
           self.send(Facebook.Message(text=REPLAY), thread_id=thread_id, thread_type=thread_type)
        self.markAsDelivered(author_id, thread_id)

client = EchoBot("Login", "Password")
    
client.listen()
