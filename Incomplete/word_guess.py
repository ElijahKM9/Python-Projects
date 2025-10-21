
#basic word guessing with a list


# words = ["free"]
#
#
# guess = input("Guess a word\n>")
# guess = guess.lower()# adds fault tolerence
# if guess in words:
#     print("you guessed it")
# else:
#     print("you guessed wrong")

#makes the guess check a function a

def guess_game(list_of_words, guess):
    if guess in list_of_words:
        print("correct word")
        return 0
    else:
        print("wrong word")
        return -1


#making the game a class object that has different methods
# method 1 display guessable words
# method 2 guess a word
# method 3 add a guessable word
# method 4 remove a guessable word

class Game:
    def __init__(self, words = []):
        self.words = words
        self.guess = None

    def add(self, word=None):
        if word == None:
            word = input("What word would you like to add?\n>")
            self.words.append(word.lower())
        else:
            self.words.append(word.lower())

    def display(self):
        print(self.words)

    def guess(self,word):
        if word in self.words:
            print("You Guessed it")


    def remove(self,index=None):
        if index:
            print(self.words)
            index = input("write the index of the word you want removed\n>")
            self.words.pop(index)
        else:
            self.words.pop(index)
