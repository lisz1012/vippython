# Author: lisz1012
# Creation date and time: 6/1/24 8:58 PM

class A:
    def info(self):
        print('A中的info方法')


class B:
    def info(self):
        print('B中的info方法')


class C(A, B):
    pass


c = C()
c.info()  # 输出A中的info方法, 因为A在前


class D(B, A):
    pass


d = D()  # 输出B中的info方法, 因为B在前
d.info()
