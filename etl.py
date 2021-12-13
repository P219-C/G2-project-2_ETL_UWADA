from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.dialects import postgresql
from urllib.parse import quote_plus as urlquote
from credentials import *
import datetime as dt 

connection_url = URL.create(
    drivername = "postgresql", 
    username = db_user,
    password = db_password,
    host = "localhost", 
    port = 5432,
    database = "music_ddl_create", 
)

engine = create_engine(connection_url)

# Reflect postgresql database
from sqlalchemy import MetaData
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
artist = metadata_obj.tables["artist"]
songs = metadata_obj.tables["songs"]
album = metadata_obj.tables["album"]
concert = metadata_obj.tables["concert"]


# Upsert: artist
insert_statement = postgresql.insert(artist).values(artist_df.to_dict(orient='records'))
upsert_statement = insert_statement.on_conflict_do_update(
    index_elements=['artist_spotify_ID'],
    set_={c.key: c for c in insert_statement.excluded if c.key not in ['artist_spotify_ID']})
engine.execute(upsert_statement)


# Upsert: songs
insert_statement = postgresql.insert(songs).values(song_df.to_dict(orient='records'))
upsert_statement = insert_statement.on_conflict_do_update(
    index_elements=['song_ID'],
    set_={c.key: c for c in insert_statement.excluded if c.key not in ['song_ID']})
engine.execute(upsert_statement)


# Upsert album
insert_statement = postgresql.insert(album).values(album_grouped_df.to_dict(orient='records'))
upsert_statement = insert_statement.on_conflict_do_update(
    index_elements=['album_name'],
    set_={c.key: c for c in insert_statement.excluded if c.key not in ['album_name']})
engine.execute(upsert_statement)


# Upsert concert
insert_statement = postgresql.insert(concert).values(event_df.to_dict(orient='records'))
upsert_statement = insert_statement.on_conflict_do_update(
    index_elements=['artist_spotify_ID'],
    set_={c.key: c for c in insert_statement.excluded if c.key not in ['artist_spotify_ID']})
engine.execute(upsert_statement)




print(f"ETL job completed at {dt.datetime.now()}")