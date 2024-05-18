class Repository:

    def __init__(self, db):
        self.db = db

    def select_id_cliente(self, cpf, data):
        query = """
        SELECT id_cliente 
        FROM reserva
        INNER JOIN cliente on cliente.id = reserva.id_cliente  
        WHERE cliente.cpf = %s and reserva.data = %s"""

        params = (cpf, data)

        return self.db.execute_query(query, params)

    def update_cliente(self, nome, telefone, email, estado, id_cliente):
        query = """
        UPDATE cliente SET
            nome = %s,
            telefone = %s,
            email = %s,
            estado = %s
        WHERE id = %s"""

        params = (nome, telefone, email, estado, id_cliente)

        return self.db.execute_query(query, params)

    def update_reserva(self, nome, id_cliente, data):
        query = """
        UPDATE reserva 
            SET nome_cliente = CASE WHEN tipo != 'OWD' AND tipo != 'ADV' THEN %s ELSE nome_cliente END
        WHERE id_cliente = %s AND data = %s;"""

        params = (nome, id_cliente, data)

        return self.db.execute_query(query, params)

    def insert_termo_clientes(self, data_reserva, id_cliente, nome, telefone, cpf, data_nascimento, email,
                              nome_emergencia,
                              telefone_emergencia, estado, pais):
        query = """
        INSERT INTO termo_clientes 
        (data_reserva, id_cliente, nome, telefone, cpf, data_nascimento, email, nome_emergencia, telefone_emergencia, estado, pais) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        params = (
            data_reserva, id_cliente, nome, telefone, cpf, data_nascimento, email, nome_emergencia, telefone_emergencia,
            estado, pais)

        return self.db.execute_query(query, params)

    def insert_termo_medico(self, id_cliente, id_termo_cliente, gravida, remedio, cardiaca, asma, pulmonar, epilepsia,
                            enjoo,
                            dd,
                            coluna, diabetes, ouvido, hemorragia, sinusite, input_cirurgia, nome_cirurgia,
                            input_tempo_cirurgia,
                            viagem, menor, bebida):

        query = """INSERT INTO termo_medico (id_cliente, id_termo_cliente, gravida, remedio, doenca_cardiaca, asma, doenca_pulmonar, epilepsia, enjoo, dd, coluna, diabetes, ouvido, hemorragia, sinusite, cirurgia, nome_cirurgia, tempo_cirurgia, viagem,  menor, bebida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        params = (id_cliente, id_termo_cliente, gravida, remedio, cardiaca, asma, pulmonar, epilepsia, enjoo, dd, coluna,
             diabetes, ouvido, hemorragia, sinusite, input_cirurgia, nome_cirurgia, input_tempo_cirurgia, viagem, menor,
             bebida)

        return self.db.execute_query(query, params)