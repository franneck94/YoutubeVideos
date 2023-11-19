# Benötigtes Wissen: Klassen und Vererbung

# Aufgabe:
# Erstelle eine Klasse, die dich als menschen
# darstellt, mit den Attributen Name, Nachname,
# Alter. Schreibe dann eine Funktion die dir die Daten
# ausgibt. Erstelle dann eine Klasse Student die davon erbt
# und ebenfalls dazu Matr. Nr., Semester und Studiengang
# als Attribut hat.
#
# Zusatzaufgabe: Erstelle einige Objekte und probier ein bisschen
# mit der print Funktion herum. Teste ob das Objekt ein Student ist oder nicht.

class Mensch:
    name = ""
    nachname = ""
    alter = 0

    def __init__(self, name, nachname, alter):
        self.name = name
        self.nachname = nachname
        self.alter = alter

    def print_daten(self):
        print('Mensch: ', self.name, " ", self.nachname, " Alter: ", self.alter)


class Student(Mensch):
    mnr = 0
    semester = 0
    studiengang = ""

    def __init__(self, mnr, semester, studiengang, name, nachname, alter):
        super(Student, self).__init__(name, nachname, alter)
        self.mnr = mnr
        self.semester = semester
        self.studiengang = studiengang

    def print_daten(self):
        super(Student, self).print_daten()
        print('Mnr: ', self.mnr, ' Semester: ', self.semester, ' Studiengang: ', self.studiengang)


jan = Student(1080, 1, 'Master AI', 'Jan', 'S', 23)
jan.print_daten()

peter = Mensch('Peter', 'H', 54)

print('Ist Jan ein Student?')
if isinstance(jan, Student):
    print('Ja')
else:
    print('Nein')

print('Ist Peter ein Student?')
if isinstance(peter, Student):
    print('Ja')
else:
    print('Nein')
