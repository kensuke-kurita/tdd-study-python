class TestCase:
  def __init__(self, name):
    self.name = name
  def setUp(self):
    pass
  def tearDown(self):
    pass
  def run(self):
      self.setUp()
      method = getattr(self, self.name)
      method()
      self.tearDown()
class WasRun(TestCase):
  def setUp(self):
    self.log = "SetUp "
  def testMethod(self):
    self.log = self.log + "testMethod "
  def tearDown(self):
    self.log = self.log + "tearDown "
class TestCaseTest(TestCase):
  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run()
    assert("SetUp testMethod tearDown " == test.log)

TestCaseTest("testTemplateMethod").run()
## クラスを先に読み込んでいなかった。

#- パフォーマンスと独立性
#よく共通化しすぎてしまう。

# テストがシンプルにできるのは、きちんと動作している他のテストがあるときだけ
