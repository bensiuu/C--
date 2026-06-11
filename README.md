# C--

A simple interpreted programming language written in Python.

## Features

* **Integer variables**
* **String variables**
* **Variable logging**
* **Conditional statements (`if`)**
* **Indentation-based blocks**
* **Logical operators (`and`, `or`)**
* **Command-line execution**

## Installation

```bash
git clone https://github.com/bensiuu/C--.git
cd C--
```

## Usage

Create a source file:

```cmm
int age = 6
str name = "My name"

console_log("age = ", age)
console_log("name = ", name)

if(a < 10)
    console_log(name," is less than 10")
```

Run the interpreter:

```bash
python3 interpreter.py program.cmm
```

## Syntax

### Integer Variables

```cmm
int age = 16
```

### String Variables

```cmm
str text = "Hello World"
```

### Logging

```cmm
console_log("Age: ", age)
```

### Conditions

```cmm
if(age == 16)
    log("Correct")
```

### Logical Operators

```cmm
if(age == 16 and score > 50)
    log("Passed")
```

## Roadmap

* [x] Variables 
* [x] Logging
* [x] Conditions
* [x] Indentation-based blocks
* [ ] Loops
* [ ] Functions
* [ ] Imports
* [ ] Lists
* [ ] Better error handling

## License

This project is open source and available under the MIT License.
  
