# 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

N = int(input());
arr = [];
count = 0;

for i in range(N):
    word = input();
    tmp = [];
    for j in word:
        tmp.append(j);
    arr.append(tmp); 

for word in arr:
    # 단어가 한글자로 이루어져있으면
    if len(word) == 1:
        count +=1;
    else:
        reminder = [];
        # print(word)
        # 첫번째 글자 넣고
        checker = True;
        reminder.append(word[0]);
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                # 이전 글자랑 같은지
                if word[i] not in reminder:
                    # 이전 글자랑 같지 않다면
                    # 리마인더에 존재하나
                    # 존재하지 않으면 처음 등장했으므로 리마인더에 넣기
                    reminder.append(word[i]);
                else:
                    # 존재하면 중복된 글자 나온것
                    checker = False;
                    break;
        if checker == True:
            count +=1;  
        
print(count);       
