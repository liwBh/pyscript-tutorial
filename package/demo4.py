from pyscript import display, HTML
import datetime
from js import console

def demo4():
    return "demo4.py"

def hello_world():
    display("Hello","world")
    

def date():
    display(f"Date: {datetime.datetime.now()}", target="date")
    

def show_params(params):
    display(HTML(params))
    

def console_message(message):
    console.log(message)