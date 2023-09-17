# Tehdään Pythonin socket-moduulia käyttävä serveri
# Serveri ottaa vastaan viestejä clientiltä ja tallentaa ne tiedostoon
# Kun client pyytää, serveri lähettää viestit clientille

import socket

# funktio tiedoston tallentamiseen
def save_data(data: str):
    with open("viestit.txt", "a") as tiedosto:
        tiedosto.write(data+"\n")

# funktio tiedoston lukemiseen
def load_data():
    with open("viestit.txt", "r") as tiedosto:
        data = tiedosto.read()
    return data

# serverin toiminnallisuus
def server():

    HOST = "localhost"
    PORT = 15000

    # family on osoiteperhe (address family), oletuksena AF_INET
    # type on socketin tyyppi, oletuksena SOCK_STREAM
    # protokollanumero proto on yleensä 0
    # jos fileno määritellään family, type ja proto tunnistetaan automaattisesti
    # socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # asetetaan socketille flagi socket.SO_REUSEADDR jolloin socketin voi ottaa
    # uudestaan käyttöön, vaikka se olisi TIME_WAIT tilassa
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"kuuntelen porttia {PORT}")
    
    while True:

        # socket.accept palauttaa tuplen, jonka ensimmäinen alkio on uusi
        # socket objekti, jota voi käyttää lähettämään ja vastaanottamaan dataa
        # toinen on osoite, johon socket on sidottu yhteyden toisessa päässä
        conn, addr = server_socket.accept()
        print(f"Yhteys avattu osoitteesta {addr}")
        
        rdata = conn.recv(1024).decode()
        print(rdata)

        if not rdata:
            break

        elif rdata.lower() == "v":
            msg_data = load_data()
            conn.send(msg_data.encode())

        else:
            save_data(rdata)
            conn.send("Viesti tallennettu".encode())

        conn.close()

if __name__=="__main__":
    server()