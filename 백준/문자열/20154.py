# 20154 이 구역의 승자는 누구야?!
# https://www.acmicpc.net/problem/20154

S = input();

arr = [];
for i in S:
    arr.append(i);

alphabet = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1];
# 알파벳 대문자에서 숫자 변환
for i in range(len(arr)):
    if arr[i] == 'A':
        arr[i] = alphabet[0]
        
        continue;
    elif arr[i] == 'B':
        arr[i] = alphabet[1];
        
        continue;
    elif arr[i] =='C':
        arr[i] = alphabet[2]
        
        continue;
    elif arr[i] == 'D':
        arr[i] = alphabet[3];
        
        continue;
    elif arr[i] == 'E':
        arr[i] = alphabet[4];
        
        continue;
    elif arr[i] == 'F':
        arr[i] = alphabet[5];
        
        continue;
    elif arr[i] == 'G':
        arr[i] = alphabet[6];
        
        continue;
    elif arr[i] == 'H':
        arr[i] = alphabet[7];
        
        continue;
    elif arr[i] == 'I':
        arr[i] = alphabet[8];
        
        continue;
    elif arr[i] == 'J':
        arr[i] = alphabet[9]
        
        continue;
    elif arr[i] == 'K':
        arr[i] = alphabet[10]
        
        continue;
    elif arr[i] == 'L':
        arr[i]=  alphabet[11]
        
        continue;
    elif arr[i] == 'M':
        arr[i] =  alphabet[12]
        
        continue;
    elif arr[i] == 'N':
        arr[i] = alphabet[13];
        
        continue;
    elif arr[i] == 'O':
        arr[i] = alphabet[14];
        
        continue;
    elif arr[i] == 'P':
        arr[i] = alphabet[15];
        
        continue;
    elif arr[i] == 'Q':
        arr[i] = alphabet[16];
        
        continue;
    elif arr[i] == 'R':
        arr[i]= alphabet[17];
        
        continue;
    elif arr[i] == 'S':
        arr[i] = alphabet[18];
        
        continue;
    elif arr[i] == 'T':
        arr[i] = alphabet[19];
        
        continue;
    elif arr[i] == 'U':
        arr[i] = alphabet[20]
        
        continue;
    elif arr[i] == 'V':
        arr[i] =  alphabet[21]
        
        continue;
    elif arr[i] =='W':
        arr[i] = alphabet[22];
        
        continue;
    elif arr[i] == 'X':
        arr[i] = alphabet[23];
        
        continue;
    elif arr[i] == 'Y' :
        arr[i] = alphabet[24];
        
        continue;
    elif arr[i] == 'Z':
        arr[i] = alphabet[25];
        
        continue;
    
v = sum(arr)
v = v % 10;
if v % 2 != 0:
    print('I\'m a winner!');
else :
    print('You\'re the winner?');
