def pow(base, power):
    if power == 0:
        return 1
    return base * pow(base, power - 1)

base, power = 2, 4
result = pow(base, power)
print(f'{base} power {power} = {result}')