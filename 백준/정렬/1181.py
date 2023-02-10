# 1181 단어 정렬
# https://www.acmicpc.net/problem/1181

N = int(input());
arr = [];

# 입력한 문자열을 리스트에 추가
for i in range(N):
    string = input();
    # 중복 검사
    if string not in arr:
        arr.append(string);

# 리스트 오름차순 정렬 => 영어 알파벳 순서로 정렬
arr.sort()
# 리스트 요소 길이 순서로 정렬 => 짧은 순서부터 길이가 같으면 알파벳 순서에 따라 정렬
arr.sort(key=len)

for i in arr:
    print(i);
