# Numeronarvauspeli luokilla
# Arvataan numeroa väliltä 1-100. Peli laskee arvausten määrän. 
# Arvauksen jälkeen peli ilmoittaa, oliko arvaus liian suuri 
# vai liian pieni. Jos arvaus on liian suuri (tai pieni) peli estää arvausta
# suuremman (tai pienemmän) luvun arvaamisen.

from random import randint
import sys

# tehdään luokka numeroille
class GameValues:
    def __init__(self):
        self.ran = None
        self.low = 1
        self.high = 100
        self.guess = None
        self.guesslist = []
        self.counter = 0
        self.status = "game"

    # alustetaan arvattava numero
    def init_number(self):
        self.ran = randint(1,100)

    # asetetaan arvausten yläraja
    def set_low(self, low):
        self.low = low

    # asetetaan arvausten alaraja
    def set_high(self, high):
        self.high = high

    # lisätään arvaus listaan ja lisätään laskuria
    def add_guess(self, guess):
        self.guess = guess
        self.guesslist.append(guess)
        self.counter += 1

    def init_all(self):
        self.init_number()
        self.low = 1
        self.high = 100
        self.guess = None
        self.guesslist = []
        self.counter = 0
        self.status = "game"

# luokka joka hoitaa toiminnallisuudet    
class Game():
    def __init__(self):
        self.values = GameValues()
        self.start_msg = "Tervetuloa pelaamaan numeronarvauspeliä!"
        self.prompt_msg = "Anna luku tai lopeta (L): "
        self.nan_error_msg = "Et antanut lukua"
        self.continue_msg = "Haluatko jatkaa? K/E: "
        self.end_msg = "Kiitos käynnistä ja tervetuloa uudelleen!"

    # evaluoidaan käyttäjän syöte
    def eval_input(self, user_input: str):
        if user_input.isnumeric():
            self.values.add_guess(int(user_input))
            self.eval_guess()
        elif user_input == "L":
            self.end_game()
        else:
            print(self.nan_error_msg)

    def test_guess(self, user_input):
        self.values.add_guess(int(user_input))           

    # evaluoidaan arvaus
    def eval_guess(self):
        if self.values.guess < self.values.low:
            self.low_limit_error()
        elif self.values.guess > self.values.high:
            self.high_limit_error()
        else:            
            if self.values.ran == self.values.guess:
                self.win()
            if self.values.ran < self.values.guess:
                self.greater()
            if self.values.ran > self.values.guess:
                self.smaller()

    def low_limit_error(self):
        print(f"Luvun pitää olla suurempi kuin {self.values.low}")

    def high_limit_error(self):
        print(f"Luvun pitää olla pienempi kuin {self.values.high}")
    
    # jos arvattu luku on suurempi
    # asetetaan yläraja
    def greater(self):
        self.values.set_high(self.values.guess)
        print(f"{self.values.counter}. arvauksesi {self.values.guess} oli liian suuri")

    # jos arvattu luku on pienempi
    # asetetaan alaraja
    def smaller(self):
        self.values.set_low(self.values.guess)
        print(f"{self.values.counter}. arvauksesi {self.values.guess} oli liian pieni")

    # jos voitto
    def win(self):
        print(f"{self.values.counter}. arvauksesi {self.values.guess} oli voittoisa!")
        print("Olet selvästi numeroiden mestari!")
        self.values.status ="win"

    # pelin lopetus
    def end_game(self):
        print("Kiitos käynnistä ja tervetuloa uudelleen!")
        sys.exit()


# pääohjelma
def game_main():
    peli = Game()
    peli.values.init_number()   

    print(peli.start_msg)

    # peliluuppi
    while True:
        if peli.values.status == "game":
            print(f"Arvaa numero väliltä {peli.values.low}-{peli.values.high}")
            user_input = str(input(peli.prompt_msg))
            peli.eval_input(user_input)

        if peli.values.status == "win":
            user_input = str(input(peli.continue_msg))
            if user_input.lower() == "k":
                peli.values.init_all()
                print(peli.start_msg)
            if user_input.lower() == "e":
                peli.end_game()

if __name__=="__main__":
    game_main()