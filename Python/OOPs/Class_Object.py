class user:
    def __init__(self,id,mobile_type,location=None):
        self.id=id
        self.mobile_type=mobile_type
        self.location=location

    def sign_ups(self):
        pass

u1=user(1,'Android/Samsung','Bengaluru')
print(u1.__dict__)