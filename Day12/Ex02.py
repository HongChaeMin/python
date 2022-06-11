def hello(name, msg):
    print('안녕, {}! {}.'.format(name, msg))

hello('수빈', '반갑다')
hello('현수', '잘 있었지?')

def hello(name, msg = '반갑다'):
    print('안녕, {}! {}.'.format(name, msg))

hello('수빈')
hello('현수', '요즘 잘 지내지?')
