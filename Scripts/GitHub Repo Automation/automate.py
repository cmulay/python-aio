import random
from time import sleep
from selenium import webdriver
from stdiomask import getpass
from repo_names import names

print('GitHub Repository Automator')
print('Instructions:\n'
      '- This python script creates a new public repository for you.')

username = input('Username: ')
password = getpass(prompt='Password: ')
names = random.choice(names)
print(f'Great repository names are short and memorable. Need inspiration? How about{names}')
repoName = input('Repository Name: ')


class NewRepo:
    def __init__(self, username, password, repoName):
        self.username = username
        self.password = password
        self.repoName = repoName

        self.driver = webdriver.Firefox()

        self.driver.get("https://github.com/login")

        # Logs into your GitHub Account
        self.driver.find_element_by_id("login_field").send_keys(self.username)
        sleep(2)
        self.driver.find_element_by_id("password").send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]").click()
        sleep(2)

        # Creates a new github repository
        self.driver.find_element_by_xpath("//*[@id='repos-container']/h2/a").click()
        sleep(2)
        self.driver.find_element_by_id("repository_name").send_keys(self.repoName)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button").click()
        sleep(2)


NewRepo(username, password, repoName)
