import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_response(message):
    response = model.generate_content(message)
    return response.text