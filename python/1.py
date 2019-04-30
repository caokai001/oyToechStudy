A=list(range(6))
for i in range(len(A)):
    print(A[i])


def foo(bar=[]):
    bar.append('bar')
    return bar
foo()
foo()
foo()
