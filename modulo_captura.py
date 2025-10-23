# modulo_captura.py
# Responsável por capturar o áudio do microfone e transcrever para texto.

import speech_recognition as sr

def ouvir_comando(recognizer, microfone):
    """
    Captura o áudio do microfone e tenta transcrevê-lo usando o Google Speech Recognition.
    Retorna o texto do comando ou None se não entender.
    """
    try:
        print("Ouvindo...")
        # Ajusta o ruído ambiente
        recognizer.adjust_for_ambient_noise(microfone, duration=0.5)
        audio = recognizer.listen(microfone, timeout=5, phrase_time_limit=10)
        
        # Tenta reconhecer o áudio
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando
        
    except sr.WaitTimeoutError:
        print("Tempo limite de escuta excedido. Tente novamente.")
        return None
    except sr.UnknownValueError:
        print("Não entendi o comando.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao acessar o serviço de reconhecimento de voz: {e}")
        return None

# Adicione esta função no final do arquivo modulo_captura.py

def ouvir_confirmacao(recognizer, microfone):
    """
    Ouve especificamente por 'sim' ou 'não' para confirmações.
    Retorna True para 'sim' e False para 'não' ou silêncio.
    """
    try:
        print("Aguardando confirmação (Sim/Não)...")
        recognizer.adjust_for_ambient_noise(microfone, duration=0.5)
        audio = recognizer.listen(microfone, timeout=4, phrase_time_limit=3)
        
        resposta = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"Confirmação: {resposta}")
        
        if "sim" in resposta or "confirmar" in resposta:
            return True
        elif "não" in resposta or "cancelar" in resposta:
            return False
        else:
            return False
            
    except sr.WaitTimeoutError:
        print("Tempo limite de confirmação excedido.")
        return False
    except sr.UnknownValueError:
        print("Confirmação não compreendida.")
        return False
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento: {e}")
        return False