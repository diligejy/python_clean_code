from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))

print('Red :          ', my_values.get('red'))
print('Green :        ', my_values.get('green'))
print('Opacity :      ', my_values.get('opacity'))

# 쿼리 문자열 : 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print('Red :          %r' % red)
print('Green :        %r' % green)
print('Opacity :      %r' % opacity)

# 삼항 표현식으로 조금 더 명확하게 표현
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

# 조금 더 명확히
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0


# 근데 이게 반복되면? 귀찮잖아. -> 헬퍼함수로 바꾸자.
def get_first_int(values, key, default = 0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

# 함수로 바꾸니까 매번 안해도 되고 명확히 보여주네
green = get_first_int(my_values, 'green')