verifiedSenders = ["callcenter@bdo.com.ph", "customercare@landbank.com", "customercare@metrobank.com.ph", "customerassistance@toyota.com.ph", "service@intl.paypal.com"]
keywords = ["Buy Now", "Urgent", "Account", "Payment", "Verify", "Important", "http://", "Link", "Unsubscribe", "Subscribe"]

# The Input
#userInput = input("What is the pattern: ")
userInput = """
From: callcenter@bdo.com.ph
"Dear customer, your recent transaction has been successfully processed."
"""
result = "" 

# To avoid loop of senderVerifier and checkKeywords na functions
attemptsToVerify = 0

# Verify sender identity
def senderVerifier():
    global result
    if any(sender in userInput for sender in verifiedSenders) and attemptsToVerify == 0:
        result += "legit"
        checkKeywords()
    elif attemptsToVerify == 1:
        result += "true"
        checkDomain()
    else:
        result += "false"

# If naay potential phishing words sa input
def checkKeywords():
    global attemptsToVerify
    global result
    
    for phishingWord in keywords:
        if phishingWord in userInput:
            if attemptsToVerify == 0:
                attemptsToVerify += 1
                result += ''.join(phishingWord.lower().split())
                senderVerifier()
    if attemptsToVerify == 0:
        result += "link"

# Check if domain is valid
def checkDomain():
    global result
    if "https://" in userInput:
        result += "https://"
    elif "http://" in userInput:
        result += "http://"

# Check the status sa conditions
senderIdentity = senderVerifier()
senderStatus = senderIdentity != "scammer"

print(result)