# G2-project-2_ETL_UWADA
Group 2 - ETL project

# Objective
The objective is to perform the ETL (Extract-Transform-Load) process by reading the dataset of Billboard, cleaning the dataset in the desired form and loading into a database for storage.

# Data Sources
- *The Hot 100* - **Web Scraping** - https://www.billboard.com/charts/hot-100/
- *The Artist 100* - **Web Scraping** - https://www.billboard.com/charts/artist-100/# Steps

## Purpose and motivation
The following ETL (Extract, Transform, Load) exercise creates a database with information of the top 100 songs (*The Hot 100*) from *The Billboard* (https://www.billboard.com/charts/hot-100/).

## Solution

### Solution architecture
### Extract:
#### Data sources
- *The Hot 100* - **Web Scraping** - https://www.billboard.com/charts/hot-100/

### Transform
In order to transform the public data and use it in our ETL project we performed the following:
- 
Used Pandas functions in Jupyter Notebook to load all three CSV files.
Reviewed the files and transformed into data frames
Removed the operator’s column and the address column due to missing information which was not relevant to the focus of this study.
Identified duplicates by doing an inner merge on the incident id column across all three data sets.
Created queries to address our hypothesis by grouping the data by state and getting the sum of the number of people killed and the number of people injured. We sorted the data in descending order so we could visually see which state had the highest numbers.#### Transformation scripts

### Load# 

Steps
We have performed ETL in three steps:

1. Extraction - the data has been downloaded from public platform and formatted as .csv files.

2. Transformation - python has been used as the tool for transformation of datasets using the Pandas Library.

- ??We used a Pandas functions in Jupyter Notebook to transform all CSV files, scraped data, and API request responses.
- ??We reviewed the files and transformed into a dataframes.
- ??We used a python transformation functions for data cleaning, joining, filtering, and aggregating.
- ??Several columns removed
- ??Duplicate rows was removed, and successfully managed.
- ??We conducted some aggregation to find totals for comparison in the datasets.

3. Loading - relational database PostgresSQL has been used to load the data.

# ERD and Data Dictionary
# Entity Relationship Diagram

![ERD](https://github.com/P219-C/G2-project-2_ETL_UWADA/blob/Oksana/ERD/QuickDBD-export%20(2).png)
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
|artist_name| The name of the artist|
|artist_spotify_ID| The unique id for each artist |

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
