import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaseLyricScrapper:
    def __init__(self, links_to_songs, result_file_path):
        self.driver = webdriver.Chrome()
        self.links = links_to_songs
        self.result_file_path = result_file_path

    def open_in_new_tab(self, link):
        self.driver.get(link)

    def close_tab(self):
        self.driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "w")

    def write_row_to_file(self, row):
        with open(self.result_file_path, "wb", newline="") as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow(row)

