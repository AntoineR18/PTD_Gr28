import compte_medailles


def affichage_medaille_pays_JO(pays, annee):
    """
    Affiche et sauvegarde le nombre de médailles d'or, d'argent, de bronze et le total
    pour un pays donné et une année (toutes saisons confondues).
    """
    annee = str(annee)
    pays = pays.strip().title()

    gold = compte_medailles.medaille_pays_annee(pays, annee, "Gold")
    silver = compte_medailles.medaille_pays_annee(pays, annee, "Silver")
    bronze = compte_medailles.medaille_pays_annee(pays, annee, "Bronze")
    total = gold + silver + bronze

    texte = (
        f"Médailles de {pays} aux JO de {annee} :\n"
        f"Or     : {gold}\n"
        f"Argent : {silver}\n"
        f"Bronze : {bronze}\n"
        f"Total  : {total}"
    )

    print(texte)

    with open("Resultat/Question3.txt", "w", encoding="utf-8") as f:
        f.write(texte + "\n")
