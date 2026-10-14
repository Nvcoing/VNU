"""
Build master notebook for Assignment 2 (Tutorial 3 - Design Patterns)
"""
import json
import os

NOTEBOOK_PATH = r"D:\Job\thothan\VNU\Software Engineering\Assigment2\assigment2-group2.ipynb"
BASE_DIR = r"D:\Job\thothan\VNU\Software Engineering\Assigment2"

notebook = {
    "cells": [],
    "metadata": {
        "language_info": {
            "name": "python",
            "version": "3.14.0"
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

def add_md(text):
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": text.strip().splitlines(keepends=True)
    })

def add_code(code):
    notebook["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": code.strip().splitlines(keepends=True)
    })

# Header & Overview
add_md("""# Software Engineering - Tutorial 3: The Design Patterns
## Assignment 2 - Group 2
**Instructor:** PhD. Ha Manh Hung  
**Repository Directory:** `D:\\Job\\thothan\\VNU\\Software Engineering\\Assigment2`  
**Master Draw.io File:** [`assigment2_all_diagrams.drawio`](assigment2_all_diagrams.drawio) (Multi-page diagram file)

---
### 📌 Executive Summary of Assignment 2
This notebook synthesizes all solutions for **Tutorial 3 - The Design Patterns**:
1. **Exercise 1: The Singleton Design Pattern**
   - Context: Bank accounts (`CompteBancaire`) sharing a common logging system (`Journalisation`).
   - Investigation of memory redundancy (multiple logger instances).
   - Redesign with **Singleton Pattern** ensuring exactly **one** global logger instance across all accounts.
2. **Exercise 2: The Decorator Design Pattern**
   - Context: Event logging system with formatting (HTML tags) and encryption (circular character shifting).
   - Evaluation of class explosion under multiple inheritance / subclassing approaches.
   - Restructuring using the **Decorator Pattern** to allow dynamic, recursive chaining of responsibilities at runtime.
""")

# Exercise 1 Section
add_md("""---
# Exercise 1: Bank Account & Singleton Pattern

### 1. Problem Statement
The application models a banking system where multiple bank accounts (`cb1`, `cb2`, `cb3`) record deposits and withdrawals into an activity log via `Journalisation.afficherLog()`.
In the initial unoptimized version, every `CompteBancaire` object instantiates its own `Journalisation` object in its constructor (`make_shared<Journalisation>()`), leading to memory wastage and lack of a centralized logging trace.

---
### 2. Answers to Questions

#### Question 1: Main Function Execution & Expected Output
Transactions performed across accounts to generate the required log output:
- `cb1.deposerArgent(100.0)` $\\to$ Deposit of 100.000000e into account 123456789.
- `cb1.retirerArgent(80.0)` $\\to$ Withdrawal of 80.000000e from account 123456789.
- `cb2.retirerArgent(50.0)` $\\to$ The bank does not allow overdrafts on account 987654321 (solde = 0).
- `cb3.deposerArgent(100.0)` $\\to$ Deposit of 100.000000e into account 456789012.

#### Question 2: Initial Number of Journalisation Objects
- **Answer:** **3 objects** of type `Journalisation` are created. Each time `new CompteBancaire(...)` is executed, its constructor explicitly calls `make_shared<Journalisation>()`, producing 3 distinct instances in memory.

#### Question 3: Class Diagram of Singleton Journalisation & Operation Mechanism
![Exercise 1 Singleton Class Diagram](diagram_images/ex1_singleton_diagram.png)

* **Operation Mechanism:**
  1. The default constructor `Journalisation()` is declared **private** (`-`) so that outside clients cannot instantiate objects directly with `new`.
  2. A private static member `uniqueInstance : Journalisation` holds the single created instance.
  3. A public static method `getInstance() : Journalisation` checks if `uniqueInstance == null`. If `true`, it creates the instance; otherwise, it returns the existing instance.

#### Question 4: Code Implementation
The refactored code below encapsulates the Singleton logger and modifies `CompteBancaire` to call `Journalisation.getInstance()`.

#### Question 5: Final Number of Journalisation Objects under Singleton
- **Answer:** Exactly **1 object** of type `Journalisation` is created throughout the entire execution, shared across `cb1`, `cb2`, `cb3`.
""")

# Code Ex 1
with open(os.path.join(BASE_DIR, "exercise1", "exercise1.py"), "r", encoding="utf-8") as f:
    add_code(f.read())

# Exercise 2 Section
add_md("""---
# Exercise 2: Event Logging & Decorator Pattern

### 1. Problem Statement
We want to keep track of abnormal application events by logging messages to a console or saving them to a file. In addition, messages may need to be:
- **Formatted in HTML:** `<HTML><BODY> <b> <msg> </b> </BODY> </HTML>`
- **Encrypted:** Circularly shifting each character $n$ positions to the left (e.g., `'Message d'erreur n°1'` shifted 4 positions becomes `'age d'erreur n°1Mess'`).

---
### 2. Answers to Questions

#### Question 1: Comment on the Proposed Solution (Figure 2)
The initial solution in Figure 2 uses classical inheritance to create specialized subclasses for every combination:
- `HTMLConsoleLogger`, `EncryptConsoleLogger`
- `HTMLFileLogger`, `EncryptFileLogger`

* **Criticisms / Drawbacks:**
  1. **Class Explosion (Combinatorial Explosion):** If we introduce $M$ log destinations (Console, File, Database, Network) and $N$ transformations (HTML, Encrypt, Timestamp, Compress), we must create $M \\times 2^N$ separate classes!
  2. **Rigid Static Binding:** Responsibilities are fixed at compile-time and cannot be added or removed dynamically at runtime.
  3. **No Support for Multiple Chaining:** Figure 2 cannot handle combined operations (e.g., both HTML formatting **AND** encryption) without inventing even more hybrid subclasses like `HTMLEncryptFileLogger`.

#### Question 2: Proposed Class Diagram using Decorator Pattern
![Exercise 2 Decorator Class Diagram](diagram_images/ex2_decorator_class_diagram.png)

- **`Logger` (Interface Component):** Declares `log(msg)`.
- **`ConsoleLogger`, `FileLogger` (Concrete Components):** Terminal output destinations.
- **`DecorateurLogger` (Base Decorator):** Implements `Logger` and holds an internal `1 -logger_: Logger` reference.
- **`HTMLLogger`, `EncryptLogger` (Concrete Decorators):** Apply formatting/encryption before delegating to the wrapped `logger_`.

#### Question 3: Object Diagram (`HTMLLogger` wrapping `FileLogger`)
See the left panel below: `hLogger: HTMLLogger` holds a pointer/reference to `fLogger: FileLogger`.

#### Question 4: Sequence Diagram (Storing HTML Log in File)
See the right panel below:
1. `Client` calls `hLogger.log("Message d'erreur n°1")`.
2. `hLogger` executes internal `formaterHTML(msg)`.
3. `hLogger` calls `fLogger.log("<HTML><BODY> <b> ... </b> </BODY> </HTML>")`.
4. `fLogger` appends formatted string to `nomFichier_`.

![Exercise 2 Object and Sequence Diagram](diagram_images/ex2_object_sequence_diagrams.png)

#### Questions 5 & 6: Python Implementation & Multi-Case Testing
The complete executable solution below validates:
- Case 1: `EncryptLogger` attached to `ConsoleLogger` (10 messages).
- Case 2: `HTMLLogger` attached to `FileLogger` (10 messages into `FichierLog1.html`).
- Case 3: Chained decoration (`HTMLLogger` $\\to$ `EncryptLogger` $\\to$ `FileLogger`).
""")

# Code Ex 2
with open(os.path.join(BASE_DIR, "exercise2", "exercise2.py"), "r", encoding="utf-8") as f:
    add_code(f.read())

with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Generated Assignment 2 master notebook successfully at", NOTEBOOK_PATH)
