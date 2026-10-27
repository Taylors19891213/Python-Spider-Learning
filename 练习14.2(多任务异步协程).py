import time
import asyncio

# async def func():
#     print("1")
#
# if __name__ == '__main__':
#     g = func()         #此时的函数是异步协程函数，此时函数执行得到的是一个异步执行对象
#     asyncio.run(g)     #协程程序运行需要asyncio模块



# async def func1():
#     print("1")
#     await asyncio.sleep(3)    #当程序出现同步操作时，异步就中断了
#     print("2")
#
# async def func2():
#     print("3")
#     #time.sleep(4)
#     await asyncio.sleep(4)
#     print("4")
#
# #必须把协程包装成task
# async def main():
#     f1 = func1()
#     f2 = func2()
#     task =[asyncio.ensure_future(f1),asyncio.ensure_future(f2)]
#
#     await asyncio.wait(task)
#
# if __name__ == '__main__':
#
#     t1=time.time()
#     asyncio.run(main())
#     t2=time.time()
#     print(t2-t1)


#在爬虫领域的应用
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  #网络请求
    print("下载完成！")
async def main():
    urls = [
        "https://www.baidu.com",
        "https://www.bilibili.com",
        "https://www.163.com",
    ]
    tasks = []
    for url in urls:
        d=asyncio.create_task(download(url))
        tasks.append(d)

    await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())
