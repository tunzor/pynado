# Pynado - the python nato alphabet reader

# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty('rate', 130)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) # sets voice to female


# def say_word(word):
#    engine.say(word)
#    engine.runAndWait()

alphabet_dict = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliet',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
    ' ': '<br/>'
}


def nadoize(word):
    word_to_speak = ''
    for letter in list(word):
        if letter in alphabet_dict.keys():
            word_to_speak = word_to_speak + alphabet_dict[letter] + ' '
    return word_to_speak


