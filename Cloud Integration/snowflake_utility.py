import snowflake.connector
import configparser


def connect_to_db():
    config = configparser.ConfigParser()
    config.read('config.ini')
    connection_config = config['CONNECTION']
    print("Establishing Connection to Snowflake")
    cnx = snowflake.connector.connect(
        user=connection_config['USERNAME'],
        password=connection_config['PASSWORD'],
        account=connection_config['ACCOUNT'],
        warehouse=connection_config['WAREHOUSE'],
        database=connection_config['DATABASE']
    )
    print("Connection Established")
    return cnx.cursor()


def load_tables(content):
    cursor = connect_to_db()
    for table, table_prop in content.items():
        fields = table_prop['fields']
        query = f"INSERT INTO {table} ({','.join(fields)}) VALUES ({','.join(['%s'] * len(fields))})"
        print(f"Loading table {table}")
        cursor.executemany(query, table_prop['data'])
