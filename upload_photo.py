from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import autoit


mobile_emulation = { "deviceName": "Pixel 2" }
opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome('Path/to/chromedriver.exe', options = opts) # change this line


driver.get('https://instagram.com')

username = 'your_insta_username'
password = 'your_insta_password'

image_path = r"Path\to\your\image" # example: r"C:\images\something.png"
caption = "Enter photo caption here"

error = 1
while error == 1:
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
        print('got next page')
        error = 0
    except:
        error = 1


print('trying login')
error = 1
while error == 1:
    try:
        print('Inputting information')
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input').send_keys(username)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/div/label/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button').click()
        
        print('Clicking Login button')
        error = 0
    except:
        error = 1


sleep(2)
print('Dismissing pop-up')
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
sleep(2)
print('Dismissing pop-up')
driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
sleep(2)
print('Clicking add button')
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()

sleep(1.5)
print('Openning File browser')
autoit.win_active("Open") 
sleep(2)
print('Typing image path')
autoit.control_send("Open","Edit1", image_path) 
sleep(1.5)
print('Submitting image')
autoit.control_send("Open","Edit1","{ENTER}")
sleep(2)

print('Going for next step')
next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

sleep(1.5)
print('Adding caption')
caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
caption_field.send_keys(caption)

print('Sharing image')
share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()


print('Done! Closing in 15 seconds...')
sleep(15)

driver.close()