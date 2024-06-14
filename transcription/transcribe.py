import openai

def transcribe_audio(api_key, audio_file_path):
    openai.api_key = api_key

    try:
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        return response['text']
    except openai.error.InvalidRequestError as e:
        print(f"Request error: {e}")
    except openai.error.AuthenticationError as e:
        print(f"Authentication error: {e}")
    except openai.error.APIError as e:
        print(f"API error: {e}")
    except openai.error.APIConnectionError as e:
        print(f"Connection error: {e}")
    except openai.error.RateLimitError as e:
        print(f"Rate limit error: {e}")

    return None