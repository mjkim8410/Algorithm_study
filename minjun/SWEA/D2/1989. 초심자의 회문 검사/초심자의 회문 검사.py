def check_outer(text):
    if text == '':
        return 1
    elif text[0] == text[-1]:
        return check_outer(text[1:-1])
    else: 
        return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    text = input()
    print(f"#{test_case} {check_outer(text)}")
