import unittest
from zad3 import *

class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.temp = Song()

    def test_one_verse(self):
        self.assertEqual(self.temp.play(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")


    def test_one_verse_2(self):
        self.assertEqual(self.temp.play(2), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")


    def test_line_interval(self):
        self.assertEqual(self.temp.play((1,2)),
                         """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.""")


    def test_whole_song(self):
        self.assertEqual(self.temp.play("all"), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""
)


    def test_wrong_number_exception(self):
        self.assertRaises(Exception, self.temp.play, 13)


    def test_negative_number_exception(self):
        self.assertRaises(Exception, self.temp.play, -1)

    def test_0_number_exception(self):
        self.assertRaises(Exception, self.temp.play, 0)


    def test_wrong_str_exception(self):
        self.assertRaises(Exception, self.temp.play, "al")


    def test_wrong_None_exception(self):
        self.assertRaises(Exception, self.temp.play, None)


    def test_wrong_dic_exception(self):
        self.assertRaises(Exception, self.temp.play, {"a":2})


    def test_wrong_float_exception(self):
        self.assertRaises(Exception, self.temp.play, 1.1)


    def test_wrong_line_interval_list_exception(self):
        self.assertRaises(Exception, self.temp.play, [1,2])


    def test_wrong_line_interval_tuple_wrong_numbers_first_good_exception(self):
        self.assertRaises(Exception, self.temp.play, (1,23))


    def test_wrong_line_interval_tuple_wrong_numbers_second_good_exception(self):
        self.assertRaises(Exception, self.temp.play, (-1,2))

    @unittest.skip
    def test_wrong_line_interval_tuple_wrong_numbers_exception(self):
        self.assertRaises(Exception, self.temp.play, (14, 23))

    @unittest.skip
    def test_wrong_line_interval_tuple_wrong_numbers_first_bigger_than_second(self):
        self.assertRaises(Exception, self.temp.play, (13, 3))


    def tearDown(self):
        self.temp = None