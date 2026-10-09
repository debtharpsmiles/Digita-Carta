import unittest
from sovereign.local_run import BYLINE, prepare_local_comment
from sovereign.agent import MARKER


class LocalRunnerTests(unittest.TestCase):
    def test_attribution_and_deduplication(self):
        result = prepare_local_comment("Why should fair punishment ever be celebrated?")
        self.assertTrue(result.startswith(BYLINE))
        self.assertIn(MARKER, result)

    def test_refuses_thinking_and_overlong_output(self):
        self.assertIsNone(prepare_local_comment("NO_POST"))
        self.assertIsNone(prepare_local_comment("<think>secret scratch</think>"))
        self.assertIsNone(prepare_local_comment("<!-- not permitted -->"))
        self.assertIsNone(prepare_local_comment("a" * 1201))


if __name__ == "__main__":
    unittest.main()
