import compte_medailles


def affichage_medaille_pays_JO(pays, annee):
    """
    Affiche le nombre de médailles d'or, d'argent, de bronze et le total
    pour un pays donné et une année (toutes saisons confondues).
    """
    annee = str(annee)
    pays = pays.strip().title()

    gold = compte_medailles.medaille_pays_annee(pays, annee, "Gold")
    silver = compte_medailles.medaille_pays_annee(pays, annee, "Silver")
    bronze = compte_medailles.medaille_pays_annee(pays, annee, "Bronze")
    total = gold + silver + bronze

    print(f"Médailles de {pays} aux JO de {annee} :")
    print(f"Or     : {gold}")
    print(f"Argent : {silver}")
    print(f"Bronze : {bronze}")
    print(f"Total  : {total}")
