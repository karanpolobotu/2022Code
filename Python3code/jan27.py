import json
import random
import numpy

def json_e1(data):

    # Exercise 1 - convert dictionary into JSON format

    jsonData = json.dumps(data)
    return jsonData

def rng_e1():

    # Exercise 1 - Generate 3 random integers between 100 and 999 which is divisble by 5
    
    return random.randrange(100, 999, 5), random.randrange(100, 999, 5), random.randrange(100, 999, 5)

def numpy_e1():
    
    firstArray = numpy.empty([4,2], dtype = numpy.uint16) 
    print("Printing Array")
    print(firstArray)

    print("Printing numpy array Attributes")
    print("1> Array Shape is: ", firstArray.shape)
    print("2>. Array dimensions are ", firstArray.ndim)
    print("3>. Length of each element of array in bytes is ", firstArray.itemsize)
    return 0

if __name__ == "__main__":
    
    data = {"key1" : "value1", "key2" : "value2"}
    
    #print(json_e1(data))

    print(rng_e1())
