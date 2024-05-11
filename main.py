from src.controller.gemini_voize import GeminiVoice


if __name__ == "__main__":
    voice_gemini = GeminiVoice("", True, True)
    voice_gemini.set_voice()
    voice_gemini.get_Welcome()
    voice_gemini.gemini_voice()