# Brincando com manipulação de strings

def concat(*args):
        return ''.join(args)

def partial_name(n):
        return n[:2], n[2:]

def shuffle_letters(t):
        a, b = t
        return b + a

def finalize_name(n):
        return n.capitalize()

print(finalize_name(concat(*shuffle_letters(partial_name("roped")))))