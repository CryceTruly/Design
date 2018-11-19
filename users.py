import datetime
'''
the user class describes user properties and behaviours
'''
class user(object):
  def __init__(self, name):
    self.name = name
  
  def get_name(self, value = None):
    '''
    returns a user name passed in into the class
    '''
    if not value:
      return(self.name)
    else:
      self.name = value
