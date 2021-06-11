from lesson_1_hello_world.hello_world import hello_world
import unittest


class TestHelloWorld(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_hello_world(self):
        r = hello_world()
        self.assertEqual(r, "Hello world")

    def test_hello_world_fail(self):
        r = hello_world()
        self.assertEqual(r, "h")