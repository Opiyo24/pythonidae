def f():
    excs = [OSError('Error 1'), SystemError('Error 2')]
    raise ExceptionGroup('There were problems', excs)

f()