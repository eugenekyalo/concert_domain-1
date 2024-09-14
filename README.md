Concert Domain Code Challenge

Overview

This repository contains the implementation of a Concert Domain as part of a code challenge. The challenge involves creating and managing a Concert domain with a focus on relational data handling using raw SQL queries. The project is designed to test your understanding of database operations and object-oriented programming in Python.

Project Structure

The project is organized into several Python modules, each handling different aspects of the Concert Domain. 
The directory structure is as follows:

bash
Copy code
concert_domain/
├── .env                   # Environment variables for database configuration
├── main.py                # Entry point for running tests
├── concert/               # Module for Concert-related operations
│   ├── __init__.py        # Initialization for the Concert module
│   └── concert.py         # Contains methods for the Concert class
├── band/                  # Module for Band-related operations
│   ├── __init__.py        # Initialization for the Band module
│   └── band.py            # Contains methods for the Band class
└── venue/                 # Module for Venue-related operations
    ├── __init__.py        # Initialization for the Venue module
    └── venue.py           # Contains methods for the Venue class

Setup

1. Install Dependencies

Ensure you have a virtual environment set up. Install the necessary dependencies using:

bash
Copy code
pip install -r requirements.txt

2. Configure Environment Variables

Create a .env file in the root directory with the following content:

DB_HOST=your_database_host
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password

3. Database Setup

Ensure your PostgreSQL database is configured with the following tables:

bands: name (String), hometown (String)
venues: title (String), city (String)

concerts: band_id (Integer), venue_id (Integer), date (String)
Use raw SQL queries to set up and migrate the database schema.

Methods

Concert Class

band(): Fetches the band associated with the concert.
venue(): Fetches the venue associated with the concert.
hometown_show(): Checks if the concert is in the band's hometown.
introduction(): Generates a string introduction for the concert.

Venue Class

concerts(): Fetches all concerts held at the venue.
bands(): Fetches all bands that have performed at the venue.
concert_on(date): Finds the first concert on a specific date at the venue.
most_frequent_band(): Identifies the band that has performed the most at the venue.

Band Class

concerts(): Fetches all concerts the band has played.
venues(): Fetches all venues where the band has performed.
play_in_venue(venue, date): Creates a new concert for the band at a specific venue on a given date.
all_introductions(): Returns all introductions for the band.
most_performances(): Finds the band with the most concerts.

Testing

To test the implemented methods, use the main.py script. This script calls various methods and prints their outputs for verification.

bash
python3 main.py
Notes
Ensure that your database connection details are correctly set in the .env file.
The project uses raw SQL queries exclusively and does not utilize SQLAlchemy or other ORM tools.
The code is structured to handle the specified operations with appropriate error handling and data retrieval.

License

This project is licensed under the MIT License - see the LICENSE file for details.

