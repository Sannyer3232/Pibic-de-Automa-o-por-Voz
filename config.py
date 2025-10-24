# config.py

# config.py
# (Substitua seu dicionário 'intents' por este)

intents = {
    # --- Navegação Web (Atualizado) ---
    "ABRIR_NAVEGADOR": [
        "Abrir navegador", "Abrir o Google", "Abrir Google Chrome", "Abrir Firefox",
        "Iniciar navegador", "Quero navegar na internet", "Abrir a internet",
        "Navegador", "Internet", "Google"
    ],
    "FECHAR_NAVEGADOR": [
        "Fechar navegador", "Encerrar navegador", "Sair do Google", "Fechar o Chrome",
        "Encerrar internet", "Sair da internet", "Fechar programa do navegador"
    ],
    "NOVA_GUIA": [
        "Abrir nova guia", "Nova aba", "Quero uma nova aba", "Abrir aba", "Mais uma aba",
        "Aba nova", "Ctrl T"
    ],
    "FECHAR_GUIA": [
        "Fechar esta guia", "Fechar aba", "Encerrar aba", "Fechar a guia atual",
        "Sair desta aba", "Ctrl W"
    ],
    "ALTERNAR_GUIA_PROXIMA": [
        "Próxima guia", "Mudar para a próxima aba", "Avançar aba", "Aba da direita",
        "Próxima", "Ctrl Tab"
    ],
    "ALTERNAR_GUIA_ANTERIOR": [
        "Guia anterior", "Voltar para aba anterior", "Aba da esquerda", "Aba anterior",
        "Anterior", "Ctrl Shift Tab"
    ],
    "ATUALIZAR_PAGINA": [
        "Atualizar página", "Recarregar página", "Atualizar", "Recarregar", "F5"
    ],
    "ABRIR_SITE": [ # A lógica de execução para isso não é genérica, mas os exemplos ajudam
        "Abrir YouTube", "Abrir Google", "Ir para G1", "Acessar UOL"
    ],
    "PESQUISAR_GOOGLE": [
        "Pesquisar sobre", "Buscar por", "Procure no Google sobre", "Quero pesquisar",
        "Busque por", "O que é", "Quem é", "Onde fica", "Qual o significado de", "Pesquisar"
    ],
    "PESQUISAR_PAGINA": [
        "Procurar por", "Buscar na página", "Encontrar na página", "Localizar palavra",
        "Onde está escrito", "Buscar aqui", "Ctrl F", "Pesquisar nesta página"
    ],
    "ROLAR_BAIXO": [
        "Descer a página", "Rolar para baixo", "Descer", "Rola para baixo", "Mais para baixo"
    ],
    "ROLAR_CIMA": [
        "Subir a página", "Rolar para cima", "Subir", "Rola para cima", "Mais para cima"
    ],
    "TOPO_PAGINA": [
        "Ir para o topo", "Voltar ao início", "Início da página", "Ir para cima de tudo", "Home"
    ],
    "FINAL_PAGINA": [
        "Ir para o final", "Descer até o final", "Fim da página", "Lá para baixo", "End"
    ],
    "WEB_PROXIMO_LINK": [
        "Próximo link", "Pular para próximo link", "Tab", "Avançar link", "Próximo item"
    ],
    "WEB_LINK_ANTERIOR": [
        "Link anterior", "Voltar link", "Shift Tab", "Item anterior", "Link acima"
    ],

    # --- Controle de Texto (Atualizado) ---
    "DIGITAR": [
        "Digitar", "Escrever", "Digite", "Escreva", "Quero escrever"
    ],
    "CONFIRMAR_ENVIO": [
        "Pressionar Enter", "Confirmar", "Enviar", "OK", "Vai", "Enter", "Confirmar envio"
    ],
    "COPIAR": [
        "Copiar", "Copiar texto", "Copiar arquivo", "Copiar seleção", "Ctrl C"
    ],
    "COLAR": [
        "Colar", "Colar texto", "Colar arquivo", "Colar seleção", "Ctrl V"
    ],
    "RECORTAR": [
        "Recortar", "Recortar arquivo", "Mover arquivo", "Cortar", "Mover", "Ctrl X"
    ],
    "APAGAR": [
        "Apagar", "Deletar", "Apagar texto", "Backspace", "Apagar o que escrevi", "Corrigir"
    ],
    "SELECIONAR_TUDO": [
        "Selecionar tudo", "Selecionar todo o texto", "Marcar tudo", "Ctrl A"
    ],

    # --- Programas de Produtividade (Atualizado) ---
    "ABRIR_BLOCO_DE_NOTAS": [
        "Abrir bloco de notas", "Iniciar bloco de notas", "Novo bloco de notas",
        "Quero anotar algo", "Abrir editor de texto"
    ],
    "ABRIR_WORD": [
        "Abrir Word", "Iniciar Microsoft Word", "Abrir o Word", "Quero digitar um documento",
        "Escrever no Word", "Novo documento"
    ],
    "ABRIR_EXCEL": [
        "Abrir Excel", "Iniciar Microsoft Excel", "Abrir planilha", "Nova planilha",
        "Quero usar o Excel", "Abrir planilhas"
    ],
    "ABRIR_CALCULADORA": [
        "Abrir calculadora", "Iniciar calculadora", "Preciso fazer uma conta",
        "Calcular", "Quero fazer contas"
    ],

    # --- Navegação no Explorador (Atualizado) ---
    "ABRIR_EXPLORADOR": [
        "Abrir explorador de arquivos", "Abrir pastas", "Acesso rápido", "Meus arquivos",
        "Abrir este computador", "Explorador de arquivos"
    ],
    "ABRIR_DESKTOP": [
        "Abrir área de trabalho", "Mostrar área de trabalho", "Ir para área de trabalho",
        "Desktop", "Ver meus ícones"
    ],
    "ABRIR_DOWNLOADS_PASTA": [
        "Abrir downloads", "Mostrar meus downloads", "Pasta downloads", "Ir para downloads"
    ],
    "ABRIR_DOCUMENTOS": [
        "Abrir documentos", "Mostrar meus documentos", "Pasta documentos", "Ir para documentos"
    ],
    "ABRIR_IMAGENS": [
        "Abrir imagens", "Mostrar minhas fotos", "Pasta imagens", "Minhas fotos"
    ],
    "ABRIR_MUSICAS": [
        "Abrir músicas", "Mostrar minhas músicas", "Pasta músicas", "Minhas músicas"
    ],
    "ABRIR_VIDEOS": [
        "Abrir vídeos", "Mostrar meus vídeos", "Pasta vídeos", "Meus vídeos"
    ],
    "ABRIR_DISCO": [
        "Abrir disco", "Acessar disco", "Ir para o disco", "Abrir disco C",
        "Abrir disco D", "Abrir pen drive"
    ], 
    "CRIAR_PASTA": [
        "Criar pasta", "Nova pasta", "Fazer uma nova pasta", "Quero criar um diretório",
        "Criar diretório", "Criar pasta chamada"
    ],
    "RENOMEAR_SELECIONADO": [
        "Renomear", "Renomear item", "Mudar nome para", "Quero renomear", "Renomear para",
        "Alterar nome", "Mudar o nome", "F2"
    ],

    # --- Navegação DENTRO do Explorador (Atualizado) ---
    "NAVEGAR_SELECIONAR_NOMEADO": [
        "Selecionar", "Achar", "Encontrar", "Selecionar item", "Focar em", "Onde está",
        "Localizar", "Selecionar arquivo", "Selecionar pasta"
    ],
    "NAVEGAR_ABRIR_NOMEADO": [
        "Abrir pasta", "Entrar em", "Ir para pasta", "Acessar pasta", "Abrir",
        "Abrir arquivo", "Abrir o arquivo", "Abrir a pasta", "Executar"
    ],
    "NAVEGAR_ABRIR_ITEM": [
        "Abrir item", "Entrar", "Abrir seleção", "Ativar link", "Clicar no link",
        "Abrir link selecionado", "Abrir o que está selecionado", "Abrir isso"
    ],
    "NAVEGAR_VOLTAR_PASTA": [
        "Voltar pasta", "Ir para trás", "Voltar", "Voltar página", "Página anterior",
        "Sair da pasta", "Nível anterior", "Alt esquerda"
    ],
    "NAVEGAR_SUBIR_PASTA": [
        "Subir pasta", "Pasta acima", "Nível acima", "Subir um nível", "Alt cima"
    ],

    # --- Paginação de Lista (Atualizado) ---
    "LISTAR_ARQUIVOS": [
        "Listar arquivos", "Listar pastas", "O que tem aqui", "Fale os arquivos",
        "Ler a pasta", "Listar itens", "Quais arquivos tem aqui"
    ],
    "PAGINA_PROXIMA": [
        "Próxima página", "Mais arquivos", "Próximos", "Ver mais", "Mais itens",
        "Próximos 5", "Continuar lista", "Mais"
    ],
    "PAGINA_ANTERIOR": [
        "Página anterior", "Arquivos anteriores", "Voltar página da lista", "Voltar lista",
        "Itens anteriores", "Página de trás", "Anteriores"
    ],

    # --- Controle de Mídia / Spotify (Atualizado) ---
    "ABRIR_SPOTIFY": [
        "Abrir Spotify", "Tocar música", "Spotify", "Quero ouvir música",
        "Iniciar Spotify", "Abrir meu spotify"
    ],
    "TOCAR_PAUSAR_MUSICA": [
        "Tocar música", "Pausar música", "Play", "Pause", "Despausar", "Retomar música",
        "Continuar música", "Parar música", "Tocar"
    ],
    "PROXIMA_MUSICA": [
        "Próxima música", "Avançar música", "Pular música", "Próxima faixa",
        "Pular faixa", "Próxima"
    ],
    "MUSICA_ANTERIOR": [
        "Música anterior", "Voltar música", "Faixa anterior", "Tocar anterior",
        "Música de trás", "Anterior"
    ],

    # --- Comandos do Sistema (Atualizado) ---
    "ENCERRAR": [
        "Encerrar aplicação", "Sair", "Fechar programa", "Parar assistente",
        "Desligar assistente", "Parar execução", "Tchau", "Até logo"
    ],
    "FECHAR_JANELA_ATUAL": [
        "Fechar janela", "Fechar janela atual", "Fechar programa atual", "Sair deste programa",
        "Fechar isso", "Alt F4"
    ], 
    "ALTERNAR_JANELA": [
        "Alternar janela", "Mudar de janela", "Mudar de programa", "Próximo programa",
        "Alt Tab", "Trocar de janela", "Próxima janela"
    ], 
    "DELETAR_ARQUIVO": [
        "Deletar arquivo", "Excluir arquivo", "Mover para lixeira", "Deletar", "Excluir",
        "Apagar arquivo", "Mandar para lixeira", "Apagar item"
    ],

    "MUSICA_ANTERIOR": [
        "Música anterior", "Voltar música", "Faixa anterior", "Tocar anterior",
        "Música de trás", "Anterior"
    ],
    # --- ADICIONANDO DE VOLTA OS CONTROLES DE VOLUME ---
    "AUMENTAR_VOLUME": [
        "Aumentar volume", "Subir o som", "Volume mais alto", "Aumentar",
        "Sobe o volume", "Aumenta o som", "Mais volume", "Volume pra cima"
    ],
    "DIMINUIR_VOLUME": [
        "Diminuir volume", "Baixar o som", "Volume mais baixo", "Diminuir",
        "Abaixa o volume", "Baixa o som", "Menos volume", "Volume pra baixo"
    ],
    "MUTAR_DESMUTAR": [
        "Mutar", "Silenciar", "Desmutar", "Ativar som", "Tirar o som",
        "Colocar no mudo", "Mudo", "Modo silencioso", "Voltar o som"
    ]
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