import streamlit as st
from Controllers.PadraoController import *
from datetime import datetime
import streamlit_antd_components as sac
import Utils as ut

def Form_Lancar_Notas():  
    
    ut.Divisor('Lançar Notas dos Alunos', 'graph-up-arrow', 'rgb(20,80,90)', 'LancarNotas01')
    
    with st.container(border=True):
        row_0_col1, row_0_col2, row_0_col3 = st.columns([3, 3, 2]) 
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5= st.columns([3, 3, 2, 3, 3])
        
        df_filtrado_qtd = listar_alunos(None, None, None, 'Todas', 0) 
        
        nomes_alunos = [f"{aluno['Matrícula']} - {aluno['Nome']}" for aluno in registros_alunos.values()]

        with row_0_col1:
            st.session_state.Matricula_Aluno =  st.selectbox('Matrícula / Aluno', nomes_alunos, index=None, placeholder='Selecione um Aluno ...')
            if not st.session_state.Matricula_Aluno:
                st.error('O campo "Matrícula / Aluno" é Obrigatorio.')
                
        # Linha 01        
        with row_0_col2:
            st.session_state.Materia =  st.selectbox('Matéria', materias, index=None, placeholder='Selecione uma matéria ...')
            if not st.session_state.Materia:
                st.error('O campo "Matéria" é Obrigatorio.')        
        
        with row_0_col3:   
            st.session_state.Nota = st.number_input("Nota", step= 1, min_value= 0, max_value=100) 
            if not st.session_state.Nota:
                st.error('O campo "Nota" é Obrigatorio.')
            
         # Linha 02
        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
           st.write('')   
            
        with row_2_col3: 
            selected_lancar_nota = sac.buttons([
                 sac.ButtonsItem(label='Salvar Nota', icon='clipboard-check', color='#25C3B0'),
                 ], label=' . ', align='center', radius='lg', color='rgb(20,80,90)', index=None)
            
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('') 
                    
        ut.Divisor('Listar as Notas Lançadas', 'clipboard2-data', 'rgb(20,80,90)', 'LancarNotas02')
        
        with st.container(border=True):
            # Chama a função listar_tarefas com os filtros selecionados
            df_filtrado = listar_alunos(None, None, None, 'Todas', 0)

            # Mostra as tarefas filtradas em um DataFrame do Pandas
            if not df_filtrado.empty:
                # st.dataframe(df_filtrado, use_container_width=True)
                # Exibir o DataFrame estilizado como HTML
                st.write(df_filtrado.to_html(), unsafe_allow_html=True)
            else:
                st.write("Não há Notas laçadas.")   
       
    if selected_lancar_nota == 'Salvar Nota':
        # Após selecionar o aluno, separar a matrícula do nome
        Matricula, Nome = st.session_state.Matricula_Aluno.split(" - ", 1)
        
        st.write('Matricula', Matricula)
        
        if adicionar_notas(Matricula, st.session_state.Materia, st.session_state.Nota):
            ut.Sucesso("", f"Nota de {st.session_state.Materia} atualizada para {st.session_state.Nome} com sucesso!")
        else:
            ut.Informacao("", "Aluno inválido.")
        
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'LancarNotas03')