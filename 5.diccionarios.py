## Dictionaries

myDictionary = {
    "Spain" : "Madrid",
    "Germany"  : "Berlin",
    "France" : "Paris",
    "UK" : "London",
    "Number" : 31,
    54 : "Andres"
}

print(myDictionary)
print(myDictionary["Germany"])

## add new key-value
myDictionary["Italy"] = "Lisboa"
print(myDictionary)

## Re asign value to key
myDictionary["Italy"] = "Rome"
print(myDictionary)

## Delete key - value
del myDictionary["UK"]
print(myDictionary)

## use tuple or array for each value
myTuple=["Spain", "UK", "France", "Italy"]
myDictionary2= {
    myTuple[0]: "Madrid",
    myTuple[1]: "London",
    myTuple[2] : "Paris",
    myTuple[3] : "Rome"    
}

print(myDictionary2)

myDictionary3 = {
    23: "Jordan",
    "Name": "Michael",
    "Team" : "Chicago Bulls",
    "Rings" : {
        "temp" : [1991, 1992, 1993, 1996, 1997, 1998],
        "team": "Chicago Bulls"
    } 
}

print(myDictionary3)

## Print Rings 
print(myDictionary3["Rings"])

## print temp 
print(myDictionary3["Rings"]["temp"])

## print only keys of the dictionary
print(myDictionary3.keys())

## print values of de keys of dictionary
print(myDictionary3.values())

## print length of the dictionary
print(len(myDictionary3))