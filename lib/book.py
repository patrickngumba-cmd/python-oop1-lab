class Book:
    def __init__(self, title, page_count):
        self.title = title
        # Setting this here automatically runs it through our validation below!
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # The prompt wants us to make sure they typed an actual number
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")