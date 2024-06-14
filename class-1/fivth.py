class UsernameError(Exception):

    def __init__(self, message, error):
        super().__init__(message)
        self.message = message
        self.error = error

    def getMesssage(self):
        return self.message + ' \'' + self.error  + '\''

class PasswordError(Exception):

    def __init__(self, message, error):
        super().__init__(message)
        self.message = message
        self.error = error

    def getMesssage(self):
        return self.message + ' \'' + ('*' * len(self.error))  + '\''

# โปรแกรมเริ่มการทำงาน
try:
    print('Login')
    username = input('Username: ')
    password = input('Password: ')

    if (username != 'mateo'):
        raise UsernameError('Invalid username', username)

    if (password != '1234'):
        raise PasswordError('Invalid password', password)

    print('Login success')

except UsernameError as e:
    print('Exception: ', e.getMesssage())

except PasswordError as e:
    print('Exception: ', e.getMesssage())