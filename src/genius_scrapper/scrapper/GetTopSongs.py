from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from ..scrapper.GeniusLyricScrapper import GeniusLyricScrapper


class GetTopSongs:
    def __init__(self, base_url, result_file_path):
        self.url = base_url + "#top-songs"
        self.__driver = webdriver.Chrome()
        self.__result_file_path = result_file_path
        self.__top_songs = []

    def __visit_genius(self):
        self.__driver.get(self.url)

    def __filter_songs(self):
        drop_box = self.__driver.find_element_by_xpath("//span[contains(text(), 'Songs')]/../..")
        drop_box.click()
        self.__driver.implicitly_wait(30)
        all_time_filter = self.__driver.find_element_by_xpath("//div[contains(text(), 'All Time')]")
        all_time_filter.click()

    def __expand_list(self):
        while True:
            try:
                load_more_btn = self.__driver.find_element_by_xpath(
                    "//div[contains(@class, 'Charts__LoadMore')]/div[1]"
                )
                load_more_btn.click()
            except NoSuchElementException:
                break

    def __collect_top_songs(self):
        top_songs_container = self.__driver.find_element_by_id("top-songs")
        top_songs_links = top_songs_container.find_elements_by_xpath(".//a")
        for link in top_songs_links:
            self.__top_songs.append(link.get_attribute("href"))

    def call(self):
        self.__visit_genius()
        self.__filter_songs()
        self.__expand_list()
        self.__collect_top_songs()
        GeniusLyricScrapper(self.__top_songs, self.__result_file_path).call()
        self.__driver.implicitly_wait(3000)
        self.__driver.close()

