# Vererbung in Python

class Tier:
    rasse = ""
    geschlecht = ""
    alter = 0

    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printRasse(self):
        print('(TIER) Rasse: ', self.rasse)


class Hund(Tier):
    tatzen_größe = 0

    def __init__(self, tatzen_größe, rasse, geschlecht, alter):
        super(Hund, self).__init__(rasse, geschlecht, alter)
        self.tatzen_größe = tatzen_größe

    def printRasse(self):
        super(Hund, self).printRasse()
        print('(HUND) Rasse: ', self.rasse)


h1 = Hund(10, 'Dackel', 'Männlich', 5)

h1.printRasse()
