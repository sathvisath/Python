#Operator precedence describes the order in which operations are performed.

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))

print((6+8)-12/2+(13-1))    #expressions inside parentheses are being evaluated first

#Multiplication "*" has higher precedence than addition "+"
print(100 + 5 * 3)

#Addition "+" and subtraction "-" has the same precedence, so we evaluate the expression from left to right
print(5 + 4 - 7 + 3)

""" This is the order of operator presedence
()	
**	
+x  -x  ~x		
*  /  //  %		
+  -		
<<  >>		
&		
^	
|	
==  !=  >  >=  <  <=  is  is not  in  not in 		
not	
and		
or 
"""