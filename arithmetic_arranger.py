import time


def arithmetic_arranger():
  print('Hello, and welcome'); time.sleep(0)
  print('Please, insert problems in "x+y" format'); time.sleep(0)
  print('Add multiple problems via ["x+y", "a+b"]'); time.sleep(0)
    
  ar = []
  
  data = input('Insert problems now: ')
  ar.append(data)
  print(ar)


arithmetic_arranger()
