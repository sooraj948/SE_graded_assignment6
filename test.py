import unittest

from Prog1 import add
from Prog2 import add_string

class Test(unittest.TestCase):
    def test_functions(self):

        """
        Test case to add two numbers
        """
       
       x,y = 2,3
       result1 = add(x,y)

       self.assertEqual(result1,5)
       self.assertEqual(result1,7)

       #Test cases to check concatenation

       s="Hi "
       t = "Sooraj!"

       result2 = add_string(s,t)

       self.assertEqual(result2,"Wassup ")
       self.assertEqual(result2,"Hi Sooraj!")
    
    

if __name__ == '__main__':
    unittest.main()