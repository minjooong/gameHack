from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path='/Users/minjoong/code/geckodriver')

driver.get('https://24glo.com/game/dino-play.html')

play_button = driver.find_element(By.CSS_SELECTOR, 'body')

play_button.send_keys(Keys.SPACE)


while True:
    is_crashed = driver.execute_script('return window.Runner.instance_.crashed')
    
    if is_crashed:
        play_button.send_keys(Keys.SPACE)
    tRex = driver.execute_script('return window.Runner.instance_.tRex.xPos')
    obstacles = driver.execute_script('return window.Runner.instance_.horizon.obstacles')
    if obstacles:
        obstacle = driver.execute_script('return window.Runner.instance_.horizon.obstacles[0].xPos')
    else:
        obstacle = 600
    
    print(obstacle-tRex)
    if obstacle-tRex<55:
        ActionChains(driver).key_down(Keys.SPACE).pause(0.1).key_up(Keys.SPACE).perform()
    
