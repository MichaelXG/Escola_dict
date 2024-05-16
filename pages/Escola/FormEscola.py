import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
    
def Form_Escola():  
    if "widget" not in st.session_state:
        st.session_state.widget = ""

    if 'Matricula' not in st.session_state:
        st.session_state.Matricula = 0
        
    if 'Nome' not in st.session_state:
        st.session_state.Nome = ''
        
    if 'Idade' not in st.session_state:
        st.session_state.Idade = None
    
    if 'Classe' not in st.session_state:    
        st.session_state.Classe
    
    ut.Divisor('Adicionar Aluno', 'person-fill', 'rgb(20,80,90)', 'key_Aluno1')

    with st.form(key = 'form_Aluno', clear_on_submit = True):
        row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([1.5, 6, 1.5, 2.5]) 
        row_1_col1, row_1_col2, row_1_col3= st.columns([4, 2, 3])
        row_2_col1, row_2_col2 = st.columns([10, 0.01]) 
        row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5= st.columns([2, 2, 1, 2, 2]) 
        
        # Linha 00
        with row_0_col1:
            st.session_state.Matricula = st.number_input("Matrícula", step= 1, min_value= 0, max_value=999) 
            if not st.session_state.Matricula:
                st.error('O campo "Matrícula" é Obrigatorio.')     
        with row_0_col2:
            st.session_state.Nome = st.text_input('Nome Aluno', key='key_Nome', placeholder='Informe o nome completo do aluno')
            if not st.session_state.Nome:
                st.error('O campo "Nome Aluno" é Obrigatorio.')
        
        with row_0_col3:   
            st.session_state.Idade = st.number_input("Idade", step= 1, min_value= 0, max_value=100) 
            if not st.session_state.Idade:
                st.error('O campo "Idade" é Obrigatorio.')
        
        with row_0_col4:   
            st.session_state.Classe =  st.selectbox('Classe', classe, index=None, placeholder='Selecione a classe...')
            if not st.session_state.Classe:
                st.error('O campo "Classe" é Obrigatorio.')     
       
        Notas = {}
        
        with row_1_col3:
            st.write('')   
             
        # Linha 02        
        with row_2_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_2_col2:   
            st.write('')
            
        # Linha 04 
        with row_4_col1:   
            st.write('')
        
        with row_4_col2:
           st.write('')   
            
        with row_4_col3: 
            form_submit_button_Aluno = st.form_submit_button('Salvar')
            
        with row_4_col4: 
            st.write('') 
        
        with row_4_col5: 
            st.write('') 
            
        if form_submit_button_Aluno:
            if st.session_state.Matricula and st.session_state.Nome and st.session_state.Idade and  st.session_state.Classe:
                adicionar_aluno(st.session_state.Matricula, st.session_state.Nome, st.session_state.Idade, st.session_state.Classe, Notas)           
            else:
                ut.Alerta('','Parametros para incluir um novo Aluno incompleto')   
    
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_Aluno2')