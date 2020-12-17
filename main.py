class Rot13:
    """
    A basic implementation of how you can
    encrypt your data using rot 13 algo
    """
    def __init__(self):
        print("type '-help' for help")
        

    def help_func(self,inp):
        self.inp = inp
        print('''
        Welcome to the rot 13 world:
        here are some of the commands that you can use
        1) -help
        2.)-ctr (convert to rot)
        3.)-cts (convert to string) 
        ''')



    def cvt_to_rot(self, inp):
        self.inp = inp
        """
          Convert a string to rot13
        """
        for i in self.inp:
            if type(i) == str:
                print(chr(int(ord(i))+13),end='')

    def cvt_to_string(self,inp):
        self.inp = inp
        """
        convert a rot13 to string

        """
        for i in self.inp:
            if type(i) == str:
                print(chr(int(ord(i))-13),end='')


# try:
#     while True:
#         enter_cmd = input(" ")
#         if type(enter_cmd) == str:
#                 # rt = Rot13(enter_cmd)
#                 if enter_cmd == '-help':
#                     rt.help_func()
#                 elif enter_cmd == '-ctr':
#                     rt.cvt_to_rot()
#                 elif enter_cmd == "-cts":
#                     rt.cvt_to_string()


# except:
#     print("the input must be a string")
rt = Rot13()
rt.cvt_to_rot("hello my name is hassan")
print("\n")
rt.cvt_to_string("hello my")