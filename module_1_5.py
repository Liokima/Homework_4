immutable_var = tuple([1, 2 , 3, 'a', 'b'])
print(immutable_var)
#immutable_var.append(True) - AttributeError: 'tuple' object has no attribute 'append' - Отнош к list

#Изменение данных внутри кортежа возможно в случае использования его без присвоения
tuple_ = ([4,5,40], 'a','b')
tuple_[0][1] = 1
print(tuple_)
#Изменение данных внутри кортежа возможно в случае использования его без присвоения

immutable_list = ['apple' , 4 , 5 , True]
print(immutable_list)
immutable_list[0] = 'banana'
print(immutable_list)
immutable_list.remove(4)
immutable_list.remove(5)
immutable_list.extend(['apple','string'])
print(immutable_list)