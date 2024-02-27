data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
def process_data(data, key_list):
    for i in data:
        for key in key_list:
            if key not in i:
                i[key] = 'unkwnow'


    for i in data:
        for key, value in i.items():
            print(f'{key}은/는{value}입니다')

process_data(data, key_list)





    


            
            



















