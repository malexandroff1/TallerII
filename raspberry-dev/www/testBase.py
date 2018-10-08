import database
import  models
import time

if __name__ == "__main__":
    user = models.User()
    user.username = 'admin'
    user.password = 'admin'
    db = database.Database()
    #db.insert_user(user)
    #db.update_password(user)
    pin = models.Pin()
    pin.pin = 1
    #db.get_pin(pin)
    #print(pin)
    pins = db.get_all_pin()
    print(pins)
