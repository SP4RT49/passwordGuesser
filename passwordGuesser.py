import random
import string
import datetime


def DateSplit():
    # Split de la date pour récupérer les informations souhaitées
    dateChoose = "19 Nov 2015  18:45:00.000"
    date = datetime.datetime.strptime(dateChoose, "%d %b %Y  %H:%M:%S.%f")

    annee = date.year
    mois = date.month
    jour = date.day
    heure = date.hour
    minute = date.minute
    seconde = date.second
    print(jour, "/", mois, "/", annee)


print(DateSplit())


# -----------------------------
Tab1 = ["A", "B", "C", "D"]
Tab2 = ["1", "2", "3", "4"]
Tab1_length = len(Tab1)
password_length = 5

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#  élément aléatoirement de la liste
def Random(Tab1):
    return random.choice(Tab1)


print("##################")
print("#      " + Random(Tab2) + Random(Tab1))
print("##################")


Tab1_list = [random.choice(Tab1) for i in range(Tab1_length)]
print(Tab1_list)

word_list = letters + digits + special_chars
password = ""
for i in range(password_length):
    password += "".join(random.choice(word_list))

print(password)
