from .testCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        self.was_set_up = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown"

    def testBrokenMethod(self):
        raise Exception    


