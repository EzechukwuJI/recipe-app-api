from django.test import SimpleTestCase


from app import calc


class CalcTests(SimpleTestCase):


    def test_add_numbers(self):
        """ test adding numbers"""
        print("Testing number additons")
        res = calc.add(5, 6)
        self. assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ subtracting numbers """
        print("Testing number subtraction")
        res = calc.subtract(10, 6)
        self.assertEqual(res, 4)