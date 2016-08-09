num=0
all_data_list=[]
def add(x, y):
    global num, all_data_list
    num+=1
    result = ("%2d  %-20s\t%6f\n" % (num, x, y))
    data_list=[num, x, y]
    all_data_list.append(data_list)
    return result

def is_in_list(x):
    global all_data_list
    for i in range(len(all_data_list)):
        if all_data_list[i][0] == x:
            all_data_list.remove(all_data_list[i])
            return True
    return False

def save_file(x):
    global all_data_list
    for i in range(len(all_data_list)):
        tmp = ("%d %s %f\n" % (all_data_list[i][0], all_data_list[i][1], all_data_list[i][2]))
        x.write(tmp)

def open_file(x):
    global num, all_data_list
    all_data_list[:] = []
    num = 0
    while True:
        line = x.readline()
        if not line : 
            return all_data_list
            break
        tmp = line.split()
        name = ''
        for i in range(1, len(tmp) - 1):
            if i != len(tmp) - 2 :
                name = name + tmp[i] + ' '
            else:
                name += tmp[i]
        all_data_list.append([int(tmp[0]), name, float(tmp[-1])])
        num += 1

def sort_by_num():
    global all_data_list
    all_data_list.sort()
    return all_data_list

def swap_data(l, idx):
    for i in range(len(l)):
        tmp = l[i][0]
        l[i][0] = l[i][idx]
        l[i][idx] = tmp

def sort_by_name():
    global all_data_list
    swap_data(all_data_list, 1)
    all_data_list.sort()
    swap_data(all_data_list, 1)
    return all_data_list

def sort_by_reverse_score():
    global all_data_list
    swap_data(all_data_list, 2)
    all_data_list.sort(reverse = True)
    swap_data(all_data_list, 2)
    return all_data_list

def sort_by_score():
    global all_data_list
    swap_data(all_data_list, 2)
    all_data_list.sort()
    swap_data(all_data_list, 2)
    return all_data_list
