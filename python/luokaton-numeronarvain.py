# Klassinen numeronarvauspeli

# Arvataan numero väliltä 1-100. Peli laskee arvausten määrän. 
# Arvauksen jälkeen peli ilmoittaa, oliko arvaus liian suuri 
# vai liian pieni. Jos arvaa 75 ja arvaus on liian suuri peli estää
# suuremman luvun arvaamisen ja sama liian pienelle. Peli estää 
# myös 1-100 ulkopuolelta arvaamisen sekä kirjaimet (string.isnumeric()). 
# Peli juhlii (päätä miten), kun arvaat oikein.

from random import randint

def game_main():
    ran = randint(1,100)
    low = 1
    hi = 100
    counter = 0

    print("Tervetuloa pelaamaan numeronarvauspeliä!")
    while True:
        print(f"Arvaa numero väliltä {low}-{hi}")
        user_input = input("Anna luku tai lopeta (L): ")
        if user_input.isnumeric():
            guess = int(user_input)
            if guess < low:
                print(f"Luvun pitää olla suurempi kuin {low}")
                continue
            if guess > hi:
                print(f"Luvun pitää olla pienempi kuin {hi}")
                continue
            if guess > ran:
                hi = guess
                counter += 1
                print(f"{counter}. arvauksesi {guess} oli liian suuri")
            if 0 < guess < ran:
                low = guess
                counter += 1
                print(f"{counter}. arvauksesi {guess} oli liian pieni")
            if guess == ran:
                counter += 1
                print(f"{counter}. arvauksesi {guess} oli voittoisa!")
                print("Olet selvästi numeroiden mestari!")
                break
        else:
            if user_input == "L":
                break
            else:
                print("Et antanut lukua")
        
game_main()