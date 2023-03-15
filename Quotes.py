# Dictionary for save articles and authors
articleBase = {}
# function for get new authors and articles
def collectArticles():
    author = input("Please input the name of article author: ").strip()
    article = input("Please input the text of the article: ").strip()
    dictionaryUpdater(articleBase, author, article )
    return articleBase
# function for update dictionary
def dictionaryUpdater(dict,aut,art):
    dict[aut] = art
# main function
def main():
    # use while loop to get new articles
    while True:
        articleBase = collectArticles()
        ask = input("Do you whant add another author and article? Y/N? ").strip().lower()
        if ask == "n":
            break
    # get dictionary keys as a string
    authorKeys = ", ".join(list(articleBase.keys()))
    # ask if user need to find article by author
    ask2 = input("Do you whant to find the article for folowing authors?\n"+authorKeys+"\n Y/N? ").strip().lower()
    if ask2 == "y":
        while True:
            ask3 = input("Please copy and past the name of folowing authors you need:\n"+authorKeys+"\n").strip()
            print(articleBase[ask3])
            ask4 = input("Do you whant to find the article for folowing authors?\n"+authorKeys+"\n Y/N? ").strip().lower()
            if ask4 == "n":
                print("Program is finished, thank you!!!")
                break
    else:
        print("Program is finished, thank you!!!")

main()

# AUTHORS and TEXTS for TESTING
# author: JAMES CLEAR

# I don’t say “Thank You” as often as I should and I doubt I’m the only one.
# In fact, I’m starting to believe that “Thank You” is the most under-appreciated and under-used phrase on the planet.
# It is appropriate in nearly any situation and it is a better response than most of the things we say.
# Let’s cover 7 common situations when we say all sorts of things, but should say “Thank You” instead.

# author: Mark Manson

# If I ask you, “What do you want out of life?” and you say something like,
# “I want to be happy and have a great family and a job I like,”
# it’s so ubiquitous it doesn’t even mean anything.

# Robin Sloane

# Here’s a case study. My pal Alexis Madrigal has got the stock/flow balance down.
# On one end of the spectrum, he’s a Twitter natural and a fast-paced writer.
# Madrigal’s got mad flow; you plug in, and you get a steady stream of interesting stuff.
# But on the other end of the spectrum—and man, this is just so important—he’s written a deep,
# nuanced history of green tech in America. This is a book intended to stand the test of time.
