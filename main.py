import streamlit as st
from functions import ControleGeral
from database import DataBaseMysql
from repository import Repository

st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

db = DataBaseMysql()
repo = Repository(db)
controle = ControleGeral(repo)

paises, estados = controle.lista_locais()

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'id_cliente' not in st.session_state:
    st.session_state.id_cliente = ''

if 'id_termo_clientes' not in st.session_state:
    st.session_state.id_termo_clientes = ''

if 'dados_cliente' not in st.session_state:
    st.session_state.dados_cliente = []

if 'termo_medico' not in st.session_state:
    st.session_state.termo_medico = []

st.subheader('Termo de Responsabilidade')
escolha_idioma = 'Português'
escolha_idioma = st.selectbox(" Seleccionar Idioma / Select Language", ["Português", "English", "Español"], index=None)

if escolha_idioma is not None:
    if st.session_state.count == 0:
        st.session_state.count += 1


titulo, data_mergulho, check_in, nome, cpf, data_nascimento, email, telefone, formato_data, endereco, botao, texto, titulo2, nome_emergencia, telefone_emergencia, botao2, titulo3, subtitulo, gravida, cardiaca, pulmonar, enjoo, coluna, ouvido, remedio, asma, epilepsia, dd, diabetes, hemorragia, sinusite, cirurgia, opcoes, opcoes1, qual_cirurgia, tempo_cirurgia, viajar, ciente1, ciente2, texto_final, pais, estado, enviar, importante, enviado, taxa, localizacao = controle.definir_idioma(
    escolha_idioma)

# Exibindo os inputs do formulário

if st.session_state.count == 1:
    with st.form('Parte 1'):
        st.subheader(titulo)
        st.write(st.session_state.count)
        input_data_mergulho = st.date_input(data_mergulho, format=formato_data)
        btn_check_in = st.text_input('Horario', value=check_in, disabled=True)
        input_nome = st.text_input(nome)
        input_data_nascimento = st.date_input(data_nascimento, format=formato_data, value=None)
        input_cpf = st.text_input(cpf)
        input_telefone = st.text_input(telefone)
        input_email = st.text_input(email)
        col1, col2 = st.columns(2)

        with col2:
            if st.form_submit_button(botao2):
                if input_nome == '' or input_data_nascimento is None or input_cpf == '' or input_telefone == '' or input_email == '':
                    st.error('Preencha todos os Campos')
                st.session_state.dados_cliente.append(
                    (input_data_mergulho, input_nome, input_data_nascimento, input_cpf, input_telefone, input_email))
                st.session_state.count += 1
                st.rerun()
if st.session_state.count == 2:

    with st.form('Pagina2'):
        if escolha_idioma == 'Português':
            input_estado = st.selectbox(estado, estados, index=None)
            input_pais = st.selectbox(pais, paises, index=23)
        else:
            input_estado = st.text_input(estado)
            input_pais = st.selectbox(pais, paises, index=None)

        endereco = st.text_input(endereco)
        input_nome_emergencia = st.text_input(nome_emergencia)
        input_telefone_emergencia = st.text_input(telefone_emergencia)

        col1, col2 = st.columns(2)

        with col2:
            if st.form_submit_button(botao2):
                data_mergulho, nome_cliente, data_nascimento, cpf, telefone, email = st.session_state.dados_cliente

                st.session_state.id_clientes = controle.verifica_cadastro(nome_cliente, data_mergulho, telefone, cpf,
                                                                          email, data_nascimento, input_nome_emergencia,
                                                                          input_telefone_emergencia, input_estado,
                                                                          input_pais)

                st.session_state.count += 1
                st.rerun()

if st.session_state.count == 3:
    with st.form('Pagina2'):
        st.write(st.session_state.count)
        st.subheader(titulo2)
        st.write(texto)
        colun1, colun2 = st.columns(2)

        with colun2:
            if st.form_submit_button(botao2):
                st.session_state.count += 1
                st.rerun()
st.write('---')
if st.session_state.count == 4:
    st.write(st.session_state.count)
    with st.form('Pagina 3'):
        st.header(titulo3)
        st.write(subtitulo)

        radio_gravida = st.radio(label=gravida, options=opcoes, horizontal=True, index=None)
        radio_cardiaca = st.radio(label=cardiaca, options=opcoes, horizontal=True, index=None)
        radio_pulmonar = st.radio(label=pulmonar, options=opcoes, horizontal=True, index=None)
        radio_enjoo = st.radio(label=enjoo, options=opcoes, horizontal=True, index=None)
        radio_coluna = st.radio(label=coluna, options=opcoes, horizontal=True, index=None)
        radio_ouvido = st.radio(label=ouvido, options=opcoes, horizontal=True,
                                index=None)

        radio_remedio = st.radio(label=remedio, options=opcoes, horizontal=True, index=None)
        radio_asma = st.radio(label=asma, options=opcoes, horizontal=True,
                              index=None)
        radio_epilepsia = st.radio(label=epilepsia, options=opcoes, horizontal=True,
                                   index=None)
        radio_dd = st.radio(label=dd, options=opcoes, horizontal=True, index=None)
        radio_diabetes = st.radio(label=diabetes, options=opcoes, horizontal=True, index=None)
        radio_hemorragia = st.radio(label=hemorragia, options=opcoes, horizontal=True, index=None)
        radio_sinusite = st.radio(label=sinusite, options=opcoes, horizontal=True, index=None)
        colun1, colun2 = st.columns(2)
        with colun2:
            if st.form_submit_button(botao2):
                st.session_state.termo_medico.append((radio_gravida, radio_remedio, radio_cardiaca, radio_asma,
                                                      radio_pulmonar, radio_epilepsia, radio_enjoo, radio_dd,
                                                      radio_coluna, radio_diabetes, radio_ouvido, radio_hemorragia,
                                                      radio_sinusite))
                st.session_state.count += 1
                st.rerun()
if st.session_state.count == 5:
    st.subheader(importante)

    input_cirurgia = st.radio(label=cirurgia, options=opcoes, horizontal=True, index=None)
    nome_cirurgia = ''
    input_tempo_cirurgia = ''
    if input_cirurgia == 'Sim':
        nome_cirurgia = st.text_input(qual_cirurgia)
        input_tempo_cirurgia = st.text_input(tempo_cirurgia)

    viagem = st.radio(viajar, options=opcoes, index=None,
                      horizontal=True)
    menor = st.radio(ciente1, opcoes1,
                     index=None)
    bebida = st.radio(ciente2, options=opcoes1, index=None)
    st.write(texto_final)
    coluna1, coluna2 = st.columns(2)

    with coluna2:
        if st.button(enviar):
            gravida, remedio, cardiaca, asma, pulmonar, epilepsia, enjoo, dd, coluna, diabetes, ouvido, hemorragia, sinusite = st.session_state.termo_medico

            id_cliente = st.session_state.id_clientes

            id_termo_cliente = st.session_state.id_termo_clientes

            repo.insert_termo_medico(id_cliente, id_termo_cliente, gravida, remedio, cardiaca, asma, pulmonar,
                                     epilepsia,
                                     enjoo, dd, coluna, diabetes, ouvido, hemorragia, sinusite, input_cirurgia,
                                     nome_cirurgia,
                                     input_tempo_cirurgia, viagem, menor, bebida)
            st.session_state.count += 1
            st.rerun()

if st.session_state.count == 6:
    st.header(enviado)
    st.write(taxa)
    st.write(localizacao)
    st.write('📍 Praça da Bandeira, 23 - Praia dos Anjos')
    st.image('imagem1.jpg', caption='Nossa loja se encontra na Praça da Bandeira, 23 - Praia dos Anjos',
             use_column_width=True)
