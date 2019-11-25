import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedinBot:
    def __init__(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        self.username = username
        self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self, username, password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def post(self, text):
        """ Make a text post """
        self.driver.find_element_by_class_name('share-box__open').click()
        self.driver.find_element_by_class_name('mentions-texteditor__content').send_keys(text)
        self.driver.find_element_by_class_name('share-actions__primary-action').click()
    
    def search(self, text, connect=False):
        """ Search execeuted from home screen """
        self._nav(self.feed_url)

        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        
        # Waiting for search results to load
        time.sleep(3)

        if connect:
            self._search_connect()

    def _search_connect(self):
        """ Called after search method to send connections to all on page """

        connect = self.driver.find_element_by_class_name('search-result__action-button')
        connect.click()
        time.sleep(2)
        self.driver.find_element_by_class_name('ml1').click()


if __name__ == '__main__':

    username = ''
    password = ''
    post_text = ''
    search_text = ''

    bot = LinkedinBot(username, password)
    bot.login(username, password)
    bot.post(post_text)
    bot.search(search_text, connect=True)