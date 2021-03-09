#####################################################
# Computer Project #5
# Neil Kim
# Algorithms
# Make definitions for different types of functions
# Asks to input text
# Prompt for inputs
# Using the text spits out information
# Display the calculations
#####################################################
def open_file():
    # This function takes no parameters, and then uses the try-except format to prompt for a filename,
    # open the data file and return the file pointer if successful.
    x = 1
    while x != 0:
        try:
            file = input("Input a file name: ")
            open(file, 'r')
            x = 0
        except FileNotFoundError:
            x += 1
    pass


def get_us_value(fp):
    #The value for the overall United States MMR coverage is in the line with the label “United
    #States”. Find and return that value.
    filelist = []
    fp.readline()
    fp.readline()
    for line in fp:
        linelist = line.split()
        filelist.append(linelist)
    x = 0
    while x != -1:
        if filelist[x][0] == 'United':
            if filelist[x][1] == 'States':
                value = float(filelist[x][2])
                return value
        else:
            x += 1

def get_min_value_and_state(fp):
    #This function should return the minimum value in the file and the associated state. Read the
    #file line-by-line, use slicing to extract the “state” and value.
    filelist = []
    fp.readline()
    fp.readline()
    for line in fp:
        linelist = line.split()
        filelist.append(linelist)
    minlist = []
    namelist = []
    for y in range(0, 55):
        numlist = filelist[y][len(filelist[y]) - 1]
        statelist = filelist[y][0]
        minlist.append(numlist)
        namelist.append(statelist)
    minlist.sort()
    fulllist = [namelist[51], float(minlist[0])]
    return fulllist

def get_max_value_and_state(fp):
    #This function should return the maximum value in the file and the associated state.
    filelist = []
    fp.readline()
    fp.readline()
    for line in fp:
        linelist = line.split()
        filelist.append(linelist)
    minlist = []
    namelist = []
    for y in range(0, 55):
        numlist = filelist[y][len(filelist[y]) - 1]
        statelist = filelist[y][0]
        if filelist[y][1].isalpha():
            statelist += ' ' + (filelist[y][1])
        minlist.append(numlist)
        namelist.append(statelist)
    minlist.sort()
    fulllist = [namelist[29], float(minlist[len(minlist) - 4])]
    return fulllist

def display_herd_immunity(fp):
    #This function displays all the states whose coverage is less than 90%, the minimal value needed
    #for measlesherdimmunity.
    filelist = []
    fp.readline()
    fp.readline()
    for line in fp:
        linelist = line.split()
        filelist.append(linelist)
        if linelist[len(linelist) - 1] == 'NA':
            filelist.remove(linelist)
    minlist = []
    x = -1
    print('\nStates with insufficient Measles herd immunity.')
    print("{:<25s}{:>5s}".format('State', 'Percent'))
    for y in range(0, 52):
        numlist = float(filelist[y][len(filelist[y]) - 1])
        statelist = filelist[y][0]
        minlist.append(numlist)
        if filelist[y][1].isalpha():
            statelist += ' ' + filelist[y][1]
        if minlist[x] < 90:
            minlist[x] = str(minlist[x])
            print("{:<25s}{:>5s}".format(statelist, minlist[x]))
            return "{:<25s}{:>5s}".format(statelist, minlist[x])


def write_herd_immunity(fp):
    #This function writes into a file named herd.txt all the states whose coverage is less than 90%,
    #the minimal value needed for measles herd immunity.
    file = open('herd.txt', 'w')
    fp.seek(0)
    fp.readline()
    fp.readline()
    file.write('\nStates with insufficient Measles herd immunity.')
    file.write("\n{:<25s}{:>5s}".format('State', 'Percent'))
    for line in fp:
        states = line[:25].strip()
        percentage = line[25:].strip()
        if percentage == 'NA':
            continue
        percentage = float(line[25:])
        if percentage < 90:
            s = states
            p = percentage
            file.write('\n{:<25s}{:>5.1f}'.format(s, p) + '%')
    file.write('\n')
    file.close()


def main():
    #In main() begin by calling open_file() to get the file pointer. Then read the header line
    #and display it. Finally, call the other functions to extract, calculate and print values.
    open_file()
    fp = open('MMR.txt', 'r')
    x = fp.readline()
    print('\n' + x)
    fp.close()
    fp = open('MMR.txt', 'r')
    x = get_us_value(fp)
    print('Overall US MMR coverage: ' + str(x) + '%')
    fp.close()
    fp = open('MMR.txt', 'r')
    x = get_min_value_and_state(fp)
    print('State with minimal MMR coverage: ' + x[0] + ' ' + str(x[1]) + '%')
    fp.close()
    fp = open('MMR.txt', 'r')
    x = get_max_value_and_state(fp)
    print('State with maximum MMR coverage: ' + x[0] + ' ' + str(x[1]) + '%')
    fp.close()
    fp = open("MMR.txt")
    write_herd_immunity(fp)
    fp.close()
    fp = open('herd.txt', 'r')
    for line in fp:
        line = line.strip()
        print(line)
    fp.close()

if __name__ == "__main__":
    main()
