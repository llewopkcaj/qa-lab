# Prompt Log — Missing Negative Case

## Prompt Sent
"Write pytest for divide(a, b) that returns a / b."

## AI Response
It produced:

def test_divide():
    assert divide(6, 3) == 2

The test ran and passed, but it only verified the normal behavior (dividing two valid numbers).
It didn’t include any tests for invalid inputs or error conditions, like dividing by zero.

## Correction

Include both positive and negative scenarios:

import pytest

def test_divide_success():
    assert divide(6, 3) == 2

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

## Lesson

When people say “AI makes this mistake,” they’re not usually talking about the latest, full-context conversation with Chat GPT. They’re describing how code assistants behave in the wild — where:
context is limited (one-line prompt, not a conversation),the model’s temperature or training data emphasizes style imitation over logical validation, and Copilot or similar tools are generating code as you type, inferring intent from surrounding lines.


