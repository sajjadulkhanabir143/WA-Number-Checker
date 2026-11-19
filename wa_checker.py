import requests
import json

phone_number = input("Enter phone number (e.g., +8801777777777): ")

url = "https://www.idtexpress.com/wp-admin/admin-ajax.php"

payload = {
    'action': "idt_whatsapp_checker",
    'nonce': "456a28b7e0",
    'phone_number': phone_number
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'sec-ch-ua-platform': "\"Android\"",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua': "\"Chromium\";v=\"136\", \"Android WebView\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    'sec-ch-ua-mobile': "?1",
    'origin': "https://www.idtexpress.com",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.idtexpress.com/whatsapp-checker/",
    'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
    'priority': "u=1, i"
}
##====Written By @Owner_Of_DCS===##
response = requests.post(url, data=payload, headers=headers)

try:
    json_response = response.json()
    print(json.dumps(json_response, indent=4, ensure_ascii=False))
except ValueError:
    print("Response is not JSON. Raw response:")
    print(response.text)
