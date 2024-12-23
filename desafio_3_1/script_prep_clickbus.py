from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime, timedelta
from openpyxl import Workbook

def generate_url():
    url = "https://www.clickbus.com.br/onibus/rio-de-janeiro-rj-todos/sao-paulo-sp-todos"
    
    data_hoje = datetime.now()
    departure_date = data_hoje.strftime("%Y-%m-%d")
    return_date = (data_hoje + timedelta(days=15)).strftime("%Y-%m-%d")
    
    return f"{url}?departureDate={departure_date}&returnDate={return_date}"

def extract_data(trips):
    data_list = []
    for trip in trips:
        departure = trip["departure"]
        arrival = trip["arrival"]
        travel_company = trip["travelCompany"]
        service_class = trip["serviceClass"]

        data_list.append({
            "Fonte": "https://www.clickbus.com.br/",
            "Operador": travel_company["name"],
            "Data_Hora_Partida": f"{departure['schedule']['date']} {departure['schedule']['time']}",
            "Data_Partida": departure["schedule"]["date"],
            "Hora_Partida": departure["schedule"]["time"],
            "Classe": service_class["name"],
            "Origem": departure["place"]["name"],
            "Destino": arrival["place"]["name"],
            "Preco": trip["price"],
            "Capacidade": trip["availableSeats"],
            "Ocupacao": trip["availableSeats"],
            "Data_Hora_Captacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Arquivo": "desafio_3/clickbus_preparado.xlsx"
        })
    return data_list

def generate_excel(data_list):
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório de Viagens"

    headers = [
        "Fonte", "Operador", "Data_Hora_Partida", "Data_Partida", "Hora_Partida", "Classe", "Origem", "Destino", 
        "Preco", "Capacidade", "Ocupacao", "Data_Hora_Captacao", "Arquivo"
    ]
    ws.append(headers)

    for trip in data_list:
        ws.append([
            trip["Fonte"], trip["Operador"], trip["Data_Hora_Partida"], trip["Data_Partida"], trip["Hora_Partida"],
            trip["Classe"], trip["Origem"], trip["Destino"], trip["Preco"], trip["Capacidade"], trip["Ocupacao"],
            trip["Data_Hora_Captacao"], trip["Arquivo"]
        ])

    filename = "desafio_3/clickbus_preparado.xlsx"
    wb.save(filename)
    print(f"Relatório gerado: {filename}")

def clickbus_data():
    url = generate_url()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        script_tag = soup.find('script', id='__NEXT_DATA__')
        
        if script_tag:
            json_data = json.loads(script_tag.string)
            
            trips = json_data["props"]["pageProps"]["pageData"]["trips"]["departures"]
            
            if trips:
                trip_data = extract_data(trips)
                generate_excel(trip_data)
        else:
            print("Tag '__NEXT_DATA__' não encontrada.")
    else:
        print(f"Erro na requisição: {response.status_code}")

if __name__ == "__main__":
    clickbus_data()
