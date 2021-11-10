import unittest

class HammingTest(unittest.TestCase):

    def test_empty_strands(self):
        self.assertEqual(hamming().distance("", ""), 0)


    def test_single_letter_identical_strands(self):
        self.assertEqual(hamming().distance("A", "A"), 0)


    def test_single_letter_different_strands(self):
        self.assertEqual(hamming().distance("G", "T"), 1)


    def test_long_identical_strands(self):
        self.assertEqual(hamming().distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)


    def test_long_different_strands(self):
        self.assertEqual(hamming().distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)


    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming().distance("AATG", "AAA")


    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming().distance("ATA", "AGTG")

   
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming().distance("", "G")

    @unittest.skip("ignore")
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming().distance("G", "")

    # Utility functions

    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")



class hamming:
    def distance(self, str1, str2):
        if len(str1)>len(str2):
            raise ValueError("Str nie są równej długości")
        elif len(str1)<len(str2):
            raise ValueError("Str nie są równej długości")
        elif len(str1)=="" and len(str2)!="":
            raise ValueError("Jeden z str jest pusty")
        elif str1==str2:
            return 0
        elif len(str1)==1 and len(str2)==1:
                return 1
        elif len(str1)>1 and len(str2)>1:
                suma=0
                for i in range(len(str1)):
                    if str1[i]!=str2[i]:
                        suma+=1
                return suma

