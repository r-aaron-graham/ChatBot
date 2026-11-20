"""Local FAQ retrieval demo with explicit source attribution."""
import argparse
import json
import re

FAQ = [
    {"id": "setup", "text": "Install Python 3.12 and run python chatbot.py to start the local demo."},
    {"id": "privacy", "text": "Questions are processed locally. This demo stores no conversation history."},
    {"id": "scope", "text": "This demo retrieves FAQ entries using token overlap."},
]


STOP_WORDS = {"a", "an", "the", "is", "are", "how", "what", "to", "and", "this", "of", "do", "i"}


def answer(question):
    tokens = set(re.findall(r"[a-z0-9]+", question.lower())) - STOP_WORDS
    scores = [len(tokens & set(re.findall(r"[a-z0-9]+", entry["text"].lower()))) for entry in FAQ]
    best = max(scores)
    if best == 0 or scores.count(best) > 1:
        return {"answer": "No matching FAQ entry found.", "source": None}
    entry = FAQ[scores.index(best)]
    return {"answer": entry["text"], "source": entry["id"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", nargs="?", default="How are questions processed locally?")
    args = parser.parse_args()
    print(json.dumps(answer(args.question), indent=2))


if __name__ == "__main__":
    main()
