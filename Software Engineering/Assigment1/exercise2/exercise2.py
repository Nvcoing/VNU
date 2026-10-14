"""
Exercise 2: Composite Pattern (Element, Noeud, Feuille)
Tutorial 1 - UML Modeling (Software Engineering)
"""
from abc import ABC, abstractmethod
from typing import List


# =====================================================================
# Component Interface
# =====================================================================
class Element(ABC):
    """Abstract Base Class representing an Element in the tree structure."""

    @abstractmethod
    def afficheElement(self) -> None:
        """Display the element."""
        pass


# =====================================================================
# Leaf (Feuille)
# =====================================================================
class Feuille(Element):
    """Leaf class storing a single integer value."""

    def __init__(self, uneValeur: int) -> None:
        self.valeur = uneValeur

    def afficheElement(self) -> None:
        print(self.valeur)


# =====================================================================
# Composite Node (Noeud)
# =====================================================================
class Noeud(Element):
    """Composite class containing a collection of Element children."""

    def __init__(self) -> None:
        self.lesElements: List[Element] = []

    def setElement(self, e1: Element, e2: Element) -> None:
        """Adds child elements e1 and e2 to the elements list."""
        self.lesElements.append(e1)
        self.lesElements.append(e2)

    def afficheElement(self) -> None:
        """Recursively displays all child elements (Pre-order traversal)."""
        for elem in self.lesElements:
            elem.afficheElement()


# =====================================================================
# Main execution matching object diagram (Figure 4)
# =====================================================================
def main():
    # Instantiating the object diagram from Figure 4
    n1 = Noeud()
    n2 = Noeud()
    f1 = Feuille(1)
    f2 = Feuille(2)
    f3 = Feuille(3)

    # Establishing hierarchy:
    # n2 contains f2 and f1
    n2.setElement(f2, f1)

    # n1 contains n2 and f3
    n1.setElement(n2, f3)

    print("--- Executing n1.afficheElement() ---")
    n1.afficheElement()

    print("\n--- Executing n2.afficheElement() ---")
    n2.afficheElement()


if __name__ == "__main__":
    main()
