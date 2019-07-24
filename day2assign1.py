def div(num):
    temp = num
    a , temp = temp//1000 , temp % 1000
    b , temp = temp//100 , temp % 100
    c , temp = temp//10 , temp % 10
    d , temp = temp//1 , temp % 1

    return a , b , c , d

if __name__ == "__main__":
    li = [ i for i in range ( 1000 , 9999 )]

    for l in li:
        a , b , c , d = div(l)
        if a + b + c + d == 12 and a - b == c and a + c == d :
            print(l)