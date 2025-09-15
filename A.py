import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "AIzaSyB46ZXN6HfBHiJpqbdp81Wmg0IEn2y0mTA")


model = genai.GenerativeModel("gemini-1.5-flash")

def generate(prompt):
    try:
      response = model.generate_content(prompt)
      return response.text
    except Exception as e:
       print(e)
def setup():
  st.title("Senseless Talking AI")
  st.write("Wallocme ot SEnSEEEless AII")
  b=st.text_input("enter YOUR quetionn(?):")
  if b:
    st.write(f"Your quettion es dis : {b}")
    response = generate(b)
    st.write(response)
if __name__ == "__main__":
  setup()


