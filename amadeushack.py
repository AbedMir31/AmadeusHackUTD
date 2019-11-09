from amadeus import Client

import tkgui
import credentials
print(credentials.clientID)

amadeus = Client(
    client_id=credentials.clientID,
    client_secret=credentials.clientSecret
)

