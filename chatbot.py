import google.generativeai as genai
import streamlit as st
genai.configure(api_key="api key")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest",
                              system_instruction=""" Here, you can ask any questions related to data science, from statistics and machine learning to data visualization and programming,AI
                                  Our AI tutor is here to help you resolve your data science doubts and deepen your understanding of this fascinating field. Feel free to ask anything about data science, 
                                 and if user ask any question other than data science then say "I don't Know" and if user ask your name "I am Data Science conversational AI chatbot" """)
st.title("AI Data Science Tutor chatbot 🤖📊")
if "memory" not in st.session_state:
    st.session_state["memory"]=[]

chat=model.start_chat(history=st.session_state["memory"])

for msg in chat.history:
       st.chat_message(msg.role).write(msg.parts[0].text)
user_prompt=st.chat_input()

if user_prompt:
        st.chat_message("user").write(user_prompt)
        response = chat.send_message(user_prompt) 
        for chunk in response:
            st.chat_message("ai").write(chunk.text)   
               
         
        st.session_state["memory"]=chat.history  