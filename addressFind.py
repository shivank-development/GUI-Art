from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
def get_address(latitude, longitude):
    try:
        # Use a real geocoding API with proper URL (example uses Google Maps API format)
        api_key = "YOUR_API_KEY"
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
        response = requests.get(url, timeout=5)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]["formatted_address"]
        return "Address not found"
    except requests.exceptions.RequestException as e:
        return f"Request Error: {str(e)}"

@app.route("/log_location", methods=["POST"])
def log_location():
    data = request.json
    print("Received Data:", data)

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    if latitude and longitude:
        address = get_address(latitude, longitude)
        print(f"✓ Exact Location: {latitude}, {longitude}")
        print(f"✓ Address: {address}")
        return jsonify({
            "status": "success",
            "latitude": latitude,
            "longitude": longitude,
            "address": address
        }), 200

    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
