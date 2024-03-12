class User:
    first_name = str
    last_name = str
    email = str
    mobile = str
    address = str

    def __init__(self, first_name,last_name,email,mobile,address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.address = address


user1 = User('Maxim','Shibaev','test@test.ru','1234567890','3-я Брянская улица, 22, деревня Образцово, Орловский муниципальный округ')


