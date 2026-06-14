
def main():
    key = input("Enter the text: ")
    method = input("Enter the method ((e)encrypt/(d)decrypt): ")
    shift = int(input("Enter the shift value: "))
    print(caesar(key,shift,method))
    # pass 
def caesar(key,shift,mode):
    '''ASCII values:
    65 to 90 for uppercase letters
    97 to 122 for lowercase letters
    '''
    result = ""
    if mode not in ['e','d']:
        return "Invalid method"
    if mode != 'e':
        shift = -shift
    for i in key:
        if i.isupper():
            result += chr(((ord(i)-65+(shift))%26)+65)
        elif i.islower():
            result += chr(((ord(i)-97+(shift))%26)+97)
        else :
            result+=i
           
    return f"the text you need is {result}"
    # pass

main()