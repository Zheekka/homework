def test(*params):
    for i in params:
        print (i)
test(1,"строка",True,8 )

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

n = 10
print(f"Факториал {n} это {factorial_recursive(n)}")

