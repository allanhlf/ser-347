print('\033[7;40mConversor de temperatura\033[m')

e = int(input('Digite 1 para converter °C to °F ou digite 2 para converter °F to °C:'))
f = 1
c = 2
if e == c:
    tf = float(input('Digite a temperatura em °F: '))
    tc = 5 * (tf - 32) / 9
    print('\033[1;31m{}°F\033[m é igual a \033[1;33m{:.1f} °C'.format(tf, tc))
else:
    tc = float(input('Digite a temperatura em °C: '))
    tf = tc * 9 / 5 + 32
    print('\033[1;31m{}°C\033[m é igual a \033[1;33m{:.1f} °F'.format(tc, tf))
