# Prime Numbers Logger Project

Welcome to the **Prime Numbers Logger Project** – a simple yet efficient Python program that identifies prime numbers and writes them to a file, while logging the function's execution.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Explanation](#code-explanation)
6. [Contributing](#contributing)
7. [License](#license)

## Overview

This project demonstrates the use of a logger decorator in Python to log the start and end of a function's execution. The main functionality includes identifying prime numbers up to a user-specified limit and writing those numbers to a file.

## Features

- **Prime Number Identification**: Checks and identifies prime numbers up to a given limit.
- **Logging**: Logs messages indicating when a function starts and finishes.
- **File Writing**: Writes the identified prime numbers to a file.

## Installation

To get started with the **Prime Numbers Logger Project**, follow these steps:

1. **Clone the Repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/prime-numbers-logger.git
    cd prime-numbers-logger
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    This project does not require any external libraries other than the standard Python library.

## Usage

1. **Run the Script**:

    ```bash
    python main.py
    ```

    The script will prompt you to enter a number. It will then compute all prime numbers less than the given number and write them to `prime.txt`. You will also see log messages indicating the start and end of the `primes_to_file` function.

## Code Explanation

### Prime Number Function

The `is_prime` function checks if a number is prime:

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
