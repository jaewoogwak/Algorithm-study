# 11720 숫자의 합
# https://www.acmicpc.net/problem/11720

N = int(input());
string = input();

# a는 문자열을 한개씩 쪼갠 문자를 가진 배열 ['1',2'..]
a = list(string); 

# b는 a의 요소를 숫자로 바꿈 [1,2, ..]
b = list(map(int, a));

# 합 구하기
sum =0;
for i in b:
    sum +=i;

print(sum)
