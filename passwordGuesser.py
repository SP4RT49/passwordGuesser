from flask import Flask, render_template, request
import random
import string
import datetime
import unicodedata

app = Flask(__name__)

class PasswordGenerator:
    def __init__(self, options):
        self.options = options
        self.passwords = []

    def generate_passwords(self, words, dates):
        password_variations = []
        word_variations = {
            "original": [],
            "lowercase": [],
            "uppercase": [],
            "capitalize": [],
            "remove_accents": [],
            "l33t": [],
        }
        for word in words:
            word_variations["original"].append(word)
            if self.options["lowercase"]:
                word_variations["lowercase"].append(self.lowercase(word))
            if self.options["uppercase"]:
                word_variations["uppercase"].append(self.uppercase(word))
            if self.options["capitalize"]:
                word_variations["capitalize"].append(self.capitalize(word))
            if self.options["remove_accents"]:
                word_variations["remove_accents"].append(self.remove_accents(word))
            if self.options["l33t"]:
                for l33t_word in self.l33t(word):
                    word_variations["l33t"].append(l33t_word)

        date_variations = []
        for date in dates:
            date_variations += self.extract_date_info(date)

        for word_variation in word_variations.values():
            variation_passwords = []
            for word in word_variation:
                for date_variation in date_variations:
                    variation_passwords.append(self.combine(word, date_variation))
            password_variations.append(variation_passwords)
        
        self.passwords = [pw for variation in password_variations for pw in variation]


    def lowercase(self, word):
        return word.lower()

    def uppercase(self, word):
        return word.upper()

    def capitalize(self, word):
        return word.capitalize()

    def remove_accents(self, word):
        return unicodedata.normalize("NFKD", word).encode("ASCII", "ignore").decode("utf-8")

    def l33t(self, word):
        variations = [word]
        replacements = {
            "a": ["@", "4", "/-\\"],
            "e": ["3", "€", "ë"],
            "i": ["1", "!", "|"],
            "o": ["0", "()", "[]"],
            "s": ["5", "$", "§"],
            "t": ["7", "+"],
        }
        for letter in word:
            if letter.lower() in replacements:
                new_variations = []
                for replacement in replacements[letter.lower()]:
                    for variation in variations:
                        new_word = variation[:variation.index(letter)] + replacement + variation[variation.index(letter) + 1:]
                        new_variations.append(new_word)
                variations += new_variations
            elif letter.upper() in replacements:
                new_variations = []
                for replacement in replacements[letter.upper()]:
                    for variation in variations:
                        new_word = variation[:variation.index(letter)] + replacement + variation[variation.index(letter) + 1:]
                        new_variations.append(new_word)
                variations += new_variations
        return variations


    def extract_date_info(self, date_str):
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        year2 = str(date.year)[-2:]
        year4 = str(date.year)
        month = self.get_month(date.month)
        day = str(date.day)
        hour = str(date.hour)
        minute = str(date.minute)
        second = str(date.second)
        return [year2, year4, month, day, hour, minute, second]


    def get_month(self, month_num):
        months = [
            "janvier",
            "février",
            "mars",
            "avril",
            "mai",
            "juin",
            "juillet",
            "août",
            "septembre",
            "octobre",
            "novembre",
            "décembre",
        ]
        return months[month_num - 1]

    def combine(self, word, date_info):
        return "".join(random.sample(word + "".join(date_info), len(word) + len(date_info)))


# Utilisation de l'encapsulation
class DynamicFields:
    def __init__(self, num_fields):
        self.num_fields = num_fields
        self.words = []
        self.dates = []

    def add_field(self, word, date):
        self.words.append(word)
        self.dates.append(date)


# Utilisation de l'héritage
class CustomPasswordGenerator(PasswordGenerator):
    def __init__(self, options, dynamic_fields):
        super().__init__(options)
        self.dynamic_fields = dynamic_fields

    def generate_passwords(self):
        words = [field.word for field in self.dynamic_fields.words]
        dates = [field.date for field in self.dynamic_fields.dates]
        super().generate_passwords(words, dates)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        options = {
            "lowercase" : "lowercase" in request.form,
            "uppercase" : "uppercase" in request.form,
            "capitalize" : "capitalize" in request.form,
            "remove_accents" : "remove_accents" in request.form,
            "l33t" : "l33t" in request.form,
        }
        
        words = []
        dates = []

        for key, value in request.form.items():
            if key.startswith("word"):
                words.append(value)
            elif key.startswith("date"):
                dates.append(value)

        pg = PasswordGenerator(options)
        pg.generate_passwords(words, dates)
        passwords = pg.passwords

        return render_template('index.html', passwords=passwords)

    return render_template('index.html')

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
