# modulo_feedback.py
# Responsável por fornecer o feedback em áudio (Text-to-Speech).

import pyttsx3

def falar(texto):
    """
    Executa a síntese de fala.
    O motor é inicializado e descartado a cada chamada
    para evitar problemas de loop do pyttsx3.
    """
    try:
        # Inicializa um NOVO motor a cada chamada
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
        
        # O motor é descartado automaticamente ao sair do escopo da função
    
    except Exception as e:
        # Adiciona um print de erro mais visível
        print("*************************************")
        print(f"ERRO NO MOTOR DE FALA: {e}")
        print("*************************************")