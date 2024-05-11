from src.api.api_gemini import ConfigGemini
import pyttsx3
import speech_recognition as sr

class GeminiVoice:

    def __init__(self, txt: str, ia_voice: bool, on_voice: bool):
      self.txt = txt
      self.ia_voice = ia_voice
      self.on_voice = on_voice
      self.convo = ConfigGemini(txt)

    def set_voice(self):
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        if self.ia_voice:
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('voice', voices[58].id)
    
    def get_Welcome(self):
      welcome = "Olá, eu sou a Gemini, como posso te ajudar?"
      print("")
      print(len(welcome) * "#")
      print(welcome)
      print(len(welcome) * "#")
        
    def gemini_voice(self):
        while True:
            if self.ia_voice:
                with self.mic as source:
                    self.rec.adjust_for_ambient_noise(source)
                    print("Fale alguma coisa (ou diga 'desligar')")
                    try:
                        audio = self.rec.listen(source, timeout=5)
                        print("Enviando para reconhecimento")
                        text = self.rec.recognize_google(audio, language="pt-BR")
                        print("Você disse:", text)
                    except sr.UnknownValueError:
                        print("Não entendi o que você disse.")
                        text = ""
                    except sr.RequestError as e:
                        print("Erro ao acessar o serviço de reconhecimento de voz:", e)
                        text = ""
            if text.lower() == "desligar":
                break
            response = self.convo.get_ia_response()
            print("Gemini:", response, "\n")
            if self.on_voice:
                self.engine.say(response.replace("*", ""))
                self.engine.runAndWait()
            print("Encerrando Chat")

