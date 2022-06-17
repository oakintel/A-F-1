import re

sum = ()
length = ()
numerator = ()
denominator = ()

def arithmetic_arranger(problems, status = False):
   
    if (len(problems) > 5):
      return 'Error: Too many problems.'
    
    for problem in problems:
     if re.search("[^\s0-9.+-]", problem):
       if re.search("[/]") or re.search("[*]"):
         return('Error: Operator must be '+' or '-'.')
       return('Error: Number must only contain digits.')

     valueone = problem.split(" ")[0]
     valuetwo = problem.split(" ")[2]
     operator = problem.split(" ")[1]

     if (len(valueone) or len(valuetwo)) > 4:
       return 'Error: Numbers cannot be more than four digits'

     sum = ("")
     if operator == ("+"):
       value = str(int(valueone) + int(valuetwo))
     elif operator == ("-"):
       value = str(int(valueone) - int(valuetwo))
       
     length = max(len(valueone), len(valuetwo))
     #numerator = valueone.rjust(length)
     #denominator = operator + valuetwo.rjust(length - 1)
     #result = str(sum).rjust(length)
     #line = ()
    
    numerator += valueone.rjust(length + 2)
    denominator = operator + ' ' + valuetwo.rjust(space)
    divline = '-' * (length + 2)


      
     
     
      
       
     

       
  
#        one = problem.split(" ")[0]
#       formula = problem.split(" ")[1]
#        two = problem.split(" ")[2]
#        if len(one) or len(two) > 4:
#          return ('Error: Numbers cannot be more than four digits.')


#arithmetic_arranger()

print('Love you forever')
#print(arithmetic_arranger(["32 + 698","3801 - 2", "45 + 43", "123+49"]))
