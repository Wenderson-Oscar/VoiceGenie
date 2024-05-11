from src.controller.gemini_voize import GeminiVoice


if __name__ == "__main__":
    voice_gemini = GeminiVoice("Houve um problema no reconhecimento de voz, verifique o Micro-fone", True, True)
    voice_gemini.set_voice()
    voice_gemini.get_Welcome()
    voice_gemini.gemini_voice()