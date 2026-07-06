import sqlalchemy as db

def init_db(): 
    engine = db.create_engine("sqlite:///eventdata.db")
    with engine.connect() as connection:
        connection.execute(db.text("""
                CREATE TABLE IF NOT EXISTS event(
                    id INTEGER PRIMARY KEY, name TEXT, url TEXT, date TEXT, venue TEXT, city TEXT
                )
            """))
        connection.execute(db.text("""
                CREATE TABLE IF NOT EXISTS weather(
                    id INTEGER PRIMARY KEY, temperature REAL, humidity REAL, description TEXT
                )
            """))
        