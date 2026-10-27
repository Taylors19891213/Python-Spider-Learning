# from threading import Thread
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if __name__ == '__main__':
#     t = Thread(target=func)   #创造线程并给线程安排任务
#     t.start()                #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
#
#     for i in range(1000):
#         print("main",i)
from threading import Thread


# class MyThread(Thread):
#     def run(self):          #线程被执行时，被执行的就是run()
#         for i in range(1000):
#             print("子线程",i)
#
# if __name__ =='__main__':
#     t = MyThread()
#     t.start()
#
#     for i in range(1000):
#         print("主线程",i)

def func(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    t1 = Thread(target=func,args=("周杰伦",))    #传递参数必须是元组
    t1.start()
    t2 = Thread(target=func,args=("王力宏",))
    t2.start()






# #线程池：一次性开辟一些线程，用户直接给线程池提交任务，线程任务的调度交给线程池来完成
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#
# def fn(name):
#     for i in range(1000):
#         print(name,i)
#
# if __name__ =='__main__':
#     #创造线程池
#     with ThreadPoolExecutor(50) as t:
#         for i in range(1000):
#             t.submit(fn,name=f"线程{i}")
#         #等待线程池中的任务全部执行完毕，才继续执行守护
#         print("123")