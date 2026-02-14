test = [1, 2, 3, 4]

result = [sum(test)]

for i in range(len(test)): 
    result.append(sum(test[:i]))

print(result)