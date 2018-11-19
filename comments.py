import datetime


class comment(object):
        def __init__(self, author, message):
            self.author = author
            self.message = message
            self.created_at = datetime.datetime.now()
    
        def author(self, value=None):
            if(not value):
                return(self.author)
            else:
                self.author = value

        def message(self, value=None):
            if(not value):
                return(self.message)
            else:
                self.message = value
            
        def created_at(self):
            return(self.created_at)

comment1 = comment("user", "message is here")
print(comment1.author + ' commented: ' + comment1.message)