# main.py
# Orquestrador principal da aplicação.

import speech_recognition as sr
from config import CRITICAL_COMMANDS
from modulo_captura import ouvir_comando, ouvir_confirmacao
from modulo_interpretacao import inicializar_vectorizer, identificar_intencao
from modulo_execucao import executar_comando
from modulo_feedback import falar

def main():
    """
    Função principal que inicializa os módulos e executa o loop de escuta.
    """
    # 1. Inicializa o Módulo de Interpretação (carrega o modelo TF-IDF)
    vectorizer = inicializar_vectorizer()
    
    # 2. Inicializa o Módulo de Captura
    recognizer = sr.Recognizer()
    microfone = sr.Microphone()
    
    # 3. Inicia o Módulo de Feedback
    falar("Sistema de controle de voz iniciado. Diga um comando.")
    
    # 4. Loop principal da aplicação
    rodando = True
    with microfone as source:
        while rodando:
            # 4.1. CAPTURA E TRANSCRIÇÃO
            comando = ouvir_comando(recognizer, source)
            
            if comando:
                # 4.2. INTERPRETAÇÃO DE INTENÇÃO
                intencao = identificar_intencao(comando, vectorizer)
                
                if intencao:
                    # --- LÓGICA DE COMANDO CRÍTICO ---
                    if intencao in CRITICAL_COMMANDS:
                        falar(f"Comando crítico detectado: {intencao.replace('_', ' ').lower()}. Você tem certeza?")
                        
                        confirmado = ouvir_confirmacao(recognizer, source)
                        
                        if confirmado:
                            falar("Confirmação recebida.")
                            executar_comando(intencao, comando)
                        else:
                            falar("Ação cancelada.")
                    
                    # --- LÓGICA DE COMANDO NORMAL ---
                    else:
                        if intencao == "ENCERRAR":
                            falar("Encerrando aplicação. Até logo!")
                            rodando = False
                        else:
                            executar_comando(intencao, comando)
                else:
                    # Feedback de falha na interpretação
                    falar("Comando não reconhecido. Por favor, tente novamente.")

if __name__ == "__main__":
    main()