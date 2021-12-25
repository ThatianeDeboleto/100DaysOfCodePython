from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification_manager = NotificationManager()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

#campinas cidade IATA - https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports VCP
#etapa 4 solicita que seja de Londres 7 dias e 28 dias
ORIGIN_CITY_IATA = ""

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Alerta de preço baixo! Somente £{flight.price} voar de {flight.origin_city}-{flight.origin_airport} para {flight.destination_city}-{flight.destination_airport}, a partir de {flight.out_date} para {flight.return_date}."
        )

