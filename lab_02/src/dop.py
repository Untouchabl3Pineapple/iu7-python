def dec_to_binint(n):
    if n == '0':
        return '0'

    flag = 0
    if '-' in n:
        flag = 1
        n = n.replace('-', '')
    n = int(n)
    res = ''

    while n > 0:
        res = str(n % 2) + res
        n = n // 2

    if flag == 0:
        return res
    else:
        return '-' + res

def dec_to_binfloat(n):
    flag = 0
    if '-' in n:
        flag = 1
        n = n.replace('-', '')
    point = n.index('.')
    left_part = n[:point:]
    right_part = '0.' + n[point + 1::]

    left_res = dec_to_binint(left_part)
    right_res = ''
    for i in range(4):
        right_part = str(float(right_part) * 2)
        if right_part[0] != '0':
            right_res += '1'
            right_part = '0.' + right_part[2::]
        elif right_part[0] == '0':
            right_res += '0'

    if flag == 0:
        return left_res + '.' + right_res
    else:
        return '-' + left_res + '.' + right_res


def bin_to_decint(n):
    if n == '0':
        return '0'

    flag = 0
    if '-' in n:
        flag = 1
        n = n.replace('-', '')
    leng = len(n)
    dig_dec = 0
    for i in range(0, leng):
        dig_dec += int(n[i]) * (2 ** (leng - i - 1))

    if flag == 0:
        return str(dig_dec)
    else:
        return '-' + str(dig_dec)

def bin_to_deсfloat(n):
    flag = 0
    if '-' in n:
        flag = 1
        n = n.replace('-', '')
    point = n.index('.')
    left_part = n[:point:]
    right_part = n[point + 1::]
    res_left = bin_to_decint(left_part)
    leng = len(right_part)
    res_right = 0
    for i in range(0, leng):
        res_right += int(right_part[i]) * (2 ** (-i - 1))

    if flag == 0:
        return str(int(res_left) + float(res_right))
    else:
        return '-' + str(int(res_left) + float(res_right))

