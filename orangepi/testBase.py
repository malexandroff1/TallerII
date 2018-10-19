import database
import  models
import time

if __name__ == "__main__":
    user = models.User()
    user.username = 'Pepe'
    user.password = 'alberto roman'
    db = database.Database()
    #db.insert_user(user)
    db.update_password(user)
