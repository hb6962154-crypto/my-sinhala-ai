import streamlit as st
import google.generativeai as genai

# ඔයාගේ API Key එක මෙතනට දාන්න
genai.configure(api_key="ඔයාගේ_API_KEY_එක_මෙතනට")

st.title("සිංහල AI සෙවුම් යන්ත්‍රය 🇱🇰")
st.write("ඕනෑම දෙයක් අහන්න, මම Google එකෙන් සෙවුම් කර සිංහලෙන් පිළිතුරු දෙන්නම්.")

# User ගෙන් ප්‍රශ්නය ලබා ගැනීම
query = st.text_input("ඔබට දැනගැනීමට අවශ්‍ය කුමක්ද?", placeholder="උදා: ලෝකයේ උසම කන්ද කුමක්ද?")

if st.button("සොයන්න"):
    if query:
        with st.spinner('පිළිතුර සකසමින් පවතී...'):
            try:
                # Gemini Model එක සෙට් කිරීම (Search හැකියාව සහිතව)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # AI එකට දෙන උපදෙස් (System Instruction)
                prompt = f"Search the web for: {query}. Summarize the findings and explain it clearly in Sinhala language."
                
                response = model.generate_content(prompt)
                
                # පිළිතුර පෙන්වීම
                st.subheader("පිළිතුර:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"දෝෂයක් සිදු වුනා: {e}")
    else:
        st.warning("කරුණාකර ප්‍රශ්නයක් ඇතුළත් කරන්න.")
