import sqlite3


conn = sqlite3.connect("meubanco.db")

def criar_tabela(conexao):
    try:
        c = conexao.cursor()
        c.execute('''CREATE TABLE tarefas(
                id INTEGER PRIMARY KEY,
                descricao TEXT,
                concluida BOOLEAN
                )''')
        conexao.commit()
        conexao.close()
    except sqlite3.OperationalError:
        print("ATENÇÃO: a tabela já existe")

criar_tabela(conn)

def inserir_tarefa(conexao, descricao, concluida):
    try:
        c = conexao.cursor()
        c.execute('''INSERT INTO tarefas
                (descricao, concluida) VALUES (?, ?)''',
                (descricao,concluida))
        conexao.commit()
        conexao.close()
    except sqlite3.ProgrammingError:
        print("ATENÇÃO: Não foi possível inserir a tarefa")

inserir_tarefa(conn, "Estudar SQLite", False)

def consultar_tarefas(conexao):
    c = conexao.cursor()
    c.execute('''SELECT * FROM tarefas''')
    for linha in c.fetchall():
        print(linha)
    conexao.commit()
    conexao.close()

consultar_tarefas(conn)

def concluir_tarefa(conexao, id):
    c = conexao.cursor()
    c.execute('''UPDATE tarefas
              SET concluida = 1
              WHERE id = ?''',
              (id,))
    conexao.commit()
    conexao.close()
concluir_tarefa(conn, 1)

def remover_tarefa(conexao, id):
    c = conexao.cursor()
    c.execute('''DELETE FROM tarefas
              WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()

remover_tarefa(conn,3)