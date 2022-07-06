class Users():
    _class = 'Users'
    
    def __init__(self, login, passcode):
        self.login = login
        self.passcode = passcode
    
    def access(self, access_level):
        return f'Access: {access_level}'
 
siobency = Users('siobency', '2341234')
shelly = Users('shelly', '6456213132')
wildizer = Users('wildizer', '2341234')

for i in (siobency, shelly, wildizer):
    print(f'{i._class}, {i.login}, {i.passcode}, {i.access("Restricted.")}')
 


class Admins(Users):
    _class = 'Admins'
    
    def access(self, access_level = 'Full.'):
        return super().access(access_level)

thunder4 = Admins('thunder4', 4654651313)
print(f'{thunder4._class}, {thunder4.login}, {thunder4.passcode}, {thunder4.access()}')