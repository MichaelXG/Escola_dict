import streamlit as st
from Controllers.PadraoController import *

class NavegadorRegistros:
    def __init__(self, dados: dict):
        self.dados = dados
        self.chaves = list(dados.keys())
        self.indice_atual = 0 if self.chaves else None
    
    def editar(self, index_n: int):
        if self.dados:
            self.indice_atual = index_n
            st.session_state.index = self.indice_atual
            return self.dados[self.chaves[self.indice_atual]]  
    
    def refresh(self, index_n: int):
        if self.dados:
            self.indice_atual = index_n
            st.session_state.index = self.indice_atual
            return self.dados[self.chaves[self.indice_atual]]  
    
    def first_registro(self):
        if self.dados:
            self.indice_atual = 0
            st.session_state.index = self.indice_atual
            return self.dados[self.chaves[self.indice_atual]]

    def registro_prior(self, index_n):
        if self.dados and index_n > 0:
            self.indice_atual = index_n - 1
            st.session_state.index = self.indice_atual
            return self.dados[self.chaves[self.indice_atual]]

    def next_registro(self, index_n):
        if self.dados and index_n < len(self.chaves) - 1:
            self.indice_atual = index_n + 1
            st.session_state.index = self.indice_atual
            return self.dados[self.chaves[self.indice_atual]]

    def last_registro(self):
        if self.dados and self.chaves:
            self.indice_atual = len(self.chaves) - 1
            st.session_state.index = self.indice_atual
            return self.dados[self.chaves[self.indice_atual]]
