import re, time
start_time = time.time()
# with open('input.txt', 'r') as file:
#     # Read the entire content of the file
#     sample = file.read().splitlines() 

sample = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
lockPosition = int(50)
zeroCounter = int(0)

for rotations in sample:
    # like all good programmers, i've stolen the regex code below from someone online
    if re.findall("[a-zA-Z]+", rotations)[0] == 'L':
        # decrease value
        number = re.findall("[0-9]+", rotations)
        result = lockPosition - int(number[0])
        if 0 <= result <= 99:
            lockPosition = result
        else:
            lockPosition = result + 100

    else:
        # increase value
        number = re.findall("[0-9]+", rotations)
        result = lockPosition + int(number[0])
        if 0 <= result <= 99:
            lockPosition = result
        else:
            lockPosition = result - 100

    if lockPosition == 0:
        zeroCounter = zeroCounter + int(1)


print('The code is:', zeroCounter)
print("--- %s seconds ---" % (time.time() - start_time))
