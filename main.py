from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:@localhost/gibis"
engine = create_engine(DATABASE_URL) 
Base = declarative_base()

class Gibi(Base):
    __tablename__ = 'gibis'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano = Column(Integer)
    editora_id = Column(Integer, ForeignKey('editoras.id'))
    autor_id = Column(Integer, ForeignKey('autores.id'))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

    editora = relationship("Editora", back_populates="gibis")
    autor = relationship("Autor", back_populates="gibis")
    categoria = relationship("Categoria", back_populates="gibis")


class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pais_origem = Column(String)

    gibis = relationship("Gibi", back_populates="autor")


class Editora(Base):
    __tablename__ = 'editoras'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cidade = Column(String)

    gibis = relationship("Gibi", back_populates="editora")


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

    gibis = relationship("Gibi", back_populates="categoria")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_editora():
    nome = input("Digite o nome da Editora: ")
    cidade = input("Digite a cidade da Editora: ")
    editora = Editora(nome=nome, cidade=cidade)
    session.add(editora)
    session.commit()
    print("Editora adicionada com sucesso!\n")

def add_autor():
    nome = input("Digite o nome do Autor: ")
    pais_origem = input("Digite o país de origem do Autor: ")
    autor = Autor(nome=nome, pais_origem=pais_origem)
    session.add(autor)
    session.commit()
    print("Autor adicionado com sucesso!\n")

def add_categoria():
    nome = input("Digite o nome da Categoria: ")
    categoria = Categoria(nome=nome)
    session.add(categoria)
    session.commit()
    print("Categoria adicionada com sucesso!\n")

def add_gibi():
    titulo = input("Digite o título do Gibi: ")
    ano = int(input("Digite o ano do Gibi: "))
    editora_id = int(input("Digite o ID da Editora: "))
    autor_id = int(input("Digite o ID do Autor: "))
    categoria_id = int(input("Digite o ID da Categoria: "))
    gibi = Gibi(titulo=titulo, ano=ano, editora_id=editora_id, autor_id=autor_id, categoria_id=categoria_id)
    session.add(gibi)
    session.commit()
    print("Gibi adicionado com sucesso!\n")

def get_gibi():
    titulo = input("Digite o título do Gibi: ")
    gibi = session.query(Gibi).filter_by(titulo=titulo).first()
    if gibi:
        print(f"Gibi encontrado: {gibi.titulo}, Ano: {gibi.ano}, Categoria: {gibi.categoria.nome}\n")
    else:
        print("Gibi não encontrado.\n")

def update_gibi():
    gibi_id = int(input("Digite o ID do Gibi a ser atualizado: "))
    novo_titulo = input("Digite o novo título do Gibi: ")
    gibi = session.query(Gibi).filter_by(id=gibi_id).first()
    if gibi:
        gibi.titulo = novo_titulo
        session.commit()
        print("Título do Gibi atualizado com sucesso!\n")
    else:
        print("Gibi não encontrado.\n")

def delete_gibi():
    gibi_id = int(input("Digite o ID do Gibi a ser deletado: "))
    gibi = session.query(Gibi).filter_by(id=gibi_id).first()
    if gibi:
        session.delete(gibi)
        session.commit()
        print("Gibi deletado com sucesso!\n")
    else:
        print("Gibi não encontrado.\n")


def menu():
    while True:
        print("Menu de Opções:")
        print("1. Adicionar Editora")
        print("2. Adicionar Autor")
        print("3. Adicionar Categoria")
        print("4. Adicionar Gibi")
        print("5. Buscar Gibi por Título")
        print("6. Atualizar Gibi")
        print("7. Deletar Gibi")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            add_editora()
        elif opcao == '2':
            add_autor()
        elif opcao == '3':
            add_categoria()
        elif opcao == '4':
            add_gibi()
        elif opcao == '5':
            get_gibi()
        elif opcao == '6':
            update_gibi()
        elif opcao == '7':
            delete_gibi()
        elif opcao == '8':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

menu()
