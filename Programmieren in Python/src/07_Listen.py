# Listen in Python
# a = a + b oder a += b?
# extend oder append?
# insert, pop, count, iterieren?

einkaufs_liste = ['milch', 'salz', 'eier', 'äpfel']
zusatz_liste = ['backpulver', 'motoröl', 'milch']
zusatz_liste2 = 'brot'

# a = a + b    <=> a += b
# einkaufs_liste = einkaufs_liste + zusatz_liste
# einkaufs_liste += zusatz_liste

einkaufs_liste.extend(zusatz_liste)
print(einkaufs_liste)
einkaufs_liste.append(zusatz_liste2)
print(einkaufs_liste)

einkaufs_liste.pop()
print(einkaufs_liste)

print(einkaufs_liste.count('milch'))

for i in range(len(einkaufs_liste)):
    print(einkaufs_liste[i])

for val in einkaufs_liste:
    print(val)
