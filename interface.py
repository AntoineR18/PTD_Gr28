import importlib
import sys
import os
import subprocess


def main():
    streamlit_process = None

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
        print("6. Question 3 (pandas) : Synthèse des médailles obtenues par un pays sur"
              "une année donnée.")
        print("7. Question 3 bonnus (streamlit)  : Application"
              " interactive des médailles.")
        print("Streamlit_Close. Fermer  Streamlit")
        print("0. Quitter")

        choix = input("Votre choix : ")

        try:
            if choix == "1":
                import Question1
            elif choix == "2":
                import Question1_panda
            elif choix == "3":
                annee = int(input("Entrez l'année des JO : "))
                import Question2
                Question2.afficher_bornes_medailles(annee)
            elif choix == "4":
                annee = int(input("Entrez l'année des JO : "))
                import Question2_panda
                Question2_panda.afficher_bornes_medailles_par_nation_pandas(annee)
            elif choix == "5":
                pays = input("Entrez le nom du pays : ")
                annee = input("Entrez l'année des JO : ")
                import Question3
                Question3.affichage_medaille_pays_JO(pays, annee)
            elif choix == "6":
                pays = input("Entrez le nom du pays : ")
                annee = int(input("Entrez l'année des JO : "))
                saison = input("Entrez la saison (Summer/Winter) : ")
                import Question3_Pandas
                Question3_Pandas.affichage_medaille_pays_JO(pays, annee, saison)
            elif choix == "7":
                try:
                    import streamlit
                except ModuleNotFoundError:
                    installer = input("⚠️ Streamlit n'est pas installé. Voulez-vous l'installer ? (o/n) : ").lower()
                    if installer == "o":
                        subprocess.call(["pip", "install", "streamlit"])
                        import streamlit
                    else:
                        print("Streamlit non installé.")
                        continue

                if streamlit_process is None or streamlit_process.poll() is not None:
                    print("Lancement de l'application Streamlit...")
                    streamlit_process = subprocess.Popen(["streamlit", "run", "Question3_Pandas_Streamlit.py"])
                else:
                    print("Streamlit est déjà en cours.")
            elif choix == "8":
                if streamlit_process is not None and streamlit_process.poll() is None:
                    print("Fermeture de Streamlit...")
                    streamlit_process.terminate()
                    streamlit_process = None
                else:
                    print("Aucune application Streamlit en cours.")
            elif choix == "0":
                if streamlit_process is not None and streamlit_process.poll() is None:
                    print("Fermeture de Streamlit avant de quitter...")
                    streamlit_process.terminate()
                print("À bientôt !")
                break
            else:
                print("Choix invalide. Réessayez.")
        except Exception as e:
            print(f"❌ Erreur : {e}")


        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()
