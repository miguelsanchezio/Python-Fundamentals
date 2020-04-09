import unittest
from .activities import eat, nap


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


if __name__ == "__main__":
    unittest.main()
