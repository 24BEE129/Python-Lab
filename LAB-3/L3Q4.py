def remove_substring(onestring, removestring):
    if removestring in onestring:
        finalstring = onestring.replace(removestring, "")
        return finalstring
    else:
        return onestring


onestring = "abcdef"
removestring = "cd"
finalstring = remove_substring(onestring, removestring)
print(finalstring)


