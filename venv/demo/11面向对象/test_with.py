# with open as f
class Testwith():
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('存在异常%s' % exc_tb)
        print('exit')


with Testwith():
    print('Test is running')
    raise NameError('Test')
