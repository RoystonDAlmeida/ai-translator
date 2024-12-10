# Create a simple Streamlit app
import streamlit as st
from transformers import pipeline

# Step 2: Set up the Translation Pipeline
# Initialize the translator for translating from Italian to English
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-it")

# Step 3: Create the Streamlit UI

# Title of the app
st.title("AI Translator")

# Add a textarea to type the text to translate
input_text = st.text_area("Enter text to translate:")

# Add a select box for selecting target language
target_language = st.selectbox("Select target language:", ["Italian", "French", "Spanish"])

if st.button("Translate"):
	# Perform translation based on selected language
	if target_language == "Italian":
		translated_text = translator(input_text)[0]['translation_text']

	elif target_language == "French":
		# Initalise the French translator
		translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
		translated_text = translator(input_text)[0]['translation_text']
  
	elif target_language == "Spanish":
		# Initalise the Spanish translator
		translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
		translated_text = translator(input_text)[0]['translation_text']

	# Print the translated text
	st.write("Translated text:", translated_text)
