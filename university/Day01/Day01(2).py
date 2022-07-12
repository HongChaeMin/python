# 문자열 연결과 반복 연산자 +, *의 활용
print("원의 원주율 : " + '3.141592');

print("python " 'programing ' + 'language');

print('파이썬 언어는 ' + "강력하다");

print('파이썬 ' + "언어! " + 3 * "방가 ");


# 삼중 따옴표와 주석

''' 01-02 commtents.py
    2019 3. by Kang Hwan Soo'''

print('# 이후는 주석'); # 한 줄에서 문장 이후에도 주석 사용가능
print('string : "python"'); # 작은 따옴표 내부에서 큰 따옴표는 문자열
print("number : 1 5 3.14"); # 문자열 내부에서 숫자도 문자열
print("string : 'python'"); # 큰 따옴표 내부에서 작은 따옴표는 문자열


# 정수와 실수, 다양한 연산자
# 이거 그냥 구글링 해서 봐 ㅅㅂ
# // : 몫 나누기
# ** : 거듭제곱


# 함수 eval()
# 모든 "실행 가능한 파이썬 문자의 문자열"을 실행
print(eval('3 + 15 / 2'));
print(eval('4 * 3 % 5'));
print(eval('3 * -2 ** 3'));
print(eval('"java " * 3'));
