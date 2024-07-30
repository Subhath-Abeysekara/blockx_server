import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFiZXlzZWthcmFzZHBfYmxvY2t4QGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiMTIzNDU2Nzg5IiwiY29kZSI6IjY2MGI5YjFjNjBkNjgzYTY0NzFiNDlmMSIsImV4cGlyZSI6MTcyMjUyMjE4Nn0.nzTEfYmtAwy6WKB1RJNggtJMRKk5a9siYcvSjmAwuCg"
body = {
    "post_id":"660c6751dc69f7187aa40f9b"
}
headers = {'token': token}
print(headers)
url = "https://www.blockxserver.xyz/v1/request_token"
validate_res = requests.post(url=url , headers=headers , json=body)
print(validate_res)
print(validate_res.json())