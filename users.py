import datetime
import time

class user(object):
    def __init__(self, name, password):
        self.name = name
        self._logged_in = False
        self.last_logged_in_at = None
        self.username = self.get_name(),
        self.password = password

    def get_name(self, value=None):
        """
        This method handles setting the name
        """
        if(not value):
            return(self.name)
        else:
            self.name = value

    def is_logged_in(self):
        return(self._logged_in)

    def get_last_logged_in_at(self):
        return(self.last_logged_in_at)

    def log_in(self):
        self._logged_in = True
        self.last_logged_in_at = datetime.datetime.now()
        return(self.last_logged_in_at)

    def sign_up_user(self):
        return "You have successfully signed up and logged in"
        
    def log_in(self):
        """
        This function returns the user last login time record
        """
        self._logged_in = True
        self.last_logged_in_at = datetime.datetime.now()

    def log_out(self):
        self._logged_in = False


if __name__ == "__main__":
    username = str(input('Please input your desired username\n'))
    password = str(input('Hey input your desired password\n'))
    user1 = user( username , password)
    print(user1.sign_up_user())
    print('Loading recent Comments')
    time.sleep(1)

