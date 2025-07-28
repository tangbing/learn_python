import os
from datetime import datetime
import re
import json
from pathlib import Path
from typing import List, Dict, Optional

from py_learn.runoob1 import runoobl1
from py_learn.runoob2 import runoobl2



class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("\n🐶 正在调用 Dog 类的 bark 方法...")
        return f"{self.name} says Woof!"

    def showCmd(self):
        print("当前目录：", os.getcwd())
        os.makedirs("py_learn", exist_ok=True)

    def showTime(self):
        now = datetime.now()
        print("今天当前时间:", now.strftime("%Y-%m-%d %H:%M:%S"))

    def match(self):
        text = "Email: test@example.com, tbit@sina.com"
        match = re.search(r"\w+@\w+\.\w+", text)
        if match:
            print("finde email: ", match.group())
    

    def json(self):
        data = {"name" : "jack", "age" : 30}
        json_str = json.dumps(data)
        print("json: ", json_str)
        data2 = json.loads(json_str)
        print("name is:", self.name)
        print("data2:", data2)

    def pathlib(self):
        p = Path("test_dir/example.text")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("Hello, World!")
        print(p.read_text())

    @staticmethod
    def total(nums: List[int]) -> int:
        return sum(nums)

    @staticmethod
    def find(name: str) -> Optional[Dict]:
        pass

    @staticmethod
    def tryLearn():
        print("正在学习 Python...")
        try:
            fh = open("testfile", "w")
            fh.write("this is test file, to test except")
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("内容写入成功")
            fh.close()



    @staticmethod
    def mye(level):
        if level < 1:
            raise Exception("Invalid level!", level)
            print('触发异常了 end！')


# 触发异常
class Networkerror(RuntimeError):
    def __init__(self, args):
        self.args = args
        


# 注意：不要用 sum 作为变量名或 lambda，会覆盖内置 sum 函数
my_sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", my_sum(10, 20))


dog = Dog("Buddy")
print(dog.bark())
dog.showCmd()
dog.showTime()
dog.match()
dog.json()
dog.pathlib()


num = Dog.total([1, 2, 3, 4, 5])
print("Total ", num)

Dog.find("Buddy")
Dog.tryLearn()


try:
    Dog.mye(0)
except Exception as err:
    print('error expection,', err.args)
else:
    print("no exception")        

try:
    raise Networkerror("Network is down")
except Networkerror as e:
    print("Networkerror:", e.args)



runoobl1()
runoobl2()


