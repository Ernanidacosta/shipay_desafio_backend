Para realizar o deploy do seu aplicativo em um ambiente produtivo usando Kubernetes e o banco de dados PostgreSQL, você pode seguir as etapas abaixo:

1. Crie um arquivo `Dockerfile` na raiz do seu projeto com o seguinte conteúdo:
   ```Dockerfile
   FROM python:3.9

   WORKDIR /app

   COPY requirements.txt .

   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. Crie um arquivo `deployment.yaml` para definir o deployment do seu aplicativo no Kubernetes. O arquivo pode ter o seguinte conteúdo:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: your-app-deployment
     labels:
       app: your-app
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: your-app
     template:
       metadata:
         labels:
           app: your-app
       spec:
         containers:
         - name: your-app
           image: your-image-name:your-tag
           ports:
           - containerPort: 8000
   ```

   Certifique-se de substituir `your-app-deployment`, `your-app`, `your-image-name` e `your-tag` pelos valores correspondentes ao seu aplicativo.

3. Crie um arquivo `service.yaml` para definir o serviço do seu aplicativo no Kubernetes. O arquivo pode ter o seguinte conteúdo:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: your-app-service
   spec:
     selector:
       app: your-app
     ports:
     - protocol: TCP
       port: 80
       targetPort: 8000
     type: LoadBalancer
   ```

   Certifique-se de substituir `your-app-service` e `your-app` pelos valores correspondentes ao seu aplicativo.

4. Crie um arquivo `postgres.yaml` para definir o deployment e serviço do banco de dados PostgreSQL no Kubernetes. O arquivo pode ter o seguinte conteúdo:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: postgres-deployment
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: postgres
     template:
       metadata:
         labels:
           app: postgres
       spec:
         containers:
         - name: postgres
           image: postgres:latest
           env:
           - name: POSTGRES_USER
             value: your-postgres-user
           - name: POSTGRES_PASSWORD
             value: your-postgres-password
           - name: POSTGRES_DB
             value: your-postgres-db
           ports:
           - containerPort: 5432

   ---
   
   apiVersion: v1
   kind: Service
   metadata:
     name: postgres-service
   spec:
     selector:
       app: postgres
     ports:
     - protocol: TCP
       port: 5432
       targetPort: 5432
   ```

   Certifique-se de substituir `your-postgres-user`, `your-postgres-password` e `your-postgres-db` pelos valores correspondentes às credenciais do seu banco de dados PostgreSQL.

5. No terminal, certifique-se de que o Kubernetes esteja configurado corretamente para o ambiente produtivo.

6. Execute os seguintes comandos para implantar seu aplicativo e o banco de dados no Kubernetes:


   ```
   kubectl apply -f postgres.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

   Isso criará o deployment e o serviço do banco de dados PostgreSQL, bem como o deployment e o serviço do seu aplicativo.

7. Você pode verificar o status dos recursos implantados executando os seguintes comandos:
   ```
   kubectl get deployments
   kubectl get services
   ```

   Certifique-se de que os pods estejam em execução e os serviços estejam ativos.

8. Agora, você pode acessar seu aplicativo em um ambiente produtivo usando o serviço definido. Você pode obter o endereço IP público do serviço executando o seguinte comando:
   ```
   kubectl get service your-app-service
   ```

   Use o endereço IP público e a porta para acessar o seu aplicativo.

Dessa forma, seu aplicativo será implantado em um ambiente produtivo usando Kubernetes e o banco de dados PostgreSQL. Certifique-se de fornecer as credenciais corretas do banco de dados no arquivo `postgres.yaml`. Além disso, você pode ajustar as réplicas e a configuração do deployment do seu aplicativo no arquivo `deployment.yaml` de acordo com as necessidades do seu ambiente produtivo.
