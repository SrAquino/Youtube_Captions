import sqlite3

# Altera o nome de uma tabela no banco de dados
def alter_table(database_path, nome_atual , novo_nome):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"ALTER TABLE {nome_atual} RENAME TO {novo_nome};")
        print(f"Tabela {nome_atual} renomeada para {novo_nome} com sucesso!")

        # Confirmar a alteração
        conn.commit()
        return novo_nome

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return False
        
    finally:
        # Fechar conexão
        conn.close()

# Altera o nome de uma coluna de uma tabela no banco de dados
def alter_column(database_path, table_name, old_column_name, new_column_name):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} TO {new_column_name};")
        print(f"Tabela {old_column_name} renomeada para {new_column_name} com sucesso!")

        # Confirmar a alteração
        conn.commit()
        return new_column_name

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return False
        
    finally:
        # Fechar conexão
        conn.close()

# Adiciona uma nova coluna a uma tabela no banco de dados
def new_collumn(database_path, table_name, table_collum, tipo_dados):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {table_collum} {tipo_dados};")
        print(f"Coluna '{table_collum}' adicionada com sucesso!")

    except sqlite3.OperationalError as e:
        print(f"Erro ao adicionar coluna: {e}")

    finally:
        conn.commit()
        conn.close()

# Recupera todos os dados de uma tabela no banco de dados
def get_all_data(database_path, table_name, table_collum, table_collum2="", table_collum3=""):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Consulta SQL para obter os dados
        if table_collum2 == "" and table_collum3 == "":
            query = f"SELECT id, {table_collum} FROM {table_name}"
        elif table_collum3 == "":
            query = f"SELECT id, {table_collum}, {table_collum2} FROM {table_name}"
        else:
            query = f"SELECT id, {table_collum}, {table_collum2}, {table_collum3} FROM {table_name}"
        
        cursor.execute(query,)

        # Buscar todos os resultados
        results = cursor.fetchall()
        return results

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []

    finally:
        # Fechar a conexão
        conn.close()

# Cria uma nova tabela
def create_table(database_path, table_name, columns):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Criar a string da consulta SQL para criação da tabela
        columns_sql = ', '.join([f"{column} {data_type}" for column, data_type in columns.items()])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"

        # Executar a consulta SQL
        cursor.execute(create_table_sql)

        # Confirmar a transação
        conn.commit()

        print(f"Tabela '{table_name}' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Exclui uma tabela do banco de dados
def drop_table(database_path, table_name):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Comando para excluir a tabela
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        print(f"Tabela {table_name} excluída com sucesso (se existia).")

    except sqlite3.Error as e:
        print(f"Erro ao excluir a tabela: {e}")

    finally:
        conn.close()

# Atualiza os dados de uma tabela no banco de dados
def update_data(database_path, table_name, table_collum, id, value):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"UPDATE {table_name} SET {table_collum} = ? WHERE id = ?", (value,id))

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()

# Insere dados em uma tabela no banco de dados
def push_data(database_path, table_name, table_collum, id, value):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"INSERT OR IGNORE INTO {table_name} (id, {table_collum}) VALUES (?, ?)", (id,value))

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()

def push_many_data(database_path, table_name, table_collum, data):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        insert_sql = f"""
        INSERT INTO {table_name} (id,{table_collum})
        VALUES (?,?)
        ON CONFLICT(id) DO UPDATE SET {table_collum} = excluded.{table_collum};
        """
        cursor.executemany(insert_sql, data)

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()



# REVISAR : 

# Função para buscar links no banco de dados
def fetch_links_from_db(database_path, table_name):
    """
    Recupera todos os links de uma tabela no banco de dados SQLite.
    
    Args:
        database_path (str): Caminho para o arquivo do banco de dados SQLite.
        table_name (str): Nome da tabela que contém os links.
    
    Returns:
        list: Uma lista de links armazenados no banco de dados.
    """
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Consultar os links na tabela
        query = f"SELECT url FROM {table_name};"
        cursor.execute(query)

        # Obter todos os resultados
        links = [row[0] for row in cursor.fetchall()]

        return links

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        # Fechar conexão
        conn.close()

# Get linguagem do vídeo
def get_languange(database_path, table_name, id):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Consultar os links na tabela
        query = f"SELECT language FROM {table_name} WHERE id = ?;"
        cursor.execute(query, (id,))

        # Obter todos os resultados
        language = cursor.fetchone()

        return language

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        # Fechar conexão
        conn.close()

def get_unique_languages(database_path, table_name):
    try:
        # Conectar ao banco
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Executar consulta para pegar idiomas únicos
        query = f"SELECT DISTINCT language FROM {table_name};"
        cursor.execute(query)
        languages = [row[0] for row in cursor.fetchall()]

        return languages

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []

    finally:
        if conn:
            conn.close()

# Função para inserir links no banco de dados
def push_links_into_db(database_path, table_name, video_links):
    """
    Adiciona links de uma lista no banco de dados SQLite.
    
    Args:
        database_path (str): Caminho para o arquivo do banco de dados SQLite.
        table_name (str): Nome da tabela para inserir os links.
    """

    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id TEXT PRIMARY KEY NOT NULL,
            url TEXT NOT NULL,
            language TEXT NOT NULL,
            likes INTEGER DEFAULT 0, 
            comments INTEGER DEFAULT 0, 
            views INTEGER DEFAULT 0
        );
        ''')

        for link in video_links.values():
            #print((link['id'], link['url'], link['language']))
            cursor.execute(f"INSERT OR IGNORE INTO {table_name} (id, url, language, likes, comments, views) VALUES (?, ?, ?, ?, ?, ?)", 
                            (link['id'], link['url'], link['language'], link['likes'], link['comments'], link['views'])
            )

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()

def push_transcribes_into_db(database_path, table_name, transcriptions,id):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id TEXT PRIMARY KEY NOT NULL,
            transcription TEXT NOT NULL,
            VideoID TEXT NOT NULL,
            FOREIGN KEY (VideoID) REFERENCES links (id)
        )
        ''')

        cursor.execute(f"INSERT OR IGNORE INTO {table_name} (id, transcription,VideoID) VALUES (?, ?, ?)", (id, transcriptions, id))

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()

def push_caption_into_db(database_path, table_name, caption,id,ssid):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id TEXT PRIMARY KEY NOT NULL,
            caption TEXT NOT NULL,
            VideoID TEXT NOT NULL,
            FOREIGN KEY (VideoID) REFERENCES links (id)
        )
        ''')

        cursor.execute(f"INSERT OR IGNORE INTO {table_name} (id, caption, VideoID) VALUES (?, ?, ?)", ((id +'_'+ ssid), caption, id))

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()

def get_data_by_video_id(database_path, table_name, video_id):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Consulta SQL para obter os dados
        query = f"SELECT * FROM {table_name} WHERE id = ?"
        cursor.execute(query, (video_id,))

        # Buscar todos os resultados
        results = cursor.fetchall()
        return results

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []

    finally:
        # Fechar a conexão
        conn.close()