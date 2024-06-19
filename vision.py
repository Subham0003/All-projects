from dotenv import load_dotenv
load_dotenv()
import streamlit.web.cli as stcli
import streamlit  as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to lead gemoni pro miodel and resposne
model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


    

st.set_page_config(page_title="Q&A Demo")
st.header("GEMINI LLM Application")
input=st.text_input("Input :",key="input")

uploaded_file = st.file_uploader("Choose a file to upload",type=['jpg', 'png','jpeg'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True)
        


submit=st.button('tell me about the image')


if submit:
   
    response=get_gemini_response(input,image)
    st.subheader("The response is ")
    st.write(response)
