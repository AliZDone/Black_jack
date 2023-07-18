import random as rand
import os
import time

class black_jack:

    def __init__(self):
        BET = 12
        card_name = ['Ase', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'solder', 'queen', 'king']
        score = []
        for i in range(1,14):
            score.append(i)
        
        card = {
            card_name : score for card_name , score in zip(card_name, score)
        }
        return card, BET
         

    def replay():
        black_jack.game()

    def get_card():
        card, BET = black_jack.__init__(self=1)
        count = 0
        player =[]
        dealer = []
        while(count < 4):
            num = rand.randint(1,13)
            if count % 2 == 0 or count == 0:
                for i, j in card.items():
                    if int(j) == num:
                        player.append(i)
                        break
                count += 1
            else:
                for i, j in card.items():
                    if int(j) == num:
                        dealer.append(i)
                        break
                count += 1
        
        return dealer, player, card, BET
    

    def get_card2(player_card, dealer_card, card):
        count = 0
        size = len(player_card)
        while(count < 2):
            num = rand.randint(1,13)
            if count % 2 == 0 or count == 0:
                for i, j in card.items():
                    if int(j) == num:
                        player_card.append(i)
                        break
                count += 1
            else:
                for i, j in card.items():
                    if int(j) == num:
                        dealer_card.append(i)
                        break
                count += 1
        
        return  player_card, dealer_card


    def dealer_card_sum(dealer_cards, card):
        score = []
        for k in dealer_cards:
            for i, j in card.items():
                if k == 'Ase' and i == k:
                    score.append([1,11])
                elif i == k:
                    if j < 11:
                        score.append(j)
                    elif 10 < j and j < 14:
                        score.append(10)
        Sum = 0
        for i in score:
            Sum += int(i)
        return Sum


    def check_win_player(player_cards, dealer_cards, card):
        score = []
        for k in player_cards:
            for i, j in card.items():
                if k == 'Ase' and i == k:
                    score.append([1,11])
                    break
                elif i == k:
                    if j < 11:
                        score.append(j)
                        break
                    elif 10 < j and j < 14:
                        score.append(10)
                        break
        Sum = 0
        for i in score:
            Sum += int(i)
        daeler_num = black_jack.dealer_card_sum(dealer_cards, card)
        if Sum > 21:
            return "lose"
        elif Sum == daeler_num:
            return "equal"
        elif Sum == 21:
            return "black jack"
        else:
            if Sum > daeler_num:
                return "win"


    def double_down(player_cards, dealer_cards, card, bet):
        player, dealer = black_jack.get_card2(player_cards, dealer_cards,card)
        
        incrase_bet = int(input("how much dO you want to increase the bet? "))
        bet += incrase_bet
        return  player, dealer, bet


    def splite(player_cards, card, bet):
        player_cards1 = player_cards[0]
        player_cards2 = player_cards[1]
        player_cards1, player_cards2 = black_jack.get_card2(player_cards1, player_cards2, card)
        bet1 = bet.copy()



    def black_jack_cards(bet, BET):
        print("you win! you have black jack")
        bet = bet*2 + (bet/2)
        BET += bet


    def win(bet, BET):
        print("you win!")
        bet *= 2
        BET += bet


    def lose(bet, BET):
        print("you lose!")
        BET -= bet


    def check_status_splite(player_status1, player_status2, dealer_card, card, bet, BET):
        number_round_win = 0
        number_round_equal = 0

        if player_status1 == "black jack":
            black_jack.black_jack_cards(bet, BET)
            print("BLACK JACK!!!\n", "you win!")
            exit()
        if player_status2 == "black jack":
            black_jack.black_jack_cards(bet, BET)
            print("BLACK JACK!!!\n", "you win!")
            exit()

        if player_status1 == "win":
            number_round_win += 1
        elif player_status2 == "lose":
            number_round_win -= 1
        elif player_status2 == "equal":
            number_round_equal += 1

        if player_status2 == "win":
            number_round_win += 1
        elif player_status2 == "lose":
            number_round_win -= 1
        elif player_status2 == "equal":
            number_round_equal += 1

        if number_round_win > 0:
            print("you win!")
            bet = bet*(number_round_win*2)
        elif number_round_win < 0:
            print("you lose!")
            BET -= bet*(number_round_win*2)
        else:
            print("you get equal round!")
            


    def game():
        dealer_cards, player_cards, card, BET = black_jack.get_card()
        print("you have ",BET, " for bet!")
        count = 0
        double_down = False
        bet = int(input("how many to you want to bet? "))
        while(True):
            time.sleep(1.5)
            os.system("cls")
            print("your bet : ",bet)
            print("your cards: ")
            print(list(i for i in player_cards))
            print("\n")
            print("\n")
            print("daeler cards:")
            if count  == 0:
                print(dealer_cards[0])
            else:
                print(list(i for i in dealer_cards))
            
            player_status = black_jack.check_win_player(player_cards, dealer_cards, card)
            if player_status == "black jack":
                black_jack.black_jack_cards(bet, BET)
                break
            elif player_status == "win":
                    black_jack.win(bet, BET)
                    break
            elif player_status == "lose":
                    black_jack.lose(bet, BET)
                    break
            elif player_status == "equal":
                    print("you get equal round!")
                    break
            
            ans = input("choose ypur move (hit, pass, double down, splite): ")
            ans = ans.lower()
            
            if ans == 'hit':
                count += 1
                if double_down == True:
                    print("you use double down you can't use hit aany more!\n", "choose anoter thing")
                    continue
                player_cards, dealer_cards = black_jack.get_card2(player_cards, dealer_cards,card)
            elif ans == 'pass':
                count += 1
                player_status = black_jack.check_win_player(player_cards, dealer_cards, card)
                if player_status == "win":
                    black_jack.win(bet, BET)
                elif player_status == "lose":
                    black_jack.lose(bet, BET)
                elif player_status == "equal":
                    print("you get equal round!")

            elif ans == "double down":
                count += 1
                double_down = True
                player_cards, dealer_cards, bet = black_jack.double_down(player_cards, dealer_cards, card, bet)
                continue
            elif ans == "splite":
                if player_cards[0] == player_cards[1] and count == 0:
                    player_cards1, player_cards2, bet1, bet2 = black_jack.splite(player_cards, dealer_cards, card, bet)
                    player_status1 = black_jack.check_win_player(player_cards1, dealer_cards, card) 
                    player_status2 = black_jack.check_win_player(player_cards2, dealer_cards, card) 
                    break
                else: 
                    print("you are not allowed to splite you cards!\n", "choose anoter thing")
                    count += 1
            else:
                print("unvalid Enter!\n", "choose anoter thing")


        answer = input("Do you want play again? (y/n)")
        answer = answer.lower()
        if answer == 'y':
            black_jack.replay()
        else:
            exit()

            

black_jack.game()

