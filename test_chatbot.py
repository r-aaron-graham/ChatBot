import unittest
from chatbot import answer


class RetrievalTests(unittest.TestCase):
    def test_cited_answer(self):
        self.assertEqual(answer("conversation history")["source"], "privacy")

    def test_no_evidence(self):
        for question in ("", "the is a", "unicorns"):
            with self.subTest(question=question):
                self.assertIsNone(answer(question)["source"])

    def test_ambiguous_query(self):
        self.assertIsNone(answer("demo")["source"])

    def test_case_and_punctuation(self):
        self.assertEqual(answer("PYTHON?!")["source"], "setup")


if __name__ == "__main__":
    unittest.main()
