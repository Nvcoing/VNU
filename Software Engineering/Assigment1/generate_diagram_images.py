"""
Render professional publication-quality UML diagrams matching drawio files
for embedding into the assignment notebook.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"D:\Job\thothan\VNU\Software Engineering\Assigment1\diagram_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def draw_uml_class(ax, x, y, w, h, name, stereotype=None, attrs=None, methods=None, bg="#DAE8FC", border="#4A6FA5"):
    attrs = attrs or []
    methods = methods or []
    # Background box
    rect = patches.FancyBboxPatch((x, y - h), w, h, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.8, zorder=2)
    ax.add_patch(rect)

    # Header text
    header_str = f"«{stereotype}»\n{name}" if stereotype else name
    ax.text(x + w / 2, y - 0.28, header_str, ha="center", va="center", fontsize=9.5, weight="bold", color="#111827", zorder=3)

    # Divider 1
    div1_y = y - (0.58 if stereotype else 0.45)
    ax.plot([x, x + w], [div1_y, div1_y], color=border, lw=1.2, zorder=3)

    # Attributes
    curr_y = div1_y - 0.16
    for a in attrs:
        ax.text(x + 0.12, curr_y, a, ha="left", va="center", fontsize=8.5, color="#1F2937", zorder=3)
        curr_y -= 0.22

    # Divider 2
    div2_y = y - h + (len(methods) * 0.22 + 0.12 if methods else 0.1)
    if div2_y < div1_y:
        ax.plot([x, x + w], [div2_y, div2_y], color=border, lw=1.2, zorder=3)
        # Methods
        curr_y = div2_y - 0.16
        for m in methods:
            ax.text(x + 0.12, curr_y, m, ha="left", va="center", fontsize=8.5, color="#1F2937", zorder=3)
            curr_y -= 0.22


# ==============================================================================
# 1. EXERCISE 1: CLASS DIAGRAM (ADAPTER PATTERN)
# ==============================================================================
def render_ex1_class_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=200)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Header
    ax.text(6.5, 8.1, "Exercise 1: Class Diagram - Adapter Pattern for SVG Export", ha="center", va="center", fontsize=14, weight="bold", color="#1E3A8A")

    # Target Interface: MoteurRendu
    draw_uml_class(ax, 7.2, 7.4, 5.3, 1.6, "MoteurRendu", stereotype="interface",
                   methods=["+ dessinerCercle(x, y, rayon): void",
                            "+ dessineRectangle(x, y, longueur, largeur): void",
                            "+ dessinerLigne(x1, y1, x2, y2): void"],
                   bg="#D5E8D4", border="#276A3C")

    # Forme Hierarchy
    draw_uml_class(ax, 0.6, 7.4, 3.6, 1.2, "Forme", stereotype="abstract",
                   methods=["+ dessiner(moteur: MoteurRendu): void"],
                   bg="#DAE8FC", border="#3B6790")

    draw_uml_class(ax, 0.2, 5.0, 2.3, 1.5, "Cercle",
                   attrs=["- x: double", "- y: double", "- rayon: double"],
                   methods=["+ dessiner(moteur): void"],
                   bg="#DAE8FC", border="#3B6790")

    draw_uml_class(ax, 2.7, 5.0, 2.5, 1.7, "Rectangle",
                   attrs=["- x: double", "- y: double", "- longueur: double", "- largeur: double"],
                   methods=["+ dessiner(moteur): void"],
                   bg="#DAE8FC", border="#3B6790")

    draw_uml_class(ax, 5.4, 5.0, 2.3, 1.7, "Ligne",
                   attrs=["- x1: double", "- y1: double", "- x2: double", "- y2: double"],
                   methods=["+ dessiner(moteur): void"],
                   bg="#DAE8FC", border="#3B6790")

    # Generalization arrows (Inheritance)
    for cx in [1.35, 3.95, 6.55]:
        ax.annotate("", xy=(2.4, 6.2), xytext=(cx, 5.0),
                    arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))

    # Dependency: Forme -> MoteurRendu
    ax.annotate("", xy=(7.2, 6.6), xytext=(4.2, 6.6),
                arrowprops=dict(arrowstyle="->", lw=1.5, ls="--", color="#4B5563", shrinkA=0, shrinkB=0, mutation_scale=15))
    ax.text(5.7, 6.8, "«uses»", ha="center", va="bottom", fontsize=9, style="italic", color="#4B5563")

    # Concrete Implementations of MoteurRendu
    draw_uml_class(ax, 8.2, 5.4, 4.3, 1.2, "MoteurRenduPDF",
                   methods=["+ dessinerCercle(x, y, rayon): void",
                            "+ dessineRectangle(x, y, longueur, largeur): void",
                            "+ dessinerLigne(x1, y1, x2, y2): void"],
                   bg="#D5E8D4", border="#276A3C")

    draw_uml_class(ax, 8.2, 3.8, 4.3, 1.2, "MoteurRenduPNG",
                   methods=["+ dessinerCercle(x, y, rayon): void",
                            "+ dessineRectangle(x, y, longueur, largeur): void",
                            "+ dessinerLigne(x1, y1, x2, y2): void"],
                   bg="#D5E8D4", border="#276A3C")

    # Adapter Class
    draw_uml_class(ax, 8.2, 2.2, 4.3, 1.5, "AdaptateurSVG", stereotype="Adapter",
                   attrs=["- writer: SVGWriter"],
                   methods=["+ dessinerCercle(x, y, rayon): void",
                            "+ dessineRectangle(x, y, longueur, largeur): void",
                            "+ dessinerLigne(x1, y1, x2, y2): void"],
                   bg="#FFE6CC", border="#D79B00")

    # Realization dashed arrows
    for y_c in [4.8, 3.2, 1.45]:
        ax.annotate("", xy=(7.2, 6.1), xytext=(8.2, y_c),
                    arrowprops=dict(arrowstyle="-|>", lw=1.5, ls="--", color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))

    # Adaptee: SVGWriter
    draw_uml_class(ax, 1.8, 2.0, 4.8, 1.4, "SVGWriter", stereotype="Adaptee - External Lib",
                   methods=["+ addCercle(cx, cy, r): void",
                            "+ addRectangle(x, y, longueur, largeur): void",
                            "+ addLigne(x1, y1, x2, y2): void"],
                   bg="#F8CECC", border="#B85450")

    # Composition / Aggregation from AdaptateurSVG to SVGWriter
    ax.annotate("", xy=(6.6, 1.3), xytext=(8.2, 1.3),
                arrowprops=dict(arrowstyle="-", lw=1.8, color="#B85450", shrinkA=0, shrinkB=0))
    # Diamond at AdaptateurSVG
    diamond = patches.Polygon([[8.2, 1.3], [8.0, 1.42], [7.8, 1.3], [8.0, 1.18]], closed=True, fc="#B85450", ec="#B85450", zorder=4)
    ax.add_patch(diamond)
    ax.text(6.8, 1.45, "1 -writer", ha="left", va="bottom", fontsize=8.5, weight="bold", color="#B85450")

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex1_class_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 2. EXERCISE 1: SEQUENCE DIAGRAM (RECTANGLE TO SVG)
# ==============================================================================
def render_ex1_sequence_diagram():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(5.0, 6.6, "Exercise 1: Sequence Diagram - Exporting Rectangle to SVG", ha="center", va="center", fontsize=13, weight="bold", color="#1E3A8A")

    lifelines = [
        (1.2, ":Main / Client", "#E1D5E7", "#9673A6"),
        (3.6, "r : Rectangle", "#DAE8FC", "#6C8EBF"),
        (6.3, "moteurSVG : AdaptateurSVG", "#FFE6CC", "#D79B00"),
        (8.8, "writer : SVGWriter", "#F8CECC", "#B85450"),
    ]

    for x, label, bg, border in lifelines:
        # Box
        rect = patches.FancyBboxPatch((x - 1.0, 5.7), 2.0, 0.55, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.4)
        ax.add_patch(rect)
        ax.text(x, 5.97, label, ha="center", va="center", fontsize=8.5, weight="bold")
        # Lifeline dashed
        ax.plot([x, x], [0.8, 5.7], ls="--", color="#6B7280", lw=1.2, zorder=1)

    # Activations
    def draw_act(x, y1, y2, bg, border):
        ax.add_patch(patches.Rectangle((x - 0.08, y2), 0.16, y1 - y2, fc=bg, ec=border, lw=1.2, zorder=3))

    draw_act(1.2, 5.4, 1.2, "#E1D5E7", "#9673A6")
    draw_act(3.6, 5.0, 1.6, "#DAE8FC", "#6C8EBF")
    draw_act(6.3, 4.4, 2.2, "#FFE6CC", "#D79B00")
    draw_act(8.8, 3.8, 2.8, "#F8CECC", "#B85450")

    # Messages
    # 1. Main -> r
    ax.annotate("", xy=(3.52, 5.0), xytext=(1.28, 5.0), arrowprops=dict(arrowstyle="->", lw=1.4, color="#1F2937"))
    ax.text(2.4, 5.15, "1: dessiner(moteurSVG)", ha="center", va="bottom", fontsize=8.5, weight="bold")

    # 2. r -> moteurSVG
    ax.annotate("", xy=(6.22, 4.4), xytext=(3.68, 4.4), arrowprops=dict(arrowstyle="->", lw=1.4, color="#1F2937"))
    ax.text(4.95, 4.55, "2: dessineRectangle(20, 30, 200, 100)", ha="center", va="bottom", fontsize=8.5, weight="bold")

    # 3. moteurSVG -> writer
    ax.annotate("", xy=(8.72, 3.8), xytext=(6.38, 3.8), arrowprops=dict(arrowstyle="->", lw=1.4, color="#1F2937"))
    ax.text(7.55, 3.95, "3: addRectangle(20, 30, 200, 100)", ha="center", va="bottom", fontsize=8.5, weight="bold")

    # Return 3
    ax.annotate("", xy=(6.38, 2.8), xytext=(8.72, 2.8), arrowprops=dict(arrowstyle="->", ls="--", lw=1.2, color="#4B5563"))
    ax.text(7.55, 2.95, "return", ha="center", va="bottom", fontsize=8, color="#4B5563")

    # Return 2
    ax.annotate("", xy=(3.68, 2.2), xytext=(6.22, 2.2), arrowprops=dict(arrowstyle="->", ls="--", lw=1.2, color="#4B5563"))
    ax.text(4.95, 2.35, "return", ha="center", va="bottom", fontsize=8, color="#4B5563")

    # Return 1
    ax.annotate("", xy=(1.28, 1.6), xytext=(3.52, 1.6), arrowprops=dict(arrowstyle="->", ls="--", lw=1.2, color="#4B5563"))
    ax.text(2.4, 1.75, "return", ha="center", va="bottom", fontsize=8, color="#4B5563")

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex1_sequence_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 3. EXERCISE 2: CLASS & OBJECT DIAGRAMS (COMPOSITE PATTERN)
# ==============================================================================
def render_ex2_diagrams():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=200, gridspec_kw={"width_ratios": [1, 1]})
    for ax in [ax1, ax2]:
        ax.axis("off")

    # Subplot 1: Class Diagram
    ax1.set_xlim(0, 7)
    ax1.set_ylim(0, 6)
    ax1.text(3.5, 5.6, "Class Diagram: Composite Pattern", ha="center", va="center", fontsize=12, weight="bold", color="#1E3A8A")

    draw_uml_class(ax1, 2.0, 5.0, 3.0, 1.2, "Element", stereotype="abstract",
                   methods=["+ afficheElement(): void {abstract}"],
                   bg="#DAE8FC", border="#3B6790")

    draw_uml_class(ax1, 0.4, 2.6, 2.6, 1.4, "Feuille",
                   attrs=["- valeur: int"],
                   methods=["+ Feuille(uneValeur: int)", "+ afficheElement(): void"],
                   bg="#D5E8D4", border="#276A3C")

    draw_uml_class(ax1, 3.8, 2.6, 3.0, 1.6, "Noeud",
                   attrs=["- lesElements: Element[*]"],
                   methods=["+ Noeud()", "+ setElement(e1, e2): void", "+ afficheElement(): void"],
                   bg="#FFE6CC", border="#D79B00")

    # Inheritance arrows
    ax1.annotate("", xy=(3.0, 3.8), xytext=(1.7, 2.6),
                 arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))
    ax1.annotate("", xy=(4.0, 3.8), xytext=(5.0, 2.6),
                 arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))

    # Composition: Noeud contains Element
    ax1.plot([5.3, 5.8, 5.8, 5.0], [2.6, 2.6, 4.4, 4.4], color="#D79B00", lw=1.6)
    diamond = patches.Polygon([[5.3, 2.6], [5.42, 2.7], [5.54, 2.6], [5.42, 2.5]], closed=True, fc="#D79B00", ec="#D79B00")
    ax1.add_patch(diamond)
    ax1.text(5.9, 3.5, "* -lesElements", ha="left", va="center", fontsize=8.5, weight="bold", color="#D79B00")

    # Subplot 2: Object Diagram (Figure 4)
    ax2.set_xlim(0, 7)
    ax2.set_ylim(0, 6)
    ax2.text(3.5, 5.6, "Object Diagram: Figure 4", ha="center", va="center", fontsize=12, weight="bold", color="#1E3A8A")

    def draw_obj(ax, x, y, w, h, name, attrs=None, bg="#FFF2CC", border="#D6B656"):
        rect = patches.FancyBboxPatch((x, y - h), w, h, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y - 0.22, name, ha="center", va="center", fontsize=9, weight="bold")
        if attrs:
            ax.plot([x, x + w], [y - 0.4, y - 0.4], color=border, lw=1)
            ax.text(x + w/2, y - 0.65, "\n".join(attrs), ha="center", va="center", fontsize=8.5)

    draw_obj(ax2, 2.6, 4.8, 1.8, 0.55, "n1 : Noeud")
    draw_obj(ax2, 1.0, 3.4, 1.8, 0.55, "n2 : Noeud")
    draw_obj(ax2, 4.2, 3.4, 1.8, 0.85, "f3 : Feuille", attrs=["valeur = 3"], bg="#D5E8D4", border="#276A3C")

    draw_obj(ax2, 0.2, 1.8, 1.6, 0.85, "f2 : Feuille", attrs=["valeur = 2"], bg="#D5E8D4", border="#276A3C")
    draw_obj(ax2, 2.2, 1.8, 1.6, 0.85, "f1 : Feuille", attrs=["valeur = 1"], bg="#D5E8D4", border="#276A3C")

    # Links
    ax2.plot([3.0, 2.0], [4.25, 3.4], color="#1F2937", lw=1.5)
    ax2.plot([3.9, 4.8], [4.25, 3.4], color="#1F2937", lw=1.5)
    ax2.plot([1.5, 1.0], [2.85, 1.8], color="#1F2937", lw=1.5)
    ax2.plot([2.3, 2.8], [2.85, 1.8], color="#1F2937", lw=1.5)

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex2_class_object_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 4. EXERCISE 2: SEQUENCE DIAGRAM (n1.afficheElement())
# ==============================================================================
def render_ex2_sequence_diagram():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(5.5, 6.6, "Exercise 2: Sequence Diagram - Execution of n1.afficheElement()", ha="center", va="center", fontsize=13, weight="bold", color="#1E3A8A")

    lifelines = [
        (1.0, ":Main", "#E1D5E7", "#9673A6"),
        (2.8, "n1 : Noeud", "#FFF2CC", "#D6B656"),
        (4.8, "n2 : Noeud", "#FFF2CC", "#D6B656"),
        (6.8, "f2 : Feuille", "#D5E8D4", "#82B366"),
        (8.6, "f1 : Feuille", "#D5E8D4", "#82B366"),
        (10.2, "f3 : Feuille", "#D5E8D4", "#82B366"),
    ]

    for x, label, bg, border in lifelines:
        rect = patches.FancyBboxPatch((x - 0.7, 5.7), 1.4, 0.55, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.4)
        ax.add_patch(rect)
        ax.text(x, 5.97, label, ha="center", va="center", fontsize=8.5, weight="bold")
        ax.plot([x, x], [0.6, 5.7], ls="--", color="#9CA3AF", lw=1.2, zorder=1)

    # Activations
    def draw_act(x, y1, y2, bg, border):
        ax.add_patch(patches.Rectangle((x - 0.08, y2), 0.16, y1 - y2, fc=bg, ec=border, lw=1.2, zorder=3))

    draw_act(1.0, 5.3, 0.9, "#E1D5E7", "#9673A6")
    draw_act(2.8, 5.0, 1.2, "#FFF2CC", "#D6B656")
    draw_act(4.8, 4.6, 2.2, "#FFF2CC", "#D6B656")
    draw_act(6.8, 4.2, 3.4, "#D5E8D4", "#82B366")
    draw_act(8.6, 3.1, 2.3, "#D5E8D4", "#82B366")
    draw_act(10.2, 1.8, 1.3, "#D5E8D4", "#82B366")

    # Messages
    # 1: Main -> n1
    ax.annotate("", xy=(2.72, 5.0), xytext=(1.08, 5.0), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax.text(1.9, 5.12, "1: afficheElement()", ha="center", va="bottom", fontsize=8, weight="bold")

    # 2: n1 -> n2
    ax.annotate("", xy=(4.72, 4.6), xytext=(2.88, 4.6), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax.text(3.8, 4.72, "2: afficheElement()", ha="center", va="bottom", fontsize=8, weight="bold")

    # 3: n2 -> f2
    ax.annotate("", xy=(6.72, 4.2), xytext=(4.88, 4.2), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax.text(5.8, 4.32, "3: afficheElement() [print 2]", ha="center", va="bottom", fontsize=7.5, weight="bold")

    ax.annotate("", xy=(4.88, 3.4), xytext=(6.72, 3.4), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))

    # 4: n2 -> f1
    ax.annotate("", xy=(8.52, 3.1), xytext=(4.88, 3.1), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax.text(6.7, 3.22, "4: afficheElement() [print 1]", ha="center", va="bottom", fontsize=7.5, weight="bold")

    ax.annotate("", xy=(4.88, 2.3), xytext=(8.52, 2.3), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))

    # Return n2 -> n1
    ax.annotate("", xy=(2.88, 2.0), xytext=(4.72, 2.0), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))

    # 5: n1 -> f3
    ax.annotate("", xy=(10.12, 1.8), xytext=(2.88, 1.8), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax.text(6.5, 1.92, "5: afficheElement() [print 3]", ha="center", va="bottom", fontsize=7.5, weight="bold")

    ax.annotate("", xy=(2.88, 1.3), xytext=(10.12, 1.3), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))

    # Return n1 -> Main
    ax.annotate("", xy=(1.08, 1.0), xytext=(2.72, 1.0), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex2_sequence_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 5. EXERCISE 3: CLASS & OBJECT DIAGRAMS
# ==============================================================================
def render_ex3_diagrams():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.0), dpi=200, gridspec_kw={"width_ratios": [1.1, 1]})
    for ax in [ax1, ax2]:
        ax.axis("off")

    # Subplot 1: Class Diagram
    ax1.set_xlim(0, 8.5)
    ax1.set_ylim(0, 6.5)
    ax1.text(4.25, 6.1, "Class Diagram: Authentication System", ha="center", va="center", fontsize=12, weight="bold", color="#1E3A8A")

    draw_uml_class(ax1, 0.3, 5.5, 2.7, 2.6, "IULogin",
                   attrs=["- gestionnaire: GestionnairePersonne", "- nom: string", "- motDePasse: string"],
                   methods=["+ IULogin()", "+ setGestionnaire(g): void", "+ demanderNom(): void",
                            "+ demanderMotDePasse(): void", "+ autoriserConnexion(): void",
                            "+ interdireConnexion(): void", "+ identification(): void"],
                   bg="#DAE8FC", border="#3B6790")

    draw_uml_class(ax1, 4.4, 5.5, 3.8, 1.7, "GestionnairePersonne",
                   attrs=["- lesPersonnes: Personne[*]"],
                   methods=["+ GestionnairePersonne()", "+ ajoute(p: Personne): void",
                            "+ verifierMotDePasse(nom, mdp): bool"],
                   bg="#D5E8D4", border="#276A3C")

    draw_uml_class(ax1, 4.4, 2.8, 3.8, 1.7, "Personne",
                   attrs=["- nom: string", "- motDePasse: string"],
                   methods=["+ Personne(nom, mdp)", "+ getNom(): string", "+ getMotDePasse(): string"],
                   bg="#FFE6CC", border="#D79B00")

    # Association IULogin -> GestionnairePersonne
    ax1.annotate("", xy=(4.4, 4.6), xytext=(3.0, 4.6), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1F2937"))
    ax1.text(3.7, 4.8, "1 -gestionnaire", ha="center", va="bottom", fontsize=8.5, weight="bold")

    # Aggregation GestionnairePersonne -> Personne
    ax1.plot([6.3, 6.3], [3.8, 2.8], color="#276A3C", lw=1.5)
    diamond = patches.Polygon([[6.3, 3.8], [6.42, 3.7], [6.3, 3.6], [6.18, 3.7]], closed=True, fc="white", ec="#276A3C", lw=1.5)
    ax1.add_patch(diamond)
    ax1.text(6.45, 3.3, "* -lesPersonnes", ha="left", va="center", fontsize=8.5, weight="bold", color="#276A3C")

    # Subplot 2: Object Diagram (Execution of identification)
    ax2.set_xlim(0, 7.5)
    ax2.set_ylim(0, 6.5)
    ax2.text(3.75, 6.1, "Object Diagram: During identification()", ha="center", va="center", fontsize=12, weight="bold", color="#1E3A8A")

    def draw_obj(ax, x, y, w, h, name, attrs=None, bg="#DAE8FC", border="#3B6790"):
        rect = patches.FancyBboxPatch((x, y - h), w, h, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y - 0.22, name, ha="center", va="center", fontsize=9, weight="bold")
        if attrs:
            ax.plot([x, x + w], [y - 0.4, y - 0.4], color=border, lw=1)
            curr_y = y - 0.58
            for a in attrs:
                ax.text(x + 0.1, curr_y, a, ha="left", va="center", fontsize=8)
                curr_y -= 0.22

    draw_obj(ax2, 0.4, 5.5, 3.0, 1.2, "unIULogin : IULogin",
             attrs=['nom = "nom2"', 'motDePasse = "motdepasse2"'], bg="#DAE8FC", border="#3B6790")

    draw_obj(ax2, 4.2, 5.5, 3.1, 0.6, "unGestionnaire : GestionnairePersonne", bg="#D5E8D4", border="#276A3C")

    # Link unIULogin to unGestionnaire
    ax2.plot([3.4, 4.2], [5.0, 5.0], color="#1F2937", lw=1.5)
    ax2.text(3.8, 5.15, "gestionnaire", ha="center", va="bottom", fontsize=8)

    # 3 Personne objects
    draw_obj(ax2, 4.2, 4.3, 3.1, 1.0, "p1 : Personne", attrs=['nom = "nom1"', 'motDePasse = "motdepasse1"'], bg="#FFE6CC", border="#D79B00")
    draw_obj(ax2, 4.2, 3.0, 3.1, 1.0, "p2 : Personne", attrs=['nom = "nom2"', 'motDePasse = "motdepasse2"'], bg="#FFE6CC", border="#D79B00")
    draw_obj(ax2, 4.2, 1.7, 3.1, 1.0, "p3 : Personne", attrs=['nom = "nom3"', 'motDePasse = "motdepasse3"'], bg="#FFE6CC", border="#D79B00")

    # Links from unGestionnaire to p1, p2, p3
    for y_p in [3.8, 2.5, 1.2]:
        ax2.plot([4.2, 3.9, 3.9, 4.2], [4.9, 4.9, y_p, y_p], color="#276A3C", lw=1.2)

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex3_class_object_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 6. EXERCISE 3: ACTIVITY DIAGRAM (IULogin.identification)
# ==============================================================================
def render_ex3_activity_diagram():
    fig, ax = plt.subplots(figsize=(8, 7.5), dpi=200)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(4.0, 8.6, "Exercise 3: Activity Diagram - IULogin.identification()", ha="center", va="center", fontsize=13, weight="bold", color="#1E3A8A")

    # Initial node (black circle)
    start_circle = patches.Circle((4.0, 8.0), 0.16, fc="black", ec="black")
    ax.add_patch(start_circle)

    # Rounded action boxes
    def draw_action(y, text, w=4.4, h=0.55, bg="#DAE8FC", border="#3B6790"):
        rect = patches.FancyBboxPatch((4.0 - w/2, y - h/2), w, h, boxstyle="round,pad=0.08", ec=border, fc=bg, lw=1.4)
        ax.add_patch(rect)
        ax.text(4.0, y, text, ha="center", va="center", fontsize=9, weight="bold")

    # Arrow down
    def draw_down_arrow(y1, y2, x=4.0):
        ax.annotate("", xy=(x, y2), xytext=(x, y1), arrowprops=dict(arrowstyle="->", lw=1.4, color="#1F2937"))

    draw_down_arrow(7.84, 7.3)
    draw_action(7.0, "demanderNom()")

    draw_down_arrow(6.72, 6.2)
    draw_action(5.9, "demanderMotDePasse()")

    draw_down_arrow(5.62, 5.1)
    draw_action(4.7, "res = gestionnaire.verifierMotDePasse(nom, motDePasse)", w=5.8, bg="#D5E8D4", border="#276A3C")

    draw_down_arrow(4.42, 3.8)

    # Decision Rhombus
    decision = patches.Polygon([[4.0, 3.8], [4.4, 3.5], [4.0, 3.2], [3.6, 3.5]], closed=True, fc="#FFF2CC", ec="#D6B656", lw=1.5)
    ax.add_patch(decision)

    # Branch left: [res == true] -> autoriserConnexion()
    ax.plot([3.6, 2.0, 2.0], [3.5, 3.5, 2.5], color="#1F2937", lw=1.4)
    ax.annotate("", xy=(2.0, 2.4), xytext=(2.0, 2.5), arrowprops=dict(arrowstyle="->", lw=1.4, color="#1F2937"))
    ax.text(2.6, 3.65, "[res == true]", ha="center", va="bottom", fontsize=8.5, weight="bold", color="#15803D")

    rect_auth = patches.FancyBboxPatch((0.8, 1.8), 2.4, 0.55, boxstyle="round,pad=0.08", ec="#276A3C", fc="#D5E8D4", lw=1.4)
    ax.add_patch(rect_auth)
    ax.text(2.0, 2.08, "autoriserConnexion()", ha="center", va="center", fontsize=8.5, weight="bold")

    # Branch right: [res == false] -> interdireConnexion()
    ax.plot([4.4, 6.0, 6.0], [3.5, 3.5, 2.5], color="#1F2937", lw=1.4)
    ax.annotate("", xy=(6.0, 2.4), xytext=(6.0, 2.5), arrowprops=dict(arrowstyle="->", lw=1.4, color="#1F2937"))
    ax.text(5.4, 3.65, "[res == false]", ha="center", va="bottom", fontsize=8.5, weight="bold", color="#B91C1C")

    rect_deny = patches.FancyBboxPatch((4.8, 1.8), 2.4, 0.55, boxstyle="round,pad=0.08", ec="#B85450", fc="#F8CECC", lw=1.4)
    ax.add_patch(rect_deny)
    ax.text(6.0, 2.08, "interdireConnexion()", ha="center", va="center", fontsize=8.5, weight="bold")

    # Merge Rhombus
    merge = patches.Polygon([[4.0, 1.2], [4.4, 0.9], [4.0, 0.6], [3.6, 0.9]], closed=True, fc="#FFF2CC", ec="#D6B656", lw=1.5)
    ax.add_patch(merge)

    ax.plot([2.0, 2.0, 3.6], [1.8, 0.9, 0.9], color="#1F2937", lw=1.4)
    ax.plot([6.0, 6.0, 4.4], [1.8, 0.9, 0.9], color="#1F2937", lw=1.4)

    # Final Node (Bullseye)
    draw_down_arrow(0.6, 0.3)
    end_outer = patches.Circle((4.0, 0.15), 0.16, fc="white", ec="black", lw=1.5)
    end_inner = patches.Circle((4.0, 0.15), 0.10, fc="black", ec="black")
    ax.add_patch(end_outer)
    ax.add_patch(end_inner)

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex3_activity_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


if __name__ == "__main__":
    render_ex1_class_diagram()
    render_ex1_sequence_diagram()
    render_ex2_diagrams()
    render_ex2_sequence_diagram()
    render_ex3_diagrams()
    render_ex3_activity_diagram()
    print("All diagrams rendered successfully!")
