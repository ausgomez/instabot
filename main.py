import instagram_bot as bot

# 👇 👇 👇 YOUR ACTIONS START HERE 👇 👇 👇


def main():
    # call the login function passing username and password as parameters
    # you must call this one first
    bot.login('your_insta_username', 'your_insta_password$')

    # UNCOMMENT ANY FUNCTION THAT YOU WOULD LIKE TO USE

    # bot.downloadPhotosByHashtag('starwars', 5)
    # bot.uploadLocalPhotoWithCaption(r"images_to_upload\instabot.png", 'Enter photo caption here 😀 #somehastag')


if __name__ == "__main__":
    main()
