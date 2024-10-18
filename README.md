Introduction
1) This repository is to extract the text from Invoices using GenAI and "gemini-1.5-flash" model and save the fields to excel file.
2) Here I have used Streamlit as a interface to handle and operate the functionality.
3) You can upload the images which have ".jpg", ".jpeg", ".png" formats, and on a single click the extracted fields will save in to excel file (If excel file does not exists in the working 
folder then code will create the new file with name 'Invoice_Details.xlsx', if the file is exists then all the details will append in a new line for every text extraction).


Steps :- 
1) Install requrements2.txt file to install dependancies 
2) You need to use your Gemini API key in either .env file or in the code line "genai.configure(api_key='')".
3) Use "streamlit run img_text_gemini_pro.py" line in your terminal 



