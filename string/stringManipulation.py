import re

def str_to_raw(s):
    raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)

# def raw_string(s):
#     if isinstance(s, str):
#         s = s.encode('string-escape')
#     elif isinstance(s, unicode):
#         s = s.encode('unicode-escape')
#     return s


string="i:/documentos/softwares/microchip/16f916/inv-94/94v1.hex"
string=string.split("/")


print(string)
print(string[4])


#print(string[2])
#print(type(string)) 
