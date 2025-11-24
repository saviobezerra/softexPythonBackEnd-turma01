import sqlite3
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self, db_name='clientes.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
            ''')

    def salvar(self, cliente: Cliente):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)',
                           (cliente.nome, cliente.email, cliente.telefone))
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, email, telefone FROM cliente')
            rows = cursor.fetchall()
            return [Cliente(nome, email, telefone) for nome, email, telefone in rows]