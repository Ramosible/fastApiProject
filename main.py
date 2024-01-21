import math
from fastapi import FastAPI, Query

'''
1 - GET /add/{num_1}/{num_2}/{num_3} ენდპოინტზე უნდა დაბრუნდეს გადაცემული სამი რიცხვის ჯამი {'result': result}
2 - GET /sub?num_1=&num_2= ენდპოინტზე უნდა დაბრუნდეს გადაცემული რიცხვების სხვაობა  {'result': result}
3 - GET /mul/{num_1}?num_2= ენდპოინტზე უნდა დაბრუნდეს გადაცემული რიცხვების ნამრავლი  {'result': result}
4 - GET /div/{num_1}/{num_2} ენდპოინტზე უნდა დაბრუნდეს გადაცემული რიცხვების განაყოფი  {'result': result}
5 - GET /{a}/{b}/{c} ენდპოინტზე უნდა დაბრუნდეს გადაცემული კვადრატული განტოლების კოეფიციენტების მიხედვით ნაპოვნი x1 და x2 {'result': result}
'''
app = FastAPI()


#1
@app.get("/add/{num_1}/{num_2}/{num_3}")
async def add_nums(num_1: int, num_2: int, num_3: int):
    return {"result ": {num_1 + num_2 + num_3}}

#2
@app.get("/sub")
async def sub_nums(num_1: int, num_2: int):
    return {"result": {num_1 - num_2}}

#3
@app.get("/mul/{num_1}")
async def mul_nums(num_1: int, num_2:  int):
    return {"result": f"result  {num_1 * num_2}"}

#4
@app.get("/div/{num_1}/{num_2}")
async def div_nums(num_1: int, num_2:  int):
    if num_2 == 0:
        return {"msg: ": "can't divide by zero"}
    else:
        return {"message": f"result  {num_1 / num_2}"}

#5
@app.get("/{a}/{b}/{c}")
async def find_x(a: int, b: int, c: int):
    d = (b * b) - (4 * a) * c
    if d == 0:
        x1 = -b / (2 * a)
        return {f" x: {x1}"}
    if d > 0:
        x1 = (-b + math.sqrt(b.__pow__(2) - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b.__pow__(2) - 4 * a * c)) / (2 * a)
        return {"x1 ":  {x1}, "x2 ": {x2}}
    if d < 0:
        return {"no solution"}

'''
ბონუსი:
გააკეთეთ GET რექვესთი ახალ ენდპოინტზე, სადაც გადავცეთ რიცხვების არაფიქსირებულ რაოდენობას 
და ენდპოინტი დაგვიბრუნებს მათ ჯამს
#http://127.0.0.1:8000/addmany/?numbers=3&numbers=3&numbers=4&numbers=5&numbers=5&numbers=7&numbers=9
'''
@app.get("/addmany/")
async def add_many(numbers: list = Query(...)):
    sum = 0
    for i in numbers:
        sum += int(i)
    return {f"result {sum}"}


