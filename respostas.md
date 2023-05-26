1 - Consulta SQL para retornar o nome, e-mail, descrição do papel e descrições das permissões/claims de um usuário:

```sql
SELECT u."name", u.email, r.description AS role_description, c.description AS claim_description
FROM users u
JOIN roles r ON u.role_id = r.id
JOIN user_claims uc ON u.id = uc.user_id
JOIN claims c ON uc.claim_id = c.id
WHERE u.id = <user_id>;

```
---
2 - exemplo da consulta anterior utilizando o ORM SQLAlchemy em Python:
```python
query = session.query(User.name, User.email, Role.description, Claim.description)\
    .join(Role, User.role_id == Role.id)\
    .join(UserClaim, User.id == UserClaim.user_id)\
    .join(Claim, UserClaim.claim_id == Claim.id)

results = query.all()
for result in results:
    print("Name:", result.name)
    print("Email:", result.email)
    print("Role Description:", result.description)
    print("Claim Description:", result.description)
```
---
## Respostas 3 e 4 no arquivo [`main.py`](/main.py)

---
Resposta 05 

## Executando o projeto em ambiente local

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python em https://www.python.org/downloads/.

2. Clone o repositório do projeto para o seu ambiente local.

3. Navegue até o diretório raiz do projeto.

4. Crie e ative um ambiente virtual (opcional, mas recomendado) para isolar as dependências do projeto.
   
    1 - Navegue até a raiz do projeto
    ```bash
    cd <raiz_projeto>
    ```
    2 - Execute
    ```python
    python -m venv <nome_desejado_normalmente_.venv>
    ```

5. Instale as dependências do projeto executando o seguinte comando no terminal:
   ```
   pip install -r requirements.txt
   ```

6. Execute o comando para iniciar o servidor local:
   ```
   uvicorn main:app --reload
   ```

7. O servidor local será executado e estará disponível em http://localhost:8000. Você pode acessar a API e testar os endpoints usando um cliente HTTP, como o Postman ou o cURL.

# Realizando o deploy em ambiente produtivo

Para realizar o deploy em ambiente produtivo, eu usaria o Heroku pela facilidade de deploy considerando um ambiente simples.

1. Crie uma conta no Heroku em https://www.heroku.com/ caso ainda não tenha uma.

2. Instale a CLI do Heroku seguindo as instruções da documentação oficial em https://devcenter.heroku.com/articles/heroku-cli.

3. Faça login na sua conta do Heroku através da CLI executando o seguinte comando no terminal:
   ```
   heroku login
   ```

4. Navegue até o diretório raiz do projeto.

5. Crie um novo aplicativo Heroku executando o seguinte comando:
   ```
   heroku create <nome-do-aplicativo>
   ```

6. Crie um arquivo `Procfile` (sem extensão) no diretório raiz do projeto com o seguinte conteúdo:
   ```
   web: uvicorn main:app --host=0.0.0.0 --port=$PORT
   ```

7. Inicialize um repositório Git executando o comando:
   ```
   git init
   ```

8. Adicione os arquivos ao repositório Git executando o comando:
   ```
   git add .
   ```

9. Faça o commit dos arquivos executando o comando:
   ```
   git commit -m "Initial commit"
   ```

10. Faça o push para o repositório remoto do Heroku executando o comando:
    ```
    git push heroku master
    ```

11. Aguarde o processo de deploy ser concluído. O Heroku irá automaticamente detectar o tipo de aplicação Python e configurar o ambiente.

12. Após o deploy ser concluído, você receberá a URL da sua aplicação no Heroku. Você pode acessar a API através dessa URL para testar os endpoints.

Essas são apenas instruções básicas para realizar o deploy em ambiente produtivo usando o Heroku. Dependendo das particularidades do projeto e do ambiente produtivo, podem ser necessárias configurações adicionais, como variáveis de ambiente, bancos de dados, etc. 

---

Resposta 6
Falta o atributo `‘WALLET_X_TOKEN_MAX_AGE'` em `'core.settings'`

Com base no registro fornecido, parece que ocorreu um erro na tarefa `renew_wallet_x_access_tokens` no arquivo `wallet_oauth.py`. A mensagem de erro informa que o módulo `'core.settings'` não possui um atributo chamado `'WALLET_X_TOKEN_MAX_AGE'`. Esse atributo é usado para calcular o tempo de expiração dos tokens de acesso relacionados à Wallet X.

Para resolver esse problema, é preciso garantir que o módulo `'core.settings'` inclua o atributo `'WALLET_X_TOKEN_MAX_AGE'`. Verificaria o arquivo `core.settings` e eventualmente `.env` e me certificaria que ele inclua a configuração necessária.

Além disso, parece que há um erro de digitação no carimbo de data/hora na última linha do registro: `[2020-07-66 20:34:49,801: INFO/ForkPoolWorker-2]`. O dia deveria ser `'06'` em vez de `'66'`.

---

Resposta 7

1. Importações desnecessárias: As importações `timezone`, `timedelta` e `traceback` não são utilizadas no código e podem ser removidas.

2. O bloco `try-except` que envolve `scheduler.start()` não é necessário, já que apenas a instrução `pass` é executada. É possível remover esse bloco.

3. Ao configurar o `RotatingFileHandler`, você definiu `maxBytes=10000`. Esse valor corresponde a 10 KB, o que é muito pequeno para um arquivo de log. Considere aumentar esse valor para um tamanho mais adequado.

4. A váriavel `task1_instance` não é executada

---
Resposta 8 

   Ainda não aprofundei os estudos em padrões de projeto, mas considerando meus conhecimentos até agora eu iria de padrão Factory porque encapsula a criação de objetos em uma classe separada, permitindo que as subclasses decidam qual objeto concreto criar. Você pode usar esse padrão para criar instâncias dos serviços de terceiros de forma transparente, com base em algum critério (por exemplo, fornecedor específico). Isso ajuda a ocultar a complexidade da criação dos objetos de serviços e fornece uma interface uniforme.
