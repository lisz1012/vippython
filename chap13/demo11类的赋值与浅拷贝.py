# Author: lisz1012
# Creation date and time: 6/2/24 3:28 PM

class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

    def __str__(self):
        return 'Computer对象(cpu:%s, disk:%s)' % (self.cpu, self.disk)


cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)
print('--' * 20)
disk1 = Disk()
computer = Computer(cpu1, disk1)

# 浅拷贝. Python拷贝一般都是浅拷贝, 拷贝时, 对象包含的子对象中的内容不拷贝, 因此, 源对象与拷贝对象会引用同一个子对象
import copy
computer2 = copy.copy(computer)
print(computer == computer2)
print(computer is computer2)
print(computer.cpu == computer2.cpu)
print(computer.cpu is computer2.cpu)
print(computer.disk == computer2.disk)
print(computer.disk is computer2.disk)
print('--' * 20)

# 深拷贝: 拷贝时, 对象包含的子对象中的内容也拷贝, 因此, 源对象与拷贝对象不会引用同一个子对象
computer3 = copy.deepcopy(computer)
print(computer == computer3)
print(computer is computer3)
print(computer.cpu == computer3.cpu)
print(computer.cpu is computer3.cpu)
print(computer.disk == computer3.disk)
print(computer.disk is computer3.disk)
