def reverse(num):
    return int(str(num)[::-1])

A, B = map(int, input().split())
A = reverse(A)
B = reverse(B)
C = A + B
print(reverse(C))