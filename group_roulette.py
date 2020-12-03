from random import randrange
cash_flow = int(input("Quelle est votre cagnotte de depart?\n>") or "0")
keep_bet = True
choice = str
print(cash_flow)

print("Bonne chance")
while cash_flow > 0:
    x_game = randrange(49)
    print(x_game)
    bet = int(input("combien voulez-vous miser?\n>") or "0")
    if bet > cash_flow:
        print(f"veuillez mettre une somme < {cash_flow}\n>")
        continue
    else:
        num = int(input("Choisir un nombre entre 0 et 49") or "-1")
    while num < -1 or num >49:
        print("mauvais choix de numéro")
        num = int(input("Choisir un nombre entre 0 et 49") or "-1")
    if num <= -1:
        parity = str(input("Choisir une couleur p/i") or "none")
        if x_game % 2 == 0:
            x_parity = "p"
        else:
             x_parity = "i"
    def game(x_game):
        if num >= 0:
            if num == x_game:
                gain = bet * 10 - bet
            else:
                gain = 0 - bet
            return gain
        elif parity == x_parity:
            gain = bet * 2 -bet
            return gain
        elif parity == "none":
            gain = 0
            return gain
        elif x_parity != x_parity:
            gain = 0 - bet
            return gain, x_game
        return gain
    print(x_game)
    print(game(x_game))
    print(cash_flow)
    cash_flow = cash_flow + game(x_game)
    print(f"votre gain est de {game(x_game)} $  il vous reste {cash_flow})")
    while choice not in ("y","n"):
        choice = str(input("veux-tu continuer y / n\n>"))
    if choice == "y":
        continue
    else:
        break
else:
    print(f"votre cash_flow est de {cash_flow} partie terminee )")
print(f"vous avez {cash_flow} euros good bye )")