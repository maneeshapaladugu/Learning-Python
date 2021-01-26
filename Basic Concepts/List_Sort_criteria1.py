# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

#sort the list based on length of elements in ascending order
cars.sort(key=myFunc)
print(cars)
