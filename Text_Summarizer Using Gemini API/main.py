import google.generativeai as genai
import streamlit as st
genai.configure(api_key="YOUR_API_KEY") #Paste your API key here within double quotes

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

# paragraph=input("Enter your paragraph:")
# response=chat.send_message("Summarise the paragraph for the user"+paragraph)
# print("\n\n")
# print(response.text)


def main():
    st.title("Text Summariser App")
    
    #input from user
    paragraph=st.text_area("Enter your paragraph")
    
    if paragraph:
        #Do something
        
       if  st.button("Summarise"):
           summary_text=chat.send_message("Summarise a paragraph for the user in 50 words only:"+paragraph)
        
           st.subheader("Summary")
           st.write(summary_text.text)
           
if __name__=='__main__':
    main()