import streamlit as st
from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return "Unable to detect language"

def main():
    st.title("Language Detection App")

    # Text input field for user input
    text_input = st.text_area("Enter some text:")

    if st.button("Detect Language"):
        if text_input:
            language = detect_language(text_input)
            st.success(f"The language is: {language}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
