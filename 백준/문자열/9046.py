# 9046 복호화
# https://www.acmicpc.net/problem/9046

T = int(input());

for time in range(T):
    string = input();
    string = string.replace(" ", "")
    arr =[];

    for i in string:
        arr.append(i);

    frequency = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    cnt = 1;
    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

    # arr는 입력한 문자열의 요소가 담긴 배열
    for i in arr:
        if i in frequency:
            counter[frequency.index(i)] += 1;
    maxNum = max(counter);    

    # 최댓값이 여러개인지 검증
    for i in counter:
        if maxNum == i:
            cnt +=1;
            
    # 최댓값 2개 이상이면 ? 출력 아니면 문자 출력
    if cnt > 2:
        print('?')
    else:
        print(frequency[counter.index(maxNum)]);        
