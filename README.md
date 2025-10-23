Aqui está uma proposta de README.md completo para o seu projeto, já formatado em Markdown.  Ele destaca a origem acadêmica do projeto (TCC/PIBIC), a sua principal descoberta (NLTK \> BERT)  e as funcionalidades robustas que você implementou.

-----

# Automatização de Controle de Computador por Comando de Voz

 Este repositório contém o projeto final de um protótipo de Tecnologia Assistiva (TA) desenvolvido como Trabalho de Conclusão de Curso (TCC)   e projeto de Iniciação Científica (PIBIC) [cite: 911, 913]  no Instituto Federal do Amazonas (IFAM).

 O objetivo principal é permitir que pessoas com deficiência visual e motora controlem um computador com sistema operacional Windows utilizando comandos de voz em português, de forma totalmente offline.

## 💡 Conceito Principal

Diferente de assistentes de voz que dependem de grandes modelos de linguagem na nuvem, este projeto foca em uma solução leve, rápida e offline.

A pesquisa inicial (apresentada no TCC 1.0) comparou duas abordagens para a interpretação de comandos:

  *  **BERT (BERTugues):** Acurácia de 68.10%.
  *  **PLN Clássico (NLTK + TF-IDF):** Acurácia de 93.97% .

 Para o escopo de comandos definidos, a abordagem clássica com **NLTK se mostrou notavelmente superior, mais robusta, leve e eficiente**, sendo esta a arquitetura implementada na versão final.

## 🚀 Funcionalidades

O assistente é capaz de interpretar uma vasta gama de comandos, incluindo:

  * **Controle de Programas:**

      * Abrir e fechar o Navegador Web.
      * Abrir aplicações de produtividade (Word, Excel, Bloco de Notas, Calculadora).
      * Abrir aplicações de mídia (Spotify).
      * Fechar qualquer janela ou programa atual (`Alt+F4`).
      * Alternar entre janelas abertas (`Alt+Tab`).

  * **Navegação no Explorador de Arquivos:**

      * Abrir pastas principais (Documentos, Downloads, Área de Trabalho, Imagens, Músicas, Vídeos).
      * Acessar discos específicos (ex: "Abrir disco C").
      * Navegar para frente, para trás e subir um nível de pasta.

  * **Ações de Arquivo e Texto:**

      * Selecionar um arquivo ou pasta **pelo nome** (ex: "Selecionar pasta TCC").
      * Abrir um arquivo ou pasta **pelo nome** (ex: "Abrir pasta TCC").
      * Copiar, Colar, Recortar (Mover) e Apagar texto ou arquivos.
      * Selecionar tudo (`Ctrl+A`) e apagar (`Backspace`).

  * **Robustez e Segurança:**

      * **Confirmação de Comandos Críticos:** O sistema pede confirmação por voz ("Sim" ou "Não") antes de executar ações destrutivas, como deletar arquivos. 

  * **Controle de Mídia (Global):**

      * Tocar/Pausar, Próxima Música, Música Anterior (Funciona com Spotify, YouTube, etc.).

## 🛠️ Tecnologias Utilizadas

  * **Python 3.10+** 
  * **SpeechRecognition:** Para captura de áudio (Speech-to-Text) via microfone.
  * **PyAudio:** Dependência para o acesso ao microfone.
  * **pyttsx3:** Para o feedback em áudio (Text-to-Speech).
  * **NLTK (Natural Language Toolkit):** Para o pré-processamento de PLN (Tokenização, Stemming, Stopwords).
  * **Scikit-learn:** Para a vetorização TF-IDF e cálculo da Similaridade de Cosseno.
  * **PyAutoGUI:** Para a automação de ações de teclado e mouse (controlar o SO).

## 🏛️ Arquitetura do Projeto

O projeto foi modularizado seguindo a arquitetura proposta no TCC 1.0 (Figura 4.4) [cite: 537-538, 1289-1290], separando responsabilidades:

  * `main.py`: Ponto de entrada e orquestrador principal. Executa o loop de escuta e gerencia o fluxo de comandos críticos.
  * `modulo_captura.py`: **(Módulo de Captura)** Responsável por ouvir o microfone e transcrever o áudio em texto.
  * `modulo_interpretacao.py`: **(Módulo de Interpretação)** O "cérebro" do projeto. Processa o texto (PLN) e usa o modelo TF-IDF para identificar a intenção do usuário.
  * `modulo_execucao.py`: **(Módulo de Execução)** As "mãos" do projeto. Recebe a intenção e executa as automações (PyAutoGUI).
  * `modulo_feedback.py`: **(Módulo de Feedback)** A "voz" do projeto. Fornece retorno sonoro ao usuário (pyttsx3).
  * `config.py`: A "base de conhecimento". Contém os dicionários de intenções, comandos críticos e caminhos de programas.

## 🏁 Como Executar

1.  Clone este repositório:

    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2.  Crie e ative um ambiente virtual (recomendado):

    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Execute o programa principal:

    ```bash
    python main.py
    ```

    O sistema informará que foi iniciado e estará pronto para receber comandos.

5.  Para parar a aplicação, diga "Encerrar aplicação".

## 🧑‍💻 Autor

  * **Sannyer Cardoso Carvalho Nery** (Autor) 
  * **Prof. MSc.  Marcelo Chamy Machado** (Orientador) 
*Instituto Federal de Educação, Ciência e Tecnologia do Amazonas (IFAM) - Campus Manaus Centro* 