





import pandas as pd

# Données : Séquences ADN, Longueur, Pourcentage de GC
data = {
    "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

# Création d'un DataFrame
df = pd.DataFrame(data)
#1)creation de tableau
print("**************** Creation et affichage *******************************\n")
print("Tableau des séquences ADN :")
print(df)
print("*****************affichege de longueur*****************************\n ")
# 2)Sélectionner la colonne "Longueur"
longueur = df["Longueur"]
print(longueur)
#3)Filtrer les séquences avec une longueur superieur à 10
print("************* Filtrage avec longueur >10 *************************\n")
filtered_df = df[df["Longueur"] > 10]
print(filtered_df)
#4)la moyenne de pourcentage GC 
print("**************moyenne de pourcentage GC%****************************\n")
average_GC=df["Pourcentage GC"].mean()
print(f"Pourcentage GC : {average_GC:.3f}")

#5)Ajouter une nouvelle colonne avec categorie
print("******************* Ajout d'une nouvelle colonne *********************\n")
# Ajouter une nouvelle colonne "categorie pourcentage"
df["Catégorie Pourcentage GC"] = df["Pourcentage GC"].apply(lambda x: "riche" if x > 55 else ("moyen" if 45 <= x <= 55 else "faible"))

print(df)
#6)ajouter une colonne de nombre de G de chaque sequence
print("*********************** Nombre de G ****************************\n")
df["Nombre de G"] = df["Séquence"].str.count('G')

print(df, "\n")

#7)calcule de l'ecart typede GC% et de la longueur
print("********écart-type du %GC et de la longueur des séquences********\n")
std_GC=df ['Pourcentage GC'].std()

std_longueur=df ["Longueur"].std()

print(f"Ecart type de %GC: {std_GC:.2f}")

print(f"Ecart type de la longeur:{std_longueur:.2f}\n")
#sauvegarder dataframe dans un fichier csv
df.to_csv("tableau_sequence.csv",index=False)
