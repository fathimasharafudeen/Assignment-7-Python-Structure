# Python Assignment 1: Data Structures – Strings & Tuples

## Overview
This project contains solutions for Python Assignment 1, covering two core data structures:

- **Strings**: concatenation, indexing and slicing, and built-in methods
- **Tuples**: concatenation, repetition, and element access

## File
- `Assignment_01_Data_structures.py`: complete solution for all parts

## Requirements
- Python 3.x
- No external libraries

## How to Run
```bash
python Assignment_01_Data_structures.py
```
The program asks for your name first (`Enter your Name:`), then prints the rest of the output.

## What the Program Does

### 1. String Concatenation
Joins `"Hello "` with the name entered by the user, then appends `", welcome to Python programming"`.

```
Enter your Name: Zara
Hello Zara
Hello Zara, welcome to Python programming
```

### 2. String Slicing and Indexing
Works on the concatenated string:

| Task | Code |
|------|------|
| First character | `text[0]` |
| Last character | `text[-1]` |
| First 5 characters | `text[:5]` |
| Last 11 characters | `text[-11:]` |
| Reverse | `text[::-1]` |
| Word "Python" | `text[23:29]`, or `text.find("Python")` with slicing |

> `text[23:29]` only works for a 4-letter name like "Zara". The `find()` version works for any name.

### 3. String Methods
Uses `strM = "Python beginner tutorial"`:

| Task | Code | Result |
|------|------|--------|
| Uppercase | `strM.upper()` | `PYTHON BEGINNER TUTORIAL` |
| Lowercase | `strM.lower()` | `python beginner tutorial` |
| Restore original form | `strM.lower().capitalize()` | `Python beginner tutorial` |
| Count of `'t'` | `strM.count("t")` | `3` |
| Replace "Python" | `strM.replace("Python", "Machine Learning")` | `Machine Learning beginner tutorial` |

### 4. Tuples
Uses `t1 = (10, 20, 30)` and `t2 = (40, 50, 60)`:

| Task | Code | Result |
|------|------|--------|
| Concatenate | `t_combine = t1 + t2` | `(10, 20, 30, 40, 50, 60)` |
| Repeat 3 times | `t_combine * 3` | the 6 elements repeated 3 times (18 total) |
| 3rd element | `t_combine[2]` | `30` |
| First three | `t_combine[:3]` | `(10, 20, 30)` |
| Last three | `t_combine[-3:]` | `(40, 50, 60)` |

## Key Concepts
- Indexing starts at `0`; negative indexes count from the end.
- Slicing `[start:stop]` includes `start` and excludes `stop`.
- Strings and tuples are immutable, so operations like `+`, `*` and `replace()` return new objects.
- `count()` is case-sensitive.

## Author
Your Name
