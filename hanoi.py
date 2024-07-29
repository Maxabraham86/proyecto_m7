def hanoi(num_discos, inicio='A', fin='C'):
    intermedio= 'ABC'.replace(inicio,'').replace(fin,'')
    
    
    if num_discos < 2 :
        raise Exception('Hanoi necesita al menos 2 discos')
    
    if num_discos== 2 :
        print(f'1: {inicio} -> {intermedio}')
        print (f'2:{inicio} ->{fin}')
        print (f'2:{intermedio} -> {fin}')
        
    else:
        hanoi(num_discos - 1, inicio, intermedio)
        print(f'{num_discos}:{inicio} ->{fin}')
        hanoi(num_discos - 1, intermedio, fin)
        
        
        
hanoi(5)