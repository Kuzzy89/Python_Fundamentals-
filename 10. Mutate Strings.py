string1 = input()
string2 = input()
def transform_string(string1, string2):
    output = [string1] # list to store unique output strings
    for i in range(len(string1)):
        string1 = string1[:i] + string2[i] + string1[i+1:] # replace the ith character
        if string1 not in output:
            output.append(string1)
            print(string1)

# test the function
transform_string((string1), (string2))
