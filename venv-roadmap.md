# Criar Ambiente Virtual de Desenvolvimento

Um ambiente virtual em Python funciona como um espaço isolado para cada um dos seus projetos. 
Isso é útil para garantir que diferentes projetos possam usar bibliotecas e versões específicas, evitando conflitos e preservando o ambiente principal do Python.

## Roteiro passo-a-passo via terminal CMD

### 1º | Crie uma pasta 
Crie uma pasta (pode ser na área de trabalho) com o nome "streamlit-project"

### 2º | Acesse o diretório da pasta
`CD C:\Users\eudes\OneDrive\Área de Trabalho\evento-streamlit\`

### 3º | Criar um ambiente virtual (https://docs.python.org/pt-br/3/library/venv.html)

 `python -m venv ambiente-virtual` 
 
 ou pode nomeá-la como virtual-env, v-env, venv... 

`python -m venv venv` 

### 4º | Navegue até a pasta 'Scripts' do ambiente virtual
`CD C:\Users\eudes\OneDrive\Área de Trabalho\evento-streamlit\ambiente-virtual\Scripts`

### 5º | Ative o ambiente virtual
Para ativar: `activate`

Para desativar: `deactivate`

### 6º | Retorne à pasta principal do projeto
Fazer o procedimento duas vezes para voltar à pasta principal.

`cd..` | `cd ..`

### 7º | Instale o Streamlit
`pip install streamlit`

Ou, para uma versão específica `pip install streamlit==1.39.0`

### Verifique a instalação
`pip show streamlit`

### 8º | Teste a estrutura do Streamlit
`streamlit hello`

### 9º | Para desligar a aplicação
Pressione Ctrl + C no terminal.

### 10º | Crie um arquivo para iniciar o aplicativo

`" echo print("Fala turma do evento!") > app.py "`

`streamlit run app.py`

### 11º | Iniciar o arquivo

Para iniciar o arquivo você pode rodar do cmd ou do terminal do VS Code.
Faça o seguinte:

- Entre na pasta colocando CD e o caminho. Ex.: `CD C:\Users\eudes\OneDrive\Área de Trabalho\evento-streamlit\`
- Digite streamlit mais o nome da aplicação que deseja rodar. Ex.: `streamlit app.py`

### 12º | Instalar o plotly

### Comandos extras úteis:

Command | Funtion
--- | ---
cls | Limpa o terminal.
dir | Mostra todos os arquivos no diretório.
mkdir <nome_do_diretório> | Cria um novo diretório.
rmdir <nome_do_diretório> | Remove um diretório vazio.
rm <arquivo> | Remove um arquivo.
pip list | Lista todos os pacotes instalados no ambiente virtual.
pip show <nome_pacote> | Mostra detalhes de um pacote instalado.
streamlit run <nomeArquivo.py> | Roda a aplicação Streamlit.
