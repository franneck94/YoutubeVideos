# Dateien lesen und schreiben

text = 'Ich gehe heute nach Hause, yippie!'
text2 = 'Ich gehe morgen auch nach Hause!'
data = [1, 3, 5, 7, 9, 11]

# w = schreiben, r = lesen, a = append
with open('geschichte.txt', 'w') as f:
    f.write(text + '\n')
    f.write(text2)

text_neu = ""

with open('geschichte.txt', 'r') as f:
    text_neu += f.readline()
    text_neu += f.readline()

print(text_neu)

with open('data.txt', 'a') as f:
    for val in data:
        f.write(str(val) + ', ')
