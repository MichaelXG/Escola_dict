# import streamlit as st
# from Controllers.PadraoController import *
# import Utils as ut

# def Form_ListarAlunos(pMatricula, pNome, pClasse, pMateria, pDesempenho):  
    
#     ut.Divisor('Listar Alunos', 'clipboard2-data', 'rgb(20,80,90)', 'ListarAlunos01')

#     with st.container(border=True):
#         # Chama a função listar_Alunoss com os filtros selecionados
#         df_filtrado = listar_alunos(pNome)

#         # Mostra as Alunoss filtradas em um DataFrame do Pandas
#         if not df_filtrado.empty:
#             st.dataframe(df_filtrado, hide_index=True)
#         else:
#             st.write("Não há Alunos correspondentes aos filtros selecionados.")
           
#     ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'ListarAlunos02')