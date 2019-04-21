#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime


def execSearch(browser: webdriver):
    """
    Googleで検索を実行する
    :param browser: webdriver
    """

    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    # get request
    browser.get("http://www.python.org")

    # check words int title
    assert "Python" in browser.title

    # select input elem
    elem = browser.find_element_by_name("q")
    # send key
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    # exists results?
    assert "No results found." not in browser.page_source

    # brower close (quit: close one tab)
    browser.close()


if __name__ == '__main__':
    # ex1
    try:
        # browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        # browser = webdriver.Chrome()   # 普通のChromeを制御する場合

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # Googleで検索実行
        execSearch(browser)

    finally:
        # 終了
        browser.close()
        browser.quit()
