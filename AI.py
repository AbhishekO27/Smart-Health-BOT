from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

def generate_greeting(name):
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = f"Good morning, {name}! Hope you have a fantastic start to your day!"
    elif 12 <= current_hour < 18:
        greeting = f"Good afternoon, {name}! Hope your day is going great!"
    elif 18 <= current_hour < 21:
        greeting = f"Good evening, {name}! Winding down for the day?"
    else:
        greeting = f"Hello, {name}! Burning the midnight oil, huh?"
    return greeting