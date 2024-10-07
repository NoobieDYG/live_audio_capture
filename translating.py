import whisper
import requests

'''def translate_ar_to_en(text):
    url="https://libretranslate.com/translate"
    data = {
        "q": text,
        "source": "ar",
        "target": "en",
        "format": "text"
    }
    response = requests.post(url,data=data)
    return response.json()["translatedText"]'''


# Function to translate Arabic to English using LibreTranslate API
def translate_ar_to_en(text):
    try:
        url = "https://libretranslate.com/translate"
        data = {
            "q": text,
            "source": "ar",
            "target": "en",
            "format": "text"
        }
        response = requests.post(url, data=data)
        response_data = response.json()
        
        # Debugging: Print the entire response to see its structure
        print(f"API Response: {response_data}")

        if 'translatedText' in response_data:
            return response_data['translatedText']
        else:
            raise KeyError("The response does not contain 'translatedText'.")
    except Exception as e:
        print(f"Translation failed: {e}")
        return None


model=whisper.load_model("small")

result=model.transcribe('chunk.wav')
arabic_text=result['text']
english_text=translate_ar_to_en(arabic_text)
print(f'Translated text is {english_text}')