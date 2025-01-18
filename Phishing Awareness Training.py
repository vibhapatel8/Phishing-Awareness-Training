import time

def display_intro():
    print("Welcome to the Phishing Awareness Training!")
    time.sleep(1)
    print("In this exercise, you will be presented with different scenarios.")
    time.sleep(1)
    print("Your task is to identify phishing attempts.")
    time.sleep(2)

def scenario_1():
    print("\nScenario 1:")
    time.sleep(1)
    print("You receive an email from your bank, stating that your account has been compromised and asking you to click a link to reset your password.")
    time.sleep(1)
    print("Options:")
    print("1. Click the link and reset the password.")
    print("2. Delete the email and contact your bank using their official website or phone number.")
    choice = input("Choose 1 or 2: ")
    if choice == "2":
        print("Correct! The email could be a phishing attempt. Always contact the institution directly.")
    else:
        print("Incorrect! This could be a phishing attempt. You should never click suspicious links.")

def scenario_2():
    print("\nScenario 2:")
    time.sleep(1)
    print("You receive a text message claiming to be from a service you use, saying that your account will be suspended unless you verify your identity by clicking a link.")
    time.sleep(1)
    print("Options:")
    print("1. Click the link to verify your account.")
    print("2. Do not click the link, and go directly to the service's official website to verify your account status.")
    choice = input("Choose 1 or 2: ")
    if choice == "2":
        print("Correct! It's safer to access your account through the official website.")
    else:
        print("Incorrect! This might be a phishing attempt. Always verify directly through official sources.")

def scenario_3():
    print("\nScenario 3:")
    time.sleep(1)
    print("You receive an urgent email from what looks like an official e-commerce site. It says you need to confirm your payment information, but it has typos and the sender's email looks suspicious.")
    time.sleep(1)
    print("Options:")
    print("1. Confirm your payment information, as the email seems urgent.")
    print("2. Delete the email and contact the e-commerce site using their official contact information.")
    choice = input("Choose 1 or 2: ")
    if choice == "2":
        print("Correct! Emails with typos and suspicious sender addresses are a red flag for phishing.")
    else:
        print("Incorrect! This email could be a phishing attempt. Always check the sender's address and avoid clicking any links in suspicious emails.")

def conclusion():
    print("\nCongratulations! You've completed the Phishing Awareness Training.")
    time.sleep(1)
    print("Remember to always be cautious when receiving unexpected communications, especially those asking for personal or financial information.")
    time.sleep(2)

def main():
    display_intro()
    scenario_1()
    scenario_2()
    scenario_3()
    conclusion()

if __name__ == "__main__":
    main()
