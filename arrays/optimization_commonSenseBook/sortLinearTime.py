# Temperatures range from 97.0 degrees Fahrenheit to 99.0 degrees Fahrenheit. 
# An important point: within this application, the decimal point never goes beyond the tenths place.
# You are to write a function that sorts these readings from lowest to highest.

def sortTemperatures(temps):

    hash_tmp = {}
    for t in temps:
        if t in hash_tmp:
            hash_tmp[t] += 1
        else:
            hash_tmp[t] = 1

    temp = 970
    sortTemps = []
    while temp <= 999:

        if temp / 10 in hash_tmp:
            times = hash_tmp[temp/10]
            while times:
                sortTemps.append(temp/10)
                times-=1
        
        temp += 1

    print(sortTemps)

array = [97.5, 97.0, 99.1, 98.2, 97.0, 97.1, 97.9, 99.9, 99.1, 98.2, 97.0]


sortTemperatures(array)

array = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]

sortTemperatures(array)