import google.generativeai as genai
from google.generativeai.types import GenerationConfig
import streamlit as st
genai.configure(api_key="AIzaSyB5UwPhatHQ8h0XqhFXx8BvxpONMprIXRo")
def gen(prompt:str) ->str:
  try:
    system="Solve every mathematical promblem given and do not explain it just give answers.Or else..."
    full=f"{system}\n problem{prompt}"
    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content(full,generation_config=GenerationConfig(temperature=0.1))
    return response.text
  except Exception as e:
    return str(e)
def steep():
  st.set_page_config("Math Expert🤓")
  st.title("Math problem solver🔢")
  abc=st.text_input("Enter the question or else..👿:")
  if st.button("Solve"):
    if abc.strip():
      with st.spinner("Thinking..🤔"):
        Ans=gen(abc.strip())
      st.write(Ans)
    else:
      st.warning("So you didn't enter the question😡. Now enter the question IF YOU DONT WANT 7 GORILLAS IN YOUR HOUSE🦍.")
steep()
