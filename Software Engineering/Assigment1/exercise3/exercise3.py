"""
Exercise 3: User Authentication System (IULogin, GestionnairePersonne, Personne)
Tutorial 1 - UML Modeling (Software Engineering)
"""
from typing import List, Optional


# =====================================================================
# Personne Class
# =====================================================================
class Personne:
    """Represents a registered user with credentials."""

    def __init__(self, nom: str, motDePasse: str) -> None:
        self.nom = nom
        self.motDePasse = motDePasse

    def getNom(self) -> str:
        return self.nom

    def getMotDePasse(self) -> str:
        return self.motDePasse


# =====================================================================
# GestionnairePersonne Class
# =====================================================================
class GestionnairePersonne:
    """Manages the list of authorized persons."""

    def __init__(self) -> None:
        self.lesPersonnes: List[Personne] = []

    def ajoute(self, p: Personne) -> None:
        self.lesPersonnes.append(p)

    def verifierMotDePasse(self, nom: str, motDePasse: str) -> bool:
        """
        Verifies credentials against the stored persons list.
        Corresponds to loop CombinedFragment in Figure 5.
        """
        for p in self.lesPersonnes:
            n = p.getNom()
            mdp = p.getMotDePasse()
            if n.strip() == nom.strip() and mdp.strip() == motDePasse.strip():
                return True
        return False


# =====================================================================
# IULogin Class (User Interface)
# =====================================================================
class IULogin:
    """User interface handling login interactions."""

    def __init__(self) -> None:
        self.gestionnaire: Optional[GestionnairePersonne] = None
        self.nom: str = ""
        self.motDePasse: str = ""

    def setGestionnaire(self, g: GestionnairePersonne) -> None:
        self.gestionnaire = g

    def demanderNom(self, simulated_input: Optional[str] = None) -> None:
        if simulated_input is not None:
            self.nom = simulated_input
            print(f"Entrer le nom : {self.nom}")
        else:
            self.nom = input("Entrer le nom : ")

    def demanderMotDePasse(self, simulated_input: Optional[str] = None) -> None:
        if simulated_input is not None:
            self.motDePasse = simulated_input
            print(f"Entrer le mot de passe : {self.motDePasse}")
        else:
            self.motDePasse = input("Entrer le mot de passe : ")

    def autoriserConnexion(self) -> None:
        print("Connexion autorisée")

    def interdireConnexion(self) -> None:
        print("Connexion interdite")

    def identification(self, simulated_nom: Optional[str] = None, simulated_mdp: Optional[str] = None) -> None:
        """
        Full authentication procedure matching the sequence and activity diagrams.
        """
        self.demanderNom(simulated_nom)
        self.demanderMotDePasse(simulated_mdp)

        if self.gestionnaire is not None:
            res = self.gestionnaire.verifierMotDePasse(self.nom, self.motDePasse)
            if res:
                self.autoriserConnexion()
            else:
                self.interdireConnexion()
        else:
            self.interdireConnexion()


# =====================================================================
# Main execution matching tutorial setup
# =====================================================================
def main():
    unIULogin = IULogin()
    unGestionnaire = GestionnairePersonne()

    # Initialization phase
    p1 = Personne("nom1", "motdepasse1")
    p2 = Personne("nom2", "motdepasse2")
    p3 = Personne("nom3", "motdepasse3")

    unIULogin.setGestionnaire(unGestionnaire)

    unGestionnaire.ajoute(p1)
    unGestionnaire.ajoute(p2)
    unGestionnaire.ajoute(p3)

    print("=== Test 1: Successful Login (nom2, motdepasse2) ===")
    unIULogin.identification(simulated_nom="nom2", simulated_mdp="motdepasse2")

    print("\n=== Test 2: Failed Login (nom1, wrong_password) ===")
    unIULogin.identification(simulated_nom="nom1", simulated_mdp="wrong_password")


if __name__ == "__main__":
    main()
