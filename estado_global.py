# estado_global.py
# Gerencia o estado da aplicação, como a lista de arquivos para paginação.

# Limite de arquivos para falar por vez
ITENS_POR_PAGINA = 5

# Variáveis de estado
arquivos_atuais = []
pagina_atual = 0

def set_lista_arquivos(lista):
    """
    Define uma nova lista de arquivos para paginar e reseta o contador.
    """
    global arquivos_atuais, pagina_atual
    arquivos_atuais = lista
    pagina_atual = 0

def get_proxima_pagina():
    """
    Retorna a próxima página de itens da lista atual.
    """
    global pagina_atual
    if not arquivos_atuais:
        return None, "Nenhuma lista de arquivos carregada."
    
    inicio = pagina_atual * ITENS_POR_PAGINA
    if inicio >= len(arquivos_atuais):
        pagina_atual = 0 # Reseta ao chegar no fim
        return None, "Você chegou ao final da lista. Próximo comando começará do início."
    
    fim = inicio + ITENS_POR_PAGINA
    pagina_atual += 1
    
    pagina_de_itens = arquivos_atuais[inicio:fim]
    mensagem = f"Mostrando itens {inicio + 1} a {min(fim, len(arquivos_atuais))} de {len(arquivos_atuais)}."
    
    return pagina_de_itens, mensagem

def get_pagina_anterior():
    """
    Retorna a página anterior de itens.
    """
    global pagina_atual
    if not arquivos_atuais:
        return None, "Nenhuma lista de arquivos carregada."
    
    if pagina_atual <= 1:
        return None, "Você já está no início da lista."
    
    # Decrementa 2: 1 para voltar à página atual, 1 para ir à anterior.
    pagina_atual -= 2
    return get_proxima_pagina()