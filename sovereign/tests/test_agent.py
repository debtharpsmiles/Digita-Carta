import unittest

from sovereign.agent import MARKER, is_human, prepare_comment, select_target


def comment(author, created, body):
    return {
        "author": {"login": author},
        "createdAt": created,
        "body": body,
    }


class SovereignTests(unittest.TestCase):
    def test_bootstrap_once(self):
        self.assertEqual(select_target([])["id"], "founding-question")
        self.assertIsNone(select_target([
            comment("github-actions[bot]", "2026-10-09T10:00:00Z", MARKER)
        ]))

    def test_select_new_human(self):
        comments = [
            comment("person1", "2026-10-09T10:00:00Z", "Old question"),
            comment("github-actions[bot]", "2026-10-09T10:10:00Z", MARKER),
            comment("person2", "2026-10-09T10:20:00Z", "New question"),
        ]
        self.assertEqual(select_target(comments)["body"], "New question")

    def test_does_not_reply_to_itself(self):
        comments = [
            comment("person1", "2026-10-09T10:00:00Z", "Question"),
            comment("github-actions[bot]", "2026-10-09T10:10:00Z", MARKER),
        ]
        self.assertIsNone(select_target(comments))
        self.assertFalse(is_human(comments[-1]))

    def test_safe_comment_boundary(self):
        self.assertIsNone(prepare_comment("NO_POST"))
        body = prepare_comment("A substantive response")
        self.assertIn("AI-authored:", body)
        self.assertIn(MARKER, body)
        with self.assertRaises(ValueError):
            prepare_comment("<!-- injected marker -->")
        with self.assertRaises(ValueError):
            prepare_comment("x" * 2801)


if __name__ == "__main__":
    unittest.main()
