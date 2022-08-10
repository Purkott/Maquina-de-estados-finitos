global RESULTADO 
global ESTADO
global contadorString 
global contadorLinhas 
global contadorArquivo 

def start():
  global arquivo
  global arquivos
  global arquivo1
  global arquivo2
  global arquivo3
  txt1 = open('arquivos/1.txt', 'r')
  arquivo1 = []
  arquivo1.append(txt1.readline().strip())
  for x in range(int(arquivo1[0])):
    arquivo1.append(txt1.readline().strip())
  txt1.close()

  txt2 = open('arquivos/2.txt', 'r')
  arquivo2 = []
  arquivo2.append(txt2.readline().strip())
  for x in range(int(arquivo2[0])):
    arquivo2.append(txt2.readline().strip())
  txt2.close()

  txt3 = open('arquivos/3.txt', 'r')
  arquivo3 = []
  arquivo3.append(txt3.readline().strip())
  for x in range(int(arquivo3[0])):
    arquivo3.append(txt3.readline().strip())
  txt3.close()
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  global contadorArquivo 
  RESULTADO = " "
  ESTADO = "ESTADO0"
  contadorString = 0
  contadorLinhas = 1
  contadorArquivo = 1
  arquivos = [arquivo1,arquivo2,arquivo3]
  arquivo = arquivo1.copy()

def estado0(arquivo):
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  if(contadorString == len(arquivo[contadorLinhas])):
    ESTADO = "COMPLETO"
    RESULTADO = "ERRO"
  else:
    if(arquivo[contadorLinhas][contadorString] == 'a'):
      ESTADO = "ESTADO1"
    else:
      ESTADO = "ESTADO3"
  contadorString = contadorString+1

def estado1(arquivo):
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  if(contadorString == len(arquivo[contadorLinhas])):
    ESTADO = "COMPLETO"
    RESULTADO = " não pertence"
  else:
    if(arquivo[contadorLinhas][contadorString] == 'b'):
      ESTADO = "ESTADO2"
    else:
      ESTADO = "ESTADO4"
  contadorString = contadorString+1

def estado2(arquivo):
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  if(contadorString == len(arquivo[contadorLinhas])):
    ESTADO = "COMPLETO"
    RESULTADO = " não pertence"
  else:
    if(arquivo[contadorLinhas][contadorString] == 'b'):
      ESTADO = "ESTADO3"
    else:
      ESTADO = "ESTADO4"
  contadorString = contadorString+1

def estado3(arquivo):
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  if(contadorString == len(arquivo[contadorLinhas])):
    ESTADO = "COMPLETO"
    RESULTADO = " pertence"
  else:
    if(arquivo[contadorLinhas][contadorString] == 'a'):
      ESTADO = "ESTADO1"
    else:
      ESTADO = "ESTADO3"
  contadorString = contadorString+1

def estado4():
  global RESULTADO 
  global ESTADO
  ESTADO = "COMPLETO"
  RESULTADO = " não pertence"

def completo(arquivo):
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  print(arquivo[contadorLinhas] + ":" + RESULTADO)
  contadorString = 0
  ESTADO = "REINICIAR"

def reiniciar():
  global contadorArquivo
  global contadorLinhas
  global arquivo
  global arquivos
  global ESTADO
  
  if(contadorLinhas == int(arquivo[0])):
    if(contadorArquivo <= 2):
      contadorArquivo = contadorArquivo+1
      arquivo = arquivos[contadorArquivo-1].copy()
      contadorLinhas = 1
      ESTADO = "ESTADO0"
    else:
      ESTADO = "FECHAR"
  else:
    contadorLinhas = contadorLinhas+1
    ESTADO = "ESTADO0"
    
    
  
start()

while(ESTADO != "FECHAR"):
  if(ESTADO == "REINICIAR"):
    reiniciar()
  elif(ESTADO == "COMPLETO"):
    completo(arquivo)
  elif(ESTADO == "ESTADO0"):
    estado0(arquivo)
  elif(ESTADO == "ESTADO1"):
    estado1(arquivo)
  elif(ESTADO == "ESTADO2"):
    estado2(arquivo)
  elif(ESTADO == "ESTADO3"):
    estado3(arquivo)
  elif(ESTADO == "ESTADO4"):
    estado4()