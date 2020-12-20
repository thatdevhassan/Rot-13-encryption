def cvt_to_rot(inp):
    for i in inp:
        if type(i) == str:
            print(chr(ord(i)+13),end='')
    print('\n')
    

inp = input("enter the input: ")
cvt_to_rot(inp)


def cvt_to_str(o):
    for i in o:
        print(chr(ord(i)-13),end="")
    
cvt_to_str("uryy|-z-{nzr-v"+str(chr(ord('s')+13))+"-un"+str(chr(ord('s')+13))+str(chr(ord('s')+13))+"n{")
