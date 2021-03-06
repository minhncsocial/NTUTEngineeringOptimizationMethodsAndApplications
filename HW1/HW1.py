# Define GOLDEN RATIO
GOLDEN_RATE = 0.3819660113; #(3 - sqrt(5)) / 2

# Define function
def fx(x):
	return x**4 - 14*x**3 + 60*x**2 - 70*x;

# Define absolute function
def abs(number):
	if number < 0:
		return -number;
	else:
		return number;

# Define function solve function func in range [startValue, endValue], result error is less than epsion
def minFGoldenSection(func, startValue, endValue, epsilon):
	if abs(endValue - startValue) < epsilon:
		return startValue;
	else:
		deltaGoldenValue = (endValue-startValue)*GOLDEN_RATE;
		midValue1 = startValue + deltaGoldenValue;
		midValue2 = endValue - deltaGoldenValue;
		if func(midValue1) < func(midValue2):
			return minFGoldenSection(func, startValue, midValue2, epsilon);
		else:
			return minFGoldenSection(func, midValue1, endValue, epsilon);


# Main program
print("Solve f(x) | 0<x<2 : X = ",minFGoldenSection(fx, 0, 2, 0.3));