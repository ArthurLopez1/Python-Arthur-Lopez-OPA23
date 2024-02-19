##___0. Pythagorean theorem (*)

#0. Pythagorean theorem (*)
#a)   A right angled triangle has the catheti: a = 3 and b = 4 length units. 
#Compute the hypothenuse of the triangle. (*)

#For this exercise I'm using the Pythagorean Theorem: a2 + b2 = c2

catheti_a = 3
catheti_b = 4

square_a = catheti_a **2
square_b = catheti_b **2

x = square_a + square_b

hypothenuse_c = x **.5

#print(x)
#print(hypothenuse_c)


#------------------------------------------------------------


# b)  A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. 
#Compute the other cathetus and round to one decimal. (*)


hyp_a = 7.0
cath_a = 5.0

x = (hyp_a**2) - (cath_a**2)
cath_b = round(x**.5,1)
#print(cath_b)


##___2. Classification accuracy (*)

#A machine learning algorithm has been trained to predict whether or not it would rain the next day. 
#Out of 365 predictions, it got 300 correct, compute the accuracy of this model.

total_predictions = 365
correct_predictions = 300
accuracy = correct_predictions / total_predictions 
#print(f"The accurary of the model is {accuracy:.4f} or {accuracy * 100:.2f}%")


#3. Classification accuracy (*)

TP = 2
FP = 2
FN = 11
TN = 985

accuracy = (TP + TN) / (TP+TN+FP+FN)

#print(f"The accuracy of this model is {accuracy:.4f} or {accuracy*100:.2f}%")


##___4.Line
#Compute the slope 'k' and the constant term 'm' of this line using the points A(4,4) and B(0,1)    

x1, y1 = 4, 4
x2, y2 = 0, 1

slope_k = (y2-y1)/(x2-x1)

constant_m = y1-slope_k*x1
    
print(f"The equation of the line is: y = {slope_k}x + {constant_m}")



#"___5. Euclidean distance(*)

#The Euclideam distance between the points P1 and P2 is the length of a line between them. 
#Let  and  and compute the distance between them.