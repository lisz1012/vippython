# Author: lisz1012
# Creation date and time: 6/3/24 8:33 PM

# 打包命令: pyinstaller -F -w stusystem.py 或者 pyinstaller -F /Users/shuzheng/PycharmProjects/vippython/chap16/stusystem.py

import os

filename = 'student.txt'

def main():
    while True:
        menu()
        choice = int(input('请选择:'))
        if choice == 0:
            answer = input('您确定要退出系统吗？(y/n):')
            if answer == 'y' or answer == 'Y':
                print('感谢您的使用！')
                break
            else:
                continue
        elif choice == 1:
            insert()
        elif choice == 2:
            search()
        elif choice == 3:
            delete()
        elif choice == 4:
            modify()
        elif choice == 5:
            sort()
        elif choice == 6:
            total()
        elif choice == 7:
            show()
        else:
            print('输入错误，请重新输入！')


def menu():
    print('=============================学生信息管理系统=============================')
    print('-----------------------------功能菜单----------------------------------')
    print('\t\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t\t0.退出')
    print('------------------------------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('请输入学生ID:')
        if not id:
            break
        name = input('请输入学生姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except ValueError:
            print('输入无效，请重新输入！')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加？(y/n):')
        if answer == 'n' or answer == 'N':
            break
    save(student_list)
    print('学生信息录入完毕！')


def save(student_list):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            for student in student_list:
                file.write(str(student) + '\n')  # str()将字典转换为字符串
    except Exception as e:
        print('保存失败！')


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2:')
            if mode == '1':
                id = input('请输入学生ID:')
            elif mode == '2':
                name = input('请输入学生姓名:')
            else:
                print('输入有误，请重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否继续查询？(y/n):')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('暂未保存数据信息！')
            return


def show_student(student_list):
    if len(student_list) == 0:
        print('没有查询到学生信息，无数据显示！')
        return

    print('查询结果如下：')
    for item in student_list:
        print(
            f'学生ID:{item["id"]},姓名:{item["name"]},英语成绩:{item["english"]},Python成绩:{item["python"]},Java成绩:{item["java"]}, 总成绩: {int(item["english"]) + int(item["python"]) + int(item["java"])}')


def delete():
    while True:
        student_id = input('请输入要删除的学生ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
        flag = False
        if student_old:
            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}
                for student in student_old:
                    d = dict(eval(student))  # 如果item是合法的字典字符串，那么通过eval就可以转成字典，可以不用dict()进行类型转换; 如果item不是合法的字典字符串，那么eval转换的结果就不是字典，这里用dict（）是为了确保转换后一定时字典，如果不是字典就会报错
                    if d['id'] != student_id:
                        wfile.write(str(d) + '\n')
                    else:
                        flag = True
                if flag:
                    print(f'ID为{student_id}的学生信息已删除！')
                else:
                    print(f'没有找到ID为{student_id}的学生信息！')
        else:
            print('无学生信息！')
            break
        show()  # 删除后显示所有学生信息
        answer = input('是否继续删除？(y/n):')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old = rfile.readlines()
            student_id = input('请输入要修改的学生ID:')
    else:
        return

    for student in student_old:
        d = dict(eval(student))
        if d['id'] == student_id:
            print('找到学生信息，可以修改！')
            while True:
                try:
                    d['name'] = input('请输入姓名:')
                    d['english'] = int(input('请输入英语成绩:'))
                    d['python'] = int(input('请输入Python成绩:'))
                    d['java'] = int(input('请输入Java成绩:'))
                except ValueError:
                    print('输入无效，请重新输入！')  # 有错误会回到while True, 重新输入, 直到输入正确
                else:
                    break
            student_new = str(d)
            student_old[student_old.index(student)] = student_new
            with open(filename, 'w', encoding='utf-8') as wfile:
                for student in student_old:
                    wfile.write(student)
            print('修改成功！')
            break

    answer = input('是否继续修改其他学生信息？(y/n):')
    if answer == 'y' or answer == 'Y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
            student_new = []
            for student in student_old:
                d = dict(eval(student))
                student_new.append(d)
        asc_or_desc = input('请选择(0升序，1降序):')
        if asc_or_desc == '0':
            asc_or_desc = False
        elif asc_or_desc == '1':
            asc_or_desc = True
        else:
            print('输入有误，排序失败！')
            sort()
        mode = input('请选择排序方式(1按英语成绩排序，2按Python成绩排序，3按Java成绩排序，0按总成绩排序):')
        if mode == '1':
            student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc)
        elif mode == '2':
            student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc)
        elif mode == '3':
            student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc)
        elif mode == '0':
            student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc)
        else:
            print('输入有误，排序失败！')
            sort()
        show_student(student_new)
    else:
        return


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print(f'一共有{len(student)}名学生！')
            else:
                print('暂未保存数据信息！')
    else:
        print('暂未保存数据信息！')


def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                student_list.append(eval(item))  # student_list是字典的列表
        if student_list:
            show_student(student_list)
        else:
            print('暂未保存数据信息！')
    else:
        print('暂未保存数据信息！')


if __name__ == '__main__':
    main()
