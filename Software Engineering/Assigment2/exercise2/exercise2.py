"""
Exercise 2: Logging System & Decorator Design Pattern
Tutorial 3 - Design Patterns (Software Engineering, VNU-IS)
"""
from abc import ABC, abstractmethod
import os


# =====================================================================
# 1. Component Interface
# =====================================================================
class Logger(ABC):
    """Abstract Component defining common interface for all loggers."""

    @abstractmethod
    def log(self, msg: str) -> None:
        pass


# =====================================================================
# 2. Concrete Components
# =====================================================================
class ConsoleLogger(Logger):
    """Logs messages directly to the standard console output."""

    def log(self, msg: str) -> None:
        print(msg)


class FileLogger(Logger):
    """Logs messages by appending them to a specified file."""

    def __init__(self, nomFichier: str) -> None:
        self.nomFichier_ = nomFichier

    def log(self, msg: str) -> None:
        try:
            with open(self.nomFichier_, "a", encoding="utf-8") as f:
                f.write(msg + "\n")
        except Exception as e:
            print(f"Erreur : impossible d'ouvrir le fichier {self.nomFichier_} : {e}")


# =====================================================================
# 3. Base Decorator
# =====================================================================
class DecorateurLogger(Logger):
    """
    Abstract Decorator maintaining a reference to a Logger component
    and conforming to the Logger interface.
    """

    def __init__(self, logger: Logger) -> None:
        self.logger_ = logger

    def log(self, msg: str) -> None:
        # Default forwarding behavior
        self.logger_.log(msg)


# =====================================================================
# 4. Concrete Decorators
# =====================================================================
class HTMLLogger(DecorateurLogger):
    """
    Decorates log messages by wrapping them inside HTML tags:
    <HTML><BODY> <b> <msg> </b> </BODY> </HTML>
    """

    def formaterHTML(self, msg: str) -> str:
        return f"<HTML><BODY> <b> {msg} </b> </BODY> </HTML>"

    def log(self, msg: str) -> None:
        html_msg = self.formaterHTML(msg)
        self.logger_.log(html_msg)


class EncryptLogger(DecorateurLogger):
    """
    Decorates log messages by circularly shifting each character
    n positions to the left (default n = 4).
    E.g. 'Message d'erreur n°1' shifted 4 positions -> 'age d'erreur n°1Mess'
    """

    def __init__(self, logger: Logger, shift: int = 4) -> None:
        super().__init__(logger)
        self.shift = shift

    def crypter(self, msg: str) -> str:
        if not msg:
            return msg
        n = self.shift % len(msg)
        return msg[n:] + msg[:n]

    def log(self, msg: str) -> None:
        encrypted_msg = self.crypter(msg)
        self.logger_.log(encrypted_msg)


# =====================================================================
# Main execution matching tutorial requirements (Question 6)
# =====================================================================
def main():
    print("=== Case 1: EncryptLogger attached to ConsoleLogger ===")
    cLogger1 = ConsoleLogger()
    eLogger1 = EncryptLogger(cLogger1, shift=4)

    # Testing specific tutorial example first:
    test_str = "Message d'erreur n°1"
    print(f"Sample test: '{test_str}' -> '{eLogger1.crypter(test_str)}'")

    print("\nGenerating 10 encrypted log messages to console:")
    for i in range(10):
        eLogger1.log(f"{i} : A message to log")

    print("\n=== Case 2: HTMLLogger attached to FileLogger ===")
    output_filename = "FichierLog1.html"
    # Ensure fresh file
    if os.path.exists(output_filename):
        os.remove(output_filename)

    fLogger1 = FileLogger(output_filename)
    hLogger1 = HTMLLogger(fLogger1)

    print(f"Generating 10 HTML formatted messages into '{output_filename}'...")
    for i in range(10):
        hLogger1.log(f"{i} : A message to log")

    print("File content preview:")
    with open(output_filename, "r", encoding="utf-8") as f:
        print(f.read().strip())

    print("\n=== Case 3: Composed Chaining (HTML + Encryption + FileLogger) ===")
    combo_file = "FichierLog_Combo.html"
    if os.path.exists(combo_file):
        os.remove(combo_file)
    comboLogger = HTMLLogger(EncryptLogger(FileLogger(combo_file)))
    comboLogger.log("Critical Error Occurred")
    with open(combo_file, "r", encoding="utf-8") as f:
        print("Combo output:", f.read().strip())


if __name__ == "__main__":
    main()
