def init(_char):
    return 57 * _char & 0xF

def dummy(a1):
    asc_a74 = '~!@#$%^&*()_+=-?'
    v3 = len(a1)
    if a1[v3 - 1] == 10:
        a1[v3 - 2] = 0

    v6 = ''
    v4 = 0
    for i in range(2*v3):
        a = ord(a1[int(i/2)])
        v1 = int(a) >> 4*( (1-i) & 1 ) 
        v4 = ( int(init(v4)) + v1) & 0xF
        v6 += asc_a74[v4]

    return v6

_input = '$@^#?#!)~@(+@$*($(&$&~#!-=()!+!*-_)?_^+$(~$(&~&@%-$(*)?^_&%%!)~-#)-~^&^(&$&%~$_~'
test = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_{}'
flag = ''

for i in range(1, int( len(_input)/2 ) + 1 ): # len(_input) = 80
    i = i*2
    target = _input[0: i]
    for j in range( len(test) ):
        tmp = flag + test[j]
        print(tmp, flush=True)
        if dummy(tmp) == target:
            flag = tmp
            break

print("flag: ", flag)
