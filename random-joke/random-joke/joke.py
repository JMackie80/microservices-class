from flask import Flask
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
    { "id": 10, "text": "I only know 25 letters of the alphabet. I don't know y."  }
]

@application.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@application.route("/joke", methods=['GET'])
def random_joke():
    index = randrange(len(jokes)) - 1
    return jokes[index]