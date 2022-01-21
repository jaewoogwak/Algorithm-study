# 4659 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659

while(1):
    vowel_count =0;
    consonant_count = 0;
    is_acceptable = True;
    having_vewel = False;
    a = 1;
    # houctuh
    password = input();
    if password == 'end': break;
    if len(password) == 1:
        if (password[0] == 'a' or password[0] =='e' or password[0] =='i' or password[0] =='o' or password[0] =='u'):
            having_vewel = True;
            print('<{}> is acceptable.'.format(password));
            # print('consonant count : {}, vowel count: {}'.format(consonant_count, vowel_count))
        else: 
            having_vewel = False;
            print('<{}> is not acceptable.'.format(password));
            # print('consonant count : {}, vowel count: {}'.format(consonant_count, vowel_count))
    else:
        if password[0] == 'a' or password[0] == 'e' or password[0] == 'i' or password[0] == 'o' or password[0] == 'u':
            vowel_count +=1;
            having_vewel = True;
        else: consonant_count +=1;

        for i in range(1, len(password)):
            if (password[i] != password[i-1]) or (password[i] == password[i-1]== 'e' or password[i] == password[i-1]== 'o'):
                a = 1;
            else:
                is_acceptable = False;
                # print('{} is not acceptable'.format(password));
                break;
            if password[i]== 'a' or password[i]== 'e' or password[i]== 'i' or password[i]== 'o' or password[i]=='u':
                vowel_count +=1;
                having_vewel = True;
                consonant_count = 0;
            else: 
                consonant_count +=1;
                vowel_count = 0;
                
            if consonant_count >=3 or vowel_count >=3:
                # print('{} is not acceptable'.format(password));
                # print('consonant count : {}, vowel count: {}'.format(consonant_count, vowel_count))
                break;
        
        if (consonant_count < 3 and vowel_count <3 ) and (having_vewel == True) and (is_acceptable == True):
            print('<{}> is acceptable.'.format(password));
            # print('consonant count : {}, vowel count: {}'.format(consonant_count, vowel_count))
        else:
            print('<{}> is not acceptable.'.format(password));
            # print('consonant count : {}, vowel count: {}'.format(consonant_count, vowel_count))


            
