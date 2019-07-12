import csv
from genius_scrapper.scrapper.GetTopSongs import GetTopSongs

HEADER = ["Author", "Title", "Lyrics", "Album", "Views"]
BASE_URL = "https://genius.com/"


def scrap(result_file_path):
    scrapped_lyrics = open(result_file_path, 'w')

    with scrapped_lyrics:
        writer = csv.writer(scrapped_lyrics)
        writer.writerow(HEADER)

    GetTopSongs(BASE_URL).call()
