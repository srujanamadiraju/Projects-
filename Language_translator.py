%%writefile C:/Users/madir/OneDrive/Desktop/translator.py

import streamlit as st
from googletrans import Translator

st.title("Google Translate Prototype")

languages = {
    'English': 'en', 'Hindi': 'hi', 'Bengali': 'bn', 'Gujarati': 'gu',
    'Kannada': 'kn', 'Malayalam': 'ml', 'Marathi': 'mr', 'Nepali': 'ne',
    'Odia': 'or', 'Punjabi': 'pa', 'Tamil': 'ta', 'Telugu': 'te',
    'Urdu': 'ur',
    'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
    'Japanese': 'ja', 'Korean': 'ko', 'Chinese (Simplified)': 'zh-cn',
    'Arabic': 'ar', 'Russian': 'ru', 'Portuguese': 'pt', 'Dutch': 'nl',
    'Turkish': 'tr', 'Swedish': 'sv', 'Polish': 'pl', 'Danish': 'da',
    'Finnish': 'fi', 'Czech': 'cs'
}

src_language = st.selectbox("Select Source Language", list(languages.keys()))
dest_language = st.selectbox("Select Destination Language", list(languages.keys()))

input_text = st.text_area("Enter Text to Translate", height=150)

translator = Translator()

if st.button("Translate"):
    if input_text:
        try:
            result = translator.translate(input_text, src=languages[src_language], dest=languages[dest_language])
            st.write(f"**Translated Text** ({dest_language}):")
            st.write(result.text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.error("Please enter text to translate.")
