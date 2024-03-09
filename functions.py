import os

import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    passwd=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME"),
    autocommit=True,
    ssl_verify_identity=False,
    ssl_ca=r"C:\users\acqua\downloads\cacert-2023-08-22.pem",
    charset="utf8")

cursor = mydb.cursor(buffered=True)

chars = "'),([]"


def linguagem(linguagem):
    if linguagem == "Português":
        titulo = "Formulário de Inscrição"
        data_mergulho = "Data do Mergulho"
        check_in = "Manhã - Check-in 07:30, Saída 08:30"
        nome = "Nome Completo"
        cpf = "CPF"
        data_nascimento = "Data de Nascimento"
        email = "E-mail"
        telefone = "Telefone"
        formato_data = 'DD/MM/YYYY'
        endereco = 'Endereço Completo'
        botao = "Anterior"
        texto = ("""
        Eu estou ciente que o mergulho recreativo com ar comprimido tem seus riscos e que antes de fazê-lo serei instruído de como proceder durante meu passeio guiado com relação aos procedimentos de segurança tais como desalagamento de máscara, regulador e o modo de se comunicar via sinais debaixo d’água.
        Serei instruído durante o briefing sobre como proceder com relação à embarcação, respiração e equalização das vias aéreas, tendo a possibilidade de tirar qualquer dúvida que restar sobre o meu passeio antes de acontecer.
        Estou ciente, ainda, que os mergulhos são realizados em um local distante, tanto em tempo, como espaço, do atendimento médico. 
        Declaro que estou ciente que uma vez que eu entre na água com o amparo do mergulhador e inicie o processo de adaptação o valor do meu batismo não será ressarcido. Entendo que é terminantemente proibido o consumo de bebida alcóolica antes do mergulho.
        
        Ciente de todos esses riscos, declaro, pelo presente termo, minha livre opção de realizar esse mergulho recreativo guiado.
        Em vista da minha participação nesta atividade eu assumo de livre e espontânea vontade, todos os riscos referentes a tal, isentando de tal forma o (s) meu (s) instrutores, guia(s), a associação, a empresa e qualquer um dos seus respectivos funcionários (doravante denominados “Partes Desobrigadas”), não somente.
        
        a) de qualquer responsabilidade por qualquer dano, lesão, morte ou quaisquer outros danos materiais ou orais sofridos por mim, por minha família, por meus herdeiros e sucessores em decorrência de minha livre participação na atividade de mergulho recreativo, de cujos riscos, confirmo, que estou plenamente ciente, mas também,
        
        b) de qualquer reivindicação ou processo que venha a ser instaurado por mim, minha família, meu espólio, meus herdeiros, ou sucessores, resultantes de minha inscrição e participação nesta atividade.
        Também fui informado e estou ciente que a prática de mergulho recreativo é atividade física extenuante e que estarei me excedendo durante o mergulho e, caso venha a sofrer uma lesão resultante de ataque cardíaco, pânico, hiper ventilação, etc, assumo expressamente o risco e responsabilidade por tais lesões e isentando de responsabilidades as “Partes Desobrigadas”.
        
        Declaro que estou apto física e mentalmente a participar das atividades de mergulho, não tendo qualquer moléstia ou problema de saúde que possam prejudicar ou causar qualquer risco antes, durante ou após a prática de mergulho.
    """)
        titulo2 = 'Certificado de Entendimento e Assunção Expressa de Risco'
        nome_emergencia = 'Nome de um contato de emergência'
        telefone_emergencia = 'Telefone do contato de emergência'
        botao2 = 'Proximo'
        titulo3 = 'HISTÓRICO MÉDICO – Informações Confidenciais'
        subtitulo = ("""
        As perguntas abaixo visam identificar problemas de saúde que possam interferir com a prática do mergulho recreativo. Isso necessariamente não irá impedi-lo de participar, porém irá requerer avaliação mais específica a se necessário opinião médica. 
            \nPor favor, preencher as lacunas com SIM ou NÃO. Você teve algumas dessas doenças?""")

        gravida = 'Está gravida ou tentando engravidar?'
        cardiaca = 'Doença ou cirurgia cardiaca?'
        pulmonar = 'Doença pulmonar ou Pneumotorax?'
        enjoo = 'Enjoos frequentes?'
        coluna = 'Problemas ou cirurgias na coluna?'
        ouvido = 'Doenças ou cirurgias no ouvido ou seios da face?'
        remedio = 'Toma medicamento regularmente?'
        asma = 'Asma,dificuldade respiratoria ou sinusite frequente?'
        epilepsia = 'Epilepsia, problemas cerebrais ou desmaios?'
        dd = 'Acidente de mergulho, doença desconpressiva?'
        diabetes = 'Diabetes ou problemas de pressão arterial?'
        hemorragia = 'Hemorragias, problmas no sangue ou ulcera?'
        cirurgia = 'Já fez alguma cirurgia?'
        opcoes = ['Sim', 'Não']

        opcoes1 = ['Sim']
        qual_cirurgia = 'Qual foi a cirurgia?'
        tempo_cirurgia = 'Quanto tempo tem sua cirgurgia?'
        viajar = 'Você viajará de avião no periodo de 12 horas após o mergulho?'
        ciente1 = 'Está ciente que a empresa não se responsabiliza em cuidar de menores de idade dentro da embarcação?'
        ciente2 = 'Está ciente que é proibido o consumo de bebida alcoolica antes do mergulho?'
        texto_final = 'Declaro, por fim, que li o presente termo, tendo-o entendido e concordado na íntegra, e que estou apto a assinar este termo de responsabilidade ou obtive a necessária autorização por escrito dos meus pais ou responsáveis, que também firmam.'
        pais = 'País'
        estado = 'Estado'
        enviar = 'Enviar Formulario'
        importante = 'Questões Importantes'
        enviado = '✅ Formulario Enviado com Sucesso'
        taxa = 'Por favor não esquecer de levar R$ 10,00 em dinheiro para taxa de embarque'
        localizaçao = 'O check-in começa as 07:30 e nossa embarcação sairá as 08:30'



    elif linguagem == 'Español':
        titulo = "Formulario de Registro"
        data_mergulho = "Fecha de Buceo"
        check_in = "Manhã - Registro 07:30, Salida 08:30"
        nome = "Nombre"
        cpf = "DNI"
        data_nascimento = "Fecha de Nacimiento"
        email = "Correo Electrónico"
        telefone = "Teléfono"
        formato_data = 'DD/MM/YYYY'
        endereco = 'Direccion Completa'
        botao = "Anterior"
        texto = """  
        Soy consciente de que el buceo recreativo con aire comprimido tiene sus riesgos y que antes de hacerlo, se me instruirá sobre cómo proceder durante mi recorrido guiado con respecto a los procedimientos de seguridad, como el despeje de la máscara, la recuperación del regulador y cómo comunicarse a través de señales submarinas.
        Se me instruirá durante la reunión informativa sobre cómo proceder con la embarcación, la respiración y la igualación de las vías respiratorias, teniendo la posibilidad de hacer cualquier pregunta que quede sobre mi recorrido antes de que ocurra.
        También soy consciente de que los buceos se realizan en un lugar lejano, tanto en tiempo como en espacio, del servicio médico. 
        Declaro que soy consciente de que una vez que entro en el agua con el apoyo del buceador y comienzo el proceso de adaptación, el valor de mi bautismo no se reembolsará. Entiendo que está terminantemente prohibido el consumo de bebidas alcohólicas antes del buceo.
        
        Consciente de todos estos riesgos, declaro, mediante este término, mi libre elección de realizar este buceo recreativo guiado.
        En vista de mi participación en esta actividad, asumo, de mi propia voluntad, todos los riesgos relacionados con ella, eximiendo de esa manera al (los) instructor (es), guía (s), la asociación, la empresa y cualquiera de sus respectivos empleados (en adelante referidos como "Partes Liberadas"), no solo.
        
        a) de cualquier responsabilidad por cualquier daño, lesión, muerte o cualquier otro daño material o oral sufrido por mí, mi familia, mis herederos y sucesores como resultado de mi participación libre en la actividad de buceo recreativo, cuyos riesgos confirmo que estoy plenamente consciente, sino también,
        
        b) de cualquier reclamo o demanda que pueda ser presentada por mí, mi familia, mi patrimonio, mis herederos o sucesores, resultantes de mi inscripción y participación en esta actividad.
        También he sido informado y soy consciente de que el buceo recreativo es una actividad física extenuante y que me estaré esforzando durante el buceo y, en caso de sufrir una lesión resultante de un ataque cardíaco, pánico, hiperventilación, etc., asumo expresamente el riesgo y la responsabilidad de tales lesiones y libero a las "Partes Liberadas" de responsabilidad.
        
        Declaro que estoy física y mentalmente apto para participar en actividades de buceo, no teniendo ninguna enfermedad o problema de salud que pueda perjudicar o causar algún riesgo antes, durante o después del buceo."""
        titulo2 = 'Certificado de Comprensión y Asunción Expresa de Riesgo'
        nome_emergencia = 'Nombre de contacto de emergencia'
        telefone_emergencia = 'Teléfono de contacto de emergencia'
        botao2 = 'Proximo'
        titulo3 = 'HISTORIA MÉDICA - Información Confidencial'
        subtitulo = ("""
        Las preguntas a continuación tienen como objetivo identificar problemas de salud que puedan interferir con el buceo recreativo. Esto no necesariamente le impedirá participar, pero puede requerir una evaluación más específica y, si es necesario, una opinión médica.
            \nPor favor, complete los espacios en blanco con SÍ o NO. ¿Ha tenido alguna de estas enfermedades?""")

        gravida = "¿Está embarazada o intentando quedar embarazada?"
        cardiaca = "¿Enfermedad cardiaca o cirugía?"
        pulmonar = "¿Enfermedad pulmonar o neumotórax?"
        enjoo = "¿Náuseas frecuentes?"
        coluna = "¿Problemas o cirugías de columna?"
        ouvido = "¿Enfermedades o cirugías de oído o senos paranasales?"
        remedio = "¿Toma medicamentos regularmente?"
        asma = "¿Asma, dificultades para respirar o sinusitis frecuente?"
        epilepsia = "¿Epilepsia, problemas cerebrales o desmayos?"
        dd = "¿Accidente de buceo, enfermedad por descompresión?"
        diabetes = "¿Diabetes o problemas de presión arterial?"
        hemorragia = "¿Trastornos hemorrágicos, problemas de sangre o úlceras?"
        cirurgia = "¿Ha tenido alguna cirugía?"
        opcoes = ['Sí', 'No']

        opcoes1 = ['Sí']
        qual_cirurgia = '¿Cuál fue la cirugía?'
        tempo_cirurgia = '¿Cuánto tiempo tiene su cirugía?'
        viajar = '¿Viajará en avión dentro de las 12 horas posteriores al buceo?'
        ciente1 = '¿Está al tanto de que la empresa no se hace responsable del cuidado de menores a bordo de la embarcación?'
        ciente2 = '¿Está al tanto de que está prohibido consumir bebidas alcohólicas antes de bucear?'
        texto_final = 'Declaro, finalmente, que he leído este documento, lo he comprendido en su totalidad y acepto firmar esta renuncia de responsabilidad, o he obtenido la autorización escrita necesaria de mis padres o tutores, quienes también firman.'
        pais = 'País'
        estado = 'Estado'
        enviar = 'Enviar Formulario'
        importante = 'Preguntas Importantes'
        enviado = '✅ Formulario Enviado con Éxito'
        taxa = 'Por favor, recuerde traer R$10.00 en efectivo para la tarifa de embarque'
        localizaçao = 'El check-in comienza a las 07:30 y nuestra embarcación partirá a las 08:30'



    elif linguagem == 'English':
        titulo = "Registration Form"
        data_mergulho = "Dive Date"
        check_in = "Morning - Check-in 07:30, Departure 08:30"
        nome = "Name"
        cpf = "SSN"
        data_nascimento = "Date of Birth"
        email = "Email"
        telefone = "Phone"
        formato_data = 'YYYY/MM/DD'
        endereco = 'Complete Address'
        botao = "Previous"
        texto = ("""
        I am aware that recreational diving with compressed air has its risks and that before doing so, I will be instructed on how to proceed during my guided tour regarding safety procedures such as mask clearing, regulator recovery, and how to communicate via underwater signals.
        I will be instructed during the briefing on how to proceed with the vessel, breathing, and equalization of the airways, having the possibility to ask any questions that remain about my tour before it happens.
        I am also aware that dives are conducted in a location far away, both in time and space, from medical assistance. 
        I declare that I am aware that once I enter the water with the diver's support and start the adaptation process, the value of my baptism will not be refunded. I understand that the consumption of alcoholic beverages before diving is strictly prohibited.
        
        Aware of all these risks, I declare, by this term, my free choice to undertake this guided recreational dive.
        In view of my participation in this activity, I assume, of my own free will, all risks related to it, exempting in such a way the instructor(s), guide(s), the association, the company, and any of their respective employees (hereinafter referred to as "Released Parties"), not only.
        
        a) from any liability for any damage, injury, death, or any other material or oral damages suffered by me, my family, my heirs, and successors as a result of my free participation in the recreational diving activity, of whose risks I confirm that I am fully aware, but also,
        
        b) from any claim or lawsuit that may be brought by me, my family, my estate, my heirs, or successors, resulting from my registration and participation in this activity.
        I have also been informed and am aware that recreational diving is an strenuous physical activity and that I will be exerting myself during the dive and, in the event that I suffer an injury resulting from a heart attack, panic, hyperventilation, etc., I expressly assume the risk and responsibility for such injuries and release the "Released Parties" from liability.
        
        I declare that I am physically and mentally fit to participate in diving activities, having no illness or health problems that could impair or cause any risk before, during, or after diving.
        """)
        titulo2 = 'Certificate of Understanding and Express Assumption of Risk'
        nome_emergencia = 'Emergency Contact Name'
        telefone_emergencia = 'Emergency Contact Phone'
        botao2 = 'Next'
        titulo3 = 'MEDICAL HISTORY - Confidential Information'
        subtitulo = ("""
        The questions below aim to identify health problems that may interfere with recreational diving. This will not necessarily prevent you from participating, but may require more specific evaluation and, if necessary, medical opinion.
            \nPlease fill in the blanks with YES or NO. Have you had any of these illnesses?""")

        gravida = "Are you pregnant or trying to get pregnant?"
        cardiaca = "Heart disease or surgery?"
        pulmonar = "Lung disease or Pneumothorax?"
        enjoo = "Frequent nausea?"
        coluna = "Spinal problems or surgeries?"
        ouvido = "Ear or sinus disease or surgeries?"
        remedio = "Do you take medication regularly?"
        asma = "Asthma, breathing difficulties, or frequent sinusitis?"
        epilepsia = "Epilepsy, seizures, brain problems, or fainting?"
        dd = "Diving accident, decompression illness?"
        diabetes = "Diabetes or blood pressure problems?"
        hemorragia = "Bleeding disorders, blood problems, or ulcers?"
        cirurgia = "Have you had any surgeries?"
        opcoes = ['Yes', 'No']
        opcoes1 = ['Yes']
        qual_cirurgia = 'What was the surgery?'
        tempo_cirurgia = 'How long ago was your surgery?'
        viajar = 'Will you be traveling by plane within 12 hours after diving?'
        ciente1 = 'Are you aware that the company is not responsible for taking care of minors on board the vessel?'
        ciente2 = 'Are you aware that consuming alcoholic beverages before diving is prohibited?'
        texto_final = 'I declare, finally, that I have read this document, understood it in its entirety, and agree to sign this liability waiver, or have obtained the necessary written authorization from my parents or guardians, who also sign.'
        pais = 'Country'
        estado = 'State'
        enviar = 'Submit Form'
        importante = 'Important Questions'
        enviado = '✅ Form Submitted Successfully'
        taxa = 'Please remember to bring R$10.00 in cash for the boarding fee'
        localizaçao = 'Check-in starts at 07:30 and our vessel will depart at 08:30'

    return titulo, data_mergulho, check_in, nome, cpf, data_nascimento, email, telefone, formato_data, endereco, botao, texto, titulo2, nome_emergencia, telefone_emergencia, botao2, titulo3, subtitulo, gravida, cardiaca, pulmonar, enjoo, coluna, ouvido, remedio, asma, epilepsia, dd, diabetes, hemorragia, cirurgia, opcoes, opcoes1, qual_cirurgia, tempo_cirurgia, viajar, ciente1, ciente2, texto_final, pais, estado, enviar, importante, enviado, taxa, localizaçao


# def create_termo_clientes():
#     mydb.connect()
#     cursor.execute("""
#             create table termo_clientes(
#                 id int not null auto_increment,
#                 data_reserva date,
#                 id_cliente int,
#                 nome varchar(40),
#                 telefone varchar(20),
#                 cpf varchar(20),
#                 data_nascimento date,
#                 email varchar(20),
#                 nome_emergencia varchar(20),
#                 telefone_emergencia varchar(20),
#                 roupa varchar(20),
#                 cidade varchar(20),
#                 estado varchar(20),
#                 pais varchar(20),
#                 primary key (id),
#                 foreign key (id_cliente) references cliente(id));
#             """)
#     mydb.close()


# def create_termo_medico():
#     mydb.connect()
#     cursor.execute("""
#         create table termo_medico (
#             id int not null auto_increment,
#             id_cliente int,
#             id_termo_cliente int,
#             gravida varchar(3),
#             remedio varchar(3),
#             doenca_cardioaca varchar(3),
#             asma varchar(3),
#             doenca_pulmonar varchar(3),
#             epilepsia varchar(3),
#             enjoo varchar(3),
#             dd varchar(3),
#             coluna varchar(3),
#             diabetes varchar(3),
#             ouvido varchar(3),
#             hemorragia varchar(3),
#             primary key (id),
#             foreign key (id_cliente) references cliente(id),
#             foreign key (id_termo_cliente) references termo_clientes(id));
#     """)
#     mydb.close()


def insert_termo_clientes(data_reserva, id_cliente, nome, telefone, cpf, data_nascimento, email, nome_emergencia,
                          telefone_emergencia, estado, pais):
    mydb.connect()

    st.write(f'id_cliente termo clientes - {id_cliente}')

    cursor.execute(
        "INSERT INTO termo_clientes (data_reserva, id_cliente, nome, telefone, cpf, data_nascimento, email, nome_emergencia, telefone_emergencia, estado, pais) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ",
        (data_reserva, id_cliente, nome, telefone, cpf, data_nascimento, email, nome_emergencia, telefone_emergencia,
         estado, pais))
    id_termo_clientes = cursor.lastrowid
    mydb.close()

    return id_termo_clientes


def cadastra_cliente(nome, data, telefone, cpf, estado):
    mydb.connect()
    nome_cliente = str(nome).split()
    st.write(nome)
    st.write(nome_cliente)
    cursor.execute(
        f"SELECT id_cliente FROM reserva  WHERE nome_cliente LIKE '{nome_cliente[0]}%' and data = '{data}'")
    dados = cursor.fetchall()
    lista = []

    if len(dados) >= 1:
        for i, dado in enumerate(dados):
            cursor.execute(f"SELECT * FROM termo_clientes where id_cliente = %s and data_reserva = %s", (dado[i], data))
            resultado = cursor.fetchall()
            if resultado:
                lista.append(dado)
        if len(lista) >= 1:
            dados = ''
    st.write(f'1 - {dados}')
    id_cliente = None

    if len(dados) != 0:
        if len(dados) > 1:
            nome_cliente = f'{nome_cliente[0]} {nome_cliente[1]}'
            st.write(nome_cliente)
            cursor.execute(
                f"SELECT c.id FROM reserva AS r INNER JOIN cliente AS c ON r.id_cliente = c.id WHERE c.nome LIKE '{nome_cliente}%' and r.data = '{data}'")
            dados = cursor.fetchall()
            st.write(f'IF 2 - {dados}')
            if len(dados) >= 1:
                id_cliente = ''

            else:
                id_cliente = str(dados).translate(str.maketrans('', '', chars))
        else:
            id_cliente = str(dados).translate(str.maketrans('', '', chars))

        st.write(id_cliente)
        cursor.execute(
            "UPDATE cliente SET nome = %s, telefone = %s, cpf = %s, estado = %s WHERE id = %s",
            (nome, telefone, cpf, estado, id_cliente)
        )

        cursor.execute("SELECT tipo from reserva where id_cliente = %s", (id_cliente,))
        tipo = cursor.fetchone()
        if tipo:
            if tipo[0] != 'OWD' and tipo[0] != 'ADV':
                cursor.execute(
                    f"UPDATE reserva set nome_cliente = '{nome}' WHERE id_cliente = {id_cliente} and data = '{data}'")

    return id_cliente


def insert_termo_medico(id_cliente, id_termo_cliente, gravida, remedio, cardiaca, asma, pulmonar, epilepsia, enjoo, dd,
                        coluna, diabetes, ouvido, hemorragia, input_cirurgia, nome_cirurgia, input_tempo_cirurgia,
                        viagem, menor, bebida):
    mydb.connect()

    cursor.execute(
        "INSERT INTO termo_medico (id_cliente, id_termo_cliente, gravida, remedio, doenca_cardiaca, asma, doenca_pulmonar, epilepsia, enjoo, dd, coluna, diabetes, ouvido, hemorragia, cirurgia, nome_cirurgia, tempo_cirurgia, viagem,  menor, bebida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (id_cliente, id_termo_cliente, gravida, remedio, cardiaca, asma, pulmonar, epilepsia, enjoo, dd, coluna,
         diabetes, ouvido, hemorragia, input_cirurgia, nome_cirurgia, input_tempo_cirurgia, viagem, menor, bebida))
