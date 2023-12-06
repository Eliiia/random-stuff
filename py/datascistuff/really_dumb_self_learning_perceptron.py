import random

def t(weight_1, weight_2, threshold):
    iterator = 0
    accuracy = []

    # try with all data points
    f = open("./data/three_numbers.txt", "r")
    for data in f.readlines():
        data = data.strip()
        data = [float(x) for x in data.split(" ")]
        
        n1 = data[0]*weight_1
        n2 = data[1]*weight_2
        n3 = int(data[2])
        out = (n1+n2) > threshold

        if out == n3: accuracy.append(True)
        else: accuracy.append(False)

        iterator = iterator + 1
    f.close()

    # return the total percentage that were successful
    return accuracy.count(True) / iterator

### Training to identify best values; through complete dumb guessing

# Start values
best_w1 = 1
best_w2 = 1
best_threshold = 1
best_accuracy = 0.0

# Iterate a max times
max = 200000
for x in range(0,max):
    w1 = random.randrange(0, 100)/100
    w2 = random.randrange(0, 100)/100
    threshold = random.randrange(0,10)/10

    accuracy = t(w1,w2,threshold)

    if accuracy > best_accuracy: 
        best_w1 = w1
        best_w2 = w2
        best_threshold = threshold
        best_accuracy = accuracy

print(f"Best settings as of {max} tries:\nw1: {best_w1}\tw2: {best_w2}\tthreshold: {threshold}\taccuracy: {accuracy}")