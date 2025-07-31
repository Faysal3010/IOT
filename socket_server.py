import network
import socket

# Access Point Configuration
ssid = "ESP32_Server"
password = "mypassword123"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA_WPA2_PSK)

print("Access Point:", ssid)
print("IP Address:", ap.ifconfig()[0])

# HTML Page
html = """<!DOCTYPE html>
<html>
  <head><title>ESP32 Server</title></head>
  <body>
    <h2>ESP32 Server is Live!</h2>
    <form method="POST">
      <input type="text" name="message" placeholder="Type something..." />
      <input type="submit" value="Send" />
    </form>
  </body>
</html>
"""

# Server Logic
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print("Web Server running! Visit:", ap.ifconfig()[0])

while True:
    conn, addr = s.accept()
    print("Client connected from:", addr)
    request = conn.recv(1024)
    request = str(request)

    # HTTP Response Send
    response = html
    conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    conn.sendall(response)
    conn.close()
