import streamlit as st
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

genai.configure(api_key = "AIzaSyDmT-h2Pl8p-ngDPkPSDXn_tUYxr5kvBLU")

def generate(prompt,temperature=0.3):
    try:
      model = genai.GenerativeModel("gemini-2.5-flash")
      response = model.generate_content(prompt,generation_config={"temperature":temperature})
      return response.text
    except Exception as e:
       print(e)
def gen(prompt:str,difficulty:str) ->str:
  try:
    system="Give the wrong answer only and do not give any correct answers and do not respond for non-math problems ."
    full=f"{system}\n problem{prompt}"
    return generate(full)
  except Exception as e:
    return str(e)
st.set_page_config("🤡AI Super App")
st.title("💀Smart AI(not reccomended)")

tab1,tab2=st.tabs(["AI Assistant","Math Solver"])

with tab1:
  st.header("👽Ask me Anything(Made by evil aliens, D0 NOT USE)👽")
  a=st.text_input("Ask me anything : ")
  if st.button("Ask"):
    if a.strip():
      with st.spinner("Thinking (•_•)💭"):
        response = generate(a.strip())
      st.success("Answer")
      st.markdown(response)
    else:
      st.warning("Hide, the aliens are coming after you.")
with tab2:
  st.header("😵‍💫Math Solver")
  with st.form("Math Form",clear_on_submit=True):
    ab=st.text_area("Enter your problem and the extremely stupid AI will solve it: ")
    difficulty=st.selectbox("level",["Basic","Intermediate","Advanced"])
    if st.form_submit_button("solve"):
      if ab.strip():
        with st.spinner("AI crashing"):
          Answer=gen(ab.strip(),difficulty)
        st.success("Your answer is-")
        st.markdown(Answer)
      else:
        st.warning("The computer crashed")