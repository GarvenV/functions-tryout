def fib(num):
    teller = 0
    eerstegetal = 0 
    tweedegetal = 1 
    overstap = 0

    while teller <= num:
        print (eerstegetal) 
        overstap = eerstegetal + tweedegetal
        eerstegetal = tweedegetal
        tweedegetal = overstap
        teller = teller + 1 
fib(20)