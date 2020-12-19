# class Rot13:
#     """
#     A basic implementation of how you can
#     encrypt your data using rot 13 algo
#     """
#     def __init__(self):
#         print("type '-help' for help")
        
#     def help_func(self):
#         print('''
#         Welcome to the rot 13 world:
#         here are some of the commands that you can use
#         1) -help
#         2.)-ctr (convert to rot)
#         3.)-cts (convert to string) 
#         ''')



#     def cvt_to_rot(self, inpctr):
 
#         """Convert a string to rot13"""
#         self.inpctr = inpctr
#         b = ''
#         for i in self.inpctr:
#             a = chr(int(ord(i))+13)
#             b+= a
#         print(b)

#     def cvt_to_string(self,inpcts):
#         self.inpcts = inpcts

#         """convert a rot13 to string"""
#         for i in self.inpcts:
#             if type(i) == str:
#                 print(chr(int(ord(i))-13),end='')

# rt = Rot13()


# rt.cvt_to_rot("Hello my name is hassan")
# rt.cvt_to_string("Uryy|-z-{nzr-v-unn{")

def cvt_to_rot(inp):
    string = ''
    for i in inp:
        a = chr(ord(i)+13)
        if a == " ":
            string+= " "
        else:
            string+= i
    print(string)



cvt_to_rot("hello my name is hassan")