import sqlite3
from models.produto import Produto

class ProdutoDAO:
    def __init__(self, db_name='clientes.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL
                )
            ''')

    def salvar(self, produto: Produto):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO produto (nome, preco) VALUES (?, ?)',
                (produto.nome, produto.preco)
            )
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, preco FROM produto')
            rows = cursor.fetchall()
            return [Produto(nome, preco) for nome, preco in rows]
