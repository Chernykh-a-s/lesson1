def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'
    
print(get_summ('learn','python'))


# Output in uppercase letters
def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'.upper()
    
print(get_summ('learn','python'))