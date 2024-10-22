values = [True, False, True, None, True]
result = []
for v in values:
    if v is True:
        result.append('yes')
    else:
        if v is False:
            result.append('no')
        else:
            result.append('unknown')

print(result)  # Output: ['yes', 'no', 'unknown', 'yes']

# Более короткая запись с использованием list comprehension

print([('yes' if v is True else 'no' if v is False else 'unknown')
      for v in values])  # Output: ['yes', 'no', 'unknown', 'yes']
