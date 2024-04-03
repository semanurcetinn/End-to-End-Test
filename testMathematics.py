import unittest
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None: #testlerden önce çalıştırılması gereken işlemler varsa onu yapar
        self.math = Mathematics()

    def test_add(self):
        result = self.math.sumTwoNumbers(10, 5)
        self.assertEqual(result, 15)  #bu kısıma assert edilen(ileri sürülen) eklenir

    def test_multiply(self):
        result = self.math.multiplyTwoNumbers(10, 5)
        self.assertEqual(result, 50)

    def tearDown(self) -> None: #oluşturulan objenin kapatılması için gereklidir.
        pass

if __name__ == '__main__':
    unittest.main()
