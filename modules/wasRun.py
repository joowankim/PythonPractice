from .testCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        self.was_set_up = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.was_run = None
        self.was_set_up = 1
        self.log = "setUp "

    def testMethod(self):
        self.was_run = 1
        self.log = self.log + "testMethod "

