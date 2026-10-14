"""
Render publication-quality UML diagrams matching Assignment 2 (TD3) drawio files.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"D:\Job\thothan\VNU\Software Engineering\Assigment2\diagram_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def draw_uml_class(ax, x, y, w, h, name, stereotype=None, attrs=None, methods=None, bg="#DAE8FC", border="#4A6FA5"):
    attrs = attrs or []
    methods = methods or []
    rect = patches.FancyBboxPatch((x, y - h), w, h, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.8, zorder=2)
    ax.add_patch(rect)

    header_str = f"«{stereotype}»\n{name}" if stereotype else name
    ax.text(x + w / 2, y - 0.28, header_str, ha="center", va="center", fontsize=9.5, weight="bold", color="#111827", zorder=3)

    div1_y = y - (0.58 if stereotype else 0.45)
    ax.plot([x, x + w], [div1_y, div1_y], color=border, lw=1.2, zorder=3)

    curr_y = div1_y - 0.16
    for a in attrs:
        is_static = a.startswith("__static__")
        display_a = a.replace("__static__", "")
        weight = "bold" if is_static else "normal"
        t = ax.text(x + 0.12, curr_y, display_a, ha="left", va="center", fontsize=8.5, color="#1F2937", zorder=3, weight=weight)
        if is_static:
            # Underline static member
            ax.plot([x + 0.12, x + 0.12 + len(display_a) * 0.14], [curr_y - 0.08, curr_y - 0.08], color="#1F2937", lw=1, zorder=4)
        curr_y -= 0.22

    div2_y = y - h + (len(methods) * 0.22 + 0.12 if methods else 0.1)
    if div2_y < div1_y:
        ax.plot([x, x + w], [div2_y, div2_y], color=border, lw=1.2, zorder=3)
        curr_y = div2_y - 0.16
        for m in methods:
            is_static = m.startswith("__static__")
            display_m = m.replace("__static__", "")
            weight = "bold" if is_static else "normal"
            ax.text(x + 0.12, curr_y, display_m, ha="left", va="center", fontsize=8.5, color="#1F2937", zorder=3, weight=weight)
            if is_static:
                ax.plot([x + 0.12, x + 0.12 + len(display_m) * 0.13], [curr_y - 0.08, curr_y - 0.08], color="#1F2937", lw=1, zorder=4)
            curr_y -= 0.22


# ==============================================================================
# 1. EXERCISE 1: SINGLETON CLASS DIAGRAM (CompteBancaire & Journalisation)
# ==============================================================================
def render_ex1_singleton_diagram():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(5.5, 5.6, "Exercise 1: Class Diagram - Singleton Pattern (Journalisation)", ha="center", va="center", fontsize=13, weight="bold", color="#1E3A8A")

    draw_uml_class(ax, 0.6, 4.8, 3.8, 2.0, "CompteBancaire",
                   attrs=["- numero: int", "- solde: double", "- journalisation: Journalisation"],
                   methods=["+ CompteBancaire(numero: int)", "+ deposerArgent(depot: double): void", "+ retirerArgent(retrait: double): void"],
                   bg="#DAE8FC", border="#3B6790")

    draw_uml_class(ax, 5.8, 4.9, 4.6, 2.2, "Journalisation", stereotype="Singleton",
                   attrs=["__static__- uniqueInstance: Journalisation = null"],
                   methods=["- Journalisation()", "__static__+ getInstance(): Journalisation", "+ afficherLog(log: string): void"],
                   bg="#D5E8D4", border="#276A3C")

    # Association CompteBancaire -> Journalisation
    ax.annotate("", xy=(5.8, 3.8), xytext=(4.4, 3.8), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1F2937"))
    ax.text(5.1, 4.0, "1 -journalisation", ha="center", va="bottom", fontsize=8.5, weight="bold")

    # Self-reference for Singleton instance
    ax.plot([8.1, 9.4, 9.4, 8.8], [4.9, 4.9, 5.4, 5.4], color="#276A3C", lw=1.5)
    ax.annotate("", xy=(8.8, 4.9), xytext=(8.8, 5.4), arrowprops=dict(arrowstyle="->", lw=1.5, color="#276A3C"))
    ax.text(9.5, 5.15, "-uniqueInstance", ha="left", va="center", fontsize=8, weight="bold", color="#276A3C")

    # Note explaining Singleton getInstance logic
    note = patches.FancyBboxPatch((5.8, 0.8), 4.6, 1.2, boxstyle="round,pad=0.08", ec="#D6B656", fc="#FFF2CC", lw=1.2)
    ax.add_patch(note)
    ax.text(6.0, 1.4, "Note: getInstance() Implementation:\nif (uniqueInstance == null)\n    uniqueInstance = new Journalisation();\nreturn uniqueInstance;",
            ha="left", va="center", fontsize=8, family="monospace", color="#78350F")

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex1_singleton_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 2. EXERCISE 2: DECORATOR CLASS DIAGRAM
# ==============================================================================
def render_ex2_class_diagram():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6.0, 7.6, "Exercise 2: Class Diagram - Decorator Pattern for Logging", ha="center", va="center", fontsize=14, weight="bold", color="#1E3A8A")

    # Component: Logger
    draw_uml_class(ax, 3.8, 7.0, 3.6, 1.2, "Logger", stereotype="interface",
                   methods=["+ log(msg: string): void {abstract}"],
                   bg="#DAE8FC", border="#3B6790")

    # Concrete Component 1: ConsoleLogger
    draw_uml_class(ax, 0.5, 4.8, 2.8, 1.2, "ConsoleLogger",
                   methods=["+ log(msg: string): void"],
                   bg="#D5E8D4", border="#276A3C")

    # Concrete Component 2: FileLogger
    draw_uml_class(ax, 3.6, 4.8, 3.4, 1.5, "FileLogger",
                   attrs=["- nomFichier_: string"],
                   methods=["+ FileLogger(nomFichier: string)", "+ log(msg: string): void"],
                   bg="#D5E8D4", border="#276A3C")

    # Base Decorator: DecorateurLogger
    draw_uml_class(ax, 7.4, 4.8, 3.8, 1.5, "DecorateurLogger", stereotype="abstract",
                   attrs=["# logger_: Logger"],
                   methods=["+ DecorateurLogger(logger: Logger)", "+ log(msg: string): void"],
                   bg="#FFE6CC", border="#D79B00")

    # Realization arrows to Logger
    ax.annotate("", xy=(4.6, 5.8), xytext=(1.9, 4.8), arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))
    ax.annotate("", xy=(5.3, 5.8), xytext=(5.3, 4.8), arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))
    ax.annotate("", xy=(6.0, 5.8), xytext=(8.8, 4.8), arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))

    # Composition from DecorateurLogger to Logger
    ax.plot([10.2, 11.2, 11.2, 7.4], [4.1, 4.1, 6.4, 6.4], color="#D79B00", lw=1.6)
    diamond = patches.Polygon([[10.2, 4.1], [10.35, 4.22], [10.5, 4.1], [10.35, 3.98]], closed=True, fc="#D79B00", ec="#D79B00")
    ax.add_patch(diamond)
    ax.text(11.3, 5.25, "1 -logger_", ha="left", va="center", fontsize=8.5, weight="bold", color="#D79B00")

    # Concrete Decorator 1: HTMLLogger
    draw_uml_class(ax, 5.4, 2.5, 3.1, 1.5, "HTMLLogger",
                   methods=["+ HTMLLogger(logger: Logger)", "+ log(msg: string): void", "+ formaterHTML(msg: string): string"],
                   bg="#FFE6CC", border="#D79B00")

    # Concrete Decorator 2: EncryptLogger
    draw_uml_class(ax, 8.8, 2.5, 3.0, 1.7, "EncryptLogger",
                   attrs=["- shift: int = 4"],
                   methods=["+ EncryptLogger(logger, shift)", "+ log(msg: string): void", "+ crypter(msg: string): string"],
                   bg="#FFE6CC", border="#D79B00")

    # Inheritance to DecorateurLogger
    ax.annotate("", xy=(8.4, 3.3), xytext=(7.0, 2.5), arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))
    ax.annotate("", xy=(9.6, 3.3), xytext=(10.3, 2.5), arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1F2937", shrinkA=0, shrinkB=0, mutation_scale=15, fc="white"))

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex2_decorator_class_diagram.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


# ==============================================================================
# 3. EXERCISE 2: OBJECT & SEQUENCE DIAGRAMS (Q3 & Q4)
# ==============================================================================
def render_ex2_object_sequence_diagrams():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=200, gridspec_kw={"width_ratios": [1, 1.3]})
    for ax in [ax1, ax2]:
        ax.axis("off")

    # Subplot 1: Object Diagram (Q3)
    ax1.set_xlim(0, 6.5)
    ax1.set_ylim(0, 6)
    ax1.text(3.25, 5.6, "Object Diagram: HTMLLogger wrapping FileLogger (Q3)", ha="center", va="center", fontsize=11, weight="bold", color="#1E3A8A")

    def draw_obj(ax, x, y, w, h, name, attrs=None, bg="#FFE6CC", border="#D79B00"):
        rect = patches.FancyBboxPatch((x, y - h), w, h, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y - 0.22, name, ha="center", va="center", fontsize=9, weight="bold")
        if attrs:
            ax.plot([x, x + w], [y - 0.4, y - 0.4], color=border, lw=1)
            ax.text(x + w/2, y - 0.65, "\n".join(attrs), ha="center", va="center", fontsize=8.5)

    draw_obj(ax1, 0.4, 4.0, 2.5, 0.9, "hLogger : HTMLLogger", attrs=["logger_ = fLogger"], bg="#FFE6CC", border="#D79B00")
    draw_obj(ax1, 3.4, 4.0, 2.8, 0.9, "fLogger : FileLogger", attrs=['nomFichier_ = "FichierLog1.html"'], bg="#D5E8D4", border="#276A3C")

    ax1.plot([2.9, 3.4], [3.55, 3.55], color="#1F2937", lw=1.5)
    ax1.text(3.15, 3.75, "wraps", ha="center", va="bottom", fontsize=8.5, weight="bold")

    # Code snippet note below
    note = patches.FancyBboxPatch((0.4, 1.2), 5.8, 1.3, boxstyle="round,pad=0.08", ec="#9CA3AF", fc="#F3F4F6", lw=1.2)
    ax1.add_patch(note)
    ax1.text(0.6, 1.85, "Code execution:\nFileLogger fLogger = new FileLogger(\"FichierLog1.html\");\nHTMLLogger hLogger = new HTMLLogger(fLogger);",
             ha="left", va="center", fontsize=8.5, family="monospace", color="#1F2937")

    # Subplot 2: Sequence Diagram (Q4)
    ax2.set_xlim(0, 8.5)
    ax2.set_ylim(0, 6)
    ax2.text(4.25, 5.6, "Sequence Diagram: Saving Log in HTML format to File (Q4)", ha="center", va="center", fontsize=11, weight="bold", color="#1E3A8A")

    lifelines = [
        (1.0, ":Client / Main", "#E1D5E7", "#9673A6"),
        (3.8, "hLogger : HTMLLogger", "#FFE6CC", "#D79B00"),
        (7.0, "fLogger : FileLogger", "#D5E8D4", "#276A3C"),
    ]

    for x, label, bg, border in lifelines:
        rect = patches.FancyBboxPatch((x - 0.9, 4.8), 1.8, 0.5, boxstyle="square,pad=0", ec=border, fc=bg, lw=1.3)
        ax2.add_patch(rect)
        ax2.text(x, 5.05, label, ha="center", va="center", fontsize=8, weight="bold")
        ax2.plot([x, x], [0.6, 4.8], ls="--", color="#9CA3AF", lw=1.2, zorder=1)

    # Activations
    ax2.add_patch(patches.Rectangle((0.92, 1.0), 0.16, 3.5, fc="#E1D5E7", ec="#9673A6", lw=1.2, zorder=3))
    ax2.add_patch(patches.Rectangle((3.72, 1.4), 0.16, 2.8, fc="#FFE6CC", ec="#D79B00", lw=1.2, zorder=3))
    ax2.add_patch(patches.Rectangle((6.92, 1.8), 0.16, 1.4, fc="#D5E8D4", ec="#276A3C", lw=1.2, zorder=3))

    # Messages
    # 1: Client -> hLogger
    ax2.annotate("", xy=(3.72, 4.2), xytext=(1.08, 4.2), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax2.text(2.4, 4.35, "1: log(\"Message d'erreur n°1\")", ha="center", va="bottom", fontsize=8, weight="bold")

    # Self-call: formaterHTML
    ax2.plot([3.88, 4.4, 4.4, 3.88], [3.6, 3.6, 3.2, 3.2], color="#D79B00", lw=1.3)
    ax2.annotate("", xy=(3.88, 3.2), xytext=(4.1, 3.2), arrowprops=dict(arrowstyle="->", lw=1.3, color="#D79B00"))
    ax2.text(4.5, 3.4, "formaterHTML(msg)", ha="left", va="center", fontsize=7.5, weight="bold", color="#D79B00")

    # 2: hLogger -> fLogger
    ax2.annotate("", xy=(6.92, 2.8), xytext=(3.88, 2.8), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1F2937"))
    ax2.text(5.4, 2.95, "2: log(\"<HTML>...<b>msg</b>...</HTML>\")", ha="center", va="bottom", fontsize=7.5, weight="bold")

    # Return 2
    ax2.annotate("", xy=(3.88, 1.8), xytext=(6.92, 1.8), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))
    ax2.text(5.4, 1.95, "return", ha="center", va="bottom", fontsize=7.5, color="#4B5563")

    # Return 1
    ax2.annotate("", xy=(1.08, 1.4), xytext=(3.72, 1.4), arrowprops=dict(arrowstyle="->", ls="--", lw=1.1, color="#4B5563"))
    ax2.text(2.4, 1.55, "return", ha="center", va="bottom", fontsize=7.5, color="#4B5563")

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "ex2_object_sequence_diagrams.png")
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print("Saved", out_file)


if __name__ == "__main__":
    render_ex1_singleton_diagram()
    render_ex2_class_diagram()
    render_ex2_object_sequence_diagrams()
    print("Assignment 2 diagrams rendered successfully!")
