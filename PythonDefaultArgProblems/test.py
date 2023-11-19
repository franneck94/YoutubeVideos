def do_something(v, l=None):
    if l: # l is not None
        l.append(v)
    else:
        l = []
        l.append(v)
    return l

def main():
    l1 = do_something(10) # 0xaa
    print(l1)
    l2 = do_something(42) # 0xff
    print(l2)

if __name__ == "__main__":
    main()
