import json


class StoreLink:
    def __init__(self):
        self.data: dict = {}

    def getData(self):
        # Open json file in read-only mode
        with open("Data.json", "r") as f:
            self.data = json.load(f)
        return self.data

    def updateData(self):
        # Open json file in write mode, To update any data that has changed
        with open("Data.json", "w") as f:
            json.dump(self.data, f, indent=4)


if __name__ == '__main__':
    link = StoreLink()
    link.getData()
