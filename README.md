# ISS Tracker 🌍🚀

Track the International Space Station (ISS) in real-time, see its location on a world map, and view details about current astronauts onboard.

---

## Features
- 🌟 **Real-time Location**: Displays the ISS's current position on a world map using Python's Turtle module.
- 🧑‍🚀 **Astronaut Details**: Lists the astronauts currently onboard the ISS.
- 🔁 **Auto Updates**: Refreshes ISS location every 5 seconds.
- 📍 **User Location**: Detects and displays your latitude and longitude.

---

## Installation
### Prerequisites
- Python 3.x
- Basic Python libraries: , , , and 
- Additional library: 

### Steps
1. **Clone the repository**:
   ```bash
   git clone git@github.com:armoustafa/ISS_Tracker.git
   cd ISS_Tracker
   ```
2. **Install required libraries**:
   ```bash
   pip install geocoder
   ```
3. **Run the script**:
   ```bash
   python iss_tracker.py
   ```

---

## How It Works
1. Retrieves ISS data from [Open Notify API](http://open-notify.org/).
2. Shows the ISS's position on a world map with the Turtle module.
3. Lists astronauts onboard and your current location (if detected).

---

## Project Structure
```plaintext
ISS_Tracker/
├── images/                  # Contains map and ISS icons
│   ├── map.gif              # Background map image
│   ├── iss.gif              # ISS icon
├── iss_tracker.py           # Main script
├── README.md                # Documentation
└── LICENSE                  # License details
```

---

## Acknowledgments
- [Open Notify API](http://open-notify.org/) for real-time ISS data.
- Python Turtle for visualization.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

