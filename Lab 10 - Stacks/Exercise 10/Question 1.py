s = Stack()
print(s.is_empty(), end=" ")
s.push(True)
print(s.peek(), end=" ")
print(s.size(), end=" ")
s.push('cat')
s.pop()
print(s.peek(), end=" ")
s.push(8)
s.pop()
print(s.size())