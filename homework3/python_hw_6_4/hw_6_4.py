# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def add_item_to_dict(dictionary, key, value):
    dictionary.update({key: value})
    return dictionary

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)





