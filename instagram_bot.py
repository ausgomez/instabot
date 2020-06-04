from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import wget
import autoit


print('🔵 🔵 Welcome to 📷 Instagram Bot by Anstroy 🤖 🔵 🔵')
print('🔵         Made only for reseach purposes            🔵 \n')

print('🌐 Starting Chrome driver 🌐')
mobile_emulation = {"deviceName": "Pixel 2"}
opts = webdriver.ChromeOptions()
opts.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(
    'Path/to/chromedriver.ex', options=opts)  # change this line


def login(username, password):
    print('🧍🧍🧍🧍🧍 LOGGING YOU IN 🧍🧍🧍🧍🧍🧍')
    goToMainPage()

    error = 1
    while error == 1:
        try:
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
            print('Skipping first page')
            error = 0
        except:
            print('something went wrong!')
            error = 1

    print('Inputting your credentials 🔐')
    error = 1
    while error == 1:
        try:
            print('Inputting information')
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input').send_keys(username)
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/div/label/input').send_keys(password)
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button').click()

            print('Clicking Login button')
            error = 0
        except:
            error = 1
    dismissPopup()


def downloadPhotosByHashtag(hashtag, limit):
    print('#️⃣ #️⃣ #️⃣ Opening Hashtag page #️⃣ #️⃣ #️⃣')
    driver.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(2)

    error = 0
    count = 1
    x = 1
    y = 1

    print('📷 📷 Downloading ' + limit + ' from list 📷 📷')
    image = None

    # scroll down
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")

    while error != 1:
        image_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[' + \
            str(x) + ']/div[' + str(y) + ']/a/div/div[1]/img'
        try:
            image = driver.find_element_by_xpath(image_xpath)
        except:
            print('😥 Image not found on path')
            print('Exit')
            error = 1

        image_url = image.get_attribute("src")

        print('🔨 Saving image #' + str(count) + ' on 📁 /images')
        local_image_filename = wget.download(
            image_url, out='images\image' + str(count) + '.jpg')

        # It will go through each row and get each image to be downloaded
        if y >= 3:
            y = 1
            x = x + 1
        else:
            y = y + 1

        if count % 10 == 0:
            print('scrolling to bottom 👇')
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

        count = count + 1

        if count > limit:
            error = 1


def uploadLocalPhotoWithCaption(path_to_photo, caption):
    # example: path_to_photo = r"C:\images\something.png"
    print('⬆️ ⬆️ Uploading Local Photo ⬆️ ⬆️ ⬆️')
    goToMainPage()
    dismissPopup()

    print('Clicking add button')
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()

    sleep(1.5)
    print('Openning File browser')
    autoit.win_active("Open")
    sleep(2)
    print('Typing image path')
    autoit.control_send("Open", "Edit1", path_to_photo)
    sleep(1.5)
    print('Submitting image')
    autoit.control_send("Open", "Edit1", "{ENTER}")
    sleep(2)

    print('Going for next step')
    next_btn = driver.find_element_by_xpath(
        "//button[contains(text(),'Next')]").click()

    sleep(1.5)
    print('Adding caption')
    caption_field = driver.find_element_by_xpath(
        "//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)

    print('Sharing image')
    share_btn = driver.find_element_by_xpath(
        "//button[contains(text(),'Share')]").click()


def closeDriver():
    print('👋 👋 Closing Driver in 5 seconds 👋 👋')
    sleep(5)
    driver.close


def dismissPopup():
    # this function only takes care of those anoying popups
    sleep(1)
    try:
        print('❌ Dismissing pop-up')
        driver.find_element_by_xpath(
            "//button[contains(text(),'Cancel')]").click()
    except:
        print('no pop-up to dismiss...')

    try:
        print('❌ Dismissing notifications pop-up')
        driver.find_element_by_xpath(
            "//button[contains(text(),'Not Now')]").click()
    except:
        print('no notifications pop-up to dismiss...')
    sleep(1)


def goToMainPage():
    print('🏠 Going to instagram.com')
    driver.get('https://instagram.com')
    sleep(2)


# 👇 👇 👇 YOUR ACTIONS START HERE 👇 👇 👇
def main():
    # call the login function passing username and password as parameters
    # you must call this one first
    login('your_insta_username', 'your_insta_password$')

    # UNCOMMENT ANY FUNCTION THAT YOU WOULD LIKE TO USE
    # downloadPhotosByHashtag('starwars', 5)
    # uploadLocalPhotoWithCaption(r"Path\to\your\image", 'Enter photo caption here 😀 #somehastag')


if __name__ == "__main__":
    main()
