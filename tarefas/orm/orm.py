from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

# engine de conexão
engine = create_engine('postgresql://postgres:1151@localhost/AtividadeBD')

# criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

# estrutura da tabela projeto
metadata = MetaData()
projeto = Table(
    'projeto', metadata,
    Column('codigo', Integer, primary_key=True),
    Column('nome', String(50)),
    Column('responsavel', Integer),
)

# estrutura da tabela atividade
atividade = Table(
    'atividade', metadata,
    Column('codigo', Integer, primary_key=True),
    Column('descricao', String(250)),
    Column('projeto', Integer),
    Column('data_inicio', Date),
    Column('data_fim', Date),
)

metadata.create_all(engine)

# inserindo uma atividade em um projeto
nova_atividade = atividade.insert().values(
    descricao='Nova Atividade',
    projeto=1,
    data_inicio='2024-04-23',
    data_fim='2024-04-24'
)
session.execute(nova_atividade)
session.commit()

# atualizando o líder de um projeto
atualizar_lider = projeto.update().where(projeto.c.codigo == 1).values(responsavel=2)
session.execute(atualizar_lider)
session.commit()

# listando todos os projetos e suas atividades
projetos = session.query(projeto).all()
for p in projetos:
    print(f"Projeto: {p.nome}, Responsável: {p.responsavel}")
    atividades = session.query(atividade).filter(atividade.c.projeto == p.codigo).all()
    for a in atividades:
        print(f"Atividade: {a.descricao}, Início: {a.data_inicio}, Fim: {a.data_fim}")


session.close()
