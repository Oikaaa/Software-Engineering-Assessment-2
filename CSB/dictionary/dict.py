# x = {} or x = dict() is dictionary; x = {'a', 'b', 'c'} is a set
phone_book = {}
phone_book['Mico'] = '0406821659'
phone_book['Jul'] = '0408572678'
phone_book['Ba'] = '9276090610'

phone_book.get('Ba')
del phone_book['Mico']

print(phone_book)