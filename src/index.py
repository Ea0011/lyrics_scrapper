import sys
sys.path.append('/Users/edvardavagyan/Programming/GeniusMood/src')

import genius_scrapper.scrapper.index as scrapper

RESULTS_FILE_PATH = "lyrics_with_dates.csv"

scrapper.scrap(RESULTS_FILE_PATH)

