-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [Artist] (
    [artist_name] VARCHAR  NOT NULL ,
    [artist_spotify_ID] VARCHAR  NOT NULL 
)

CREATE TABLE [Songs] (
    [song_ID] INTEGER  NOT NULL ,
    [song_title] VARCHAR  NOT NULL ,
    [album_name] VARCHAR  NOT NULL ,
    [track_spotify_ID] VARCHAR  NOT NULL ,
    [artist_spotify_ID] VARCHAR  NOT NULL ,
    [song_ranking] INTEGER  NOT NULL ,
    [spotify_popularity] INTEGER  NOT NULL ,
    [song_duration(ms)] INTEGER  NOT NULL ,
    [song_release_date] DATE  NOT NULL 
)

CREATE TABLE [Album] (
    [album_name] VARCHAR  NOT NULL ,
    [album_type] VARCHAR  NOT NULL ,
    CONSTRAINT [PK_Album] PRIMARY KEY CLUSTERED (
        [album_type] ASC
    )
)

CREATE TABLE [Concert] (
    [artist_spotify_ID] VARCHAR  NOT NULL ,
    [api_artist] VARCHAR  NOT NULL ,
    [venue] VARCHAR  NOT NULL ,
    [country] VARCHAR  NOT NULL ,
    [location] VARCHAR  NOT NULL ,
    [datetime] DATA  NOT NULL 
)

ALTER TABLE [Songs] WITH CHECK ADD CONSTRAINT [FK_Songs_album_name] FOREIGN KEY([album_name])
REFERENCES [Album] ([album_name])

ALTER TABLE [Songs] CHECK CONSTRAINT [FK_Songs_album_name]

ALTER TABLE [Songs] WITH CHECK ADD CONSTRAINT [FK_Songs_artist_spotify_ID] FOREIGN KEY([artist_spotify_ID])
REFERENCES [Artist] ([artist_spotify_ID])

ALTER TABLE [Songs] CHECK CONSTRAINT [FK_Songs_artist_spotify_ID]

ALTER TABLE [Concert] WITH CHECK ADD CONSTRAINT [FK_Concert_artist_spotify_ID] FOREIGN KEY([artist_spotify_ID])
REFERENCES [Artist] ([artist_spotify_ID])

ALTER TABLE [Concert] CHECK CONSTRAINT [FK_Concert_artist_spotify_ID]

COMMIT TRANSACTION QUICKDBD