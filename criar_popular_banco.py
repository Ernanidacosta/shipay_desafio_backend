import sqlite3
import random
import string

def create_and_populate_database():
    # Criar conexão com o banco de dados SQLite
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Criar tabelas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS claims (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            role_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_claims (
            user_id INTEGER NOT NULL,
            claim_id INTEGER NOT NULL,
            UNIQUE(user_id, claim_id)
        )
    """)

    # Popular tabelas com dados de exemplo
    roles = [
        (1, "Admin"),
        (2, "User"),
        (3, "Guest")
    ]
    cursor.executemany("INSERT INTO roles (id, description) VALUES (?, ?)", roles)

    claims = [
        (1, "Read"),
        (2, "Write"),
        (3, "Delete")
    ]
    cursor.executemany("INSERT INTO claims (id, description) VALUES (?, ?)", claims)

    users = [
        (1, "John Doe", "john@example.com", "password123", 1, "2023-05-26", None),
        (2, "Jane Smith", "jane@example.com", "abc123", 2, "2023-05-26", None)
    ]
    cursor.executemany("INSERT INTO users (id, name, email, password, role_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)", users)

    user_claims = [
        (1, 1),
        (1, 2),
        (2, 1)
    ]
    cursor.executemany("INSERT INTO user_claims (user_id, claim_id) VALUES (?, ?)", user_claims)

    # Commit das alterações e fechar conexão
    conn.commit()
    conn.close()

# Chamar a função para criar e popular o banco de dados
create_and_populate_database()
