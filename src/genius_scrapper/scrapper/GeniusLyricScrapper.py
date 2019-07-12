from src.BaseLyricScrapper.BaseLyricScrapper import BaseLyricScrapper


class GeniusLyricScrapper(BaseLyricScrapper):
    def __init__(self, links_to_songs, result_file_path):
        BaseLyricScrapper.__init__(self, links_to_songs, result_file_path)

    def call(self):
        for i in range(0, 5):
            self.open_in_new_tab(self.links[i])
