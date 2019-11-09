from amadeus import Client, ResponseError
import credentials

print(credentials.clientID)

amadeus = Client(
    client_id=credentials.clientID,
    client_secret=credentials.clientSecret
)

