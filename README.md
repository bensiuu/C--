# C--

A simple interpreted programming language written in Python.

## Features

- Integer variables
- String variables
- Console output
- Mathematical expressions
- Conditional statements (`if` / `else`)
- Nested `if` statements
- Indentation-based blocks
- Logical operators (`and`, `or`)
- Comparison operators:
  - `==`
  - `!=`
  - `>`
  - `<`
  - `>=`
  - `<=`

## Example

```c
int a = -1

console_log("a = ", a)

if(a)
    if(a >= -10)
        console_log(5 + a)
    else
        console_log("B")
else
    console_log("C")
```

Output:

```text
a = -1
4
```

## Installation

```bash
git clone https://github.com/bensiuu/C--.git
cd C--
```

## Usage

```bash
python3 interpreter.py program.cmm
```

## Syntax

### Integer variable

```c
int age = 16
```

### String variable

```c
str name = "Jakub"
```

### Output

```c
console_log("Hello")
console_log(name)
console_log("Age: ", age)
```

### Math

```c
console_log(5 + 5)
console_log(age + 10)
console_log(age * 2)
```

### Conditions

```c
if(age >= 16)
    console_log("Allowed")
else
    console_log("Denied")
```

### Logical operators

```c
if(age >= 16 and age < 18)
    console_log("Teenager")
```

## Roadmap

- Functions
- Loops
- User input
- Boolean variables
- Better expression parser
- Modules / imports

## License

MIT License
