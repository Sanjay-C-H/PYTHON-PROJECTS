import random
import sys

played_words = []


def choose_word():
    words = ['things', 'resume', 'sanjay']

    available_words = [w for w in words if w not in played_words]

    if not available_words:
        sys.exit(2)  # Exit 2 if all words have been played

    word = random.choice(available_words)
    played_words.append(word)
    return word


def jumble_word(word):
    jumbled = list(word)
    random.shuffle(jumbled)
    return ''.join(jumbled)


def play_round(player1, player2):
    score_board = {player1: 0, player2: 0}

    while True:
        original_word = choose_word()
        jumbled_word = jumble_word(original_word)

        def guess_correct(original_word, jumbled_word, player=player1, round=1):
            print(f"\nJumbled word: {jumbled_word}")
            print(f"\n{player}'s turn:")
            guess = input("Your guess: ").lower()
            if guess == original_word:
                print("Correct! You guessed the word.")
                score_board[player] += 1
                if round < 2:
                    original_word = choose_word()
                    jumbled_word = jumble_word(original_word)
                    guess_correct(original_word, jumbled_word, player2, 2)
            elif guess != original_word:
                if player == player2 and round == 2:
                    print(f"Incorrect.{player1}'s turn:")
                    guess_correct(original_word, jumbled_word, player1, 2)
                elif round < 2:
                    print(f"Incorrect.{player2}'s turn:")
                    guess_correct(original_word, jumbled_word, player2, 2)
                else:
                    print(f"Correct Answer is:{original_word}")

        play = int(input("PRESS 1 TO PLAY 0 TO QUIT: "))
        if play == 1:
            guess_correct(original_word, jumbled_word, player=player1, round=1)
        else:
            return score_board


def main():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    score_board = play_round(player1, player2)

    print("\nGame Over!")
    print(f"Final Scores of the players:{score_board}")

    winner, looser = max(score_board, key=score_board.get), min(score_board, key=score_board.get)
    max_value, min_value = score_board[winner], score_board[looser]

    if max_value != min_value:
        print(f"{winner} wins!")
    else:
        print("Tie game.")


if __name__ == "__main__":
    main()
