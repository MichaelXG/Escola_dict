import Utils as ut
import pandas as pd 
import streamlit as st

# criar lista de Login
login = []

login = [{"Apelido":'Suporte',"Password": '123'},
         {"Apelido":'Visitante',"Password": 'visitante123'},
         {"Apelido":'Maria',"Password": 'Maria@123'}
        ]
apelidos = ['Suporte', 'Visitante', 'Maria']

# Lista para armazenar Nomes
registros_alunos = {
    1: {
        "Matrícula": 1,
        "Nome": "João Silva",
        "Idade": 15,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 85, "Língua Portuguesa": 78, "Ciências": 92, "História": 93}
    },
    2: {
        "Matrícula": 2,
        "Nome": "Maria Oliveira",
        "Idade": 14,
        "Classe": "8º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 90, "Língua Portuguesa": 82, "Ciências": 88, "História": 84}
    },
    3: {
        "Matrícula": 3,
        "Nome": "Carlos Santos",
        "Idade": 16,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 59, "Língua Portuguesa": 80, "Ciências": 75, "História": 78}
    },
    4: {
        "Matrícula": 4,
        "Nome": "Ana Pereira",
        "Idade": 15,
        "Classe": "9º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 92, "Língua Portuguesa": 85, "Ciências": 90, "História": 88}
    },
    5: {
        "Matrícula": 5,
        "Nome": "Pedro Costa",
        "Idade": 14,
        "Classe": "8º Ano - Ensino Fundamental",
        "Notas": {"Matemática": 88, "Língua Portuguesa": 79, "Ciências": 84, "História": 80}
    }
}

classe = ['1º Ano - Ensino Fundamental', '2º Ano - Ensino Fundamental','3º Ano - Ensino Fundamental','4º Ano - Ensino Fundamental',
          '5º Ano - Ensino Fundamental', '6º Ano - Ensino Fundamental','7º Ano - Ensino Fundamental','8º Ano - Ensino Fundamental',
          '9º Ano - Ensino Fundamental', '1º Ano - Ensino Médio','2º Ano - Ensino Médio','3º Ano - Ensino Médio']

classe_p = ['Todas'] + classe

materias = ['Língua Portuguesa', 'Matemática','Ciências','História','Geografia','Língua Estrangeira','Educação Física','Artes','Educação Ambiental','Filosofia','Sociologia','Ensino Religioso']

materias_p = ['Todas'] + materias

# Função para gerar nova matrícula
def gerar_nova_matricula():
    if registros_alunos:
        nova_matricula = max(registros_alunos.keys()) + 1
    else:
        nova_matricula = 1
    return nova_matricula

def style_df_notas(val):
    try:
        val = float(val)
        if val < 60:
            color = 'red'
        else:
            color = 'green'
        return f'color: {color}'
    except ValueError:
        return ''  # Se não puder converter para float, não aplica estiloo

# Função para estilizar linhas alternadas
def zebra_style(row):
    return ['background-color: #f2f2f2' if row.name % 2 == 0 else '' for _ in row]

# Função para estilizar o DataFrame
def style_df(df):
    # Aplicar estilo apenas nas colunas de notas
    notas_cols = [col for col in df.columns if col not in ['Matrícula', 'Nome', 'Idade', 'Classe']]
    styled_df = df.style.applymap(style_df_notas, subset=pd.IndexSlice[:, notas_cols])
    styled_df = styled_df.apply(zebra_style, axis=1)
    return styled_df

#  Função para adicionar uma novo Aluno
def adicionar_aluno(Nome, Idade, Classe, Notas):
    Matricula = gerar_nova_matricula()
    novo_aluno = {
        "Matrícula": Matricula,
        "Nome": Nome,
        "Idade": Idade,
        "Classe": Classe,
        "Notas": Notas
    }
    if Matricula in registros_alunos:
        ut.Erro("", "Já existe um aluno com esta matrícula.")
    else:
        registros_alunos[Matricula] = novo_aluno
        ut.Sucesso("", "Aluno adicionado com sucesso!")
        
# Função para listar todos os alunos ou usando um filtro
def listar_alunos(pMatricula=None, pNome=None, pClasse='Todas', pMateria='Todas', pDesempenho=None):
    if not registros_alunos:
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver alunos
    
    # Criar um DataFrame
    df = pd.DataFrame.from_dict(registros_alunos, orient='index')

    # Expandir a coluna 'Notas'
    Notas_df = df['Notas'].apply(pd.Series)

    # Concatenar o DataFrame original com o DataFrame de Notas
    df = pd.concat([df.drop(columns=['Notas']), Notas_df], axis=1)
    
    # Convertendo as notas para float antes da formatação
    for col in Notas_df.columns:
        df[col] = df[col].astype(float)
    
    # Aplicar os filtros
    df_filtrado = df.copy()
    
    if pMatricula is not None and pMatricula != 0:
        df_filtrado = df_filtrado[df_filtrado['Matrícula'] == pMatricula]
    
    if pNome:
        # Alunos que começam com a string de busca
        inicio = df_filtrado[df_filtrado['Nome'].str.lower().str.startswith(pNome.lower())]
        # Alunos que contêm a string de busca
        contem = df_filtrado[df_filtrado['Nome'].str.lower().str.contains(pNome.lower())]
        # Remover duplicatas mantendo a ordem
        df_filtrado = pd.concat([inicio, contem]).drop_duplicates().reset_index(drop=True)

    # Filtrar por classe
    if pClasse and pClasse != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Classe'].str.lower().str.startswith(pClasse.lower())]

    # Filtrar por matéria e desempenho
    if pMateria and pMateria != 'Todas' and pDesempenho is not None:
        if pMateria not in df_filtrado.columns:
            ut.Informacao("", f"Matéria '{pMateria}' não encontrada.")
            return pd.DataFrame()
        df_filtrado = df_filtrado[df_filtrado[pMateria] >= float(pDesempenho)]

    # Formatar as colunas de notas com 2 casas decimais
    notas_cols = Notas_df.columns
    for col in notas_cols:
        if col in df_filtrado.columns:
            df_filtrado.fillna(0, inplace=True)  # Preencher NaN com zero
            df_filtrado[col] = df_filtrado[col].apply(lambda x: f'{x:.2f}')
    
    return df_filtrado

# Adicionar Notas pelo Nome do aluno e a Matéria
def adicionar_notas(Matricula, Materia, Nota):
    if Nota < 0 or Nota > 100:
        ut.Erro("", "Nota deve estar entre 0 e 100.")
        return False
    
    try:
        matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
    except ValueError:
        ut.Erro("", "A matrícula deve ser um número inteiro.")
        return False
    
    if matricula_int not in registros_alunos:
        ut.Erro("", "Matrícula não encontrada.")
        return False
    
    aluno = registros_alunos[matricula_int]
    aluno["Notas"][Materia] = Nota  # Adiciona ou atualiza a nota
    # ut.Sucesso("", "Nota adicionada com sucesso!")
    return True

# Função para alterar dados de um aluno 
def alterar_aluno(Matricula, Nome=None, Idade=None, Classe=None, Notas=None):
    if Matricula not in registros_alunos:
        ut.Erro("", "Matrícula não encontrada.")
        return False
    
    aluno = registros_alunos[Matricula]
    
    if Nome:
        aluno["Nome"] = Nome
    if Idade:
        aluno["Idade"] = Idade
    if Classe:
        aluno["Classe"] = Classe
    if Notas:
        aluno["Notas"].update(Notas)  # Atualiza as notas existentes ou adiciona novas
    
    ut.Sucesso("", "Dados do aluno atualizados com sucesso!")
    return True

def deletar_registro(Matricula: int) -> bool:
    try:
        st.write(Matricula)
        matricula_int = int(Matricula)  # Convertendo a matrícula para inteiro
    except ValueError:
        ut.Erro("", "A matrícula deve ser um número inteiro.")
        return False
    
    if matricula_int in registros_alunos:
        del registros_alunos[matricula_int]
        return True
    
    if matricula_int not in registros_alunos:
        # ut.Sucesso('', f'Matrícula "{Matricula}" deletada com sucesso') 
        return True