from data import StoreLink
import webbrowser as wb


class BrowseLink:
    def __init__(self, product_name, data):
        self.product_name: str = product_name
        self.data: dict = data

    def beginSearch(self):
        for store in self.data["Stores"]:
            if store["search"]:
                wb.open(store["link"].format(self.product_name))


if __name__ == '__main__':
    link = StoreLink()
    BrowseLink("pico", link.getData()).beginSearch()
