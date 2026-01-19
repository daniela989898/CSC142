import random
def draw_card(hand, deck):
    hand.append(deck.pop())
def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            aces += 1
        else:
            score += int(card)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score
def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_hand = []
    dealer_hand = []
    random.shuffle(deck)
    draw_card(dealer_hand, deck)
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)
    print("Carta del dealer:", dealer_hand[0])
    print("Tus cartas:", player_hand)
    while True:
        player_score = calculate_score(player_hand)
        print("Tu puntaje:", player_score)
        if player_score > 21:
            print("Te pasaste de 21. Perdiste.")
            return
        choice = input("¿Hit o Stay? ").lower()
        if choice == "hit":
            draw_card(player_hand, deck)
            print("Tus cartas:", player_hand)
        else:
            break
    while calculate_score(dealer_hand) < 17:
        draw_card(dealer_hand, deck)
    dealer_score = calculate_score(dealer_hand)
    print("Cartas del dealer:", dealer_hand)
    print("Puntaje del dealer:", dealer_score)
    if dealer_score > 21:
        print("El dealer se pasó. ¡Ganaste!")
    elif dealer_score > player_score:
        print("El dealer gana.")
    elif dealer_score < player_score:
        print("¡Ganaste!")
    else:
        print("Empate.")
if __name__ == "__main__":
    main()