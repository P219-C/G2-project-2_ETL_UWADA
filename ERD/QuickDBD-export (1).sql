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
        "artist_id"
     )
);

CREATE TABLE "Songs" (
    "artist_id" INTEGER   NOT NULL,
    "song_title" VARCHAR   NOT NULL,
    "artist_name" VARCHAR   NOT NULL,
    "album_name" VARCHAR   NOT NULL,
    "song_ranking" INTEGER   NOT NULL,
    "duration" INTEGER   NOT NULL
);

CREATE TABLE "Album" (
    "artist_name" INTEGER   NOT NULL,
    "album_name" VARCHAR   NOT NULL,
    "release_year" DATA   NOT NULL,
    CONSTRAINT "pk_Album" PRIMARY KEY (
        "artist_name"
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
    "genres_name" VARCHAR   NOT NULL
);

ALTER TABLE "Songs" ADD CONSTRAINT "fk_Songs_artist_id" FOREIGN KEY("artist_id")
REFERENCES "Artist" ("artist_id");

ALTER TABLE "Album" ADD CONSTRAINT "fk_Album_artist_name" FOREIGN KEY("artist_name")
REFERENCES "Songs" ("artist_name");

ALTER TABLE "Concert" ADD CONSTRAINT "fk_Concert_artist_name" FOREIGN KEY("artist_name")
REFERENCES "Artist" ("artist_name");

