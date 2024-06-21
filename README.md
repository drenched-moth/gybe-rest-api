# Godspeed You! Black Emperor Concerts API

## Overview
This project is a REST API implemented with Python-Flask, designed to manage and provide data related to live concerts of the rock band Godspeed You! Black Emperor. The API offers detailed information on setlists, band compositions, and recordings of each performance.

## Features

- **Retrieve setlists** for each performance
- **Get details** on band compositions for each show
- **Access recordings** and related metadata
- **API endpoints** for bots and frontend developers
- **User-friendly interface** for data maintenance


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8+
- MySQL

### Setup

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/godspeed-you-black-emperor-api.git
    cd godspeed-you-black-emperor-api
    ```

2. Create and activate a virtual environment using `pipenv`:

    ```
    pipenv install
    pipenv shell
    ```

3. Configure the database:

    Create a MySQL database and update the configuration in `config.py`:

    ```python
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
    ```

4. Initialize the database:

    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:

    ```
    flask run
    ```

## API Endpoints

### Concerts

- **Get all concerts**
  - `GET /concerts`
  - Query Parameters:
    - `date` (string, date): Specific date of the concert (YYYY-MM-DD)
    - `year` (integer): Year of the concerts
    - `beforeYear` (integer): Concerts before specified year
    - `afterYear` (integer): Concerts after specified year
    - `venue` (string): Venue of the concerts
    - `city` (string): City of the concerts
    - `state` (string): State of the concerts
    - `country` (string): Country of the concerts

- **Create a new concert**
  - `POST /concerts`
  - Request Body: New concert object

- **Get a specific concert**
  - `GET /concerts/{concert_id}`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

- **Update an existing concert**
  - `PUT /concerts/{concert_id}`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert
  - Request Body: Updated concert object

- **Delete an existing concert**
  - `DELETE /concerts/{concert_id}`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

### Songs

- **Get all songs**
  - `GET /songs`
  - Query Parameter:
    - `matches` (string): Aliases of the song name

- **Create a new song**
  - `POST /songs`
  - Request Body: New song object

- **Get a specific song**
  - `GET /songs/{song_id}`
  - Path Parameter:
    - `song_id` (integer): ID of the song

- **Add aliases to a specific song**
  - `POST /songs/{song_id}`
  - Path Parameter:
    - `song_id` (integer): ID of the song
  - Request Body: New aliases object

- **Delete an existing song**
  - `DELETE /songs/{song_id}`
  - Path Parameter:
    - `song_id` (integer): ID of the song

### Members

- **Get all members**
  - `GET /members`

- **Add a new member**
  - `POST /members`
  - Request Body: New member object

- **Update an existing member**
  - `PUT /members/{member_id}`
  - Path Parameter:
    - `member_id` (integer): ID of the member
  - Request Body: Updated member object

- **Delete an existing member**
  - `DELETE /members/{member_id}`
  - Path Parameter:
    - `member_id` (integer): ID of the member

### Recordings

- **Get all recordings**
  - `GET /recordings`
  - Query Parameters:
    - `date` (string, date): Specific date of the recording (YYYY-MM-DD)
    - `year` (integer): Year of the recordings
    - `beforeYear` (integer): Recordings before specified year
    - `afterYear` (integer): Recordings after specified year
    - `venue` (string): Venue of the recordings
    - `city` (string): City of the recordings
    - `state` (string): State of the recordings
    - `country` (string): Country of the recordings

- **Get a specific recording**
  - `GET /recordings/{recording_id}`
  - Path Parameter:
    - `recording_id` (integer): ID of the recording

- **Update an existing recording**
  - `PUT /recordings/{recording_id}`
  - Path Parameter:
    - `recording_id` (integer): ID of the recording
  - Request Body: Updated recording object

- **Delete an existing recording**
  - `DELETE /recordings/{recording_id}`
  - Path Parameter:
    - `recording_id` (integer): ID of the recording

- **Get recordings of a specific concert**
  - `GET /concerts/{concert_id}/recordings`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

- **Create a recording for a concert**
  - `POST /concerts/{concert_id}/recordings`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert
  - Request Body: New recording object

### Band Compositions

- **Get the band composition at a specific concert**
  - `GET /concerts/{concert_id}/members`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

- **Create the band composition for a concert**
  - `POST /concerts/{concert_id}/members`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert
  - Request Body: Band composition object

- **Delete an existing band composition**
  - `DELETE /concerts/{concert_id}/members`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

### Setlists

- **Get played songs at a specific concert**
  - `GET /concerts/{concert_id}/songs`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

- **Create a setlist for a concert**
  - `POST /concerts/{concert_id}/songs`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert
  - Request Body: Setlist object

- **Update a setlist for a concert**
  - `PUT /concerts/{concert_id}/songs`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert
  - Request Body: Updated setlist object

- **Delete an existing setlist**
  - `DELETE /concerts/{concert_id}/songs`
  - Path Parameter:
    - `concert_id` (integer): ID of the concert

### Recordings by Song

- **Get recordings where a specified song can be heard**
  - `GET /songs/{song_id}/recordings`
  - Path Parameter:
    - `song_id` (integer): ID of the song

## Database Schema

![Database Schema](./diagram.svg)
