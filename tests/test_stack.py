from hexlet_pytest import stack

def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)
    stack.pop()
    assert not stack
