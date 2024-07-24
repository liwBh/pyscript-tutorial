import arrr
from pyscript import document, display
from js import console



def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
    console.log(arrr.translate(english))
