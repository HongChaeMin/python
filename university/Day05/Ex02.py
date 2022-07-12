orgPwd = int(input('ID 로 사용할 여덟 자리의 정수를 입력하세요 >> '))
keyMask = 27182818
encPwd = orgPwd ^ keyMask
print('입력한 ID : %d' % orgPwd)
print('암호화에 저장된 ID : %d' % encPwd)
inPwd = int(input('로그인할 ID를 입력하세요 >>'))
result = encPwd ^ keyMask
print('로그인 결과 : {}'.format(inPwd == result))


