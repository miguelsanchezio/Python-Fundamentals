import unittest
from .activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple."
        )

    def test_eat_unhealthy(self):
        """eat should have a message for junk food"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO."
        )

    def test_eat_healthy_boolean(self):
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="maybe")

    def test_short_nap(self):
        """nap should have a message for a short nap"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap."
        )

    def test_long_nap(self):
        """nap should have a message for a long nap"""
        self.assertEqual(
            nap(3),
            "Whoops! I took a long 3 hours nap!"
        )

    def test_is_funny_time(self):
        # self.assertEqual(is_funny("tim"), False)
        self.assertFalse(is_funny("tim"), "Tim shouldn't be funny.")

    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "blue should be tammy")
        self.assertTrue(is_funny("sven"), "blue should be sven")

    def test_laugh(self):
        self.assertIn(laugh(), ("lol", "lmao", "rofl"))

if __name__ == "__main__":
    unittest.main()
