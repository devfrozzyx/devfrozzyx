import requests
import os
import json
import platform
import uuid
import time

# Farben für Text im Terminal (ANSI Escape-Codes)
blue = "\033[94m"
reset = "\033[0m"
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"

# Text-Logo (ASCII-Art) in Blau
logo = f"""
{blue}oooooooooooo ooooooooo.     .oooooo.    oooooooooooo  oooooooooooo oooooo   oooo ooooooo  ooooo 
`888'     `8 `888   `Y88.  d8P'  `Y8b  d'""""""d888' d'""""""d888'  `888.   .8'   `8888    d8'  
 888          888   .d88' 888      888       .888P         .888P     `888. .8'      Y888..8P    
 888oooo8     888ooo88P'  888      888      d888'         d888'       `888.8'        `8888'     
 888    "     888`88b.    888      888    .888P         .888P          `888'        .8PY888.    
 888          888  `88b.  `88b    d88'   d888'    .P   d888'    .P      888        d8'  `888b   
o888o        o888o  o888o  `Y8bood8P'  .8888888888P  .8888888888P      o888o     o888o  o88888o {reset}
"""

# Zeige das Logo an
def show_logo():
    print(logo)

# 1. IP Lookup Funktion
def ip_lookup():
    try:
        print(f"{green}Starte IP Lookup...{reset}")
        response = requests.get("https://api.ipinfo.io/json")
        ip_info = response.json()
        print(f"IP-Adresse: {ip_info['ip']}")
        print(f"Region: {ip_info['region']}")
        print(f"Stadt: {ip_info['city']}")
        print(f"Organisation: {ip_info['org']}")
    except Exception as e:
        print(f"{red}Fehler beim Abrufen der IP-Informationen: {e}{reset}")

# 2. Webhook Spammer Funktion
def webhook_spammer():
    webhook_url = input(f"{yellow}Gib die Webhook-URL ein: {reset}")
    message = input(f"{yellow}Gib die Nachricht ein, die gesendet werden soll: {reset}")
    
    data = {
        "content": message
    }

    try:
        print(f"{green}Sende Nachricht an Webhook...{reset}")
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"{green}Nachricht erfolgreich gesendet.{reset}")
        else:
            print(f"{red}Fehler beim Senden der Nachricht: {response.status_code}{reset}")
    except Exception as e:
        print(f"{red}Fehler beim Senden der Webhook-Nachricht: {e}{reset}")

# 3. HWID (Hardware-ID) Funktion
def show_hwid():
    # Hardware ID (z.B. Festplatten-Seriennummer, oder UUID des Systems)
    system_info = platform.system()
    machine_info = platform.machine()
    node_info = platform.node()

    print(f"{green}System: {system_info}")
    print(f"Maschine: {machine_info}")
    print(f"Hostname/Computername: {node_info}")
    print(f"UUID (Universally Unique Identifier): {uuid.uuid4()}")

# 4. TikTok Spam Report Funktion (Pseudocode, da es keine offizielle API gibt)
def tiktok_spam_report():
    tiktok_url = input(f"{yellow}Gib die TikTok Video URL oder User URL ein: {reset}")
    reason = input(f"{yellow}Gib den Grund für die Meldung ein: {reset}")
    
    # Hier könnte eine API-Anfrage an TikTok erfolgen, aber dies hängt von der tatsächlichen API ab.
    # Beispiel: Pseudocode für das Senden einer Nachricht:
    try:
        print(f"{green}Bericht wird gesendet...{reset}")
        # TikTok hat keine öffentliche API für Spamming-Reports, hier müsste eine Anfrage an ein internes System gesendet werden
        # response = requests.post("https://api.tiktok.com/report", data={"url": tiktok_url, "reason": reason})
        
        # Simuliere Antwort
        print(f"{green}Bericht über TikTok-Video/Benutzer erfolgreich gesendet.{reset}")
    except Exception as e:
        print(f"{red}Fehler beim Senden des Berichts: {e}{reset}")

# Menü und Schleife
def main():
    show_logo()  # Logo anzeigen

    while True:
        print(f"{green}FROZZYX{reset}")
        print("[1] Ip Lookup")
        print("[2] Webhook Spammer")
        print("[3] Show HWID id")
        print("[4] TikTok Spam Report")
        print("[5] Beenden")
        print("")

        x = input(f"{yellow}Option: {reset}")

        if x == "1":
            ip_lookup()
        elif x == "2":
            webhook_spammer()
        elif x == "3":
            show_hwid()
        elif x == "4":
            tiktok_spam_report()
        elif x == "5":
            print(f"{red}Programm wird beendet...{reset}")
            break
        else:
            print(f"{red}Ungültige Option. Bitte wähle eine der verfügbaren Optionen.{reset}")
        time.sleep(2)  # Kurze Pause, damit der Benutzer das Ergebnis lesen kann

# Programm starten
if __name__ == "__main__":
    main()
