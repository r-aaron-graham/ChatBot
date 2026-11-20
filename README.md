# Local FAQ Chatbot

A small Python FAQ retrieval example. Answers quote an entry from a bundled FAQ and include its source ID. Questions with zero useful token overlap or ambiguous matches receive an explicit no-match response.

## Run

Python 3.12 is sufficient.

```sh
python chatbot.py "How are questions processed locally?"
```

Expected output includes source `privacy` and the FAQ statement about local processing. Run `python chatbot.py zzzz` to see the no-match response.

## Implementation

The code tokenizes questions and FAQ entries, ranks entries by shared token count, and returns the no-match response when the best entries tie. This lexical baseline provides a reproducible starting point for retrieval evaluation. It has three bundled entries. Relevance thresholds, a larger evaluated corpus, semantic retrieval, authentication, and service deployment require further implementation.

## Verify

Run `python -m unittest -v test_chatbot` from the repository root. The tests check cited answers, unknown and empty questions, tied matches, and case normalization. Common question words are excluded from scoring.
