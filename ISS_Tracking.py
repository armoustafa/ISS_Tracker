import json
import turtle
import urllib.request
import webbrowser
import geocoder
import os

# Get the current ISS data
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Save data to a text file
with open("iss.txt", "w") as file:
    file.write("There are currently " +
               str(result["number"]) + " astronauts on the ISS: \n\n")
    for p in result["people"]:
        file.write(f"{p['name']} - on board\n")

    # Get current latitude and longitude
    g = geocoder.ip('me')
    if g.latlng:
        file.write(f"\nYour current lat / long is: {g.latlng}")
    else:
        file.write("\nUnable to determine your current location.")

# Open the text file in the browser
webbrowser.open("file://" + os.path.abspath("iss.txt"))

# Setup the world map in turtle
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load the map and ISS images
screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")
iss = turtle.Turtle()
iss.shape("images/iss.gif")
# iss.penup()

# Update ISS location
def update_iss():
    try:
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        location = result["iss_position"]
        lat = float(location['latitude'])
        lon = float(location['longitude'])
        print(f"\nLatitude: {lat}, Longitude: {lon}")
        iss.goto(lon, lat)
    except Exception as e:
        print(f"Error updating ISS location: {e}")

    # Schedule the next update
    screen.ontimer(update_iss, 5000)

# Start the updates
update_iss()
turtle.mainloop()