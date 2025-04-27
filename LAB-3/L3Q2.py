
def to_lower_case(s):
    result = ''
    for char in s:
        
        if 'A' <= char <= 'Z':
            
            result += chr(ord(char) + 32)
        else:
            
            result += char
    return result

def to_upper_case(s):
    result = ''
    for char in s:
        
        if 'a' <= char <= 'z':
            
            result += chr(ord(char) - 32)
        else:
            
            result += char
    return result


def toggle_case(s):
    result = ''
    for char in s:
        
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            
            result += char
    return result


input_string = "Maitrak"

print("Original:", input_string)
print("Lowercase:", to_lower_case(input_string))
print("Uppercase:", to_upper_case(input_string))
print("Toggled case:", toggle_case(input_string))
