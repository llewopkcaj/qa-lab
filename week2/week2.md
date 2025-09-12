# Week 2 — Loops, Functions, Exceptions

## Pages Read
- W3Schools: If/Else, Operators, Booleans, For/While, Functions, Try/Except  
- Python Docs: Control Flow (if/for/range/break/continue/else), enumerate(), Errors and Exceptions  
- Automate the Boring Stuff: selected sections on Flow Control and Exceptions  

## Exercises Completed
- **grade_classifier.py** — classifies numeric grade into A/B/C/D/F using if/elif/else.  
- **truth_table.py** — prints results of boolean expressions with `and`/`or`/`not`.  
- **loop_katas.py** — six loop practice problems (sum 1..100, countdown, break/continue, etc.).  
- **math_utils.py** — utility functions: add, mean, describe_person.  
- **scope_demo.py** — shows why returning values is better than mutating globals.  
- **safe_divide.py** — division with error handling for invalid inputs / divide-by-zero.  
- **file_reader.py** — opens a file safely with try/except and friendly errors.  
- **cli_calculator.py** — command-line calculator with input validation, exceptions, and docstrings.  

## Code Snippets I’m Proud Of

```python
# Using enumerate for clean indexed iteration
for i, value in enumerate(["apple", "banana", "cherry"], start=1):
    print(i, value)
