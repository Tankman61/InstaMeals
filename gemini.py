import google.generativeai as genai

genai.configure(api_key="AIzaSyCeIA0bZI40-Ckq3A47QdFvbVYJkzu0qAM")
model = genai.GenerativeModel('gemini-1.5-flash')

def prompt(p):
    return model.generate_content(p + " short brief concise kind").text
    
