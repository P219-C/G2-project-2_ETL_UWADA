# G2-project-2_ETL_UWADA
Group 2 - ETL project

# Objective
The objective is to perform the ETL (Extract-Transform-Load) process by reading the dataset of Billboard, cleaning the dataset in the desired form and loading into a database for storage.

# Data Sources
- *The Hot 100* - **Web Scraping** - https://www.billboard.com/charts/hot-100/
- *The Artist 100* - **Web Scraping** - https://www.billboard.com/charts/artist-100/# Steps

# Steps
We have performed ETL in three steps:

1. Extraction - the data has been downloaded from public platform and formatted as .csv files.

2. Transformation - python has been used as the tool for transformation of datasets using the Pandas Library.

3. Loading - relational database PostgresSQL has been used to load the data.

# ERD and Data Dictionary
# Entity Relationship Diagram

![ERD](https://github.com/P219-C/G2-project-2_ETL_UWADA/blob/Oksana/ERD/QuickDBD-export%20(1).png)
The ERD diagram was created using: https://app.quickdatabasediagrams.com/#/

![test](https://github.com/P219-C/G2-project-2_ETL_UWADA/blob/Oksana/ERD/QuickDBD-export.png)

# Data Dictionary
Below are the data definitions for the following tables:

<b>`Songs`</b>
|Column name| Definition | 
|-|-|
|song_ranking|The ranking of the song| 
|song_title| The name of the song |
|artist_name| The name of the artist |
|artist_id| The unique id for each artist|
|album_name| The name of the album |
|duration| The duration of the song |
|song_release_date| The date song was released dd-mm-yyyy|

<b>`Artist`</b>
|Column name| Definition | 
|-|-|
|artist_id| The unique id of the artist |
|artist_name| The name of the artist|
|artist_ranking| The ranking of the artist |
|gender| The gender of the artist |
|age| The age of artist|

<b>`Album`</b>
|Column name| Definition | 
|-|-|
|artist_name| The name of the artist |
|artist_id| The unique id for each artist|

<b>`Concert`</b>
|Column name| Definition | 
|-|-|
|artist_name| The name of the artist |
|venue| The place where the concert took place |
|location| The location where the concert took place |
|date| The date when the concert happened |
