import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"YK TRICKS INDIA ")

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_messages():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('[-] <==> Incorrect Password!')
        sys.exit()

    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == ' 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print("\033[1;32m◑◑◑ MANI PANEL DAKU 302 ◑◑◑")

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'referer': 'www.google.com'
    }

    mmm = requests.get('https://pastebin.com/raw/ewfh22A0').text
    if mmm not in password:
        print('[-] Incorrect Password!')
        sys.exit()

    liness()

    access_tokens = [token.strip() for token in tokens]
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()
    with open('file.txt', 'r') as file:
        text_file_path = file.read().strip()
    with open(text_file_path, 'r') as file:
        messages = file.readlines()
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()
    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]
                message = messages[message_index].strip()
                url = f"https://graph.facebook.com/v15.0/t_{convo_id}/"
                parameters = {'access_token': access_token, 'message': f"{haters_name} {message}"}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[+] Message {message_index+1}/{num_messages} sent ✔️: {message}")
                else:
                    print(f"[x] Failed {message_index+1}/{num_messages} ❌: {message}")
                time.sleep(speed)
            print("\n[+] Cycle complete. Restarting...\n")
        except Exception as e:
            print(f"[!] Error: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages()

if __name__ == '__main__':
    main()
