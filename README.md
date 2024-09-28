# PyDepCheck

**PyDepCheck** is a command-line tool in Python that analyzes a Python script to identify its dependencies and optionally installs those that are not present in the environment. It is a practical solution for developers who want to ensure that all necessary libraries are installed.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributions](#contributions)
- [License](#license)

## Features

- Analyzes a Python file to extract dependencies.
- Checks if the dependencies are installed.
- Automatically installs missing dependencies if desired.
- Mapping of import names to installation names.

## Installation

1. Make sure you have Python 3 and `pip` installed on your system.
2. Clone the repository:

   ```bash
   git clone https://github.com/your_username/PyDepCheck.git
   cd PyDepCheck



Usage

To use PyDepCheck, run the script in the terminal as follows:

python pydepcheck.py path/to/your/script.py [-i | --install]

path/to/your/script.py: The path to the Python script you want to analyze.

-i or --install: (Optional) Automatically installs missing dependencies.


Example

python pydepcheck.py my_script.py --install

How It Works

1. The program analyzes the specified Python script and extracts dependencies using the ast library to process the syntax tree of the code.


2. It checks if the dependencies are installed by attempting to import them.


3. If it finds dependencies that are not installed, the user can choose to install them automatically.


4. A JSON file (matches.json) is used to map import names to installation names, ensuring that the correct packages are installed.



Example of a matches.json file

{
  "PIL": "pillow",
  "bs4": "beautifulsoup4",
  "cv2": "opencv-python"
}

Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements.





# PyDepCheck

**PyDepCheck** é uma ferramenta de linha de comando em Python que analisa um script Python para identificar suas dependências e, opcionalmente, instala as que não estão presentes no ambiente. É uma solução prática para desenvolvedores que desejam garantir que todas as bibliotecas necessárias estejam instaladas.

## Tabela de Conteúdos

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Como Funciona](#como-funciona)
- [Contribuições](#contribuições)

## Recursos

- Analisa um arquivo Python para extrair dependências.
- Verifica se as dependências estão instaladas.
- Instala automaticamente as dependências não instaladas, se desejado.
- Mapeamento de nomes de importação para nomes de instalação.

## Instalação

1. Certifique-se de que você tenha o Python 3 e `pip` instalados em seu sistema.
2. Clone o repositório:

   ```bash
   git clone https://github.com/marcosarlove/PyDepCheck.git
   cd PyDepCheck



Uso

Para utilizar o PyDepCheck, execute o script no terminal da seguinte forma:

python pydepcheck.py caminho/do/seu/script.py [-i | --install]

caminho/do/seu/script.py: O caminho para o script Python que você deseja analisar.

-i ou --install: (Opcional) Instala automaticamente as dependências não instaladas.


Exemplo

python pydepcheck.py meu_script.py --install

Como Funciona

1. O programa analisa o script Python especificado e extrai as dependências utilizando a biblioteca ast para processar a árvore de sintaxe do código.


2. Ele verifica se as dependências estão instaladas, tentando importá-las.


3. Se encontrar dependências que não estão instaladas, o usuário pode optar por instalá-las automaticamente.


4. Um arquivo JSON (matches.json) é utilizado para mapear nomes de importação para nomes de instalação, garantindo que os pacotes corretos sejam instalados.



Exemplo de um arquivo matches.json

{
  "PIL": "pillow",
  "bs4": "beautifulsoup4",
  "cv2": "opencv-python"
}

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para discutir melhorias.
