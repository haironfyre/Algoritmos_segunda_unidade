def troca(s, velho, novo):
    s = list(s)
    aux1 = 0
    aux2 = 0
    feito = False 
    if not feito:
        while (aux1 < len(s)):
            while (aux2 <= len(s)):
                if s[aux1:aux2] == list(velho):
                    s[aux1:aux2] = novo
                aux2 += 1
            aux2 = 0
            aux1  += 1
        Done = True
    s = ''.join(s) #Retira a lista de s e aspas
    return s
