from src.BaseLyricScrapper.BaseLyricScrapper import BaseLyricScrapper
from selenium.common.exceptions import NoSuchElementException


class GeniusLyricScrapper(BaseLyricScrapper):
    def __init__(self, links_to_songs, result_file_path):
        BaseLyricScrapper.__init__(self, links_to_songs, result_file_path)
        self.row = []  # Author,Title,Lyrics,Album,Views

    def __get_author(self):
        author = self.driver.find_element_by_xpath("//a[contains(@class, 'primary_artist')]").text
        self.row.append(author)

    def __get_title(self):
        title = self.driver.find_element_by_tag_name("h1").text
        self.row.append(title)

    def __get_lyrics(self):
        lyrics = self.driver.find_element_by_xpath("//div[@class='lyrics']/section/p").text
        self.row.append(lyrics)

    def __get_album(self):
        try:
            album = self.driver.find_element_by_xpath("//a[@ng-bind='album.name']").text
        except NoSuchElementException:
            album = "NA"
        self.row.append(album)

    def __get_views(self):
        views = self.driver.find_element_by_xpath("//div[@ng-if='song.stats.pageviews']/span").text
        self.row.append(views)

    def call(self):
        for song_link in self.links:
            self.open_in_new_tab(song_link)
            self.__get_author()
            self.__get_title()
            self.__get_lyrics()
            self.__get_album()
            self.__get_views()
            self.write_row_to_file(self.row)
            self.row = []

        self.driver.implicitly_wait(1000)
        self.driver.close()
