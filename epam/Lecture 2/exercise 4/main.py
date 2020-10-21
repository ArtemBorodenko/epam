def replace1(s: str):
    a = s.find(' reasonable')
    b = s.find('unreasonable')
    str = s[0:b] + s[b + 2:-1] + s[-1]

    return str[0:a + 1] + s[b:b + 2] + str[a + 1:-1] + str[-1]


if __name__ == '__main__':
    input_str = 'The reasonable man adapts himself to the world; ' \
                'the unreasonable one persists in typing to adapt the world to himself'
    print(replace1(input_str))
