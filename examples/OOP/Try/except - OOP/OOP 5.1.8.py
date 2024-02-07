lst_in = "1 -5.6 2 abc 0 False 22.5 hello world".split()
def f(x):
    try:
        int(x)
        return True
    except:
        return False

print(sum(list(map(int, (filter(f, lst_in))))))