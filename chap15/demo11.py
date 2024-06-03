# Author: lisz1012
# Creation date and time: 6/2/24 6:42 PM

# MyContentMgr类的实例对象可以使用with语句, 因为它实现了__enter__和__exit__方法, 遵守了上下文管理器协议
class MyContentMgr:
    def __enter__(self):
        print('enter方法被调用')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用')

    def show(self):
        print('show方法被调用', 1/0)   # 即使产生了异常, 也不会影响with 中 enter 和 exit语句的执行(自动关闭资源)


mcm = MyContentMgr()
print(type(mcm))

with mcm as file:
    file.show()
