import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
    
def Form_PesquisaEscola():  

    ut.Divisor('Pesquisar Alunos', 'search', 'rgb(20,80,90)', 'key_Alunos01')

    with st.form(key = 'form_Alunos_pesquisar', clear_on_submit = False):
        row_0_col0, row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([1.5, 3, 3, 3, 2])   
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5= st.columns([3, 3, 2, 3, 3]) 
        
        df_filtrado_qtd = listar_alunos(None, None, None, 'Todas', 0) 
        p_max_value = len(df_filtrado_qtd)
        
         # Linha 00
        with row_0_col0:
            Matricula = st.number_input("Matricula", min_value= 0, max_value=p_max_value)
            
        with row_0_col1:
            Nome = st.text_input('Nome Aluno', key='key_Nome')
                
        with row_0_col2:
            Classe = st.selectbox('Classe', classe_p, index=0, placeholder='Seleciona a classe...')
        
        with row_0_col3:
            Materia = st.selectbox('Matéria', materias_p, index=0, placeholder='Seleciona uma Matéria...')
        
        with row_0_col4:
            Desempenho = st.number_input("Desempenho", min_value= 0, max_value=100)

        with row_1_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_1_col2:   
            st.write('')
       
        # Linha 02
        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
           st.write('')   
            
        with row_2_col3: 
            form_submit_button_peqsuisar = st.form_submit_button('Pesquisar')
            
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('') 
            
        if form_submit_button_peqsuisar:
        
            # Chama a função listar_Alunos com os filtros selecionados
            df_filtrado = listar_alunos(Matricula, Nome, Classe, Materia, Desempenho)
            # Mostra as Alunos filtradas em um DataFrame do Pandas
            if not df_filtrado.empty:
                # Obter o DataFrame estilizado
                styled_df = style_df(df_filtrado)
                # Exibir o DataFrame estilizado como HTML
                st.write(styled_df.to_html(), unsafe_allow_html=True)
            else:
                st.write("Não há Alunos correspondentes aos filtros selecionados.")        
         
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_Alunos02')