Para executar o projeto em ambiente local usando Docker, Docker Compose e SQLite, você pode seguir as etapas abaixo:

1. Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema.

2. Crie um arquivo `Dockerfile` na raiz do seu projeto com o seguinte conteúdo:
   ```
   FROM python:3.9

   WORKDIR /app

   COPY requirements.txt .

   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

3. Crie um arquivo `docker-compose.yml` na raiz do seu projeto com o seguinte conteúdo:
   ```
   version: "3"
   services:
     app:
       build:
         context: .
         dockerfile: Dockerfile
       ports:
         - 8000:8000
       depends_on:
         - db
     db:
       image: "sqlite"
       volumes:
         - ./database:/database
   ```

4. Certifique-se de que a estrutura do banco de dados esteja definida no seu código, como mencionado anteriormente.

5. No terminal, navegue até o diretório do seu projeto e execute o seguinte comando para construir as imagens e iniciar os contêineres:
   ```
   docker-compose up --build
   ```

6. O Docker Compose irá construir a imagem do seu aplicativo e criar um contêiner para o aplicativo FastAPI, juntamente com um contêiner para o banco de dados SQLite. O aplicativo será executado na porta 8000 do seu sistema local.

7. Agora, você pode acessar a API localmente em `http://localhost:8000`.

Dessa forma, seu projeto estará sendo executado em ambiente local usando Docker, Docker Compose e SQLite. Certifique-se de que a string de conexão do banco de dados SQLite esteja configurada corretamente no seu código. O Docker Compose criará um volume para persistir os dados do banco de dados na pasta `./database` do seu projeto. Isso garantirá que os dados não sejam perdidos quando os contêineres forem reiniciados.
