# Jinghua Zhang, Eriq Deng, Kevin Sim
# 2/20/2021 CS231 Spr 2021
# Adding/Updating a song to Terminus db
# Description: The following code takes user input and adds or updates an object in the local terminus database
from terminusdb_client import WOQLObj
from terminusdb_client import WOQLQuery as WQ
from terminusdb_client import WOQLClass
from terminusdb_client import TerminusDB

server_url = "https://127.0.0.1:6363"
db = input("Please input local database id")
user = "admin"
account = "admin"
key = "root"
client = TerminusDB(server_url=server_url, user=user, account=account, key=key, db_id=db)


def update_song(o_title, new_artist, n_title, new_length, new_album):
    client.run(WQ().delete_object(f"doc:song_{o_title}"))
    add_song(new_artist, n_title, new_length, new_album)


def add_song(s_artist, s_title, s_length, s_album) -> None:
    song = WOQLClass(
        obj_id="song",
    )
    song.add_property("artist", "string", label="artist", description="name of artist")
    song.add_property("song_title", "string", label="song_title", description="title of song")
    song.add_property("song_length", "string", label="song_length", description="length of song")
    song.add_property("album", "string", label="song_length", description="name of album")
    new_object = WOQLObj(
        obj_id=s_title,
        obj_type=song,
        obj_property={
            "artist": {"value": s_artist},
            "song_title": {"value": s_title},
            "song_length": {"value": s_length},
            "album": {"value": s_album}
        }
    )
    client.add_object(new_object)


if __name__ == "__main__":
    loop = True
    while loop:
        user_input = input("Please input your action(add for adding songs, update for updating entry, q to quit)")\
            .lower()
        if user_input == "q":
            loop = False
        elif user_input == "add":
            artist = input("Please input name of artist: ")
            title = input("Please input song title: ")
            length = input("Please input song length: ")
            album = input("Please input album name: ")
            add_song(artist, title, length, album)
            print(f"Successfully added {title}")
        elif user_input == "update":
            original_title = input("Please input the original title of the song you wish to update: ")
            new_title = input("Please input new song title: ")
            artist = input("Please input new name of artist: ")
            length = input("Please input new song length:")
            album = input("Please input new album name: ")
            update_song(original_title, artist, new_title, length, album)
            print(f"Successfully updated {new_title}")
        else:
            print("Invalid input, please try again: ")
