import unittest
from users import user

user1 = user('User 1')

<<<<<<< Updated upstream
class Test(unittest.TestCase):
  def test_instantiation(self):
    self.assertEqual(user1.name,'User 1', 'User name is set cor')

if __name__ == '__main__':
    unittest.main()
=======

class Test(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(user1.name, 'User 1', 'User name is set correctly')

if __name__ == '__main__':
    unittest.main()
>>>>>>> Stashed changes
