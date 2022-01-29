def ds_e1(a1, a2):
    
    # Exercise 1 - create a list by picking an odd-index items from the first list and even index items from the second
    
    a3 = []
    i = j = 0
    while i < len(a1):
        if i % 2 != 0:
            a3.append(a1[i])
        i += 1

    while j < len(a2):
        if j % 2 == 0:
            a3.append(a2[j])
        j += 1

    return a3
                        


def list_e1(a1):
    
    #Exercise 1 - Reverse a list

    reval = []
    for i in range(len(a1) - 1, -1, -1):
        reval.append(a1[i])

    return reval

def dict_e1(keys, values):
    
    # Exercise 1 - Covert two lists into a dictionary

    dictionary = {keys[0] : values[0]}
    
    for i in range(1, len(keys)):
        dictionary.update([(keys[i], values[i])])

    return dictionary

def set_e1(set1, list1):
    
    # Exercise 1 - add a list of elements to a set
    
    for i in range(len(list1)):
        set1.update([list1[i]])
    
    return set1

def tuple_e1(tuple1):

    # Exercise 1 - reverse the tuple
    tuple2 = ()
    tuple2 = tuple1[::-1]

    return tuple2

def dt_e1():

    # Exercise 1 -  print current date and time

    import datetime
    print(datetime.datetime.now())

    print(datetime.datetime.now().time())

    return 0


if __name__ == "__main__":

# boilerplate code to avoid Script issues

    # arr1 = [3,2,5,62,3,4,2134,2]
    # arr2 = [54,2,12,3,4134,123]
    # print(ds_e1(arr1, arr2))

    # a1 = [1, 2, 3, 4, 5]
    # print(list_e1(a1))

    # keys = ['key 1', 'key 2', 'key 3']
    # values = [10, 20, 30]
    # print(dict_e1(keys, values))

    # set1 = {"jan", "feb"}
    # list1 = ["march", "april"]
    # print(set_e1(set1, list1))

    # tuple1 = (10, 20, 30)
    # print(tuple_e1(tuple1))

    # dt_e1()


