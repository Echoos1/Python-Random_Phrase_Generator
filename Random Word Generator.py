import random

# Import Text Files
adjective = open('parts of speech word files/adjectives/28K adjectives.txt').read().splitlines()
adverb = open('parts of speech word files/adverbs/6K adverbs.txt').read().splitlines()
noun = open('parts of speech word files/nouns/91K nouns.txt').read().splitlines()
verb = open('parts of speech word files/verbs/31K verbs.txt').read().splitlines()


def gen():
    print("\nThe", random.choice(adjective), random.choice(noun), random.choice(adverb), random.choice(verb))
    prompt()


def prompt():
    retry = input("\nTry Again? (y/n)")
    if retry.upper() == "Y":
        gen()
    elif retry.upper() == "N":
        quit()
    else:
        print("\nI don't understand")
        prompt()


gen()
prompt()
