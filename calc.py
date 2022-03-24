
class C():      # Cálculos

    def concat(lista):  #concatena lista recibida
        conc = lista[0]+'.'+lista[1]+'.'+lista[2]+'.'+lista[3]
        return conc


    def dec_a_hexad(decimal):   #convierte decimal a hexadecimal
        contador = 1
        a_concatenar = []
        while contador != 5:    #bloque que toma un byte
            byte = ''
            for i in decimal:

                if i == '.':
                    break

                byte = byte+i
            
            hexadecimal = hex(int(byte))
            hexadecimal = str(hexadecimal[2:].upper())
            if len(hexadecimal) < 2:
                hexadecimal = '0'+hexadecimal
            a_concatenar.append(hexadecimal)
            decimal = decimal[len(byte)+1:] #se recorre al siguiente byte
            contador+=1
        
        return C.concat(a_concatenar)


    def dec_a_bin(decimal): #convierte de decimal a binario
        contador = 1
        a_concatenar = []
        while contador != 5:
            byte = ''
            for i in decimal:
                if i == '.':
                    break
                byte = byte+i

            dec = int(byte)
            
            binario = 0
            i=0
            while(dec>0):
                digito = dec%2
                dec = int(dec/2)
                binario = binario+digito*(10**i)
                i+=1
            binario = str(binario)
            if len(binario) < 8:
                while len(binario) < 8:
                    binario = '0'+binario
            a_concatenar.append(binario)
            decimal = decimal[len(byte)+1:]
            contador+=1

        return C.concat(a_concatenar)

    
    def bin_a_dec(binario): #convierte de binario a decimal
        contador = 1
        a_concatenar = []
        
        while contador != 5:
            byte = ''
            for i in binario:
                if i == '.':
                    break
                byte += i

            indice = 0
            decimal = 0
            byte = byte[::-1]
            for x in byte:
                opera = 2**indice
                decimal += int(x)*opera
                indice+=1
            a_concatenar.append(str(decimal))
            binario = binario[len(byte)+1:]
            contador+=1
        
        return C.concat(a_concatenar)


    def broadcast(dir,prefSubR):
        ldir = list(dir)
        numbit = 0
        indice = 0
        for i in ldir:
            if i == '.':
                indice+=1
                continue
            
            elif numbit >= prefSubR:
                ldir[indice] = '1'

            numbit+=1
            indice+=1

        strDir = ''.join(ldir)
        return strDir


    def netmask(dir, prefSubR): #calcula netmask
        ldir = list(dir)
        numbit = 0
        indice = 0
        for i in ldir:
            if i == '.':
                indice+=1
                continue
            
            elif numbit < prefSubR:
                ldir[indice] = '1'

            else:
                ldir[indice] = '0'

            numbit+=1
            indice+=1

        strDir = ''.join(ldir)
        return strDir


    def wildcard(dir,prefSubR): #cálculo de wildcard
        ldir = list(dir)
        numbit = 0
        indice = 0
        for i in ldir:
            if i == '.':
                indice+=1
                continue
            
            elif numbit < prefSubR:
                ldir[indice] = '0'

            else:
                ldir[indice] = '1'

            numbit+=1
            indice+=1

        strDir = ''.join(ldir)
        return strDir

    
    def network(dir,prefSubR):  #cálculo de network
        ldir = list(dir)
        numbit = 0
        indice = 0
        for i in ldir:
            if i == '.':
                indice+=1
                continue
            
            elif numbit >= prefSubR:
                ldir[indice] = '0'

            numbit+=1
            indice+=1

        strDir = ''.join(ldir)
        return strDir


    def max_minHost(dir,prefSubR,min): #cálculo de host máximo y mín
        ldir = list(dir)
        if min:
            ldir[-1] = '1'

        else:
            if prefSubR != 32:
                numbit = 0
                indice = 0
                for i in ldir:
                    if i == '.':
                        indice+=1
                        continue
                    
                    elif numbit >= prefSubR:
                        ldir[indice] = '1'

                    numbit+=1
                    indice+=1
                ldir[-1] = '0'
            
        strDir = ''.join(ldir)
        
        return strDir 


    def clasifica(num):     #clasifica las redes
            num = int(num)
            if num <= 127:
                clase = 'A'
            elif num >=128 and num <=191:
                clase = 'B'
            elif num >=192 and num <= 223:
                clase = 'C - Private network'
            elif num >= 224 and num <= 239:
                clase = 'D - Multicast'
            else:
                clase = 'Experimental network'

            return clase
