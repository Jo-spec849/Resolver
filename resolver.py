
import argparse
import requests
import json
import socket
import openpyxl
import csv
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

# Lista de banners
banners = [
    """

$$$$$$$\                                $$\                                
$$  __$$\                               $$ |                               
$$ |  $$ | $$$$$$\   $$$$$$$\  $$$$$$\  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
$$$$$$$  |$$  __$$\ $$  _____|$$  __$$\ $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
$$  __$$< $$$$$$$$ |\$$$$$$\  $$ /  $$ |$$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$   ____| \____$$\ $$ |  $$ |$$ |  \$$$  /  $$   ____|$$ |      
$$ |  $$ |\$$$$$$$\ $$$$$$$  |\$$$$$$  |$$ |   \$  /   \$$$$$$$\ $$ |      
\__|  \__| \_______|\_______/  \______/ \__|    \_/     \_______|\__|

        """,
    
        '''
888b.                  8                   
8  .8 .d88b d88b .d8b. 8 Yb  dP .d88b 8d8b 
8wwK' 8.dP' `Yb. 8' .8 8  YbdP  8.dP' 8P   
8  Yb `Y88P Y88P `Y8P' 8   YP   `Y88P 8

        ''',

        """

@@@@@@@   @@@@@@@@   @@@@@@    @@@@@@   @@@       @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@       @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!       !@@       @@!  @@@  @@!       @@!  @@@  @@!       @@!  @@@  
!@!  @!@  !@!       !@!       !@!  @!@  !@!       !@!  @!@  !@!       !@!  @!@  
@!@!!@!   @!!!:!    !!@@!!    @!@  !@!  @!!       @!@  !@!  @!!!:!    @!@!!@!   
!!@!@!    !!!!!:     !!@!!!   !@!  !!!  !!!       !@!  !!!  !!!!!:    !!@!@!    
!!: :!!   !!:            !:!  !!:  !!!  !!:       :!:  !!:  !!:       !!: :!!   
:!:  !:!  :!:           !:!   :!:  !:!   :!:       ::!!:!   :!:       :!:  !:!  
::   :::   :: ::::  :::: ::   ::::: ::   :: ::::    ::::     :: ::::  ::   :::  
 :   : :  : :: ::   :: : :     : :  :   : :: : :     :      : :: ::    :   : :
 
    """,
    """

                                 
 _____             _             
| __  |___ ___ ___| |_ _ ___ ___ 
|    -| -_|_ -| . | | | | -_|  _|
|__|__|___|___|___|_|\_/|___|_|

    """
]

# Função para girar a roleta
def girar_roleta():
    banner_selecionado = random.choice(banners)
    print(banner_selecionado)

def print_all_banners():
    for banner in banners:
        print(banner)
    exit(0)
    


def resolve_ip(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error as e:
        print(f"ERROR: {e}")
        return None

def shodan_lookup(api_key, host, save_json=False, save_print=False, output_folder=".", print_folder="", json_folder=""):
    ip = resolve_ip(host)
    if ip is None:
        return None, None

    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if save_json:
                now = datetime.now()
                timestamp = now.strftime("%d_%m_%Y")
                host_filename = host.replace('.', '_')
                json_filename = f"shodan_{host_filename}_{timestamp}.json"
                json_filepath = os.path.join(json_folder, json_filename)
                with open(json_filepath, "w") as json_file:
                    json_file.write(json.dumps(data))  # Salva o JSON como string
            return data, response.status_code
        else:
            print(f"ERROR: {response.text}")
            data = None
            status_code = response.status_code
            return data, status_code
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")
        return None, None

def save_as_xlsx(output_file, sheet, output_folder):
    workbook = openpyxl.Workbook()
    output_sheet = workbook.active

    for row in sheet:
        output_sheet.append(row)

    output_filepath = os.path.join(output_folder, output_file)
    workbook.save(output_filepath)

def save_as_csv(output_file, sheet, output_folder):
    output_filepath = os.path.join(output_folder, output_file)
    with open(output_filepath, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerows(sheet)

def clean_files(file, output_folder, print_folder, json_folder):
    if output_folder is not None:
        output_filepath = os.path.join(output_folder, file)
        if os.path.exists(output_filepath):
            os.remove(output_filepath)

    if print_folder is not None:
        print_filepath = os.path.join(print_folder, f"{file}.png")
        if os.path.exists(print_filepath):
            os.remove(print_filepath)

    if json_folder is not None:
        json_filepath = os.path.join(json_folder, f"{file}.json")
        if os.path.exists(json_filepath):
            os.remove(json_filepath)
# Parte 3 - Linhas de 101 a 150

def main():
    parser = argparse.ArgumentParser(description="Perform a Shodan lookup for a list of hosts and save the results to a file.")
    parser.add_argument("-b", "--banners", action="store_true", help="print all banners")
    parser.add_argument("input_file", help="file containing a list of hosts to lookup")
    parser.add_argument("api_key", help="Shodan API key")
    parser.add_argument("-v", "--verbose", action="store_true", help="print progress during execution")
    parser.add_argument("--save-json", action="store_true", help="save the JSON responses from Shodan")
    parser.add_argument("--save-print", action="store_true", help="save the screenshot of the accessed website")
    parser.add_argument("--output-folder", help="path to the output folder")
    parser.add_argument("--print-folder", help="path to the screenshot folder")
    parser.add_argument("--json-folder", help="path to the JSON folder")
    parser.add_argument("--output-format", choices=["xlsx", "csv"], default="xlsx", help="output format (xlsx or csv)")
    parser.add_argument("--clean", action="store_true", help="clean files from previous executions")
    
    args = parser.parse_args()

    if args.banners:
        print_all_banners()


    hosts = []
    offline_hosts = []
    with open(args.input_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            hosts.append(line)

    if args.output_folder is None:
        output_folder = os.getcwd()
    else:
        output_folder = args.output_folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    if args.print_folder is None:
        print_folder = output_folder
    else:
        print_folder = args.print_folder
        if not os.path.exists(print_folder):
            os.makedirs(print_folder)

    if args.json_folder is None:
        json_folder = output_folder
    else:
        json_folder = args.json_folder
        if not os.path.exists(json_folder):
            os.makedirs(json_folder)

    output_sheet = [["Host", "IP", "Organization", "Vulnerabilities", "Ports", "HTTP Status Code", "Protocol", "Date"]]

    for host in hosts:
        if args.verbose:
            print(f"Performing Shodan lookup for {host}")

        result, status_code = shodan_lookup(args.api_key, host, save_json=args.save_json, save_print=args.save_print, output_folder=output_folder, print_folder=print_folder, json_folder=json_folder)
        if result is None:
            offline_hosts.append(host)
            continue

        organization = result.get("org", "N/A")
        vulnerabilities = ", ".join(result.get("vulns", []))
        ports = ", ".join([str(port) for port in result.get("ports", [])])

        protocol = ""
        if 'http' in result:
            protocol = "HTTP"
        elif 'https' in result:
            protocol = "HTTPS"

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output_sheet.append([host, result['ip_str'], organization, vulnerabilities, ports, status_code, protocol, date])

        if args.save_print:
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(f"http://{host}")
            driver.save_screenshot(os.path.join(print_folder, f"{host}.png"))
            driver.quit()

    for offline_host in offline_hosts:
        output_sheet.append([offline_host, "Host Offline", "Host Offline", "Host Offline", "Host Offline", "Host Offline", "", ""])

    output_file = os.path.splitext(args.input_file)[0]
    if args.output_format == "xlsx":
        save_as_xlsx(f"{output_file}.xlsx", output_sheet, output_folder)
        print(f"Results saved as XLSX to {os.path.join(output_folder, f'{output_file}.xlsx')}")
    elif args.output_format == "csv":
        save_as_csv(f"{output_file}.csv", output_sheet, output_folder)
        print(f"Results saved as CSV to {os.path.join(output_folder, f'{output_file}.csv')}")

    if args.save_json:
        print("JSON responses were saved.")
		
	
   


if __name__ == "__main__":
    print("#By João Ribeiro.")
    girar_roleta()
    main()
    
