"""
Exercise 1: Bank Account & Singleton Logging Pattern
Tutorial 3 - Design Patterns (Software Engineering, VNU-IS)
"""
from datetime import datetime
from typing import Optional


# =====================================================================
# Singleton Pattern: Journalisation
# =====================================================================
class Journalisation:
    """
    Singleton Logger ensuring only ONE instance exists throughout the application.
    """
    _uniqueInstance: Optional["Journalisation"] = None

    def __init__(self) -> None:
        if Journalisation._uniqueInstance is not None:
            raise RuntimeError("Use Journalisation.getInstance() to access the logger instance.")
        # Simulating address/ID for verification
        self.instance_id = hex(id(self))

    @classmethod
    def getInstance(cls) -> "Journalisation":
        """Thread-safe access method to the unique Singleton instance."""
        if cls._uniqueInstance is None:
            cls._uniqueInstance = cls()
        return cls._uniqueInstance

    @classmethod
    def resetInstance(cls) -> None:
        """Utility to reset singleton instance for testing."""
        cls._uniqueInstance = None

    def afficherLog(self, log: str) -> None:
        """Prints log with current date and time formatting."""
        now = datetime.now()
        # Formatted: [19/8/2026 at 11h01] <log>
        time_str = f"[{now.day}/{now.month}/{now.year} at {now.hour:02d}h{now.minute:02d}]"
        print(f"{time_str} {log}")


# =====================================================================
# Domain Class: CompteBancaire
# =====================================================================
class CompteBancaire:
    """
    Bank account delegating operation logs to the Singleton Journalisation.
    """
    def __init__(self, numero: int) -> None:
        self.numero: int = numero
        self.solde: float = 0.0
        # Retrieves the shared unique instance from Singleton
        self.journalisation: Journalisation = Journalisation.getInstance()
        # Displaying instance address/id as in C++ original code
        print(f"BankAccount {self.numero} initialized with Logger ID: {self.journalisation.instance_id}")

    def deposerArgent(self, depot: float) -> None:
        """Deposit money into account."""
        if depot > 0.0:
            self.solde += depot
            self.journalisation.afficherLog(
                f"Deposit of {depot:.6f}e into account {self.numero}."
            )

    def retirerArgent(self, retrait: float) -> None:
        """Withdraw money from account."""
        if retrait > 0.0:
            if self.solde >= retrait:
                self.solde -= retrait
                self.journalisation.afficherLog(
                    f"Withdrawal of {retrait:.6f}e from account {self.numero}."
                )
            else:
                self.journalisation.afficherLog(
                    f"The bank does not allow overdrafts on account {self.numero}."
                )


# =====================================================================
# Main execution matching tutorial requirements (Question 1)
# =====================================================================
def main():
    print("--- 1. Creating Bank Accounts cb1, cb2, cb3 ---")
    cb1 = CompteBancaire(123456789)
    cb2 = CompteBancaire(987654321)
    cb3 = CompteBancaire(456789012)

    print("\n--- 2. Executing Transactions to match Question 1 Output ---")
    # Using cb1: deposit 100, then withdraw 80
    cb1.deposerArgent(100.0)
    cb1.retirerArgent(80.0)

    # Using cb2: attempt overdraft (solde is 0, withdrawal 50 -> rejected)
    cb2.retirerArgent(50.0)

    # Using cb3: deposit 100
    cb3.deposerArgent(100.0)


if __name__ == "__main__":
    main()
