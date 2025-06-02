from loguru import logger

class Labour:
    def __init__(self,first_name,last_name,wage):
        self.first_name=first_name
        self.last_name=last_name
        self.wage=wage
# if we add prefix __variable it will become private

    def save_to_db(self):
        query = "SELECT id from labours where lower(first_name)= %s AND lower(last_name) = %s"
        result = self.crud.read_from_mysql(query,(self.first_name,self.last_name))

        if result: #if labour already exists, return existing ID
                logger.info(f"Labour already existes with ID: {result[0][0]}")
                return result[0][0]

    def login(self):
        pass


l1=Labour("Mohan","Kumar",500)
l1=Labour("Rajesh","Sing",600)