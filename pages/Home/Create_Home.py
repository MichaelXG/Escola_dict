import streamlit as st
import Utils as ut

def Create_Home():  
    with st.container(): 
        ut.Divisor('Escola', 'mortarboard-fill','rgb(20,80,90)', 'Home01')
        st.write('\n \n')
        col1, col2, col3 = st.columns([3, 2, 3])
        col1_d, col2_d = st.columns([8, 0.01])

        with col1:
            st.write('')

        with col2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7IXmgTxQAaJ1q3vrff6Hzq1wC7_ScfywO0w&usqp=CAU', width=300, use_column_width='auto') 
        
        with col3:
            st.write('')
        
        with col1_d:
            st.write("""
                [PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. \n
                O programa deve permitir adicionar, remover, atualizar e listar os alunos.

                Para isso, você deve implementar um módulo que contém as seguintes funções: \n

                1 . AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos. \n

                2 . RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos. \n

                3. AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário. \n

                4. VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um. \n
            """)
        with col2_d:
            st.write('')
        
        st.write('\n \n')
        ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'Home02')
