import random # for generate random numbers
from math import ceil # return the smallest integral value greater than number


player_money = 1500
keep_playing = True # Boolean = True while we continue the game

print(f"Bienvenue à la roulette, rien que la roulette ! Vous avez {player_money} €.")

while keep_playing: # while we keep playing, we ask the player on what number he wants to bet
    num_bet = -1 # initialise number for while
    num_color = "" # assign an empty value we'll use for the color of the numbers
    while num_bet < 0 or num_bet > 49: # stay in the loop while the player write a number not between 0 and 49
        # ask the player to choose a number between 0 and 49
        num_bet = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        try: # convert the number in int
            num_bet = int(num_bet)
        except ValueError: # if try fail, print message and get back to the beginning
            print("Vous n'avez pas saisi de nombre")
            num_bet = -1 # reinitialize num_bet at -1
            continue # repeat the loop at the beginning if the player type a number not in between 0 and 49
        if num_bet < 0: # if the number is negative
            print("Ce nombre est négatif, positivez ! Entrez un nombre entre 0 et 49")
        elif num_bet > 49: # if the number is superior of 49
            print("Ce nombre est supérieur à 49 ! Entrez un nombre entre 0 et 49")
        elif num_bet % 2 == 0: # if the result of the division by 2 is 0 (if the number is even)
          num_color = True
          print(f"Vous avez choisi le {num_bet}, ce numéro est rouge !")
        else:
          num_color = False
          print(f"Vous avez choisi le {num_bet}, ce numéro est noir !")


    # we ask the player how much money he wants to bet
    bet = 0
    while bet <= 0 or bet > player_money:
        bet = input("Combien voulez-vous miser ? ")
        # convert the bet in int, like the number
        try:
            bet = int(bet)
        except ValueError: # if return ValueError, print message and get back to the beginning
            print("Vous n'avez pas saisi de nombre")
            bet = -1
            continue
        if bet <= 0: # if the number is negative
            print("La mise saisie est négative ou nulle.")
        if bet > player_money: # if the bet is superior of the player's money
            print(f"Vous ne pouvez miser autant, vous n'avez que {player_money} €")

    # we generate a random number with the function randrange
    win_num = random.randrange(50)
    
    print(f"Rien ne va plus. Faites vos jeux ! La roulette tourne... le numéro gagnant est : {win_num} ! ")

    # results
    if win_num == num_bet: # if same number
        print(f"Félicitations, c'est gagné ! Vous obtenez {bet * 3} € !")
        player_money += bet * 3
    elif win_num % 2 == num_bet % 2:  # if they are the same color
        bet = ceil(bet * 0.5) # the player take back half of the bet
        print(f"C'est la bonne couleur, mais pas le bon numéro. Vous obtenez {bet} €")
        player_money += bet
    else: # if they are not the same color and wrong number
        print("Mince...raté, vous perdez entièrement votre mise.")
        player_money -= bet

    # if the player is broke, the game is stop
    if player_money <= 0:
        print("Vous êtes ruiné ! Allez dormir.")
        keep_playing = False
    else:
        # we print the player's money
        print(f"Vous avez à présent {player_money} €")
        leave = input("Souhaitez-vous quitter le jeu (o/n) ? ")
        if leave == "o" or leave == "O":
            print(f"Vous quittez le jeu avec {player_money} € . A bientôt !")
            keep_playing = False



