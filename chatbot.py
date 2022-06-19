import re
import random

class ChatBot:

    negative_responses = ('no', 'nope', 'nah', 'naw', 'not a chance','sorry')

    exit_commands = ('quit', 'pause', 'exit', 'goodbye', 'bye', 'later')

    random_questions = (
        "Why are you here?",
        "Are there many people?",
        "What is your favorite food?",
        "Do you know where USA is?"
        "What's your favorite GPU brand?"
    )