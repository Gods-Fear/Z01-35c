def mult(x, y):
    return x * y


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div_int(x, y):
    return x // y


def div_f(x, y):
    return x / y


def count_equation(user_input):
    result = 0

    if '*' in user_input:
        split_inp = user_input.split('*')

        if '+' in split_inp[0]:
            split_plus = split_inp[0].split('+')
            mul = mult(float(split_plus[1]), float(split_inp[1]))
            result = int(add(float(split_plus[0]), mul))

        elif '+' in split_inp[1]:
            split_plus = split_inp[1].split('+')
            mul = mult(float(split_plus[0]), float(split_inp[0]))
            result = int(add(mul, float(split_plus[1])))

        elif '-' in split_inp[0]:
            split_min = split_inp[0].split('-')
            mul = mult(float(split_min[1]), float(split_inp[1]))
            result = int(sub(float(split_min[0]), mul))

        elif '-' in split_inp[1]:
            split_min = split_inp[1].split('-')
            mul = mult(float(split_min[0]), float(split_inp[0]))
            result = int(sub(mul, float(split_min[1])))
        else:
            result = int(mult(float(split_inp[0]), float(split_inp[1])))

    if '/' in user_input:
        split_d_int = user_input.split('/')
        if split_d_int[1] == '0':
            print("Error value, you can not divide by 0")
        else:

            if '+' in split_d_int[0]:
                split_plus = split_d_int[0].split('+')
                div = div_f(float(split_plus[1]), float(split_d_int[1]))
                result = int(add(float(split_plus[0]), div))

            elif '+' in split_d_int[1]:
                split_plus = split_d_int[1].split('+')
                div = div_f(float(split_d_int[0]), float(split_plus[0]))
                result = int(add(div, float(split_plus[1])))

            elif '-' in split_d_int[0]:
                split_min = split_d_int[0].split('-')
                div = div_f(float(split_min[1]), float(split_d_int[1]))
                result = int(sub(float(split_min[0]), div))

            elif '-' in split_d_int[1]:
                split_min = split_d_int[1].split('-')
                div = div_f(float(split_d_int[0]), float(split_min[0]))
                result = int(sub(div, float(split_min[1])))
            else:
                result = int(div_f(float(split_d_int[0]), float(split_d_int[1])))

    if '+' in user_input:
        split_add = user_input.split('+')

        if '-' in split_add[0]:
            split_s = split_add[0].split('-')
            subs = sub(float(split_s[0]), float(split_s[1]))
            result = int(add(subs, float(split_add[1])))

        elif '-' in split_add[1]:
            split_s = split_add[1].split('-')
            subs = sub(float(split_s[0]), float(split_s[1]))
            result = int(add(float(split_add[1]), subs))
        else:
            result = int(eval(user_input))

    if '-' in user_input:
        result = int(eval(user_input))

    return result


def to_dic(user_input):
    res = {item: item for item in user_input}
    print(res)

    def formatData(t, s):
        if not isinstance(t, dict) and not isinstance(t, list):
            if str(t) == '+' or str(t) == '*' or str(t) == '-' or str(t) == '/':
                print("\t" * (s+1) + str(t))
            else: print("\t" * s + str(t))
        else:
            for key in t:
                if not isinstance(t, list):
                    formatData(t[key], s + 1)

    formatData(res, 0)


if __name__ == '__main__':
    user_in = input('Please put an equations: ')
    print(f'{user_in} = {count_equation(user_in)} \n')
    to_dic(user_in)
