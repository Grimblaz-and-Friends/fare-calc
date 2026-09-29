import unittest

from fare_calc import Rider, day_charges, fare_cents


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


class DailyCapTests(unittest.TestCase):
    def test_under_cap_charges_each_trip(self):
        self.assertEqual(day_charges(Rider("adult"), [(1, 12), (1, 13)]), [250, 250])

    def test_trips_after_cap_are_free(self):
        trips = [(3, 8), (3, 17), (1, 20), (1, 21)]
        self.assertEqual(day_charges(Rider("adult"), trips), [450, 0, 250, 0])


if __name__ == "__main__":
    unittest.main()
