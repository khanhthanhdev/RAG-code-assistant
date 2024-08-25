import requests

url = "https://api.together.xyz/v1/completions"

payload = {
    "model": "meta-llama/Meta-Llama-3-8B-Instruct-Lite",
    "prompt": f"Chuẩn hóa chữ viết tiếng Việt theo yêu cầu chuyển đổi các số, ngày tháng, tiền tệ, và phần trăm (%) thành chữ viết. Hãy đảm bảo rằng tất cả các số liệu trong đoạn văn sau được chuyển đổi chính xác thành dạng chữ viết bằng tiếng Việt.  **Ví dụ**: - 100 thành \"một trăm\" - 1.000.000 VNĐ thành \"một triệu đồng\" - Ngày 15/8/2023 thành \"ngày mười lăm tháng tám năm hai không hai ba\" - 25% thành \"hai mươi lăm phần trăm\"  **Dữ liệu đầu vào**: {p}  **output**:",
    "max_tokens": 256,
    "temperature": 0.1,
    "repetition_penalty": 1,
    "stream": False
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer 7ec57fc0e23263df0d100a4b132f76032c14e8039e4343e881fc96c45ff440b8"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)