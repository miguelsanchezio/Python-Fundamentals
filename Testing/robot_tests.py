import unittest
from .robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.vision = Robot("Vision", battery=50)

    def test_charge(self):
        self.vision.charge()
        self.assertEqual(self.vision.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.vision.say_name(),
            "BEEP BOOP BEEP BOOP. I AM VISION."
        )
        self.assertEqual(
            self.vision.battery,
            49
        )


if __name__ == "__main__":
    unittest.main()