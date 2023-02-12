def get_summ(one, two, delimiter='&'):
    return(print(f'{one}{delimiter}{two}'))
    
get_summ('learn','python')

# Output in uppercase letters
def get_summ(one, two, delimiter='&'):
    return(print((f'{one}{delimiter}{two}').upper()))
    
get_summ('learn','python')