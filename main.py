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
#         for i in self.inpctr:
#             if type(i) == str:
#                 print(chr(int(ord(i))+13))

#     def cvt_to_string(self,inpcts):
#         self.inpcts = inpcts

#         """convert a rot13 to string"""
#         for i in self.inpcts:
#             if type(i) == str:
#                 print(type(i))
#                 print(chr(int(ord(i))-13),end='')



# rt = Rot13()
# rt.cvt_to_string("z-{nzr-v-unn{")



def cvt_to_rot(inp):
    string = ''
    for i in inp:
        if i =="1":
            string += " "
        else:
            string+=chr(ord(i)-13)
    print(string)



cvt_to_rot("uryy|-z -{nzr-v -un  n{")