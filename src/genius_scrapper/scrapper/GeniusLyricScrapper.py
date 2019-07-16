from src.BaseLyricScrapper.BaseLyricScrapper import BaseLyricScrapper
from selenium.common.exceptions import NoSuchElementException

SCROLL_PAUSE_TIME = 0.5


class GeniusLyricScrapper(BaseLyricScrapper):
    def __init__(self, links_to_songs, result_file_path):
        BaseLyricScrapper.__init__(self, links_to_songs, result_file_path)
        self.row = []  # Author,Title,Lyrics,Album,Views,Release.Date

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

    def __get_date(self):
        self.__scroll_to_bottom()
        date = self.driver.find_element_by_xpath("//div[@ng-if='date_components']/span[2]").text
        self.row.append(date)

    def __scroll_to_bottom(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.implicitly_wait(SCROLL_PAUSE_TIME)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def call(self):
        for song_link in self.links:
            self.open_in_new_tab(song_link)
            self.__get_author()
            self.__get_title()
            self.__get_lyrics()
            self.__get_album()
            self.__get_views()
            self.__get_date()
            self.write_row_to_file(self.row)
            self.row = []

        self.driver.implicitly_wait(1000)
        self.driver.close()
