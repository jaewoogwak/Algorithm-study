# 4949 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

sen = input();
while(sen != '.'):
    bucket = []; 
    is_equality = True;
    # bucket
    for i in range(len(sen)):
        # 1. 괄호가 나오는 순간부터 스택에 집어넣기
        if sen[i] == '[' or sen[i] == ']' or sen[i] == '(' or sen[i] == ')':
            if len(bucket) >=1:
                # 3. 괄호 입력 받기전에 괄호의 열림 닫힘 유무랑 문자열의 균형 검사
                if bucket[-1][0] =='[' and sen[i] == ']' :
                    bucket.pop();
                elif bucket[-1][0] =='(' and sen[i] == ')' :
                    bucket.pop();
                else:
                    bucket.append([sen[i], sen[i-1]]);
            # 2. 처음엔 스택 크기가 0이라서 괄호 먼저 입력받음 (괄호, 앞or뒤 문자)
            else:
                if sen[i] == '(' or sen[i] == '[':
                    bucket.append([sen[i], sen[i+1]]);
                else:
                    # 처음부터 닫힌 괄호 나오면 바로 종료
                    is_equality = False;
                    break;
    if is_equality == True and len(bucket) == 0:
        print('yes');
    else: print('no');      
    # print('bucket', bucket)
    sen = input(); # 입력 받기, '.' 입력이면 종료

   
