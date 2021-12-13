# G2-project-2_ETL_UWADA
Group 2 - ETL project

## Objective
The objective is to perform the ETL (Extract-Transform-Load) process by reading the dataset of *The Billboard*, *The Spotify*, cleaning the dataset in the desired form and loading into a database for storage.

## Data Sources
- *The Hot 100* - **Web Scraping** - https://www.billboard.com/charts/hot-100/
- *The Artist 100* - **Web Scraping** - https://www.billboard.com/charts/artist-100/
- *The Spotify* - **Web Scraping** - https://www.spotify.com

## Solution

**We have performed ETL in three steps**:

**_Extraction_**: 
The data was web scraped from a public platforms *The Billboard*, *The Spotify* and formatted as .cvs files.

**_Transformation_**: 
?? Python has been used as the tool for transformation of datasets using the Pandas Library.

**_Loading_**: 
Relational database PostgressSQL has been used to load the data.

## ERD and Data Dictionary

### Entity Relationship Diagram
![ERD](https://github.com/P219-C/G2-project-2_ETL_UWADA/blob/Oksana/ERD/QuickDBD-export%20(3).png)

The ERD diagram was created using: https://app.quickdatabasediagrams.com/#/

### Data dictionary
<b>`Songs`</b>
|Column name| Definition | 
|-|-|
|song_ID|The unique id for each song| 
|song_title| The name of the song |
|album_name| The name of the album |
|track_spotify_ID| The unique track id|
|artist_spotify_ID| The unique id for each artist|
|song_ranking| The ranking of the song|
|spotify_popularity| The popularity of te song on Spotify |
|album_name| The name of the album ||song_duration| The duration of the song |
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
|album_type| The type of the album |

<b>`Concert`</b>
|Column name| Definition | 
|-|-|
|artist_spotify_ID| The unique id for each artist |
|api_artist| The api of the artist |
|venue| The place where the concert took place |
|country| The country where the concert took place |
|location| The location where the concert took place |
|date| The date when the concert happened |

## Usage

### Python requirements / dependencies
### How to run the code locally
### How to run unit tests
### How to schedule jobs
