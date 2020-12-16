class Rot13:
    """
    A basic implementation of how you can
    encrypt your data using rot 13 algo
    """
    def __init__(self,inp):
        print("type '-help' for help")
        self.inp = inp

    def help_func(self):
        print('''
        Welcome to the rot 13 world:
        here are some of the commands that you can use
        1) -help
        2.)-ctr (convert to rot)
        3.)-cts (convert to string) 
        ''')



    def cvt_to_rot(self):
        """
          Convert a string to rot13
        """
        for i in self.inp:
            if type(i) == str:
                print(chr(int(ord(i))+13),end='')

    def cvt_to_string(self):
        """
        convert a rot13 to string

        """
        for i in self.inp:
            if type(i) == str:
                print(chr(int(ord(i))-13),end='')


try:
    while True:
        inp = input()
        if type(inp) == str:
                rt = Rot13(inp)
                if inp == '-help':
                    rt.help_func()
                elif inp == '-ctr':
                    rt.cvt_to_rot()
                elif inp == "-cts":
                    rt.cvt_to_string()


except:
    print("the input must be a string")