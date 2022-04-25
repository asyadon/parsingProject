class Phone:
    def __init__(self, name: str, price: str, url: str):
        self.name = name
        self.price = price
        self.url = url


class PhoneList:
    def __init__(self):
        self.phone_list = []

    def add(self, phone: Phone):
        self.phone_list.append(phone)
