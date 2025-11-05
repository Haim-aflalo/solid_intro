class SaveToFile:

    @staticmethod
    def save_txt(txt):
        with open("content.txt","a") as f:
            f.write(txt)
