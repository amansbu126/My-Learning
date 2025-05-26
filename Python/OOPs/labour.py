from loguru import logger

class Labour:
    def __init__(self,first_name,last_name,wage):
        self.first_name=first_name
        self.last_name=last_name
        self.wage=wage
# if we add prefix __variable it will become private
    def save_to_db(self,db_connection):
        pass

    def login(self):
        pass


l1=Labour("Mohan","Kumar",500)
l1=Labour("Rajesh","Sing",600)