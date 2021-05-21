# GitHub Repository Automator

This script automates your task of creating repository.
  
In order to use this repository automator there are some things you need to do: 

## Installation

1. <img src="https://raw.githubusercontent.com/cmulay/python-projects/5e50774b529950d6f3c856ea2a4311a6a8884ddc/_repo_assets/fork.svg" width="15" height="15"> Fork this repository.

2. Clone the forked project to your local machine

    ```bash
    git clone https://www.github.com/<YOUR-USER-NAME>/python-projects.git
    ```

3. Go to the project directory
    
   ```bash
    cd python-projects
    cd GitHub Repo Automation
    ```
   Change the FireFox to your default browser 
   <br>Example: For Chrome it would be
   ```bash
   self.driver = webdriver.Chrome()
   ```
4. Run the project with sudo permissions:
   ```bash
   sudo python3 automate.py
   ```
5. If you get WebDriverException make sure that webdriver PATH is set. 
