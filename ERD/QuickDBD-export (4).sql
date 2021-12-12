-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [Artist] (
    [artist_id] INTEGER  NOT NULL ,
    [artist_name] VARCHAR  NOT NULL ,
    [artist_ranking] INTEGER  NOT NULL ,
    [gender] VARCHAR  NOT NULL ,
    [age] DATA  NOT NULL ,
    CONSTRAINT [PK_Artist] PRIMARY KEY CLUSTERED (
        [artist_id] ASC,[artist_ranking] ASC
    )
)

CREATE TABLE [Songs] (
    [song_ranking] INTEGER  NOT NULL ,
    [song_title] VARCHAR  NOT NULL ,
    [artist_name] VARCHAR  NOT NULL ,
    [artist_id] INTEGER  NOT NULL ,
    [album_name] VARCHAR  NOT NULL ,
    [duration] INTEGER  NOT NULL ,
    [song_release_date] DATA  NOT NULL ,
    CONSTRAINT [PK_Songs] PRIMARY KEY CLUSTERED (
        [song_ranking] ASC
    )
)

CREATE TABLE [Album] (
    [album_name] VARCHAR  NOT NULL ,
    [artist_name] VARCHAR  NOT NULL ,
    CONSTRAINT [PK_Album] PRIMARY KEY CLUSTERED (
        [album_name] ASC
    )
)

CREATE TABLE [Concert] (
    [artist_name] VARCHAR  NOT NULL ,
    [venue] VARCHAR  NOT NULL ,
    [location] VARCHAR  NOT NULL ,
    [date] DATA  NOT NULL ,
    CONSTRAINT [PK_Concert] PRIMARY KEY CLUSTERED (
        [artist_name] ASC
    )
)

ALTER TABLE [Songs] WITH CHECK ADD CONSTRAINT [FK_Songs_artist_id] FOREIGN KEY([artist_id])
REFERENCES [Artist] ([artist_id])

ALTER TABLE [Songs] CHECK CONSTRAINT [FK_Songs_artist_id]

ALTER TABLE [Songs] WITH CHECK ADD CONSTRAINT [FK_Songs_album_name] FOREIGN KEY([album_name])
REFERENCES [Album] ([album_name])

ALTER TABLE [Songs] CHECK CONSTRAINT [FK_Songs_album_name]

ALTER TABLE [Concert] WITH CHECK ADD CONSTRAINT [FK_Concert_artist_name] FOREIGN KEY([artist_name])
REFERENCES [Artist] ([artist_name])

ALTER TABLE [Concert] CHECK CONSTRAINT [FK_Concert_artist_name]

COMMIT TRANSACTION QUICKDBD