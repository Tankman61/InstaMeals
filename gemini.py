import google.generativeai as genai

genai.configure(api_key="AIzaSyCeIA0bZI40-Ckq3A47QdFvbVYJkzu0qAM")
model = genai.GenerativeModel('gemini-1.5-flash')

def prompt(p):
    return model.generate_content(p + " short brief concise kind").text

a = "I want you to make "
time_to_make = 0
difficulty = 0
cuisine_origin = ""
contains_ingredients = []
recipe_type = "" # dessert, appetizer, drink, etc. etc.
print(prompt(""))