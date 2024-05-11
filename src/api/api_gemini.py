import google.generativeai as genai
import environs
import pyttsx3


env = environs.Env()
env.read_env()

class ConfigGemini:

    def __init__(self, txt: str):
      self.txt = txt
      self.genai = genai
      self.genai.configure(api_key=env.str("API_KEY"))
      self.generation_config = {"temperature": 1, "top_p": 0.95, "top_k": 0, "max_output_tokens": 8192}
      self.safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
      ]
      self.model = self.genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest", 
        generation_config=self.generation_config, 
        safety_settings=self.safety_settings
        )
      self.convo = self.model.start_chat(history=[])
    
    def get_ia_response(self):
      self.convo.send_message(self.txt)
      return self.convo.last.text
