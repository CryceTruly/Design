import datetime

class user(object):

    def __init__(self, name):
        self.name = name
        self._logged_in = False
        self.last_logged_in_at = None

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

user1 = user("Stanley")
user1.log_in()
print(user1.last_logged_in_at)
        """
        This function returns the user last login status
        """
        return(self.last_logged_in_at)

    def log_in(self):
        """
        This function returns the user last login time record
        """
        self._logged_in = True
        self.last_logged_in_at = datetime.datetime.now()

    def log_out(self):

        self._logged_in = False

