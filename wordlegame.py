import random

def init_game():
    pass

def load_words(txt_path: str):
    """
    Load the words from given txt_path

    Args:
        - `txt_path`: path of the text file to read.

    Returns:
        - `word_list`: the list of word .
    """
    with open(txt_path, "r") as file:
        word_list = [word.strip() for word in file]

    return word_list

def get_feedback(corr_word:str, answer:str) -> str:
    """
    Return the feedback  grading the answer 

    Args:
        - `corr_word`: The correct word for reference.
        - `answer`: The user's answer for grading.

    Returns:
        - `feedback`: Feedback string indicating matching characters, positions, and mismatches.
    """
    feedback = " "

    for i in range(5):
        if user_input[i] == random_word[i] :
            feedback += [i]
        elif user_input[i] in random_word :
            feedback += '#'
        else: 
            feedback += '_'
    return feedback

def get_user_input()->str:
    """
    Prompt the user to input a 5-digit word or '@' to end the game.
    
    Returns:
        - `user_input`: The user's input as a string, which can be a 5-digit word or '@' to end the game.
    """

    while True:
        user_input = input("Type in 5 digit word! Press @ if you want to end\n")
        if user_input == '@' :
            print("Game Ended.")
            exit()

        if len(user_input) != 5:
            print("Wrong input. Please type in 5 digit word.")
            continue

        return user_input
    
if __name__ == '__main__':
    random.seed(42)

    print("Let's start the Wordle!")

    word_list = load_words('C:\\git\\wordle\\five_digit_word.txt')


    while True:
        random_word = random.choice(word_list)
        attempts = 0

        while True: 
            user_input = get_user_input()            
            attempts += 1

            if user_input == random_word : 
                print("You're Right!")
                print("Right answer in", attempts, "times")
                break
            
            feedback = get_feedback(random_word, user_input)
            print(feedback)