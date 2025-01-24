from validate_answers import simple_assert

def validIPAddresses(string):
    validIps = []
    for i in range(1, min(len(string), 4)):
        IpParts = ['', '', '', '']
        IpParts[0] = string[:i]
        if not isValidIPs(IpParts[0]):
            continue
         
        for j in range(i+1, i+min(len(string)-i, 4)):
            IpParts[1] = string[i:j]
            if not isValidIPs(IpParts[1]):
                continue
            
            for k in range(j+1, j+min(len(string)-j, 4)):
                IpParts[2] = string[j:k]
                IpParts[3] = string[k:]
                if isValidIPs(IpParts[2]) and isValidIPs(IpParts[3]):
                    validIps.append(".".join(IpParts))
    return validIps

def isValidIPs(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False 
    return len(string) == len(str(stringAsInt))
                
    

input = "1921680"
expected = [
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0",
]
actual = validIPAddresses(input)
simple_assert(actual, expected)
