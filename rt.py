def calculate(r,unit,arr,n):
	if arr is None or n == 0:
		return -1
	totalFoodRequired = r * unit
	FoodTillNow = 0
	
	for house in range(n):
		FoodTillNow+=arr[house]
		if FoodTillNow >= totalFoodRequired:
			return house+1
	return 0
	
	
r = int(input("Enter no of rats"))

unit = int(input("Enter value of units"))

n = int(input("Enter no of elements in an array"))

arr = list(map(int,input("List the elements with space seperator").split()))

print(calculate(r,unit,arr,n))
		
