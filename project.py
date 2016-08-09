#-*- coding:utf-8 -*-

from tkinter import *
import project_functions
from project_sort_functions import sort_map, sort_list

window = Tk()
window.title("Student Score Management Program")

label_entry = Frame(window)
label_entry.grid(row=0, column=0, sticky=W)

Label(label_entry, text='이름: ').grid(row=0, column=0, sticky=E)
name = Entry(label_entry, width=25, bg='light green')
name.grid(row=0, column=1, sticky=W)

Label(label_entry, text='점수: ').grid(row=0, column=2, sticky=E)
score = Entry(label_entry, width=10, bg='light green')
score.grid(row=0, column=3, sticky=W)

Label(label_entry, text='번호: ').grid(row=1, column=2, sticky=E)
number = Entry(label_entry, width=8, bg='light green')
number.grid(row=1, column=3, sticky=W)

Label(label_entry, text='파일이름: ').grid(row=2, column=2, sticky=E)
file_save = Entry(label_entry, width=25, bg='light blue')
file_save.grid(row=2, column=3, sticky=W)

Label(label_entry, text='파일이름: ').grid(row=3, column=2, sticky=E)
file_open = Entry(label_entry, width=25, bg='light blue')
file_open.grid(row=3, column=3, sticky=W)

sort_pad = Frame(window)
sort_pad.grid(row=4, column=0, sticky=N)

data_output = Frame(window)
data_output.grid(row=5, column=0, sticky=N)

data = Text(data_output, width=75, height=10, wrap=WORD, background="light yellow")
data.grid(row=0, column=0, sticky=W)

status_output = Frame(window)
status_output.grid(row=6, column=0, sticky=N)

status = Text(status_output, width=75, height=0, wrap=WORD, background="light pink")
status.grid(row=0, column=0, sticky=W)

sort_list=[
    '번호순', '이름순', '점수내림차순', '점수오름차순'
    ]

btn_list=[
    ['추가', 5],
    ['삭제', 5],
    ['저장', 5],
    ['열기', 5],
    ['번호순', 5], ['이름순', 5], ['점수내림차순', 15], ['점수오름차순', 15]
    ]

def to_lower(s):
    x=''
    for i in range(len(s)):
        if s[i].isalpha():
            x+=s[i].lower()
    return x

def is_digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
    return False

def update_status(s):
    global status
    status.delete(0.0, END)
    status.insert(END, s)

lower_name=[]
def click(key):
    global lower_name
    if key == '추가':
        n = name.get()
        x = to_lower(n)
        if is_digit(n):
            name.delete(0, END)
            update_status("이름에 숫자가 들어갈 수 없습니다.")
        elif len(x)==0:
            name.delete(0, END)
            update_status("이름이 빈칸일 수 없습니다.")
        else:
            if x not in lower_name:
                try:
                    s = float(score.get())
                    data.insert(END, project_functions.add(n, s))
                    lower_name.append(x)
                    name.delete(0, END)
                    score.delete(0, END)
                    update_status("데이터가 추가되었습니다.")
                except:
                    score.delete(0, END)
                    update_status("점수가 올바르지 않습니다.")
            else:
                name.delete(0, END)
                update_status("이미 존재하는 이름입니다.")
    elif key == '삭제':
        try:
            num = int(number.get())
            if project_functions.is_in_list(num):
                data.delete(0.0, END)
                for i in range(len(project_functions.all_data_list)):
                    s = ("%2d  %-20s\t%6f\n" % (project_functions.all_data_list[i][0],
                                                project_functions.all_data_list[i][1],
                                                project_functions.all_data_list[i][2]))
                    data.insert(END, s)
                number.delete(0, END)
                update_status("데이터가 삭제되었습니다.")
            else:
                number.delete(0, END)
                update_status("데이터가 존재하지 않습니다.")
        except:
            number.delete(0, END)
            update_status("번호가 올바르지 않습니다.")
    elif key == '저장':
        try:
            f = open(file_save.get(), 'w')
            project_functions.save_file(f)
            f.close()
            file_save.delete(0, END)
            update_status("파일저장에 성공했습니다.")
        except:
            file_save.delete(0, END)
            update_status("저장할 파일을 열기에 실패했습니다.")
    elif key == '열기':
        try:
            lower_name = []
            f = open(file_open.get())
            data_list = project_functions.open_file(f)
            data.delete(0.0, END)
            for i in range(len(data_list)):
                s = ("%2d  %-20s\t%6f\n" % (int(data_list[i][0]),
                                            data_list[i][1],
                                            float(data_list[i][2])))
                lower_name.append(to_lower(data_list[i][1]))
                data.insert(END, s)
            f.close()
            file_open.delete(0, END)
            update_status("파일읽기에 성공했습니다.")
        except:
            file_open.delete(0, END)
            update_status("파일이 존재하지 않습니다.")
    elif key in sort_list:
        data_list = sort_map[sort_list.index(key)][1]()
        if data_list == []:
            update_status("데이터가 존재하지 않습니다.")
        else:
            data.delete(0.0, END)
            for i in range(len(data_list)):
                s = ("%2d  %-20s\t%6f\n" % (int(data_list[i][0]),
                                            data_list[i][1],
                                            float(data_list[i][2])))
                data.insert(END, s)
            status.delete(0.0, END)


r=0; c=0
for btn in btn_list:
    def cmd(x=btn[0]):
        click(x)
        #pass
    if r != 4:
        Button(label_entry,
               text=btn[0],
               width=btn[1],
               command=cmd).grid(row=r, column=4)
    elif r==4:
        Button(sort_pad,
               text=btn[0],
               width=btn[1],
               command=cmd).grid(row=r, column=c)
    c+=1
    if r<4:
        r+=1
        c=0
