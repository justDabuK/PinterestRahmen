from selenium import webdriver
from pinterest_scraper import scraper as s
import sys


def grab(user, password, pin_board_url="https://www.pinterest.de/kevinjust87/art/"):
    chrome = webdriver.Chrome()
    ph = s.Pinterest_Helper(user, password, chrome)
    images = ph.runme(pin_board_url)
    image_str = []

    for image in images:
        image_str.append(image.decode("utf-8"))
    s.download(image_str, "./download")


if __name__ == "__main__":
    grab(sys.argv[1], sys.argv[2])
