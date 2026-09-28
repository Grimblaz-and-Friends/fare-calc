import unittest

from fare_calc import Rider, fare_cents


class FareTests(unittest.TestCase):
    def test_adult_single_zone_off_peak(self):
        self.assertEqual(fare_cents(Rider("adult"), 1, 12), 250)

    def test_zones_add_per_zone_charge(self):
        self.assertEqual(fare_cents(Rider("adult"), 3, 12), 400)

    def test_peak_surcharge(self):
        self.assertEqual(fare_cents(Rider("adult"), 1, 8), 300)

    def test_senior_half_price(self):
        self.assertEqual(fare_cents(Rider("senior"), 1, 12), 125)

    def test_child_rides_free(self):
        self.assertEqual(fare_cents(Rider("child"), 4, 8), 0)

    def test_transfer_is_free(self):
        self.assertEqual(fare_cents(Rider("adult", has_transfer=True), 2, 8), 0)

    def test_rejects_zero_zones(self):
        with self.assertRaises(ValueError):
            fare_cents(Rider("adult"), 0, 12)


if __name__ == "__main__":
    unittest.main()
