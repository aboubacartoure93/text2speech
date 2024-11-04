
'''
from gtts import gTTS
import os

# Define the text you want to convert to audio
text = "Hello Aboubacar! This is a simple text-to-speech conversion using Python."

# Set language (you can change to 'fr' for French, 'es' for Spanish, etc.)
language = 'en'

# Create a gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to an mp3 file
tts.save("output.mp3")

# Optionally, play the audio file (only works on some systems)
os.system("start output.mp3")  # On Windows, use "start"; on macOS, use "afplay"; on Linux, use "mpg321" or "vlc"
'''

'''
scope of the app***********************
text to audio (pdf, picture, handwritting)
several language, translation

pyttsx3 2.98 offline check
'''


from PyPDF2 import PdfReader
from gtts import gTTS

#python3.10 -m pip install PyPDF2
#install module python version

# Define a function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Define the PDF file path
pdf_path = "mathbook.pdf"

# Extract text from PDF
text = extract_text_from_pdf(pdf_path)

# Convert the extracted text to speech
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

# Save the audio to an mp3 file
tts.save("outputmath1.mp3")

print("Audio saved as output.mp3")

