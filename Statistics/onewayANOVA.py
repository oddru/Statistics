#One Way Anova

from scipy.stats import f

#Tables

col = []

col_input = int(input("Enter Amount of Columns: "))

for i in range(col_input):
    print("|Column {0}|".format(i+1))
    colValue_input = int(input("Enter Amount of Values in Column {0}: ".format(i+1)))
    col_values = []
    for j in range(colValue_input):
        nxtCol_input = int(input(f"Enter Value {j+1}: "))
        col_values.append(nxtCol_input)
    col.append(col_values)

print(f"Table: {col}")

#Pre-Requisites

sumOfX = []
sumOfX_sqrd = []

for col_values in col:
    sumOfX_2 = sum(col_values)
    sumOfX_sqrd_2 = sum(x**2 for x in col_values)
    sumOfX.append(sumOfX_2)
    sumOfX_sqrd.append(sumOfX_sqrd_2)

print(f"X: {sumOfX}")
print(f"X Squared: {sumOfX_sqrd}")

#Formulas 

#F Distribution
alpha = float(input("Alpha (α): "))

def getCritValue(DFbt, DFwt, alpha):
    return f.ppf(1 - alpha, DFbt, DFwt)

DFbt = col_input - 1
DFwt = sum(len(col_values) for col_values in col) - col_input

crit_val = getCritValue(DFbt, DFwt, alpha)

print(f"Critical Value: {crit_val:.2f}")

#Sources of Variation 

def SSbt()