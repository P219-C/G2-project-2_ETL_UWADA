# G2-project-2_ETL_UWADA
Group 2 - ETL project

## Purpose and motivation
The following ETL (Extract, Transform, Load) exercise creates a database with information of the top 100 songs (*The Hot 100*) from *The Billboard* (https://www.billboard.com/charts/hot-100/).


## Solution

### Solution architecture
### Extract:
#### Data sources
- *The Hot 100* - **Web Scraping** - https://www.billboard.com/charts/hot-100/

### Transform
#### Transformation scripts
#### Job schedule (screenshot)
### Load
#### Entity Relationship Diagram
![ERD](https://github.com/P219-C/G2-project-2_ETL_UWADA/blob/Oksana/ERD/QuickDBD-export%20(1).png)

#### Data dictionary
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

## Usage

### Python requirements / dependencies
### How to run the code locally
### How to run unit tests
### How to schedule jobs
