from modules.wasRun import WasRun
from modules.testCase import TestCase
from modules.testResult import TestResult

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown" == test.log)
    
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

TestCaseTest("testMethod").testTemplateMethod()
