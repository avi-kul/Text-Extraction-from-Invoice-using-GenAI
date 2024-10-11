from dotenv import load_dotenv

load_dotenv() # This will be import the Env variables.
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel('gemini-pro-vision')
model = genai.GenerativeModel('gemini-1.5-flash')


def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        
        # read the file into bytes 
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type, # get the mime type of the uploaded file
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")
    


##### Streamlit setup #####

st.set_page_config(page_title='Text Extractor')

st.header('Text Extractor')

input = st.text_input('Input Prompt : ',key='input')
uploaded_file = st.file_uploader("Please upload an image of Invoice...",type=['jpg','jpeg','png'])
image = ''

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Image successfully uploaded...!',use_column_width=True)


submit = st.button("Generate the Answer")



# input_prompt = """
# You are an expert in understanding invoices. We will upload an image as invoice and you will have to answer 
# any questions based on the uploaded invoice image 
# """

input_prompt = """
You are an expert in understanding invoices. We will upload an image as invoice and you will have to answer 
any questions based on the uploaded invoice image.
We are specifically looking to extract the following details:
- Invoice number
- Consignee name
- Vendor name
- Total amount
"""

# if submit button is clicked

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
    print(response)
    print(type(response[0]))

    



