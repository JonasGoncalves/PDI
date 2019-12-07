#!/usr/bin/python3
import math
import numpy as np
import cv2
import os 
import statistics
import pyfiglet


def opcoes():
    while True:
        options = {}
        options['1'] = "Ler Imagem"
        options['2'] = "Converter Para YIQ"
        options['3'] = "Converter YIQ Para RGB"
        options['4'] = "Negativo da Imagem"
        options['5'] = "Brilho Multiplicativo"
        options['6'] = "Filtro de Mediana"
        options['7'] = "Negativo em Y"
        options['8'] = "Brilho Multiplicativo em Y"
        options['9'] = "Convolução"
        options['10'] =  "Filtro do Filtro da Mediana"
        options['11'] = "MonoCromatica"
        options['12'] = "Bandas Individual"
        print(pyfiglet.figlet_format("PDI"))
        print("###########################")
        print("O Que Deseja Fazer :")
        for option in options:
            print(option + ". " +options[option])
        choice = input("Escolha Uma Opção : ")
        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        elif choice == '3':
            return 3
        elif choice == '4':
            return 4
        elif choice == '5':
            return 5
        elif choice == '6':
            return 6
        elif choice == '7':
            return 7
        elif choice == '8':
            return 8
        elif choice == '9':
            return 9
        elif choice == 'x':
            return 'x'
        elif choice == '10':
            return 10
        elif choice == '11':
            return 11
        elif choice == '12':
            return 12
        else:
            ImprimirAlerta("Opção Invalida")
            return -1

def MudarValorByte(imagem, linha, coluna, cor, novoValor):
    if(novoValor > 255 or novoValor < 0):
        print("Valor não está entre 0 e 255 : Out of Range")
        exit(0)
    elif(linha < 0 or linha > (NumeroDeLinhas(imagem) - 1)):
        print("Linha Invalida : Out of Range")
        exit(0)
    elif(coluna < 0 or coluna > (NumeroDeColunas(imagem) - 1)):
        print("Coluna Invalida : Out of Range")
        exit(0)
    elif(cor != "blue" and cor != "red" and cor != "green"):
        print("Cor Invalida")
        exit(0)
    elif(cor == "blue"):
        imagem.itemset((linha, coluna, 0), novoValor)
    elif(cor == "red"):
        imagem.itemset((linha, coluna, 2), novoValor)
    elif(cor == "green"):
        imagem.itemset((linha, coluna, 1), novoValor)

def opcoes():
    while True:
        options = {}
        options['1'] = "Ler Imagem"
        options['2'] = "Converter Para YIQ"
        options['3'] = "Converter YIQ Para RGB"
        options['4'] = "Negativo da Imagem"
        options['5'] = "Brilho Multiplicativo"
        options['6'] = "Filtro de Mediana"
        options['7'] = "Negativo em Y"
        options['8'] = "Brilho Multiplicativo em Y"
        options['9'] = "Convolução"
        options['10'] =  "Filtro do Filtro da Mediana"
        options['11'] = "MonoCromatica"
        options['12'] = "Bandas Individual"
        print(pyfiglet.figlet_format("PDI"))
        print("###########################")
        print("O Que Deseja Fazer :")
        for option in options:
            print(option + ". " +options[option])
        choice = input("Escolha Uma Opção : ")
        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        elif choice == '3':
            return 3
        elif choice == '4':
            return 4
        elif choice == '5':
            return 5
        elif choice == '6':
            return 6
        elif choice == '7':
            return 7
        elif choice == '8':
            return 8
        elif choice == '9':
            return 9
        elif choice == 'x':
            return 'x'
        elif choice == '10':
            return 10
        elif choice == '11':
            return 11
        elif choice == '12':
            return 12
        else:
            ImprimirAlerta("Opção Invalida")
            return -1

def LerImagem(caminhoImagem = ""):
    while True:
        if not caminhoImagem:
            fileName =  input("Digite O Nome da Imagem com Extensão : ")
        if not os.path.isfile(fileName):
            ImprimirAlerta("O Arquivo " + fileName + " Não Existe .")
            caminhoImagem = ""
        else:
            img = cv2.imread(fileName, cv2.IMREAD_ANYCOLOR)
            ImprimirAlerta("Imagem encontrada Com Sucesso.")
            return img

def Truncar(valor):
    valor = math.trunc(valor)
    if(valor > 255):
        return 255
    elif(valor < 0):
        return 0
    return valor

def MostrasImagem(imagem, tituloJanela):
    cv2.imshow(tituloJanela, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def CriaMatriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            linha.append(0)
        matriz.append(linha)
    return matriz

def NumeroDeLinhas(img):
    return img.shape[0]

def NumeroDeColunas(img):
    return img.shape[1]

def ValorDoByte(imagem, linha, coluna, cor):
    if(linha < 0 or linha > (NumeroDeLinhas(imagem) - 1)):
        print("Linha Invalida : Out of Range")
        exit(0)
    elif(coluna < 0 or coluna > (NumeroDeColunas(imagem) - 1)):
        print("Coluna Invalida : Out of Range")
        exit(0)
    elif(cor != "blue" and cor != "red" and cor != "green"):
        print("Cor Invalida")
        exit(0)
    elif(cor == "blue"):
        return imagem[linha, coluna, 0]
    elif(cor == "green"):
        return imagem[linha, coluna, 1]
    elif(cor == "red"):
        return imagem[linha, coluna, 2]

def Convolucao(imagem,lPivo, cPivo):
    red = 0
    blue = 0
    green = 0
    cont1 = 0
    cont2 = 0
    #mMask = linhaMask
    #nMask = colunaMask
    #leitura do arquivo
    arq = open('mascara.txt','r')
    mascara = arq.read()
    arq.close()

    matriz_mascara = mascara.split( )
    tamanho_mascara = len(matriz_mascara)

    linhaMask = int(matriz_mascara.pop(0))
    colunaMask = int(matriz_mascara.pop(0))

    matriz = CriaMatriz(linhaMask,colunaMask)
    k = 0
    for i in range (linhaMask):
        for j in range (colunaMask):
            matriz[i][j] = float(matriz_mascara[k])
            k = k + 1
            
    #Rebatendo a mascara
    matriz = matriz[::-1]

    for i in range(len(matriz)):
        matriz[i] = matriz[i][::-1]

    maskTeste = matriz 

    #Tamanho minimo de uma matriz eh 1x1
    if(linhaMask < 1) or (colunaMask < 1):
        print("Tamanho da mascara invalida")
        return 0

    #Primeira posicao do pivo eh no (0,0)
    if(lPivo < 0) or (cPivo < 0):
        print("Posicao do pivo invalida")
        return 0

    #Verifica de o pivo esta dentro da mascara
    if(lPivo > (linhaMask-1)) or (cPivo > (colunaMask-1)):
         print("Posicao do pivo invalida")
         return 0
        
    #Copia da imagem, nLinhas e nColunas
    imgMedia = imagem.copy()
    mImg = NumeroDeLinhas(imagem)
    nImg = NumeroDeColunas(imagem)

    #Verifica se a mascara eh menor que a imagem
    if(linhaMask > mImg) or (colunaMask > nImg):
        print("Mascara maior que a imagem. Impossivel fazer sem extensao por zero")
        return 0
    
    #Calcula a distancia do PIVO ate as bordas da MASCARA
    dPivL0 = lPivo - 0
    dPivLm = (linhaMask-1) - lPivo
    dPivC0 = cPivo - 0
    dPivCn = (colunaMask-1) - cPivo

    #Laço para percorrer toda a imagem
    for i in range(0, mImg):
        for j in range(0, nImg):
            #Calcula a distacia do PIXEL ATUAL ate as bordas da IMAGEM
            dImgL0 = i - 0
            dImgLm = (mImg-1) - i
            dImgC0 = j - 0
            dImgCn = (nImg-1) - j

            #Verifica se as distancias do PIXEL ATUAL ate as bordas da IMAGEM eh menor do que a distancia do PIVO ate as bordas da MASCARA
            if (dImgL0 < dPivL0) or (dImgLm < dPivLm) or (dImgC0 < dPivC0) or (dImgCn < dPivCn):
                MudarValorByte(imgMedia, i, j, "red", 0)
                MudarValorByte(imgMedia, i, j, "blue", 0)
                MudarValorByte(imgMedia, i, j, "green", 0)
                continue
            
            #Percorre um "pedaço" da imagem (de acordo com o tamanho da mascara) e acumula o valor dos pixel nessa região
            for a in range(i - dPivL0, i + dPivLm +1):
                for b in range(j - dPivC0, j + dPivCn + 1):
                    red = red + (ValorDoByte(imagem, a, b, "red")* (maskTeste[cont1][cont2]))
                    blue = blue + (ValorDoByte(imagem, a, b, "blue") *(maskTeste[cont1][cont2]))
                    green = green + (ValorDoByte(imagem, a, b, "green") *(maskTeste[cont1][cont2]))
                    cont2 +=1
                cont2 = 0
                cont1 +=1

            red = Truncar(float(abs(red)))
            blue = Truncar(float(abs(blue)))
            green = Truncar(float(abs(green)))

            #Atualiza o valor do pixel i,j
            MudarValorByte(imgMedia, i, j, "red", red)
            MudarValorByte(imgMedia, i, j, "blue", blue)
            MudarValorByte(imgMedia, i, j, "green", green)
            
            #Reseta as variavies para a proxima iteração
            red = 0
            blue = 0
            green = 0
            cont1 = 0
            cont2 = 0
    
    return imgMedia

def BrilhoMultiplicativo(imagem, fatorMultiplicativo):
    saida = imagem.copy()
    if(fatorMultiplicativo < 0):
        ImprimirAlerta("O fator multiplicativo precisa ser um número real maior que 0.")
        saida = []
        return saida
    
    for linha in range(NumeroDeLinhas(imagem)):
        for coluna in range(NumeroDeColunas(imagem)):
            red = Truncar(ValorDoByte(imagem, linha, coluna, "red") * fatorMultiplicativo)
            blue = Truncar(ValorDoByte(imagem, linha, coluna, "blue") * fatorMultiplicativo)
            green = Truncar(ValorDoByte(imagem, linha, coluna, "green") * fatorMultiplicativo)

            MudarValorByte(saida, linha, coluna, "red", red)
            MudarValorByte(saida, linha, coluna, "blue", blue)
            MudarValorByte(saida, linha, coluna, "green", green)

    return saida

def BrilhoMultiplicativoY(imagem, fatorMultiplicativo):
    saida = imagem.copy()
    if(fatorMultiplicativo < 0):
        ImprimirAlerta("O fator multiplicativo precisa ser um número real maior que 0.")
        return []
    
    for linha in range(NumeroDeLinhas(imagem)):
        for coluna in range(NumeroDeColunas(imagem)):
            red = Truncar(ValorDoByte(imagem, linha, coluna, "red") * fatorMultiplicativo)

            MudarValorByte(saida, linha, coluna, "red", red)
    return ConverteYIQ_RGB(saida)

def ConverteRGB_YIQ(imagem):
    imgYIQ = imagem.copy()

    for k in range(NumeroDeLinhas(imagem)):
        for j in range(NumeroDeColunas(imagem)):

            r = ValorDoByte(imagem, k, j, "red")
            g = ValorDoByte(imagem, k, j, "green")
            b = ValorDoByte(imagem, k, j, "blue")

            y = Truncar((0.299 * r) + (0.587 * g) + (0.114 * b))
            i = Truncar((0.596 * r) - (0.274 * g) - (0.322 * b))
            q = Truncar((0.211 * r) - (0.523 * g) + (0.312 * b))

            MudarValorByte(imgYIQ, k, j, "red", y)
            MudarValorByte(imgYIQ, k, j, "green", i)
            MudarValorByte(imgYIQ, k, j, "blue", q)

    return imgYIQ

def ConverteYIQ_RGB(imagem):
     
    imgRGB = imagem.copy()

    for linha in range (NumeroDeLinhas(imagem)):
        for coluna in range (NumeroDeColunas(imagem)):

            y = ValorDoByte(imagem, linha, coluna, "red")
            i = ValorDoByte(imagem, linha, coluna, "green")
            q = ValorDoByte(imagem, linha, coluna, "blue")

            r = Truncar((1.000 * y) + (0.956 * i) + (0.621 * q))
            g = Truncar((1.000 * y) - (0.272 * i) - (0.647 * q))
            b = Truncar((1.000 * y) - (1.106 * i) - (1.703 * q))

            MudarValorByte(imgRGB, linha, coluna, "red", r)
            MudarValorByte(imgRGB, linha, coluna, "green", g)
            MudarValorByte(imgRGB, linha, coluna, "blue", b)

    return imgRGB


def Negativo(imagem):
    #Subtrai o valor do canal por 255
    saida = imagem.copy()
    saida = 255 - saida
    return saida

def NegativoY(imagem):
    #dupla de for que vai percorrer a matriz YIQ imagem para fazer
    # a banda Y virar negativa
    converte = imagem.copy()
    #converte = ConverteRGB_YIQ(converte)
    for i in range(NumeroDeLinhas(imagem)):
        for j in range(NumeroDeColunas(imagem)):
            Y = 255 - ValorDoByte(converte, i, j, "red")
            MudarValorByte(converte, i, j, "red", Y)
        
    return ConverteYIQ_RGB(converte)

def FiltroMediana(imagem, m, n):
    saida = imagem.copy()

    if(m > NumeroDeLinhas(saida)):
        ImprimirAlerta("Filtro com muitas linhas")
        exit(0)
    elif(n > NumeroDeColunas(saida)):
        ImprimirAlerta("Filtro com muitas colunas")
        exit(0)

    iniciopivolinha = int(m/2)
    iniciopivocoluna = int(n/2)

    limitepivolinha = NumeroDeLinhas(imagem) - iniciopivolinha
    limitepivocoluna = NumeroDeColunas(imagem) - iniciopivocoluna

    for linha in range(iniciopivolinha, limitepivolinha):
        for coluna in range(iniciopivocoluna, limitepivocoluna):
            #Aplicando a máscara
            aRed = []
            aBlue = []
            aGreen = []

            x = linha - iniciopivolinha
            y = linha + iniciopivolinha+1
            z = coluna - iniciopivocoluna
            w = coluna + iniciopivocoluna+1
            
            for i in range(x, y):
                for j in range(z, w):
                    aRed.append(ValorDoByte(imagem, i, j, "red"))
                    aBlue.append(ValorDoByte(imagem, i, j, "blue" ))
                    aGreen.append(ValorDoByte(imagem, i, j, "green" ))
            
           
            newRed = statistics.median(aRed)
            newBlue = statistics.median(aBlue)
            newGreen = statistics.median(aGreen)

            MudarValorByte(saida, linha, coluna, "red", newRed)
            MudarValorByte(saida, linha, coluna, "blue", newBlue)
            MudarValorByte(saida, linha, coluna, "green", newGreen)
        
    return saida

def MonoCromatica(imagem, banda):
    
    imgMono = imagem.copy()
    bandas = ["red","blue","green"]
    
    if banda not in bandas:
        ImprimirAlerta("Banda Inválida")
        return imgMono
    
    bandas.remove(banda)

    for i in range(NumeroDeLinhas(imagem)):
        for j in range(NumeroDeColunas(imagem)):
            valor = ValorDoByte(imgMono, i, j, banda)
            MudarValorByte(imgMono, i, j, bandas[0], valor)
            MudarValorByte(imgMono, i, j, bandas[1], valor)

    return imgMono

def RGBIndividual(imagem, banda):
    imgRGB = imagem.copy()

    bandas = ["red","blue","green"]
    
    if banda not in bandas:
        ImprimirAlerta("Banda Inválida")
        return imagem
    
    bandas.remove(banda)

    for i in range(NumeroDeLinhas(imagem)):
        for j in range(NumeroDeColunas(imagem)):
            MudarValorByte(imgRGB, i, j, bandas[0], 0)
            MudarValorByte(imgRGB, i, j, bandas[1], 0)

    return imgRGB


def ImprimirAlerta(alerta):
    print("" + alerta + "")

def Menu():
    isYIQ = False
    isRGB = False
    isMediana = False
    imgComMediana = []
    yiq = []
    img = []
    while True:
        while True:
            choice = opcoes()
            if choice == 1:
                isMediana = False
                imgComMediana = []
                yiq = []
                isRGB = False
                isYIQ = False
                img = LerImagem()
                MostrasImagem(img, "Original")
                isRGB = True
            elif choice == 2:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break
                yiq = ConverteRGB_YIQ(img)
                MostrasImagem(yiq, "YIQ")
                isYIQ = True
            elif choice == 3:
                if not isYIQ:
                    ImprimirAlerta("Nenhuma Imagem YIQ Disponível. ")
                    break
                rgb = ConverteYIQ_RGB(yiq)
                MostrasImagem(rgb, "RGB")
            elif choice == 4:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break
                negativo = Negativo(img)
                MostrasImagem(negativo, "Negativo")
            elif choice == 5:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break
                fatorMult = input("Digite o Fator Multiplicativo : ")
                brilhoMult = BrilhoMultiplicativo(img, float(fatorMult) * 1.0)
                MostrasImagem(brilhoMult, "Brilho Multiplicativo")
            elif choice == 6:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break
                linhas = input("Digite o numero de Linhas : ")
                colunas = input("Digite o numero de colunas : ")
                filtroMediana = FiltroMediana(img, int(linhas), int(colunas))
                imgComMediana = filtroMediana
                isMediana = True
                MostrasImagem(filtroMediana, "Filtro Mediana")
            elif choice == 7:
                if not isYIQ:
                    ImprimirAlerta("Nenhuma Imagem YIQ Disponível. ")
                    break
                negativoY = NegativoY(yiq)
                MostrasImagem(negativoY, "NegativoY")
            elif choice == 8:
                if not isYIQ:
                    ImprimirAlerta("Nenhuma Imagem YIQ Disponível. ")
                    break
                fatorMult = input("Digite o Fator Multiplicativo : ")
                brilhoMultY = BrilhoMultiplicativoY(yiq, float(fatorMult) * 1.0)
                MostrasImagem(brilhoMultY, "Brilho Multiplicativo em Y. ")
            elif choice == 9:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break
                linha = input("Digite a linha do Pivo : ")
                coluna = input("Digite a coluna do Pivo : ")
                convolulao = Convolucao(img, int(linha), int(coluna))
                MostrasImagem(convolulao, "Convolução")
            elif choice == 10:
                if not isMediana:
                    ImprimirAlerta("Nenhum filtro com mediana foi feito. ")
                    break
                linhas = input("Digite o numero de Linhas : ")
                colunas = input("Digite o numero de colunas : ")
                imgComMediana = FiltroMediana(imgComMediana, int(linhas), int(colunas))
                MostrasImagem(imgComMediana, "Filtro do Filtro Mediana")
            elif choice == 11:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break 
                banda = input("Digite a Banda : ")
                mono = MonoCromatica(img, banda)
                MostrasImagem(mono, "MonoCromatica")
            elif choice == 12:
                if not isRGB:
                    ImprimirAlerta("Nenhuma Imagem Carregada. ")
                    break
                banda = input("Digite a Banda : ")
                rgb = RGBIndividual(img, banda)
                MostrasImagem(rgb, "RGB Individual")
            elif choice == 'x':
                print(pyfiglet.figlet_format("DA DEZ PONTO AI"))
                exit(0)



        
    
def main():
    Menu()
    #Links úteis
    #https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    #http://www.joaomatosf.com/blog/index080c.html?option=com_content&view=article&id=63&catid=36&Itemid=54
    #https://www.youtube.com/playlist?list=PLh6SAYydrIpctChfPFBlopqw-TGjwWf_8
    return 0

if __name__ == "__main__":
    main()