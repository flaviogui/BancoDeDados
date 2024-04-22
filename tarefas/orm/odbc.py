import psycopg2

# função que faz a conexão ao banco 
def conectar_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="AtividadeBD",
            user="postgres",
            password="1151",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

# função para inserir uma atividade em um projeto
def inserir_atividade(projeto_codigo, descricao, data_inicio, data_fim):
    try:
        conn = conectar_banco()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)",
                           (descricao, projeto_codigo, data_inicio, data_fim))
            conn.commit()
            print("Atividade inserida com sucesso!")
            cursor.close()
            conn.close()
    except Exception as e:
        print("Erro ao inserir a atividade:", e)

# função para atualizar o líder de um projeto
def atualizar_lider_projeto(projeto_codigo, novo_lider):
    try:
        conn = conectar_banco()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE projeto SET responsavel = %s WHERE codigo = %s", (novo_lider, projeto_codigo))
            conn.commit()
            print("Líder do projeto atualizado com sucesso!")
            cursor.close()
            conn.close()
    except Exception as e:
        print("Erro ao atualizar o líder do projeto:", e)

# função para listar todos os projetos e suas atividades
def listar_projetos_e_atividades():
    try:
        conn = conectar_banco()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT p.nome as projeto, a.descricao as atividade FROM projeto p LEFT JOIN atividade a ON p.codigo = a.projeto")
            rows = cursor.fetchall()
            for row in rows:
                print("Projeto:", row[0], "- Atividade:", row[1])
            cursor.close()
            conn.close()
    except Exception as e:
        print("Erro ao listar os projetos e suas atividades:", e)

# Exemplos de uso das funções
inserir_atividade(4, "Atividade Greve", "2024-04-22", "2024-04-30")
atualizar_lider_projeto(1, 3)
listar_projetos_e_atividades()
