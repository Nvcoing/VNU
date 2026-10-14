"""
Exercise 1: Adapter Pattern for SVG Drawing Engine
Tutorial 1 - UML Modeling (Software Engineering)
"""
from abc import ABC, abstractmethod


# =====================================================================
# Target Interface & Concrete Renderers
# =====================================================================
class MoteurRendu(ABC):
    """Target Abstract Interface for Rendering Shapes."""

    @abstractmethod
    def dessinerCercle(self, x: float, y: float, rayon: float) -> None:
        pass

    @abstractmethod
    def dessineRectangle(self, x: float, y: float, longueur: float, largeur: float) -> None:
        pass

    @abstractmethod
    def dessinerLigne(self, x1: float, y1: float, x2: float, y2: float) -> None:
        pass


class MoteurRenduPDF(MoteurRendu):
    """Concrete PDF Renderer."""

    def dessinerCercle(self, x: float, y: float, rayon: float) -> None:
        print("PDF : cercle")

    def dessineRectangle(self, x: float, y: float, longueur: float, largeur: float) -> None:
        print("PDF : rectangle")

    def dessinerLigne(self, x1: float, y1: float, x2: float, y2: float) -> None:
        print("PDF : ligne")


class MoteurRenduPNG(MoteurRendu):
    """Concrete PNG Renderer."""

    def dessinerCercle(self, x: float, y: float, rayon: float) -> None:
        print("PNG : cercle")

    def dessineRectangle(self, x: float, y: float, longueur: float, largeur: float) -> None:
        print("PNG : rectangle")

    def dessinerLigne(self, x1: float, y1: float, x2: float, y2: float) -> None:
        print("PNG : ligne")


# =====================================================================
# Adaptee (External Library)
# =====================================================================
class SVGWriter:
    """External Library with incompatible interface for SVG export."""

    def addCercle(self, cx: float, cy: float, r: float) -> None:
        print(f'<circle cx="{int(cx)}" cy="{int(cy)}" r="{int(r)}"/>')

    def addRectangle(self, x: float, y: float, longueur: float, largeur: float) -> None:
        print(f'<rect x="{int(x)}" y="{int(y)}" width="{int(longueur)}" height="{int(largeur)}"/>')

    def addLigne(self, x1: float, y1: float, x2: float, y2: float) -> None:
        print(f'<line x1="{int(x1)}" y1="{int(y1)}" x2="{int(x2)}" y2="{int(y2)}" stroke="black" stroke-width="2"/>')


# =====================================================================
# Adapter (Object Adapter Pattern)
# =====================================================================
class AdaptateurSVG(MoteurRendu):
    """Adapter bridging MoteurRendu calls to SVGWriter methods."""

    def __init__(self, writer: SVGWriter | None = None) -> None:
        self.writer = writer if writer is not None else SVGWriter()

    def dessinerCercle(self, x: float, y: float, rayon: float) -> None:
        self.writer.addCercle(x, y, rayon)

    def dessineRectangle(self, x: float, y: float, longueur: float, largeur: float) -> None:
        self.writer.addRectangle(x, y, longueur, largeur)

    def dessinerLigne(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.writer.addLigne(x1, y1, x2, y2)


# =====================================================================
# Geometric Shapes Hierarchy
# =====================================================================
class Forme(ABC):
    """Base class for geometric shapes."""

    @abstractmethod
    def dessiner(self, moteur: MoteurRendu) -> None:
        pass


class Cercle(Forme):
    def __init__(self, x: float, y: float, rayon: float) -> None:
        self.x = x
        self.y = y
        self.rayon = rayon

    def dessiner(self, moteur: MoteurRendu) -> None:
        moteur.dessinerCercle(self.x, self.y, self.rayon)


class Rectangle(Forme):
    def __init__(self, x: float, y: float, longueur: float, largeur: float) -> None:
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur

    def dessiner(self, moteur: MoteurRendu) -> None:
        moteur.dessineRectangle(self.x, self.y, self.longueur, self.largeur)


class Ligne(Forme):
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def dessiner(self, moteur: MoteurRendu) -> None:
        moteur.dessinerLigne(self.x1, self.y1, self.x2, self.y2)


# =====================================================================
# Main execution matching tutorial requirements
# =====================================================================
def main():
    c = Cercle(100, 100, 50)
    r = Rectangle(20, 30, 200, 100)
    l = Ligne(10, 10, 20, 20)

    moteurPNG = MoteurRenduPNG()
    moteurPDF = MoteurRenduPDF()
    moteurSVG = AdaptateurSVG()

    print("===== PDF =====")
    c.dessiner(moteurPDF)
    r.dessiner(moteurPDF)
    l.dessiner(moteurPDF)

    print("\n===== PNG =====")
    c.dessiner(moteurPNG)
    r.dessiner(moteurPNG)
    l.dessiner(moteurPNG)

    print("\n===== SVG =====")
    c.dessiner(moteurSVG)
    r.dessiner(moteurSVG)
    l.dessiner(moteurSVG)


if __name__ == "__main__":
    main()
