# _*_coding:utf-8 _*_




#定义一个存放书籍信息的列表
BookList = []
No = []
BorrowList1 = []
BorrowList2 = []


# 实例化出事书籍编号，存放在列表中
No1 = No.append(0)
No2 = No.append(1)
No3 = No.append(2)
class Book(object):
    def __init__(self, no, name, author, existing, number):
        self.no = no
        self.name = name
        self.author = author
        self.existing = existing
        self.number = number


class Menu(object):

    @staticmethod
    def MyMenu():
        print '欢迎来到图书管理系统\n'
        print'[1]查看所有藏书\n'
        print'[2]借阅图书\n'
        print'[3]归还图书\n'
        print'[4]添加图书\n'
        print'[5]删除图书\n'
        print'[6]查看借书记录\n'
        print'[7]退出系统\n'
        while True:
            choice = raw_input('请选择您要进行的操作：')
            if choice == '1':
                Choice.See()
            elif choice == '2':
                Id.Borrow()
            elif choice == '3':
                Id.Return()
            elif choice == '4':
                Choice.Add()
            elif choice == '5':
                Choice.Delete()
            elif choice == '6':
                Id.Record()
            elif choice == '7':
                print ''
                print '感谢您的使用，再会。'
                break

class Choice(object):

    #增加图书
    @staticmethod
    def Add():
        no = raw_input('请输入书籍编号：')
        if no in No:
            print'库存中已有这种书：'
            x = raw_input('请输入添加数量：')
            BookList[no] = BookList[no] + x
            print'添加成功'
            print''
            print'图书馆的书籍有：'
            Choice.See()
        else:
            name = raw_input('请输入书籍的名称：')
            author = raw_input('请输入书籍的作者：')
            existing = raw_input('请输入书籍的数量：')
            number = existing

            BookList.append(Book(no, name, author, existing, number))
            No.append(no)
            print'%s 添加成功' % name
            print''
            print'图书馆所有的书籍有：'
            Choice.See()


    #删除书
    @staticmethod
    def Delete():
        no = raw_input('请输入书籍编号：')
        for book in BookList:
            if no == book.no:
                BookList.remove(Book(book.no, book.name, book.author, book.existing, book.number))
                print'删除成功'
            else:
                print'图书馆中不存在此书'



    #遍历所有图书
    @staticmethod
    def See():
        print'图书馆所有的书有：'
        for book in BookList:
            print' 编号：%s \t《%s》 作者: %s \t 现存数：%s \t总库存：%s \t'%(book.no, book.name, book.author, book.existing, book.number)

class Id(object):
    def __init__(self, id, day):
        self.id = id
        self.day = day


    #借书
    @staticmethod
    def Borrow():
        no = raw_input('请输入要查询的书的编号：')
        for book in No:
            if no == book.no:
                if book.existing <= 0:
                    print'抱歉，本书现无库存，请下次再来'
                else:
                    id = raw_input('请输入您的图书卡号：')
                    day = raw_input('请输入您的还书日期：')
                    BorrowList1.append(Id(id, day))
                    BorrowList2.append(no)
                    book.existing -= 1

                    print'借书成功'
            else:
                print'抱歉，本图书馆暂未收录此书'

    #还书
    @staticmethod
    def Return():
        no = raw_input('请输入要归还的书籍的编号')
        for book in BorrowList2:
            if no == book.no:
                id = raw_input('请输入您的图书卡号：')
                day = raw_input('请输入您的还书日期：')
                BorrowList1.remove(Id(id, day))
                BorrowList2.remove(no)
                book.existing += 1

                print '还书成功'
            else:
                print'抱歉，此书不是从本图书馆借的'

    #查阅借书记录
    @staticmethod
    def Record():
        print'图书馆被借阅的书的编号有：' ,BorrowList2
        print'借阅人及还书日期分别为：',BorrowList1


if __name__ == '__main__':
    Menu.MyMenu()

# 实例化初始书籍信息，存放在列表中
    book1 = BookList.append(Book('0','c程序设计','谭浩强',4,5))
    book2 = BookList.append(Book('1','初识python','廖雪峰',2,5))
    book3 = BookList.append(Book('2','python进阶','廖雪峰',2,5))

