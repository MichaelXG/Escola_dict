import streamlit as st
from Controllers.PadraoController import *
from Controllers.NavegadorController import *
import streamlit_antd_components as sac
import Utils as ut

def Form_Escola():
    
    def disable_form(action:int):
        if action == 0:
            st.session_state.Novo = True
            st.session_state.form_Habilitado = False
        elif action == 1 or action == 3:
            st.session_state.Edit = True
            st.session_state.form_Habilitado = False
        
    def reset_session_state():
        # Definir st.session_state como um dicionário vazio
        st.session_state.contador = 0
        st.session_state.form_Habilitado = True
        st.session_state.Primeiro_acesso = True
        st.session_state.Edit = False
        st.session_state.Novo = False                     
        
    reset_session_state() 
    
    if "widget" not in st.session_state:
        st.session_state.widget = ""

    if 'index' not in st.session_state:
        st.session_state.index = 0

    if 'Matricula' not in st.session_state:
        st.session_state.Matricula = 0

    if 'Nome' not in st.session_state:
        st.session_state.Nome = ''

    if 'Idade' not in st.session_state:
        st.session_state.Idade = None

    if 'Classe' not in st.session_state:
        st.session_state.Classe = None

    ut.Divisor('Adicionar / Alterar Alunos', 'person-fill', 'rgb(20,80,90)', 'key_Aluno1')

    df_filtrado_qtd = listar_alunos(None, None, None, 'Todas', 0) 
    p_max_value = len(df_filtrado_qtd) -1
        
    def menu_itens():
        action = sac.buttons([
            # 0 - Novo
            sac.ButtonsItem(label='', icon='plus-circle', color='rgb(20,80,90)'), 
            # 1 - Editar
            sac.ButtonsItem(label='', icon='pen', color='yellow'),
            # 2 - Salvar
            sac.ButtonsItem(label='', icon='check2-circle', color='green', disabled= True),
            # 3 - Cancelar
            sac.ButtonsItem(label='', icon='x-circle', color='red'),
            # 4 - Atualizar
            sac.ButtonsItem(label='', icon='arrow-repeat', color='orange'),
            # 5 - First
            sac.ButtonsItem(label='', icon='chevron-double-left', color='rgb(20,80,90)'),
            # 6 - Prior
            sac.ButtonsItem(label='', icon='chevron-left', color='rgb(20,80,90)'),
            # 7 - Next
            sac.ButtonsItem(label='', icon='chevron-right', color='rgb(20,80,90)'),
            # 8 - Last
            sac.ButtonsItem(label='', icon='chevron-double-right', color='rgb(20,80,90)'),
            # 9 - Deletar
            sac.ButtonsItem(label='', icon='trash-fill', color='dark'),
            # 10 - Informação
            sac.ButtonsItem(icon='info-circle', color='blue')
         ], label='', key='menu-nav-escola', align='center', radius='lg', color='rgb(20,80,90)', return_index=True, index=8)
    
        return action

    # Cria o menu de navegação entre os itens
    action_escola= menu_itens()
    
    get_record_user_geral = registros_alunos
    get_record_user_atual = NavegadorRegistros(get_record_user_geral)
    get_record_user = {}
    
    # st.write('get_record_user ', get_record_user)
    if action_escola == 0:  # Novo
        disable_form(action_escola)
        get_record_user = None

    if action_escola == 1:  # Editar
        disable_form(action_escola)
        get_record_user = get_record_user_atual.editar(st.session_state.index)

    if action_escola == 2:  # Salvar
        pass  # Implemente a lógica para salvar as alterações no registro

    if action_escola == 4:  # Atualizar
        ut.fn_spinner_3('Aguarde, recarregando o registro...')
        get_record_user = get_record_user_atual.refresh(st.session_state.index)

    if action_escola == 3:  # Cancelar
        if not(st.session_state.form_Habilitado):
            reset_session_state()
        else:
            ut.Alerta('', f'O item não esta em edição.')
                    
        get_record_user_geral = {}
        get_record_user_atual = {}
        get_record_user = {}
        get_record_user_geral = registros_alunos
        get_record_user_atual = NavegadorRegistros(get_record_user_geral)
        get_record_user = get_record_user_atual.refresh(st.session_state.index)
    
    if action_escola == 4:  # Atualizar
        reset_session_state()
        ut.fn_spinner_3('Aguarde, recarregando o registro...')   
        get_record_user_geral = registros_alunos 
        get_record_user_atual = NavegadorRegistros(get_record_user_geral)
        get_record_user = {}
        get_record_user = get_record_user_atual.refresh(st.session_state.index)   
                                                          
    if action_escola == 5:  # First
        ut.fn_spinner_3('Carregando primeiro registro...')
        get_record_user = get_record_user_atual.first_registro()

    if action_escola == 6:  # Prior
        if st.session_state.index > 0:  # Verifica se não está no primeiro registro
            ut.fn_spinner_3('Carregando registro anterior...')
            get_record_user = get_record_user_atual.registro_prior(st.session_state.index)
        else:
            ut.Alerta('', 'Já está no primeiro registro.')
            get_record_user = get_record_user_atual.first_registro()  # Mantém o primeiro registro na tela


    if action_escola == 7:  # Next
        ut.fn_spinner_3('Carregando próximo registro...')
        if st.session_state.index < p_max_value:
            get_record_user = get_record_user_atual.next_registro(st.session_state.index)
        else:
            ut.Alerta('', 'Já está no último registro.')
            get_record_user = get_record_user_atual.last_registro() 
             
    if action_escola == 8:  # Último registro
        ut.fn_spinner_3('Carregando último registro...')
        get_record_user = get_record_user_atual.last_registro()
    
    if action_escola == 9:  # Deletar 
        if deletar_registro(st.session_state.Matricula): 
            ut.fn_spinner_3('Aguarde...')   
            ut.Sucesso('', f'Usuário "{st.session_state.Matricula} - {st.session_state.Nome}" deletado com sucesso')
            get_record_user_geral = registros_alunos 
            get_record_user_atual = NavegadorRegistros(get_record_user_geral)
            get_record_user = {}
            get_record_user = get_record_user_atual.last_registro()
            reset_session_state()
            
    if action_escola == 10:  # Informação
        get_record_user = get_record_user_atual.informacoes(st.session_state.index)
        ut.Alerta('', 'Não implementado...')
   
    if get_record_user:
        st.session_state.Matricula = get_record_user.get('Matrícula', 0)
        st.session_state.Nome = get_record_user.get('Nome', '')
        st.session_state.Idade = get_record_user.get('Idade', None)
        st.session_state.Classe = get_record_user.get('Classe', '')

    # Exibir o registro na tela
    if bool(get_record_user) and st.session_state.Novo == False:
        
        if bool(get_record_user):
            permissao_editar = False if not(st.session_state.form_Habilitado) else True
        else:
            permissao_editar = True
            ut.Alerta('', 'Edição permitida somente pelo Administrador.')
            
        with st.form(key='form_Aluno', clear_on_submit=True):
            row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([1.5, 6, 1.5, 2.5])
            row_1_col1, row_1_col2, row_1_col3 = st.columns([4, 2, 3])
            row_2_col1, row_2_col2 = st.columns([10, 0.01])
            row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5 = st.columns([2, 2, 1, 2, 2])

            with row_0_col1:
                st.session_state.Matricula = st.number_input("Matrícula", step=1, min_value=0, max_value=999, value=st.session_state.Matricula, disabled=True)
                if not st.session_state.Matricula:
                    st.error('O campo "Matrícula" é Obrigatorio.')
                    
            with row_0_col2:
                st.session_state.Nome = st.text_input('Nome Aluno', key='key_Nome', value=st.session_state.Nome, placeholder='Informe o nome completo do aluno', disabled=permissao_editar)
                if not st.session_state.Nome:
                    st.error('O campo "Nome Aluno" é Obrigatorio.')

            with row_0_col3:
                st.session_state.Idade = st.number_input("Idade", step=1, min_value=0, max_value=100, value=st.session_state.Idade, disabled=permissao_editar)
                if not st.session_state.Idade:
                    st.error('O campo "Idade" é Obrigatorio.')

            with row_0_col4:
                class_index = classe.index(st.session_state.Classe) if st.session_state.Classe in classe else 0
                
                st.session_state.Classe = st.selectbox('Classe', classe, index=class_index, placeholder='Selecione a classe...', disabled=permissao_editar)
                if not st.session_state.Classe:
                    st.error('O campo "Classe" é Obrigatorio.')

            Notas = {}

            with row_1_col3:
                st.write('')

            with row_2_col1:
                sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
            with row_2_col2:
                st.write('')

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
                if not(st.session_state.form_Habilitado) and st.session_state.Edit == True:
                    if st.session_state.Matricula and st.session_state.Nome and st.session_state.Idade and st.session_state.Classe:
                        alterar_aluno(st.session_state.Matricula, st.session_state.Nome, st.session_state.Idade, st.session_state.Classe, Notas)
                        ut.fn_spinner_3('Aguarde, alterado registro...')  
                        # get_record_user_geral = registros_alunos
                        get_record_user_atual = NavegadorRegistros(get_record_user_geral)
                        get_record_user = {}
                        get_record_user = get_record_user_atual.refresh(st.session_state.index)
                        
                        reset_session_state()
                        ut.Sucesso('', f'Matrícula "{get_record_user['Matrícula']} - {get_record_user['Nome']}",  alterado com sucesso')
                        st.rerun()
                    else:
                        ut.Alerta('', 'Parametros para Alterar um Aluno incompleto') 
                else:
                    ut.Alerta('', 'É preciso clicar no botão editar.')
    else:
        with st.form(key='form_Aluno_new', clear_on_submit=True):
            row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([1.5, 6, 1.5, 2.5])
            row_1_col1, row_1_col2, row_1_col3 = st.columns([4, 2, 3])
            row_2_col1, row_2_col2 = st.columns([10, 0.01])
            row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5 = st.columns([2, 2, 1, 2, 2])

            with row_0_col1:
                st.session_state.Matricula = st.number_input("Matrícula", step=1, min_value=0, max_value=999, disabled= True)

            with row_0_col2:
                st.session_state.Nome = st.text_input('Nome Aluno', key='key_Nome', placeholder='Informe o nome completo do aluno')
                if not st.session_state.Nome:
                    st.error('O campo "Nome Aluno" é Obrigatorio.')

            with row_0_col3:
                st.session_state.Idade = st.number_input("Idade", step=1, min_value=0, max_value=100)
                if not st.session_state.Idade:
                    st.error('O campo "Idade" é Obrigatorio.')

            with row_0_col4:
                st.session_state.Classe = st.selectbox('Classe', classe, index=None, placeholder='Selecione a classe...')
                if not st.session_state.Classe:
                    st.error('O campo "Classe" é Obrigatorio.')

            Notas = {}

            with row_1_col3:
                st.write('')

            with row_2_col1:
                sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
            with row_2_col2:
                st.write('')

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
                if st.session_state.Nome and st.session_state.Idade and st.session_state.Classe:
                    adicionar_aluno(st.session_state.Nome, st.session_state.Idade, st.session_state.Classe, Notas)
                else:
                    ut.Alerta('', 'Parametros para incluir um novo Aluno incompleto')
                    
    ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'key_Aluno2')
