from math import radians, sin, cos, sqrt, atan2
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import requests
import re
from database import init_db

app = Flask(__name__)
CORS(app)

# Initialize database
init_db()

# ---------------- UTILS ----------------
def get_connection():
    return sqlite3.connect("users.db")


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def estimate_transport_cost(distance_km, is_international, destination=None, same_state=False):
    transport = {}

    if not is_international:
        transport["bus"] = int(distance_km * 3)
        transport["train"] = int(distance_km * 2)

        # Flights only available for distances >= 300km and not for same state or specific destinations
        if distance_km >= 300 and not same_state and destination != "Koraput":
            if distance_km < 500:
                flight_rate = 9
            elif distance_km < 1500:
                flight_rate = 7
            else:
                flight_rate = 6

            transport["flight"] = int(distance_km * flight_rate)
    else:
        if distance_km < 3000:
            flight_rate = 15
        elif distance_km < 7000:
            flight_rate = 12
        else:
            flight_rate = 10

        transport["flight"] = int(distance_km * flight_rate)

    return transport
@app.route("/")
def home():
    return "TravelMate Backend is Running 🚀"

# ---------------- REGISTER ----------------
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")
    question = data.get("security_question")
    answer = data.get("security_answer")

    if not all([name, email, phone, password, question, answer]):
        return jsonify({"success": False, "message": "All fields required"}), 400

    # Password validation
    if len(password) < 8:
        return jsonify({"success": False, "message": "Password must be at least 8 characters long"}), 400
    if not re.search(r'[A-Z]', password):
        return jsonify({"success": False, "message": "Password must contain at least one uppercase letter"}), 400
    if not re.search(r'[a-z]', password):
        return jsonify({"success": False, "message": "Password must contain at least one lowercase letter"}), 400
    if not re.search(r'\d', password):
        return jsonify({"success": False, "message": "Password must contain at least one number"}), 400
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return jsonify({"success": False, "message": "Password must contain at least one special character"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (name, email, phone, password, security_question, security_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, phone, password, question, answer))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"success": False, "message": "Email already exists"}), 400
    finally:
        conn.close()

    return jsonify({"success": True})


# ---------------- GET SECURITY QUESTION ----------------
@app.route("/api/get-security-question", methods=["POST"])
def get_security_question():
    data = request.get_json()
    email = data.get("email")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT security_question FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({"success": False, "message": "Email not found"}), 404

    return jsonify({"success": True, "securityQuestion": row[0]})


# ---------------- RESET PASSWORD ----------------
@app.route("/api/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json()

    email = data.get("email")
    answer = data.get("security_answer")
    new_password = data.get("new_password")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT security_answer FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()

    if not row or row[0].lower() != answer.lower():
        conn.close()
        return jsonify({"success": False, "message": "Invalid credentials"}), 403

    cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "Password reset successful"})


# ---------------- TRIP DETAILS (MAP + HOTELS) ----------------
@app.route("/api/trip-details", methods=["POST"])
def trip_details():
    data = request.get_json()
    source = data.get("source")
    destination = data.get("destination")
    days = data.get("days", 1)

    if not source or not destination:
        return jsonify({"success": False, "message": "Source or destination missing"}), 400

    # Check destination in database first
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT latitude, longitude, country, currency, is_international,
               budget_per_day, medium_per_day, luxury_per_day, category
        FROM destinations WHERE name LIKE ?
    """, (f"%{destination}%",))
    
    dest_record = cursor.fetchone()
    conn.close()

    geo_url = "https://nominatim.openstreetmap.org/search"

    def geocode(place):
        res = requests.get(
            geo_url,
            params={
                "q": place,
                "format": "json",
                "limit": 1
            },
            headers={"User-Agent": "travel-app"}
        ).json()

        if not res:
            return None

        addr = res[0].get("address", {})
        state = addr.get("state", "") or addr.get("region", "") or addr.get("county", "")
        return float(res[0]["lat"]), float(res[0]["lon"]), addr, state

    # 1️⃣ Geocode source
    source_geo = geocode(source)
    if not source_geo:
        return jsonify({"success": False, "message": "Invalid source city"}), 400

    src_lat, src_lon, src_addr, src_state = source_geo

    # 2️⃣ Use database or geocode destination
    if dest_record:
        dest_lat, dest_lon, dest_country, currency, is_international, budget_day, medium_day, luxury_day, dest_state = dest_record
    else:
        dest_geo = geocode(destination)
        if not dest_geo:
            return jsonify({"success": False, "message": "Invalid destination city"}), 400
        dest_lat, dest_lon, dest_addr, dest_state = dest_geo
        src_country = src_addr.get("country_code", "")
        dest_country = dest_addr.get("country_code", "")
        is_international = src_country != dest_country
        currency = "USD" if is_international else "INR"
        budget_day = 500 if not is_international else 100
        medium_day = 1000 if not is_international else 200
        luxury_day = 2500 if not is_international else 500

    # 3️⃣ Distance calculation
    distance = calculate_distance(src_lat, src_lon, dest_lat, dest_lon)

    # Check if same state (no domestic flights within state)
    same_state = src_state == dest_state and not is_international

    # 4️⃣ Transport cost
    transport_costs = estimate_transport_cost(distance, is_international, destination, same_state)
    extra_cost = 1000

    # 5️⃣ Per-day accommodation costs
    accommodation_costs = {
        "budget": {
            "per_day": budget_day,
            "total": budget_day * days
        },
        "medium": {
            "per_day": medium_day,
            "total": medium_day * days
        },
        "luxury": {
            "per_day": luxury_day,
            "total": luxury_day * days
        },
        "currency": currency,
        "days": days
    }

    # Determine cheapest transport cost
    available_transports = [cost for cost in transport_costs.values() if cost is not None]
    cheapest_transport = min(available_transports) if available_transports else 0

    # Total budgets including accommodation, extra, and cheapest transport
    total_budgets = {
        "budget": {
            "accommodation": accommodation_costs["budget"]["total"],
            "transport": cheapest_transport,
            "extra": extra_cost,
            "total": accommodation_costs["budget"]["total"] + extra_cost + cheapest_transport
        },
        "medium": {
            "accommodation": accommodation_costs["medium"]["total"],
            "transport": cheapest_transport,
            "extra": extra_cost,
            "total": accommodation_costs["medium"]["total"] + extra_cost + cheapest_transport
        },
        "luxury": {
            "accommodation": accommodation_costs["luxury"]["total"],
            "transport": cheapest_transport,
            "extra": extra_cost,
            "total": accommodation_costs["luxury"]["total"] + extra_cost + cheapest_transport
        },
        "currency": currency
    }

    # 6️⃣ FETCH HOTELS FROM TOMTOM
    TOMTOM_KEY = "MS39QFw2ocwUvr3eBI6C9sVkiVfjoTYK"

    tomtom_url = "https://api.tomtom.com/search/2/poiSearch/hotel.json"

    params = {
        "lat": dest_lat,
        "lon": dest_lon,
        "radius": 15000,
        "limit": 20,
        "key": TOMTOM_KEY
    }

    tt_response = requests.get(tomtom_url, params=params)

    hotels = []

    if tt_response.status_code == 200:
        tt_data = tt_response.json()

        for result in tt_data.get("results", []):
            hotels.append({
                "name": result.get("poi", {}).get("name", "Unnamed Hotel"),
                "lat": result.get("position", {}).get("lat"),
                "lon": result.get("position", {}).get("lon")
            })

    # 7️⃣ FINAL RESPONSE
    return jsonify({
        "success": True,
        "data": {
            "source": source,
            "destination": destination,
            "latitude": dest_lat,
            "longitude": dest_lon,
            "hotels": hotels,
            "distance_km": int(distance),
            "transport": transport_costs,
            "extra_cost": extra_cost,
            "accommodation_costs": accommodation_costs,
            "total_budgets": total_budgets,
            "is_international": is_international
        }
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
