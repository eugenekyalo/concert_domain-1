from band.band import Band
from venue.venue import Venue
from concert.concert import Concert

def main():
    # Example Band, Venue, and Concert IDs
    band_id = 1
    venue_id = 1
    concert_id = 1

    # Test Band Methods
    band = Band(band_id)
    print(band.concerts())
    print(band.venues())
    print(band.all_introductions())
    print(band.most_performances())

    # Test Venue Methods
    venue = Venue(venue_id)
    print(venue.concerts())
    print(venue.bands())
    print(venue.concert_on('2024-09-14'))
    print(venue.most_frequent_band())

    # Test Concert Methods
    concert = Concert(concert_id)
    print(concert.band())
    print(concert.venue())
    print(concert.hometown_show())
    print(concert.introduction())

if __name__ == "__main__":
    main()
