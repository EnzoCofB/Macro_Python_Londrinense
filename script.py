import pyautogui # SERVE PARA IDENTIFICAÇÃO DE EVENTOS NO COMPUTADOR
import keyboard # BIBLIOTECA PARA IDENTIFICAR EVENTOS DO TECLADO
altura = 600 # CRIAÇÃO DA VARIAVEL ALTURA
largura = 500 # CRIAÇÃO DA VARIAVEL LARGURA
captura =(360, 320, altura, largura) # CRIAÇÃO DA VARIAVEL COM OS VALORES A SEREM TIRADOS DA FOTO, COM OS PRIMEIROS VALORES SENDO X E Y DA REGIÃO INICIAL DA CAPTURA
ecra = pyautogui.screenshot(region=captura) # CRIAÇÃO DA VARIAVEL QUE TIRARÁ A FOTO

def identifica_vermelho(imagem): # FUNÇÃO QUE IDENTIFICARÁ OS PIXEIS VERMELHOS
    altura_imagem , largura_imagem = imagem.size
    for x in range(0, altura_imagem): # PERCORRENDO TODA A DISTANCIA PELO CAMINHO X(ALTURA)
        for y in range(0, largura_imagem): # PERCORRENDO TODA A DISTANCIA PELO CAMINHO Y(LARGURA)
            if imagem.getpixel((x, y)) == (255, 0, 0): # COMPARAÇÃO DENTRO DO ESPAÇO CARTESIANO PARA SABER QUAL A COR DO PIXEL DA IMAGEM(NO CASO VERMELHO)
                return x, y # CASO A CONDIÇÃO ACIMA OCORRA, RETORNARÁ OS VALORES DE X E Y
    
while not keyboard.is_pressed('m'): # ENQUANTO NÃO APERTAR A TECLA 'M', O CÓDIGO ABAIXO CONTINUARÁ RODANDO
    pixel_vermelho = identifica_vermelho(ecra) # VARIAVEL QUE RECEBERA O VALOR SE EXISTIR PIXEL VERMELHO NA IMAGEM FOTOGRAFADA
    if pixel_vermelho: # CASO SEJA UM PIXEL VERMELHO, REALIZA O CÓDIGO ABAIXO
        pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1]) # SE DIRECIONA PARA O PIXEL VERMELHO
        pyautogui.mouseDown() # E LOGO APÓS MEXE O MOUSE PARA BAIXO
    pyautogui.sleep(0.016) # TEMPO DE PAUSA ENTRE AS REPETIÇÕES
    ecra = pyautogui.screenshot(region=captura) # TIRAR OUTRA FOTO PARA RECOMEÇAR O LOOP
#pyautogui.moveTo(largura,altura, duration=0.1)