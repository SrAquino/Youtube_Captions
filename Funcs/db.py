import sqlite3

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

def push_data(database_path, table_name, table_collum, id, value, video_id):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id TEXT PRIMARY KEY NOT NULL,
            {table_collum} TEXT NOT NULL,
            VideoID TEXT NOT NULL,
            FOREIGN KEY (VideoID) REFERENCES links (id)
        )
        ''')

        cursor.execute(f"INSERT OR IGNORE INTO {table_name} (id, {table_collum}, VideoID) VALUES (?, ?, ?)", (id,value,video_id))

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    
    finally:
        conn.commit()
        conn.close()

def get_data(database_path, table_name, table_collum, video_id):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Consulta SQL para obter os dados
        query = f"SELECT {table_collum} FROM {table_name} WHERE VideoID = ?"
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

#print(get_data('videos_data.db','transcribes','transcription','24YsiQewxeQ'))
#print(get_data('videos_data.db','captions','caption','24YsiQewxeQ'))
