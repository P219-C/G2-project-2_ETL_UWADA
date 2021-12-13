-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/ON4jKz
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "artist" (
    "artist_name" VARCHAR   NOT NULL,
    "artist_spotify_ID" VARCHAR   NOT NULL,
    CONSTRAINT "pk_artist" PRIMARY KEY (
        "artist_spotify_ID"
     )
);

CREATE TABLE "songs" (
    "song_ID" INTEGER   NOT NULL,
    "song_title" VARCHAR   NOT NULL,
    "album_name" VARCHAR   NOT NULL,
    "track_spotify_ID" VARCHAR   NOT NULL,
    "artist_spotify_ID" VARCHAR   NOT NULL,
    "song_ranking" INTEGER   NOT NULL,
    "spotify_popularity" INTEGER   NOT NULL,
    "song_duration[ms]" INTEGER   NOT NULL,
    "song_release_date" DATE   NOT NULL,
    CONSTRAINT "pk_songs" PRIMARY KEY (
        "song_ID"
     )
);

CREATE TABLE "album" (
    "album_name" VARCHAR   NOT NULL,
    "album_type" VARCHAR   NOT NULL,
    CONSTRAINT "pk_album" PRIMARY KEY (
        "album_name"
     )
);

CREATE TABLE "concert" (
    "artist_spotify_ID" VARCHAR   NOT NULL,
    "api_artist" VARCHAR   NOT NULL,
    "venue" VARCHAR   NOT NULL,
    "country" VARCHAR   NOT NULL,
    "location" VARCHAR   NOT NULL,
    "datetime" DATE   NOT NULL,
    CONSTRAINT "pk_concert" PRIMARY KEY (
        "artist_spotify_ID"
     )
);

ALTER TABLE "songs" ADD CONSTRAINT "fk_songs_album_name" FOREIGN KEY("album_name")
REFERENCES "album" ("album_name");

ALTER TABLE "songs" ADD CONSTRAINT "fk_songs_artist_spotify_ID" FOREIGN KEY("artist_spotify_ID")
REFERENCES "artist" ("artist_spotify_ID");

ALTER TABLE "concert" ADD CONSTRAINT "fk_concert_artist_spotify_ID" FOREIGN KEY("artist_spotify_ID")
REFERENCES "artist" ("artist_spotify_ID");

