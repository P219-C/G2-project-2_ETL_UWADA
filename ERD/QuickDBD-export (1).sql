-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Artist" (
    "artist_id" INTEGER   NOT NULL,
    "artist_name" VARCHAR   NOT NULL,
    "artist_ranking" INTEGER   NOT NULL,
    "birth_place" VARCHAR   NOT NULL,
    "gender" VARCHAR   NOT NULL,
    "age" DATA   NOT NULL,
    CONSTRAINT "pk_Artist" PRIMARY KEY (
        "artist_id","artist_ranking"
     )
);

CREATE TABLE "Songs" (
    "song_ranking" INTEGER   NOT NULL,
    "song_title" VARCHAR   NOT NULL,
    "artist_name" VARCHAR   NOT NULL,
    "artist_id" INTEGER   NOT NULL,
    "album_name" VARCHAR   NOT NULL,
    "duration" INTEGER   NOT NULL,
    "genres_id" INTEGER   NOT NULL,
    CONSTRAINT "pk_Songs" PRIMARY KEY (
        "song_ranking"
     )
);

CREATE TABLE "Album" (
    "album_name" VARCHAR   NOT NULL,
    "artist_name" VARCHAR   NOT NULL,
    "release_year" DATA   NOT NULL,
    CONSTRAINT "pk_Album" PRIMARY KEY (
        "album_name"
     )
);

CREATE TABLE "Concert" (
    "artist_name" VARCHAR   NOT NULL,
    "venue" VARCHAR   NOT NULL,
    "location" VARCHAR   NOT NULL,
    "date" DATA   NOT NULL,
    CONSTRAINT "pk_Concert" PRIMARY KEY (
        "artist_name"
     )
);

CREATE TABLE "Genres" (
    "genres_id" INTEGER   NOT NULL,
    "genres_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Genres" PRIMARY KEY (
        "genres_id"
     )
);

ALTER TABLE "Songs" ADD CONSTRAINT "fk_Songs_artist_id" FOREIGN KEY("artist_id")
REFERENCES "Artist" ("artist_id");

ALTER TABLE "Songs" ADD CONSTRAINT "fk_Songs_album_name" FOREIGN KEY("album_name")
REFERENCES "Album" ("album_name");

ALTER TABLE "Songs" ADD CONSTRAINT "fk_Songs_genres_id" FOREIGN KEY("genres_id")
REFERENCES "Genres" ("genres_id");

ALTER TABLE "Concert" ADD CONSTRAINT "fk_Concert_artist_name" FOREIGN KEY("artist_name")
REFERENCES "Artist" ("artist_name");

