import streamlit as st

import page.insert as insert
import page.select as select

#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox_cadastro = st.sidebar.selectbox('Cadastrar', ['Funcionario', 'Paciente'])
selectbox_login = st.sidebar.selectbox('Usuario', ['Login'])
selectbox_pesquisar = st.sidebar.selectbox('Pesquisar', ['Usuario'])

if selectbox_cadastro == 'Funcionario':
    insert.inserir_usuario_funcionario()
if selectbox_cadastro == 'Paciente':
    insert.inserir_usuario_paciente()

'''if selectbox_login == 'Login':
    insert.inserir_funcionario()

if selectbox_pesquisar == 'Usuario':
    select.procurar_usuario()'''