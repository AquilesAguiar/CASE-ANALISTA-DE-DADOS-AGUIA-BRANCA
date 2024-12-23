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
            "Tipo": trip["type"],
            "Preço": trip["price"],
            "Desconto": trip["discountedPrice"],
            "Duração": trip["duration"]["hours"],
            "Assentos Disponíveis": trip["availableSeats"],
            "Data Partida": departure["schedule"]["date"],
            "Hora Partida": departure["schedule"]["time"],
            "Local Partida": departure["place"]["name"],
            "Terminal Partida": departure["place"]["terminal"],
            "Data Chegada": arrival["schedule"]["date"],
            "Hora Chegada": arrival["schedule"]["time"],
            "Local Chegada": arrival["place"]["name"],
            "Terminal Chegada": arrival["place"]["terminal"],
            "Classe Serviço": service_class["name"],
            "Empresa": travel_company["name"],
            "Logo Empresa": travel_company["logo"],
        })
    return data_list

def generate_excel(data_list):
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório de Viagens"

    headers = [
        "Tipo", "Preço", "Desconto", "Duração", "Assentos Disponíveis",
        "Data Partida", "Hora Partida", "Local Partida", "Terminal Partida",
        "Data Chegada", "Hora Chegada", "Local Chegada", "Terminal Chegada",
        "Classe Serviço", "Empresa", "Logo Empresa"
    ]
    ws.append(headers)

    for trip in data_list:
        ws.append([
            trip["Tipo"], trip["Preço"], trip["Desconto"], trip["Duração"], trip["Assentos Disponíveis"],
            trip["Data Partida"], trip["Hora Partida"], trip["Local Partida"], trip["Terminal Partida"],
            trip["Data Chegada"], trip["Hora Chegada"], trip["Local Chegada"], trip["Terminal Chegada"],
            trip["Classe Serviço"], trip["Empresa"], trip["Logo Empresa"]
        ])

    filename = "desafio_1/relatorio_viagens.xlsx"
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