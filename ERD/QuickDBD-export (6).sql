-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Artist" (
    "artist_name" VARCHAR   NOT NULL,
    "artist_spotify_ID" VARCHAR   NOT NULL
);

CREATE TABLE "Songs" (
    "song_ID" INTEGER   NOT NULL,
    "song_title" VARCHAR   NOT NULL,
    "album_name" VARCHAR   NOT NULL,
    "track_spotify_ID" VARCHAR   NOT NULL,
    "artist_spotify_ID" VARCHAR   NOT NULL,
    "song_ranking" INTEGER   NOT NULL,
    "spotify_popularity" INTEGER   NOT NULL,
    "song_duration(ms)" INTEGER   NOT NULL,
    "song_release_date" DATE   NOT NULL
);

CREATE TABLE "Album" (
    "album_name" VARCHAR   NOT NULL,
    "album_type" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Album" PRIMARY KEY (
        "album_type"
     )
);

CREATE TABLE "Concert" (
    "artist_spotify_ID" VARCHAR   NOT NULL,
    "api_artist" VARCHAR   NOT NULL,
    "venue" VARCHAR   NOT NULL,
    "country" VARCHAR   NOT NULL,
    "location" VARCHAR   NOT NULL,
    "datetime" DATA   NOT NULL
);

ALTER TABLE "Songs" ADD CONSTRAINT "fk_Songs_album_name" FOREIGN KEY("album_name")
REFERENCES "Album" ("album_name");

ALTER TABLE "Songs" ADD CONSTRAINT "fk_Songs_artist_spotify_ID" FOREIGN KEY("artist_spotify_ID")
REFERENCES "Artist" ("artist_spotify_ID");

ALTER TABLE "Concert" ADD CONSTRAINT "fk_Concert_artist_spotify_ID" FOREIGN KEY("artist_spotify_ID")
REFERENCES "Artist" ("artist_spotify_ID");

