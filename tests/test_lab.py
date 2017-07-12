from Lab import lab
from Lab import Global
import unittest

class LabTest(unittest.TestCase):
    def test_lab(self):
        @lab.setup("test", [])
        def setup(project):
            @project.dummy_task.define
            def dummy_task(project):
                return "I'm kinda dumb aren't I?"

        self.assertEqual(Global.root.test.fetch()[0]("dummy_task"), "I'm kinda dumb aren't I?")
