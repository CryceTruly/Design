import datetime

class user(object):
  def __init__(self, name):
    self.name = name
  
  def get_name(self, value = None):
    if(not value):
      return(self.name)
    else:
      self.name = value
