x = 1 # 초기설정 팩토리얼 할 곱셉 누적하는 값
n = int(input("Input factorial number : "))
a_list = list() # a_list 또는 my_list
for i in range(1, n+1):
    a_list.append(x)
    x = x * 1 # 원래 팩토리얼이라면 1 대신 i를 넣어야 함
print(f"{n}! = {x}")
print(a_list)
# O(n) Space complexity 공간복잡도 : 코드가 실행되면서 컴퓨터 메모리공간을 얼마나 차지할까? 개념