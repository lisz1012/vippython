# Author: lisz1012
# Creation date and time: 6/3/24 8:33 PM

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
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()
