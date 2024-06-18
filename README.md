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

- **GET /concerts**: Retrieve a list of all concerts.
- **GET /concerts/\<id\>**: Retrieve details of a specific concert.
- **POST /concerts**: Add a new concert.
- **PUT /concerts/\<id\>**: Update a concert.
- **DELETE /concerts/\<id\>**: Delete a concert.

### Setlists

- **GET /concerts/\<id\>/setlist**: Retrieve the setlist of a specific concert.

### Band Composition

- **GET /concerts/\<id\>/band**: Retrieve the band composition for a specific concert.

### Recordings

- **GET /concerts/\<id\>/recordings**: Retrieve recordings of a specific concert.


## Database Schema

![Database Schema](./diagram.svg)
