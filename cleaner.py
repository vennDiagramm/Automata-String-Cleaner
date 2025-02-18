verifiedSenders = ["callcenter@bdo.com.ph", "customercare@landbank.com", "customercare@metrobank.com.ph", "customerassistance@toyota.com.ph", "service@intl.paypal.com"]
keywords = ["Buy Now", "Urgent", "Account", "Payment", "Verify", "Important", "http://", "Link", "Unsubscribe", "Subscribe"]

# The Input
#userInput = input("What is the pattern: ")
userInput = """
Claim your FREEBIE of 1GB for surfing valid for 7 days now! Simply load a total of P90 before 02/23/2025. REF#: FGRN15
"""
userInput = ''.join(userInput.split()) 

# Verify sender identity
def senderVerifier():
    for sender in verifiedSenders:
        if sender in userInput:
            checkKeywords()
            return "legit"
    return "scammer"

# To avoid loop of senderVerifier and checkKeywords na functions
attemptsToVerify = 0

# If naay potential phishing words sa input
def checkKeywords():
    global attemptsToVerify
    for phishingWord in keywords:
        if phishingWord in userInput:
            if attemptsToVerify == 0:
                attemptsToVerify += 1
                senderVerifier()
            else:
                checkDomain()
    return "link"

# Check if domain is valid
def checkDomain():
    if userInput.startswith("https://"):
        return True
    elif userInput.startswith("http://"):
        return False


# Check the status sa conditions
senderIdentity = senderVerifier()
senderStatus = senderIdentity != "scammer"
domainStatus = checkDomain()

if not senderStatus or not domainStatus:
    print("Phishing Detected")
else:
    print("No Phishing Detected")