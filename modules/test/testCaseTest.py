from modules.wasRun import WasRun
from modules.testCase import TestCase

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.was_run)

    def testSetUp(self):
        self.test.run()
        assert(self.test.was_set_up)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
