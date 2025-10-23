# config.py

intents = {
    # --- Navegação Web (Existente) ---
    "ABRIR_NAVEGADOR": ["Abrir navegador", "Abrir Google Chrome", "Abrir Firefox"],
    "FECHAR_NAVEGADOR": ["Fechar navegador", "Encerrar navegador"],
    "NOVA_GUIA": ["Abrir nova guia", "Nova aba"],
    "FECHAR_GUIA": ["Fechar esta guia", "Fechar aba"],
    "ALTERNAR_GUIA_PROXIMA": ["Próxima guia", "Mudar para a próxima aba"],
    "ALTERNAR_GUIA_ANTERIOR": ["Guia anterior", "Voltar para aba anterior"],
    "ATUALIZAR_PAGINA": ["Atualizar página", "Recarregar página"],
    "ABRIR_SITE": ["Abrir YouTube", "Abrir Google", "Ir para [site]"],
    "PESQUISAR_GOOGLE": ["Pesquisar sobre", "Buscar por"],
    "PESQUISAR_PAGINA": ["Procurar por", "Buscar na página"],
    "ACESSAR_FAVORITOS": ["Abrir favoritos", "Acessar marcadores"],
    "ROLAR_BAIXO": ["Descer a página", "Rolar para baixo"],
    "ROLAR_CIMA": ["Subir a página", "Rolar para cima"],
    "TOPO_PAGINA": ["Ir para o topo", "Voltar ao início"],
    "FINAL_PAGINA": ["Ir para o final", "Descer até o final"],
    "CLICAR": ["Clicar em", "Selecionar"],
    "BAIXAR_ARQUIVO": ["Baixar", "Fazer download"],
    "ABRIR_DOWNLOADS": ["Abrir pasta de downloads", "Ver downloads"],

    # --- Controle de Texto (Existente) ---
    "DIGITAR": ["Digitar", "Escrever"],
    "CONFIRMAR_ENVIO": ["Pressionar Enter", "Confirmar"],
    "COPIAR": ["Copiar", "Copiar texto", "Copiar arquivo", "Copiar seleção"],
    "COLAR": ["Colar", "Colar texto", "Colar arquivo", "Colar seleção"],
    "RECORTAR": ["Recortar", "Recortar arquivo", "Mover arquivo"],
    "APAGAR": ["Apagar", "Deletar", "Apagar texto", "Backspace"],
    "SELECIONAR_TUDO": ["Selecionar tudo", "Selecionar todo o texto"],

    # --- Programas de Produtividade (Existente) ---
    "ABRIR_BLOCO_DE_NOTAS": ["Abrir bloco de notas", "Iniciar bloco de notas"],
    "ABRIR_WORD": ["Abrir Word", "Iniciar Microsoft Word"],
    "ABRIR_EXCEL": ["Abrir Excel", "Iniciar Microsoft Excel"],
    "ABRIR_CALCULADORA": ["Abrir calculadora", "Iniciar calculadora"],

    # --- Navegação no Explorador (Novos e Atualizados) ---
    "ABRIR_EXPLORADOR": ["Abrir explorador de arquivos", "Abrir pastas", "Acesso rápido"],
    "ABRIR_DESKTOP": ["Abrir área de trabalho", "Mostrar área de trabalho"],
    "ABRIR_DOWNLOADS_PASTA": ["Abrir downloads", "Mostrar meus downloads", "Pasta downloads"],
    "ABRIR_DOCUMENTOS": ["Abrir documentos", "Mostrar meus documentos", "Pasta documentos"],
    "ABRIR_IMAGENS": ["Abrir imagens", "Mostrar minhas fotos", "Pasta imagens"],
    "ABRIR_MUSICAS": ["Abrir músicas", "Mostrar minhas músicas", "Pasta músicas"],
    "ABRIR_VIDEOS": ["Abrir vídeos", "Mostrar meus vídeos", "Pasta vídeos"],
    "ABRIR_DISCO": ["Abrir disco", "Acessar disco", "Ir para o disco"], # Ex: "Abrir disco C"


    # --- Navegação DENTRO do Explorador ---
    "NAVEGAR_SELECIONAR_NOMEADO": ["Selecionar", "Achar", "Encontrar", "Selecionar item"], 
    "NAVEGAR_ABRIR_NOMEADO": ["Abrir pasta", "Entrar em", "Ir para pasta", "Acessar pasta", "Abrir"],
    "NAVEGAR_ABRIR_ITEM": ["Abrir item", "Entrar", "Abrir seleção"], 
    "NAVEGAR_VOLTAR_PASTA": ["Voltar pasta", "Ir para trás", "Voltar"],
    "NAVEGAR_SUBIR_PASTA": ["Subir pasta", "Pasta acima"],
    

    # --- Controle de Mídia / Spotify (Existente) ---
    "ABRIR_SPOTIFY": ["Abrir Spotify", "Tocar música", "Spotify"],
    "TOCAR_PAUSAR_MUSICA": ["Tocar música", "Pausar música", "Play", "Pause", "Despausar"],
    "PROXIMA_MUSICA": ["Próxima música", "Avançar música"],
    "MUSICA_ANTERIOR": ["Música anterior", "Voltar música"],

    

    # --- Comandos do Sistema (Existente) ---
    "ENCERRAR": ["Encerrar aplicação", "Sair", "Fechar programa"],
    "FECHAR_JANELA_ATUAL": ["Fechar janela", "Fechar janela atual", "Fechar programa atual"], 
    "ALTERNAR_JANELA": ["Alternar janela", "Mudar de janela", "Mudar de programa", "Próximo programa"], 
    "DELETAR_ARQUIVO": ["Deletar arquivo", "Excluir arquivo", "Mover para lixeira"]
}

# Caminhos dos programas
comandos_programas = {
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "bloco de notas": "notepad.exe",
    "calculadora": "calc.exe",
    "spotify": "spotify.exe" 
}

# --- DEFINIÇÃO DE COMANDOS CRÍTICOS ---
CRITICAL_COMMANDS = {
    "DELETAR_ARQUIVO",
}