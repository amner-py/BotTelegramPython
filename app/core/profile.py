class Profile():
    def __init__(self):
        self.ID = ''
        self.NAME = ''
        self.ADDRESS = ''

    def set_id(self,id):
        self.ID = id

    def set_name(self,name):
        self.NAME = name

    def set_address(self,address):
        self.ADDRESS = address

    def get_id(self):
        return self.ID

    def get_name(self):
        return self.NAME

    def get_address(self):
        return self.ADDRESS