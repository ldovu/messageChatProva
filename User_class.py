# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:47:17 2022

@author: ludov
"""

class User: 
    def __init__(self, userID, password, admin):
        self.userID = userID
        self.password = password
        self.admin = admin


class NormalUser(User):
    def __init__(self, userID, password, admin):
        self.userID = userID
        self.password = password
        self.admin = False
    
class Admin(User):
    def __init__(self, userID, password, admin):
        self.userID = userID
        self.password = password
        self.admin = True
                 
    #def deleteMessage():
        #function

class Message:
    def __init__(self, user, time, text):
        self.user = User()
        self.time = time
        self.text = text
        
