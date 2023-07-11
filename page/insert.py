import streamlit as st

import controller.cliente as cliente
import random


def inserir_usuario_funcionario():
    st.title('Cadastrar Funcionario')
    cargos = ['Recepcionista', 'Dentista', 'Faxineira', 'Auxiliar de dentista']
    
    with st.form(key='insert_funcionario'):
        input_id = random.randrange(1, 100)
        input_email = st.text_input(label='Insira o email:')
        input_cpf = st.number_input(label='Insira o cpf:', format='%d', step=1)
        input_senha = st.text_input(label='Insira a senha:')
        
        input_nome = st.text_input(label='Insira o nome:')
        input_telefone = st.number_input(label='Insira o telefone:', format='%d', step=1)
        input_idade  = st.number_input(label='Insira a idade:', format='%d', step=1)
        input_cargo = st.selectbox(label='Cargo', options=cargos)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir_usuario_funcionario(input_id, input_email, input_cpf, input_senha, input_nome, input_telefone, input_idade, input_cargo)
            st.success('Funcionario incluido com sucesso') 

        
def inserir_usuario_paciente():
    st.title('Cadastrar Paciente')
    
    with st.form(key='insert_paciente'):
        input_id = random.randrange(1, 100)
        input_email = st.text_input(label='Insira o email:')
        input_cpf = st.number_input(label='Insira o cpf:', format='%d', step=1)
        input_senha = st.text_input(label='Insira a senha:')
        
        input_nome = st.text_input(label='Insira o nome:')
        input_telefone = st.number_input(label='Insira o telefone:', format='%d', step=1)
        input_idade  = st.number_input(label='Insira a idade:', format='%d', step=1)


        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir_usuario_paciente(input_id, input_email, input_cpf, input_senha, input_nome, input_telefone, input_idade)
            st.success('Paciente incluido com sucesso') 