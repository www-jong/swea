number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people+=1

def create_user(name,age,address):
    increase_user()
    tmp_data={}
    tmp_data['name']=name
    tmp_data['age']=age
    tmp_data['address']=address
    print(f'{name}님 환영합니다!')
    return tmp_data

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user=list(map(create_user,name,age,address))


def rental_book(info):
    pass
