filename = './_Serato_/Subcrates/Turntablism.crate'

fullstring = ''
with open(filename, 'rb') as f:
    while 1:
        byte_s = f.read(1)
        if not byte_s:
            break
        # print(byte_s)
        # print(byte_s.decode("utf-8"))
        # if (byte_s == "b'\x00'"):
        # print('hi')
        fullstring = fullstring + byte_s.decode("latin-1")
        # fullstring = fullstring + byte_s.decode("utf-8")
        # fullstring = fullstring + byte_s.decode("ascii")
        # if not byte_s:
        # break
        # byte = byte_s[0]
        # print(chr(byte))
    print(fullstring)

# print(fullstring)
