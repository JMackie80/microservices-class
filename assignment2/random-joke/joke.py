from flask import Flask, request, jsonify
from random import randrange

application = Flask(__name__)
jokes = [
    { "id": 1, "text": "A termite walks into a bar and asks is the bar tender here?"  },
    { "id": 2, "text": "A horse walks into a bar. The bartender asks. Why the long face? The horse responds, I don't know I was born with it."  },
    { "id": 3, "text": "A bear walks into a bar and says I'll have a...I'll have a...a pepsi. The bartender asks, why the big pause? The bear responds, I don't know I was born with them"  },
    { "id": 4, "text": "What do a tick and the Eiffel Tower have in common? They're both Paris sites."  },
    { "id": 5, "text": "How do you follow Will Smith in the snow? You follow the fresh prints"  },
    { "id": 6, "text": "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along"  },
    { "id": 7, "text": "What do you call a factory that makes okay products? A satisfactory"  },
    { "id": 8, "text": "Dear Math, grow up and solve your own problems."  },
    { "id": 9, "text": "What did the janitor say when he jumped out of the closet? Supplies!"  },
    { "id": 10, "text": "I only know 25 letters of the alphabet. I don't know y."  },
    { "id": 11, "text": "I am reading a book about anti-gravity. Its impossible to put down!" },
    { "id": 12, "text": "I made a pencil with two erasers. It was pointless." },
    { "id": 13, "text": "Why did the scarecrow win an award? Because he was outstanding in his field." },
    { "id": 14, "text": "I am on a seafood diet. I see food and I eat it" },
    { "id": 15, "text": "Have you ever tried to catch a fog? I tried yesterday but I mist." },
    { "id": 16, "text": "I used to play piano by ear. Now I use my hands." },
    { "id": 17, "text": "I once got fired from a canned juice company. Apparently I couldn't concentrate." },
    { "id": 18, "text": "A cheeseburger walks into a bar. The bartender says, Sorry, we don't serve food here." },
    { "id": 19, "text": "Did you hear about the kidnapping at school? It's okay, he woke up" },
    { "id": 20, "text": "I once had a dream I was floating in an ocean of orange soda. It was more of a fanta sea." },
    { "id": 21, "text": "If a child refuses to nap, are they guilty of resisting a rest?" },
    { "id": 22, "text": "Shout out to my fingers. I can count on all of them." },
    { "id": 23, "text": "That car looks nice but the muffler seems exhausted." }
]

def get_random_joke():
    index = randrange(len(jokes)) - 1
    return jokes[index]

def get_random_jokes(num, dict):
    if len(dict) == num:
        return dict
    else:
        joke = get_random_joke()
        dict[joke['id']] = joke
        return get_random_jokes(num, dict)

@application.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@application.route("/joke", methods=['GET'])
def random_joke():
    return get_random_joke()

@application.route("/jokes", methods=['GET'])
def random_jokes():
    numString = request.args.get('num')
    num = 10
    if numString is not None:
        num = int(numString)
    return jsonify(list(get_random_jokes(num, {}).values()))