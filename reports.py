def count_games(file_name):
    with open(file_name, 'r') as f:
        data= f.readlines()
        return len(data)


def decide(file_name, year):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    for i in range(len(data)):
        a_list.append(data[i].split('\t'))
        if str(year) in a_list[i]:
            return True
    return False


def get_latest(file_name):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    for i in range(len(data)):
        a_list.append(data[i].split('\t'))
        if i==0:
            year=a_list[i][2]
            j=i
            continue
        if int(a_list[i][2]) > int(year):
            year = a_list[i][2]
            j=i
    return a_list[j][0]


def count_by_genre(file_name, genre):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    j=0
    for i in range(len(data)):
        a_list.append(data[i].split('\t'))
        if a_list[i][3] == genre:
            j += 1
    return j


def get_line_number_by_title(file_name, title):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    for i in range(len(data)):
        a_list.append(data[i].split('\t'))
        if a_list[i][0] == title:
            return i+1
    raise ValueError


def sort_abc(file_name):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    for i in range(len(data)):
        a_list.append(data[i].split('\t',1))
        del a_list[i][1]
        a_list[i]=a_list[i][0]
    for i in range(len(a_list)):
        for j in range(len(a_list)-1):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


def get_genres(file_name):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    genres=[]
    for i in range(len(data)):
        a_list.append(data[i].split('\t',4))
        if a_list[i][3] not in genres:
            genres.append(a_list[i][3])
    for i in range(len(genres)):
        for j in range(len(genres)-1):
            if genres[j] > genres[j+1]:
                genres[j],genres[j+1] = genres[j+1], genres[j]
    return genres


def when_was_top_sold_fps(file_name):
    with open(file_name, 'r') as f:
        data=f.readlines()
    a_list=[]
    year=0
    rating =0 
    for i in range(len(data)):
        a_list.append(data[i].split('\t'))
        if a_list[i][3]=='First-person shooter' and float(a_list[i][1]) > rating:
            rating = float(a_list[i][1])
            year = int(a_list[i][2])
    if year ==0 or rating ==0:
        raise ValueError
    else:
        return year
