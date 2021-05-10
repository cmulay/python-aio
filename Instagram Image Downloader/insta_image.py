import instaloader

print('Instagram Profile Picture Downloader')


class ImageDownloader:
    def __init__(self, user_name):
        self.username = user_name

    def __repr__(self):
        try:
            self.get_pp(self.username)
            return f"\nProfile picture of user with username\"{self.username}\" has been downloaded successfully.\n"
        except:
            return f"\nUser \"{self.username}\" does not exist.\n"

    @staticmethod
    def get_pp(user):
        session = instaloader.Instaloader()
        session.download_profile(user, profile_pic_only=True)
        return 0


if __name__ == "__main__":
    username = input("Enter username: ")
    print(ImageDownloader(username))
