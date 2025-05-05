import importlib
import sys


def main():
    while True:
        print("=== Menu PTD Groupe 28 ===")
        print("1. Question 1 : Déterminer le nombre de médailles gagnées par"
              " Michael Phelps.")
        print("2. Question 1 (pandas) : Question 1 + Le type de médaille.")
        print("3. Question 2 : Calculer les bornes de médailles par pays pour"
              " une année donnée.")
        print("4. Question 2 (pandas) : Idem avec pandas.")
         print("5. Question 3 : Synthèse des médailles obtenues par un pays sur une"
               " année donnée.")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            try:
                import Question1
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de Question1 : {e}")
        elif choix == "2":
            try:
                import Question1_panda
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de Question1_panda : {e}")
        elif choix == "3":
            try:
                annee = input("Entrez l'année des JO souhaité : ")
                annee = int(annee)
                module_q2 = importlib.import_module("Question2")
                module_q2.afficher_bornes_medailles(annee)
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de Question2 : {e}")
        elif choix == "4":
            try:
                annee = int(input("Entrez l'année des JO souhaité : "))
                module_q2p = importlib.import_module("Question2_panda")
                module_q2p.afficher_bornes_medailles_par_nation_pandas(annee)
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de Question2_panda : {e}")
        elif choix == "5":
            try:
                pays = input("Entrez le nom du pays : ")
                annee = input("Entrez l'année des JO : ")
                module_q3 = importlib.import_module("Question3")
                module_q3.affichage_medaille_pays_JO(pays, annee)
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de Question3 : {e}")
        elif choix == "0":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Réessayez.")

        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()
