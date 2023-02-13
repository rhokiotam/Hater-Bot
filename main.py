# This is a simple chat bot that responses with negative/pessimistic messages to the user
# In the future, the AI will be trained with supervised learning
# to where it responds to user input with its own negative/pessimistic messages

# choosing a random greeting and goodbye for each interaction with the user
import random

# greetings and goodbyes
greetings = ["Hi", "Hey", "Hello", "How are you doing"]
goodbyes = ["Didn't want to keep talking to you anyway", "See you around, loser", "Sucks to suck, later"]

# keywords for certain responses
keywords = ["music", "books", "games", "school", "pets"]
responses = ["Your music taste is trash", "...you really like reading, what a nerd?", "Go touch some grass", "Bet you stick your head into books all day...",
             "I'm sure you can barely take care of yourself, now you're adding a pet to the mix?"]

# choosing a random greeting for the user
print(random.choice(greetings))

user = input ("Say something...(or type bye to quit): ")
# converting the user input to lowercase
user = user.lower()

# while loop so user can keep interacting with the bot until user inputs bye
while user != "bye":
    keyword_found = False

    for index in range(len(keywords)):
        if keywords[index] in user:
            print("HaterBot: " + responses[index])
            keyword_found = True

    # if keyword is not found in keywords list, user can input a response
    # given a keyword
    if not keyword_found:
        new_keyword = input("I'm don't understand you, I need a keyword to respond to, idiot")
        keywords.append(new_keyword)
        new_response = input("How should I respond to " + new_keyword + "? ")
        responses.append(new_response)

    user = input("You got something else to say? (or type bye to quit): ")
    user = user.lower()

print(random.choice(goodbyes))