import sqlite3
from fastapi import FastAPI
import random
import string
import sqlite3
from pydantic import BaseModel

app = FastAPI()

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# Rota para obter o papel de um usuário pelo "role_id"
@app.get('/users/{user_id}/role')
async def get_user_role(user_id: int):
    cursor.execute(
        'SELECT r.description FROM roles r JOIN users u ON u.role_id = r.id WHERE u.id = ?',
        (user_id,),
    )
    role_description = cursor.fetchone()
    if role_description:
        return {'role_description': role_description[0]}
    else:
        return None


# Fechar a conexão com o banco de dados
@app.on_event('shutdown')
def close_connection():
    cursor.close()
    conn.close()


# Conexão com o banco de dados SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Definir modelo de dados para criar usuário
class UserCreate(BaseModel):
    name: str
    email: str
    role_id: int
    password: str = None


# Rota para criar um usuário
@app.post('/users')
async def create_user(user: UserCreate):
    # Gerar senha aleatória se não for fornecida
    if not user.password:
        user.password = generate_random_password()

    # Salvar usuário no banco de dados
    user_id = generate_user_id()
    cursor.execute(
        'INSERT INTO users (name, email, password, role_id) VALUES (?, ?, ?, ?)',
        (user.name, user.email, user.password, user.role_id),
    )
    conn.commit()

    return {'user_id': user_id}


# Função para gerar senha aleatória
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Função para gerar ID de usuário único
def generate_user_id():
    cursor.execute('SELECT MAX(id) FROM users')
    result = cursor.fetchone()
    if result and result[0]:
        return result[0] + 1
    else:
        return 1


# Fechar a conexão com o banco de dados
@app.on_event('shutdown')
def close_connection():
    cursor.close()
    conn.close()


# Executar a API
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
