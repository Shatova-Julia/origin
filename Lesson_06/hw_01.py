# Декодировать в строку байтовое значение:  b'r\xc3\xa9sum\xc3\xa9'.
# Затем результат преобразовать в байтовый вид в кодировке ‘Latin1’
# и результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).



bytes_decode = b'r\xc3\xa9sum\xc3\xa9'
print(bytes_decode)

decode = bytes_decode.decode()
print(decode)

encode_Latin = decode.encode('Latin1')
print(encode_Latin)

bytes_decode2 = b'r\xe9sum\xe9'
decode_two = bytes_decode2.decode('Latin1')
print(decode_two)


