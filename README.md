# C--

A simple interpreted programming language inspired by C, written in Python.

## Features

* Integer variables (`int`)
* String variables (`str`)
* Variable reassignment
* Arithmetic expressions

  * `+`
  * `-`
  * `*`
  * `/`
  * Parentheses
* Conditional statements

  * `if`
  * `else`
  * Nested conditions
* Logical operators

  * `and`
  * `or`
* Comparison operators

  * `==`
  * `!=`
  * `>`
  * `<`
  * `>=`
  * `<=`
* Console output using `console_log()`

## Installation

Clone the repository:

```bash
git clone https://github.com/bensiuu/C--.git
cd C--
```

Run a program:

```bash
python3 interpreter.py example.cmm
```

## Example

```c
int score = 15
int lives = 3

console_log("=== GAME START ===")

score = score + 10

if(score >= 20)
    console_log("Bonus unlocked!")

    if(lives > 0)
        console_log("Player is alive")
    else
        console_log("Game Over")
else
    console_log("Need more points")

console_log("Final score: ", score)
```

## Syntax

### Variables

```c
int age = 16
str name = "Jakub"
```

### Assignment

```c
age = age + 1
age = age * 2
```

### Conditions

```c
if(age >= 18)
    console_log("Adult")
else
    console_log("Minor")
```

### Boolean Conditions

```c
if(age > 10 and age < 20)
    console_log("Teenager")
```

### Expressions

```c
console_log(2 + 3 * 4)
console_log((2 + 3) * 4)
```

## Project Status

Current implementation includes:

* Variables
* Arithmetic expressions
* Conditional statements
* Nested `if/else`
* Expression evaluation through Python AST

Planned features:

* Loops (`while`)
* Functions
* Arrays
* User-defined procedures
* Better parser and error reporting

## License

MIT License
