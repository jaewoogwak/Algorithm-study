# 10798 세로 읽기
# https://www.acmicpc.net/problem/10798

arr = [];

# 15 x 5 size 배열로 초기화
for i in range(5):
    arr.append([' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',])     

# 한 줄에 입력받은 문자열의 각 요소를 기존 arr 배열에 대입
# 이 과정을 거치면 값이 존재하는 문자 요소만 arr에서 ' '를 대체하고 나머지 요소는 ' '로 유지
for i in range(5):
    letter = input();

    for j in range(len(letter)):
        
        arr[i][j] = letter[j];

# 세로로 출력하기 위해 인덱스 바꿈, 이때 값이 ' '인 경우는 출력하지 않음.
# 결과적으로 아까 입력한 문자열 5줄을 세로로 읽으면서 ' '는 무시함.
for i in range(15):
    for j in range(5):
        if arr[j][i] != ' ':         
            print(arr[j][i], end='')
