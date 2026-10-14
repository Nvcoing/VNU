"""
Build optimized notebook with embedded UML diagram images and consolidated answers.
"""
import json
import os

NOTEBOOK_PATH = r"D:\Job\thothan\VNU\Software Engineering\Assigment1\assigment1-group2.ipynb"
BASE_DIR = r"D:\Job\thothan\VNU\Software Engineering\Assigment1"

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

# 1. Title & Executive Summary
add_md("""# Software Engineering - Tutorial 1: UML Modeling
## Assignment 1 - Group 2
**Instructor:** PhD. Manh-Hung Ha  
**Repository Directory:** `D:\\Job\\thothan\\VNU\\Software Engineering\\Assigment1`  
**Master Draw.io File:** [`assigment1_all_diagrams.drawio`](assigment1_all_diagrams.drawio) (Contains 3 multi-page tabs for StarUML / Diagrams.net)

---
### 📌 Executive Summary of Assignment 1
This notebook provides the complete theoretical, architectural, and executable solutions for all 3 exercises in **Tutorial 1 - UML Modeling**:
1. **Exercise 1: Adapter Design Pattern** - Unified rendering system for geometric shapes supporting PDF, PNG, and SVG (integrating an incompatible external `SVGWriter` library). Includes Class Diagram & Sequence Diagram.
2. **Exercise 2: Composite Design Pattern** - Hierarchical tree structure manipulation with abstract `Element`, composite `Noeud`, and leaf `Feuille`. Includes Class Diagram, Object Diagram (Figure 4), Sequence Diagram for recursive traversal, and algorithmic complexity/traversal type analysis.
3. **Exercise 3: Authentication System** - Complete design of a secure multi-user credential verification workflow with `IULogin`, `GestionnairePersonne`, and `Personne`. Includes Class Diagram, Activity Diagram, executable Python implementation, and Object Diagram during execution.
""")

# 2. Exercise 1
add_md("""---
# Exercise 1: Geometric Shapes & Adapter Pattern

### 1. Problem Statement
We have an object-oriented drawing application that manipulates geometric shapes (`Circle`, `Rectangle`, `Line`, etc.) through an abstract rendering interface `MoteurRendu`.
- Existing renderers: `MoteurRenduPDF` and `MoteurRenduPNG` are already implemented.
- Objective: Export shapes to the SVG file format using an external third-party library `SVGWriter`.
- Technical Challenge: `SVGWriter` provides an incompatible interface:
  - Expected (`MoteurRendu`): `dessinerCercle(x, y, rayon)`, `dessineRectangle(x, y, longueur, largeur)`, `dessinerLigne(x1, y1, x2, y2)`.
  - Provided (`SVGWriter`): `addCercle(cx, cy, r)`, `addRectangle(x, y, longueur, largeur)`, `addLigne(x1, y1, x2, y2)`.

---
### 2. Theoretical Analysis & Design Pattern
We apply the **Adapter Pattern (Object Adapter)**:
- **Target Interface (`MoteurRendu`)**: Defines the domain-specific drawing operations used by the client `Forme`.
- **Adaptee (`SVGWriter`)**: The existing third-party class that provides the actual SVG rendering logic but has different method signatures.
- **Adapter (`AdaptateurSVG`)**: Implements `MoteurRendu` and maintains an instance of `SVGWriter` (composition `1 -writer`). When a target method is invoked (e.g., `dessineRectangle`), the adapter translates and delegates the call to the adaptee method (`writer.addRectangle`).

---
### 3. UML Diagrams
- Draw.io Source: [`exercise1/exercise1_diagrams.drawio`](exercise1/exercise1_diagrams.drawio)

#### Question 1: Class Diagram (Adapter Pattern)
![Exercise 1 Class Diagram](diagram_images/ex1_class_diagram.png)

#### Question 2: Sequence Diagram (Exporting Rectangle to SVG)
![Exercise 1 Sequence Diagram](diagram_images/ex1_sequence_diagram.png)

**Sequence of Messages:**
1. Caller (`main`) invokes `r.dessiner(moteurSVG)` on `r : Rectangle`.
2. `r : Rectangle` invokes `moteurSVG.dessineRectangle(20, 30, 200, 100)` on `moteurSVG : AdaptateurSVG`.
3. `moteurSVG : AdaptateurSVG` adapts and delegates to `writer.addRectangle(20, 30, 200, 100)` on `writer : SVGWriter`.
4. `writer : SVGWriter` outputs the SVG XML tag: `<rect x="20" y="30" width="200" height="100"/>`.
5. Returns propagate back to `r` and then to `main`.
""")

# Code Ex 1
with open(os.path.join(BASE_DIR, "exercise1", "exercise1.py"), "r", encoding="utf-8") as f:
    add_code(f.read())

# 3. Exercise 2
add_md("""---
# Exercise 2: Composite Pattern (Element, Noeud, Feuille)

### 1. Problem Statement & Architecture
We model a hierarchical tree data structure using the **Composite Pattern**:
- **Component (`Element`)**: Abstract base class declaring the unified operation `afficheElement()`.
- **Leaf (`Feuille`)**: Represents terminal nodes storing a single integer `valeur`.
- **Composite (`Noeud`)**: Represents internal branch nodes containing a collection `lesElements` of `Element` children, supporting recursive traversal via `afficheElement()`.

---
### 2. Answers to Tutorial Questions

#### Question 1: Instantiation of Object Diagram (Figure 4)
- Leaf `f1` is instantiated with `valeur = 1`.
- Leaf `f2` is instantiated with `valeur = 2`.
- Leaf `f3` is instantiated with `valeur = 3`.
- Internal node `n2` contains children `[f2, f1]` via `n2.setElement(f2, f1)`.
- Root node `n1` contains children `[n2, f3]` via `n1.setElement(n2, f3)`.

#### Question 2: Class Diagram
See the left panel below for the inheritance relationships and composition (`Noeud` composed of `0..* Element`).

#### Question 3: Sequence Diagram for `n1.afficheElement()`
See the Sequence Diagram below illustrating activation lifetimes and message sequence.

#### Question 4: Displayed Output & Tree Traversal Type
- **Output displayed when executing `n2.afficheElement()`:**
  ```text
  2
  1
  ```
  *(Because `n2` was constructed with `n2.setElement(f2, f1)`, where `f2.valeur = 2` and `f1.valeur = 1`).*
- **Type of Traversal:** **Pre-order Traversal (Depth-First Search - DFS)**. In this recursive traversal, parent nodes delegate display to their child elements from left to right, visiting each branch completely before moving to adjacent siblings.

---
### 3. UML Diagrams
- Draw.io Source: [`exercise2/exercise2_diagrams.drawio`](exercise2/exercise2_diagrams.drawio)

#### Class Diagram & Object Diagram (Figure 4)
![Exercise 2 Class and Object Diagram](diagram_images/ex2_class_object_diagram.png)

#### Sequence Diagram: Execution of `n1.afficheElement()`
![Exercise 2 Sequence Diagram](diagram_images/ex2_sequence_diagram.png)
""")

# Code Ex 2
with open(os.path.join(BASE_DIR, "exercise2", "exercise2.py"), "r", encoding="utf-8") as f:
    add_code(f.read())

# 4. Exercise 3
add_md("""---
# Exercise 3: User Authentication System

### 1. Problem Statement & Architecture
The application models a secure user identification procedure:
- **`Personne`**: Entity storing credentials (`nom`, `motDePasse`).
- **`GestionnairePersonne`**: Domain manager storing registered authorized persons (`lesPersonnes: Personne[*]`) and verifying credentials (`verifierMotDePasse`).
- **`IULogin`**: Boundary/Presentation class interacting with the user (`demanderNom`, `demanderMotDePasse`), triggering identification through `GestionnairePersonne`, and notifying results (`autoriserConnexion` or `interdireConnexion`).

---
### 2. Answers to Tutorial Questions

#### Question 1: Class Diagram
Modeled with unidirectional associations: `IULogin` maintains `1 -gestionnaire: GestionnairePersonne`, and `GestionnairePersonne` aggregates `* -lesPersonnes: Personne`.

#### Question 2: Activity Diagram of `IULogin.identification()`
Models the exact execution logic:
- `demanderNom()` ➔ `demanderMotDePasse()` ➔ Call `gestionnaire.verifierMotDePasse(nom, motDePasse)` ➔ Decision diamond:
  - If `[res == true]` ➔ `autoriserConnexion()` ➔ End.
  - If `[res == false]` ➔ `interdireConnexion()` ➔ End.

#### Question 3: Implementation & Validation
Completed `identification()` and `verifierMotDePasse()`, verified with both valid credentials (`nom2`, `motdepasse2`) and invalid credentials (`nom1`, `wrong_password`).

#### Question 4: Object Diagram
A runtime snapshot of objects when `identification()` is active:
- Object `unIULogin : IULogin` with current fields `nom = "nom2"`, `motDePasse = "motdepasse2"`.
- Associated to `unGestionnaire : GestionnairePersonne`.
- Associated to instances `p1`, `p2`, `p3` of class `Personne`.

---
### 3. UML Diagrams
- Draw.io Source: [`exercise3/exercise3_diagrams.drawio`](exercise3/exercise3_diagrams.drawio)

#### Class Diagram & Object Diagram (During identification)
![Exercise 3 Class and Object Diagram](diagram_images/ex3_class_object_diagram.png)

#### Activity Diagram: IULogin Operations
![Exercise 3 Activity Diagram](diagram_images/ex3_activity_diagram.png)
""")

# Code Ex 3
with open(os.path.join(BASE_DIR, "exercise3", "exercise3.py"), "r", encoding="utf-8") as f:
    add_code(f.read())

with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Generated notebook successfully at", NOTEBOOK_PATH)
