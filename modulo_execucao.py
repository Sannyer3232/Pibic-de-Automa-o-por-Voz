# modulo_execucao.py
# Responsável por executar as ações (automação) e chamar o feedback.

import webbrowser
import pyautogui
import pyperclip
import time
import estado_global as estado
import os
from config import comandos_programas, intents
from modulo_feedback import falar

def abrir_programa(nome_programa):
    """
    Tenta abrir um programa com base no nome e no caminho em config.py.
    """
    caminho = comandos_programas.get(nome_programa.lower())
    if caminho:
        try:
            os.startfile(caminho)
            falar(f"Abrindo {nome_programa}")
        except Exception as e:
            print(f"Erro ao abrir {nome_programa}: {e}")
            falar(f"Não consegui abrir o {nome_programa}. Verifique o caminho.")
    else:
        falar(f"Não conheço o programa {nome_programa}")

def executar_comando(intencao, comando_original):
    """
    Recebe a intenção identificada e o comando de voz original.
    Executa a ação correspondente (pyautogui, os, webbrowser).
    """
    try:
        # --- AÇÕES DE NAVEGAÇÃO WEB ---
        if intencao == "ABRIR_NAVEGADOR":
            falar("Abrindo o navegador.")
            webbrowser.open("https://www.google.com")
        
        elif intencao == "FECHAR_NAVEGADOR":
            falar("Fechando o navegador.")
            pyautogui.hotkey("alt", "f4")
        
        elif intencao == "NOVA_GUIA":
            falar("Abrindo nova guia.")
            pyautogui.hotkey("ctrl", "t")
        
        elif intencao == "FECHAR_GUIA":
            falar("Fechando guia.")
            pyautogui.hotkey("ctrl", "w")
        
        elif intencao == "ALTERNAR_GUIA_PROXIMA":
            falar("Próxima guia.")
            pyautogui.hotkey("ctrl", "tab")
        
        elif intencao == "ALTERNAR_GUIA_ANTERIOR":
            falar("Guia anterior.")
            pyautogui.hotkey("ctrl", "shift", "tab")
        
        elif intencao == "ATUALIZAR_PAGINA":
            falar("Atualizando.")
            pyautogui.hotkey("ctrl", "r")
        
        elif intencao == "ROLAR_BAIXO":
            falar("Rolando para baixo.")
            pyautogui.scroll(-500)
        
        elif intencao == "ROLAR_CIMA":
            falar("Rolando para cima.")
            pyautogui.scroll(500)
        
        elif intencao == "TOPO_PAGINA":
            falar("Indo para o topo.")
            pyautogui.hotkey("home")
        
        elif intencao == "FINAL_PAGINA":
            falar("Indo para o final.")
            pyautogui.hotkey("end")
        
        elif intencao == "PESQUISAR_GOOGLE":
            pesquisa = comando_original.replace("pesquisar sobre", "").replace("buscar por", "").strip()
            falar(f"Pesquisando sobre {pesquisa}")
            pyautogui.hotkey("ctrl", "l") # Foca na barra de endereço
            pyautogui.write(pesquisa)
            pyautogui.press("enter")
        
        elif intencao == "PESQUISAR_PAGINA":
            pesquisa = comando_original.replace("procurar por", "").replace("buscar na página", "").strip()
            falar(f"Procurando por {pesquisa} na página.")
            pyautogui.hotkey("ctrl", "f")
            pyautogui.write(pesquisa)

        # --- AÇÕES DE EDIÇÃO DE TEXTO E ARQUIVOS ---
        elif intencao == "DIGITAR":
            texto_digitado = comando_original.replace("digitar", "").replace("escrever", "").strip()
            falar(f"Digitando: {texto_digitado}")
            pyautogui.write(texto_digitado)
            
        elif intencao == "COPIAR":
            falar("Copiado.")
            pyautogui.hotkey("ctrl", "c")
            
        elif intencao == "COLAR":
            falar("Colado.")
            pyautogui.hotkey("ctrl", "v")

        elif intencao == "RECORTAR":
            falar("Recortado.")
            pyautogui.hotkey("ctrl", "x")
            
        elif intencao == "APAGAR":
            falar("Apagado.")
            pyautogui.press("backspace")

        elif intencao == "SELECIONAR_TUDO":
            falar("Tudo selecionado.")
            pyautogui.hotkey("ctrl", "a")
            
        elif intencao == "CONFIRMAR_ENVIO":
            falar("Confirmado.")
            pyautogui.press("enter")

        # --- AÇÕES DE NAVEGAÇÃO DE PASTAS ---
        
        # Comandos PARA ABRIR o Explorer em locais
        elif intencao == "ABRIR_EXPLORADOR":
            falar("Abrindo o explorador de arquivos.")
            abrir_no_explorer("") # Abre o "Acesso Rápido"
            
        elif intencao == "ABRIR_DESKTOP":
            falar("Abrindo a área de trabalho.")
            abrir_no_explorer("shell:desktop")

        elif intencao == "ABRIR_DOWNLOADS_PASTA":
            falar("Abrindo a pasta de downloads.")
            abrir_no_explorer("shell:downloads")

        elif intencao == "ABRIR_DOCUMENTOS":
            falar("Abrindo a pasta de documentos.")
            abrir_no_explorer("shell:documents")

        elif intencao == "ABRIR_IMAGENS":
            falar("Abrindo a pasta de imagens.")
            abrir_no_explorer("shell:pictures")

        elif intencao == "ABRIR_MUSICAS":
            falar("Abrindo a pasta de músicas.")
            abrir_no_explorer("shell:music")

        elif intencao == "ABRIR_VIDEOS":
            falar("Abrindo a pasta de vídeos.")
            abrir_no_explorer("shell:videos")
            
        elif intencao == "ABRIR_DISCO":
            comando_lower = comando_original.lower()
            partes = comando_lower.split("disco ")
            if len(partes) > 1:
                letra = partes[1].strip()[0] 
                if 'a' <= letra <= 'z':
                    caminho_disco = f"{letra}:"
                    falar(f"Abrindo o disco {letra}.")
                    abrir_no_explorer(caminho_disco)
                else:
                    falar("Não entendi a letra do disco. Tente dizer 'Abrir disco C'.")
            else:
                falar("Não entendi a letra do disco. Tente dizer 'Abrir disco C'.")
        
        # --- AÇÕES DENTRO do Explorer ---
        elif intencao == "CRIAR_PASTA":
            caminho_atual = get_explorer_path()
            if caminho_atual:
                nome_pasta = None
                comando_lower = comando_original.lower()
                triggers = intents["CRIAR_PASTA"]
                
                for trigger in triggers:
                    trigger_lower = trigger.lower()
                    if comando_lower.startswith(trigger_lower + " "):
                        nome_pasta = comando_original[len(trigger):].strip()
                        if nome_pasta:
                            break
                
                if not nome_pasta: # Se o comando foi só "Criar pasta"
                    nome_pasta = "Nova pasta"
                    
                try:
                    os.mkdir(os.path.join(caminho_atual, nome_pasta))
                    falar(f"Pasta '{nome_pasta}' criada.")
                except Exception as e:
                    falar(f"Não foi possível criar a pasta. Erro: {e}")
            else:
                falar("Não consegui identificar a pasta atual para criar o diretório.")

        elif intencao == "RENOMEAR_SELECIONADO":
            nome_novo = None
            comando_lower = comando_original.lower()
            triggers = intents["RENOMEAR_SELECIONADO"]
            
            for trigger in triggers:
                trigger_lower = trigger.lower()
                if comando_lower.startswith(trigger_lower + " "):
                    nome_novo = comando_original[len(trigger):].strip()
                    if nome_novo:
                        break
            
            if nome_novo:
                falar(f"Renomeando para {nome_novo}")
                pyautogui.press("f2")
                time.sleep(0.1)
                pyautogui.write(nome_novo)
                pyautogui.press("enter")
            else:
                falar("Não entendi o novo nome. Tente 'Renomear para [novo nome]'.")

        elif intencao == "NAVEGAR_SELECIONAR_NOMEADO":
            nome_item = None
            comando_lower = comando_original.lower()
            triggers = intents["NAVEGAR_SELECIONAR_NOMEADO"]
            
            for trigger in triggers:
                trigger_lower = trigger.lower()
                if comando_lower.startswith(trigger_lower + " "):
                    nome_item = comando_original[len(trigger):].strip()
                    if nome_item:
                        break
            
            if nome_item:
                falar(f"Selecionando {nome_item}")
                pyautogui.write(nome_item) 
            else:
                falar("Não entendi o que devo selecionar.")
        
        elif intencao == "NAVEGAR_ABRIR_NOMEADO":
            nome_pasta = None
            comando_lower = comando_original.lower()
            triggers = intents["NAVEGAR_ABRIR_NOMEADO"]
            
            for trigger in triggers:
                trigger_lower = trigger.lower()
                if comando_lower.startswith(trigger_lower + " "):
                    nome_pasta = comando_original[len(trigger):].strip()
                    if nome_pasta:
                        break
            
            if nome_pasta:
                falar(f"Abrindo {nome_pasta}")
                pyautogui.write(nome_pasta) 
                pyautogui.press("enter")
            else:
                falar("Não entendi o nome da pasta.")

        elif intencao == "NAVEGAR_ABRIR_ITEM":
            falar("Abrindo item selecionado.")
            pyautogui.press("enter")
            
        elif intencao == "NAVEGAR_VOLTAR_PASTA":
            falar("Voltando.")
            pyautogui.hotkey("alt", "left") # Funciona no Explorer E no Navegador
            
        elif intencao == "NAVEGAR_SUBIR_PASTA":
            falar("Subindo pasta.")
            pyautogui.hotkey("alt", "up")
            
        # --- AÇÕES DE PAGINAÇÃO DE LISTA ---
        elif intencao == "LISTAR_ARQUIVOS":
            caminho = get_explorer_path()
            if caminho:
                try:
                    falar(f"Listando arquivos em {os.path.basename(caminho)}")
                    lista_arquivos = os.listdir(caminho)
                    estado.set_lista_arquivos(lista_arquivos)
                    
                    itens, msg = estado.get_proxima_pagina()
                    falar(msg)
                    if itens:
                        texto_lista = ". ".join(itens)
                        falar(texto_lista)
                        
                except Exception as e:
                    falar(f"Não consegui ler os arquivos. Erro: {e}")
            else:
                falar("Não foi possível determinar a pasta atual.")
                
        elif intencao == "PAGINA_PROXIMA":
            itens, msg = estado.get_proxima_pagina()
            falar(msg)
            if itens:
                texto_lista = ". ".join(itens)
                falar(texto_lista)

        elif intencao == "PAGINA_ANTERIOR":
            itens, msg = estado.get_pagina_anterior()
            falar(msg)
            if itens:
                texto_lista = ". ".join(itens)
                falar(texto_lista)
                
        # --- AÇÕES DE NAVEGAÇÃO WEB (NOVAS) ---
        elif intencao == "WEB_PROXIMO_LINK":
            falar("Próximo link.")
            pyautogui.press("tab")

        elif intencao == "WEB_LINK_ANTERIOR":
            falar("Link anterior.")
            pyautogui.hotkey("shift", "tab")

        # --- AÇÕES DE MÍDIA / SPOTIFY ---
        elif intencao == "ABRIR_SPOTIFY":
            abrir_programa("spotify")
            
        elif intencao == "TOCAR_PAUSAR_MUSICA":
            falar("Play / Pause.")
            pyautogui.press("playpause")
            
        elif intencao == "PROXIMA_MUSICA":
            falar("Próxima música.")
            pyautogui.press("nexttrack")
            
        elif intencao == "MUSICA_ANTERIOR":
            falar("Música anterior.")
            pyautogui.press("prevtrack")
        
        # --- BLOCO DE CONTROLE DE VOLUME ADICIONADO ---
        elif intencao == "AUMENTAR_VOLUME":
            falar("Aumentando o volume.")
            pyautogui.press("volumeup")

        elif intencao == "DIMINUIR_VOLUME":
            falar("Diminuindo o volume.")
            pyautogui.press("volumedown")

        elif intencao == "MUTAR_DESMUTAR":
            falar("Mudo.")
            pyautogui.press("volumemute")

        # --- AÇÕES DE PROGRAMAS ---
        elif intencao == "ABRIR_BLOCO_DE_NOTAS":
            abrir_programa("bloco de notas")
        
        elif intencao == "ABRIR_WORD":
            abrir_programa("word")
        
        elif intencao == "ABRIR_EXCEL":
            abrir_programa("excel")
        
        elif intencao == "ABRIR_CALCULADORA":
            abrir_programa("calculadora")

        elif intencao == "FECHAR_JANELA_ATUAL":
            falar("Fechando janela atual.")
            pyautogui.hotkey("alt", "f4")

        elif intencao == "ALTERNAR_JANELA":
            falar("Alternando janela.")
            pyautogui.hotkey("alt", "tab")

        # --- AÇÕES CRÍTICAS (JÁ CONFIRMADAS PELO MAIN) ---
        elif intencao == "DELETAR_ARQUIVO":
            falar("Enviando para a lixeira.")
            pyautogui.press("delete")
            
        # --- AÇÕES DO SISTEMA ---
        elif intencao == "ENCERRAR":
            falar("Encerrando aplicação.")
            
        else:
            falar(f"Intenção {intencao} reconhecida, mas sem ação definida.")

    except Exception as e:
        print(f"Erro ao executar a ação {intencao}: {e}")
        falar("Ocorreu um erro ao tentar executar o comando.")
def abrir_no_explorer(caminho_shell):
    """
    Usa o comando 'explorer.exe' para abrir um caminho específico.
    Isso é mais robusto para 'shell:' e letras de disco.
    """
    try:
        os.system(f"explorer.exe {caminho_shell}")
    except Exception as e:
        print(f"Erro ao abrir explorer com {caminho_shell}: {e}")
        falar("Não consegui abrir o explorador.")

# Em modulo_execucao.py, abaixo da função abrir_no_explorer

def get_explorer_path():
    """
    Tenta obter o caminho da pasta ativa no Windows Explorer.
    Foca na barra de endereço (Alt+D), copia (Ctrl+C) e lê do clipboard.
    """
    try:
        pyautogui.hotkey("alt", "d") # Foca na barra de endereço
        time.sleep(0.1) # Pequena pausa para o SO responder
        pyautogui.hotkey("ctrl", "c") # Copia o caminho
        time.sleep(0.1)
        caminho = pyperclip.paste() # Lê o caminho do clipboard
        return caminho
    except Exception as e:
        print(f"Erro ao tentar obter o caminho do explorer: {e}")
        falar("Não consegui identificar a pasta atual.")
        return None