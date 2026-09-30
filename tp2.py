import math
import os

# Exercice 1: Generation des documents
def charger_documents(chemin_fichier):
    documents = {}
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            parts = ligne.split(': ', 1)
            if len(parts) == 2:
                doc_id_str, contenu = parts
                doc_id = int(doc_id_str.replace('doc', ''))
                documents[doc_id] = contenu
    return documents

# Exercice 2: Construction des index inverses
def construire_index(documents):
    index_inverse = {}
    for doc_id, texte in documents.items():
        mots = texte.lower().split()
        for mot in mots:
            if mot not in index_inverse:
                index_inverse[mot] = []
            if doc_id not in index_inverse[mot]:
                index_inverse[mot].append(doc_id)
    for mot in index_inverse:
        index_inverse[mot].sort()
    return index_inverse

# Exercice 3: Intersection de deux listes inverses
def intersection(list1, list2):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

# Exercice 4: Ajout de skip pointers
def intersection_skip(list1, list2):
    i, j = 0, 0
    result = []
    skip1 = max(1, int(math.sqrt(len(list1))))
    skip2 = max(1, int(math.sqrt(len(list2))))
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            if (i % skip1 == 0) and (i + skip1 < len(list1)) and list1[i + skip1] <= list2[j]:
                i += skip1
            else:
                i += 1
        else:
            if (j % skip2 == 0) and (j + skip2 < len(list2)) and list2[j + skip2] <= list1[i]:
                j += skip2
            else:
                j += 1
    return result

if __name__ == "__main__":
    documents = charger_documents("documents.txt")
    index = construire_index(documents)

    terme1 = input("Entrez le premier terme: ")
    terme2 = input("Entrez le deuxieme terme: ")

    docs1 = index.get(terme1, [])
    docs2 = index.get(terme2, [])

    print(f"Intersection: {intersection(docs1, docs2)}")
    print(f"Intersection skip: {intersection_skip(docs1, docs2)}")

