import requests

payload = {"ano": "2017", "estado": "SP", "cidade": "SAO_PAULO", "token": "cmFjYXNhbnRvc0BpY2xvdWQuY29tJmhhc2g9MTU3MzE5NzA="}
response = requests.get("http://www.calendario.com.br/api/api_feriados.php", params=payload)
data = response.content

if response.status_code == 200:
    print data