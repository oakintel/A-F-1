#Import the regular expression module
import re

#Define the function for arithmetic arrnagement while taking note of the status. The status could be True or False. With the latter as default
def arithmetic_arranger(problems, status = False):

#Constraint number 1	
    if (len(problems) > 5):
      return 'Error: Too many problems.'

#Curate empty variables
    first = ""
    second = ""
    lines = ""
    tots = ""
    completion = ""
  
    
#Use a loop to isolate problem sets and isolare more constraints using Regexp    
    for problem in problems:
     if (re.search("[^\s0-9.+-]", problem)):
       if (re.search("[/]", problem) or re.search("[*]", problem)):
         return "Error: Operator must be '+' or '-'."
       return "Error: Numbers must only contain digits."

#Split single problem to isolate values and operators
     valueone = problem.split(" ")[0]
     valuetwo = problem.split(" ")[2]
     operator = problem.split(" ")[1]

#Constraint number 4
     if (len(valueone)>= 5 or len(valuetwo) >= 5):
       return "Error: Numbers cannot be more than four digits."

#A conditional using operator to reach a value for the solution
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

#set up lines using the maximum length of the maximum number + 2 
# +2 is essential to create space for the operator and a space between operator & value e.g. Line 2: |+| |326|. 
# Where '| |' represents a space

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

#Print out each section line by line while using '\n' to transition into a new line	
    if status == True:
      completion = first + "\n" + second + "\n" + lines + "\n" + tots
    elif status == False: 
      completion = first + "\n" + second + "\n" + lines
    return completion
				
#Congratulations, we print the solution.
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False))
