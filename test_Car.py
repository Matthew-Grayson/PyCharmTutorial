from unittest import TestCase
from Car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car()


class TestInit(TestCar):
    def test_init_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_init_time(self):
        self.assertEqual(self.car.time, 0)

    def test_init_odometer(self):
        self.assertEqual(self.car.odometer, 0)


class TestAccelerate(TestCar):
    def test_accelerate(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerates(self):
        for _ in range(1, 5):
            self.car.accelerate()
            self.assertEqual(self.car.speed, _*5)


class TestBrake(TestCar):
    def test_brake(self):
        self.car.speed = 50
        self.car.brake()
        self.assertEqual(self.car.speed, 45)

    def test_multiple_brakes(self):
        self.car.speed = 50
        for _ in range(1, 5):
            self.car.brake()
            self.assertEqual(self.car.speed, 50 - (_*5))

    # def test_step(self):
    #     self.fail()
    #
    # def test_average_speed(self):
    #     self.fail()
