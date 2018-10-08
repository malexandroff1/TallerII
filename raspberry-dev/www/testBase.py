import database
import  models
import time

if __name__ == "__main__":
    user = models.User()
    user.username = 'admin'
    user.password = 'admin1'
    db = database.Database()
    #db.insert_user(user)
    #db.update_password(user)
    pin = models.Pin()
    pin.pin = 2
    pin.state = "ON"
    pin.ty = "GPIO"
    #db.get_pin(pin)
    #print(pin)
    db.update_pin(pin)
    
