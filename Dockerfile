# Imagem base
FROM python:3.9-slim-buster

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de código-fonte para o diretório de trabalho
COPY . /app

# Instalar as dependências do projeto
RUN pip install -r requirements.txt

# Definir o comando de inicialização do servidor da API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
