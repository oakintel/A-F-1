import re

def arithmetic_arranger(problems, status = False):

    if (len(problems) > 5):
      return 'Error: Too many problems.'
    
    first = ""
    second = ""
    lines = ""
    tots = ""
    completion = ""
  
    
    
    for problem in problems:
     if (re.search("[^\s0-9.+-]", problem)):
       if (re.search("[/]", problem) or re.search("[*]", problem)):
         return "Error: Operator must be '+' or '-'."
       return "Error: Numbers must only contain digits."

     valueone = problem.split(" ")[0]
     valuetwo = problem.split(" ")[2]
     operator = problem.split(" ")[1]

     if (len(valueone)>= 5 or len(valuetwo) >= 5):
       return "Error: Numbers cannot be more than four digits."

     value = ""
     if (operator == "+"):
       value = str(int(valueone) + int(valuetwo))
     elif (operator == "-"):
       value = str(int(valueone) - int(valuetwo))
       
     length = max(len(valueone), len(valuetwo)) + 2
     numerator = str(valueone).rjust(length)
     denominator = operator + str(valuetwo).rjust(length - 1)
     result = str(value).rjust(length)
     line = ""
			
     for s in range(length):
      line += "-"

			
     if  problem != problems[-1]:
       	first += numerator + '    '
       	second += denominator + '    '
       	lines += line + '    '
       	tots += result + '    '
     else:
        first += numerator 
        second += denominator
        lines += line
        tots += result

    if status == True:
      completion = first + "\n" + second + "\n" + lines + "\n" + tots
    elif status == False: 
      completion = first + "\n" + second + "\n" + lines
    return completion
				

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False))