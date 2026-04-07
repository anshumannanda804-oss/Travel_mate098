import sqlite3

DB_NAME = "users.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        password TEXT NOT NULL,
        security_question TEXT NOT NULL,
        security_answer TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS destinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        country TEXT NOT NULL,
        category TEXT NOT NULL,
        budget_per_day INTEGER,
        medium_per_day INTEGER,
        luxury_per_day INTEGER,
        currency TEXT DEFAULT 'INR',
        is_international INTEGER DEFAULT 0
    )
    """)

    # Insert destinations
    destinations = [
        # ODISHA DESTINATIONS
        ('Puri', 19.8136, 85.8312, 'India', 'Odisha', 800, 1500, 3000, 'INR', 0),
        ('Bhubaneswar', 20.2961, 85.8245, 'India', 'Odisha', 700, 1200, 2800, 'INR', 0),
        ('Konark', 19.8837, 86.0938, 'India', 'Odisha', 600, 1000, 2500, 'INR', 0),
        ('Rourkela', 22.2034, 84.8534, 'India', 'Odisha', 500, 1000, 2200, 'INR', 0),
        ('Cuttack', 20.4625, 85.8830, 'India', 'Odisha', 600, 1100, 2600, 'INR', 0),
        ('Balasore', 21.4942, 87.1069, 'India', 'Odisha', 700, 1300, 2900, 'INR', 0),
        ('Chilika Lake', 19.7500, 85.2833, 'India', 'Odisha', 800, 1400, 3100, 'INR', 0),
        ('Sambalpur', 21.5626, 83.9858, 'India', 'Odisha', 550, 1050, 2300, 'INR', 0),
        ('Berhampur', 19.3155, 84.7941, 'India', 'Odisha', 650, 1150, 2550, 'INR', 0),
        ('Jharsuguda', 21.8458, 84.0190, 'India', 'Odisha', 500, 950, 2200, 'INR', 0),
        ('Balangir', 20.7281, 83.4655, 'India', 'Odisha', 520, 1000, 2250, 'INR', 0),
        ('Koraput', 18.8120, 82.7123, 'India', 'Odisha', 600, 1100, 2400, 'INR', 0),

        # ANDHRA PRADESH
        ('Hyderabad', 17.3850, 78.4867, 'India', 'Andhra Pradesh', 800, 1500, 3200, 'INR', 0),
        ('Visakhapatnam', 17.6869, 83.2185, 'India', 'Andhra Pradesh', 750, 1400, 3000, 'INR', 0),
        ('Tirupati', 13.1886, 79.8260, 'India', 'Andhra Pradesh', 650, 1200, 2700, 'INR', 0),
        ('Vijayawada', 16.5062, 80.6480, 'India', 'Andhra Pradesh', 700, 1300, 2900, 'INR', 0),

        # ARUNACHAL PRADESH
        ('Itanagar', 28.2180, 93.6053, 'India', 'Arunachal Pradesh', 600, 1200, 2800, 'INR', 0),
        ('Tawang', 27.5928, 91.3725, 'India', 'Arunachal Pradesh', 700, 1400, 3100, 'INR', 0),

        # ASSAM
        ('Guwahati', 26.1445, 91.7362, 'India', 'Assam', 700, 1300, 2900, 'INR', 0),
        ('Kaziranga', 26.6000, 93.2700, 'India', 'Assam', 800, 1500, 3200, 'INR', 0),
        ('Shillong', 25.5788, 91.8933, 'India', 'Meghalaya', 750, 1400, 3050, 'INR', 0),

        # BIHAR
        ('Patna', 25.5941, 85.1376, 'India', 'Bihar', 650, 1200, 2700, 'INR', 0),
        ('Bodh Gaya', 24.6955, 84.9852, 'India', 'Bihar', 700, 1300, 2900, 'INR', 0),
        ('Rajgir', 25.3547, 85.4401, 'India', 'Bihar', 650, 1250, 2800, 'INR', 0),

        # CHHATTISGARH
        ('Raipur', 21.2514, 81.6296, 'India', 'Chhattisgarh', 650, 1200, 2700, 'INR', 0),
        ('Bilaspur', 22.0896, 82.1506, 'India', 'Chhattisgarh', 600, 1150, 2600, 'INR', 0),

        # GOA
        ('Goa', 15.2993, 73.8243, 'India', 'Goa', 1000, 1800, 4000, 'INR', 0),
        ('Panaji', 15.4909, 73.8278, 'India', 'Goa', 950, 1750, 3900, 'INR', 0),

        # GUJARAT
        ('Ahmedabad', 23.0225, 72.5714, 'India', 'Gujarat', 750, 1400, 3100, 'INR', 0),
        ('Surat', 21.1702, 72.8311, 'India', 'Gujarat', 700, 1300, 2900, 'INR', 0),
        ('Vadodara', 22.3072, 73.1812, 'India', 'Gujarat', 700, 1350, 3000, 'INR', 0),
        ('Rajkot', 22.3039, 70.8022, 'India', 'Gujarat', 650, 1250, 2800, 'INR', 0),

        # HARYANA
        ('Faridabad', 28.4089, 77.3178, 'India', 'Haryana', 700, 1350, 3000, 'INR', 0),
        ('Gurgaon', 28.4595, 77.0266, 'India', 'Haryana', 850, 1600, 3500, 'INR', 0),

        # HIMACHAL PRADESH
        ('Shimla', 31.7725, 77.1770, 'India', 'Himachal Pradesh', 800, 1500, 3500, 'INR', 0),
        ('Manali', 32.2396, 77.1887, 'India', 'Himachal Pradesh', 900, 1700, 3800, 'INR', 0),
        ('Kullu', 32.2227, 77.1093, 'India', 'Himachal Pradesh', 750, 1450, 3200, 'INR', 0),
        ('Dharamshala', 32.2190, 76.3263, 'India', 'Himachal Pradesh', 700, 1350, 3100, 'INR', 0),

        # JAMMU & KASHMIR
        ('Srinagar', 34.0837, 74.7973, 'India', 'Jammu & Kashmir', 850, 1650, 3800, 'INR', 0),
        ('Leh', 34.1526, 77.5770, 'India', 'Jammu & Kashmir', 900, 1700, 3900, 'INR', 0),
        ('Kashmir Valley', 34.3000, 75.5000, 'India', 'Jammu & Kashmir', 900, 1750, 4000, 'INR', 0),

        # JHARKHAND
        ('Ranchi', 23.3441, 85.3096, 'India', 'Jharkhand', 650, 1250, 2800, 'INR', 0),
        ('Jamshedpur', 22.8046, 86.1826, 'India', 'Jharkhand', 650, 1200, 2700, 'INR', 0),

        # KARNATAKA
        ('Bangalore', 12.9716, 77.5946, 'India', 'Karnataka', 900, 1700, 3800, 'INR', 0),
        ('Mysore', 12.2958, 76.6394, 'India', 'Karnataka', 750, 1400, 3100, 'INR', 0),
        ('Coorg', 12.3381, 75.7421, 'India', 'Karnataka', 800, 1500, 3300, 'INR', 0),
        ('Hampi', 15.3350, 76.4789, 'India', 'Karnataka', 600, 1150, 2700, 'INR', 0),

        # KERALA
        ('Kochi', 9.9312, 76.2673, 'India', 'Kerala', 1000, 1800, 4000, 'INR', 0),
        ('Thiruvananthapuram', 8.5241, 76.9366, 'India', 'Kerala', 900, 1700, 3800, 'INR', 0),
        ('Munnar', 10.5892, 76.7533, 'India', 'Kerala', 850, 1600, 3600, 'INR', 0),
        ('Alleppey', 9.4981, 76.3388, 'India', 'Kerala', 950, 1750, 3900, 'INR', 0),

        # MADHYA PRADESH
        ('Indore', 22.7196, 75.8577, 'India', 'Madhya Pradesh', 700, 1350, 3000, 'INR', 0),
        ('Bhopal', 23.1815, 79.9864, 'India', 'Madhya Pradesh', 700, 1300, 2900, 'INR', 0),
        ('Khajuraho', 24.8314, 79.7477, 'India', 'Madhya Pradesh', 750, 1450, 3200, 'INR', 0),
        ('Jabalpur', 23.1815, 79.9864, 'India', 'Madhya Pradesh', 650, 1250, 2800, 'INR', 0),

        # MAHARASHTRA
        ('Mumbai', 19.0760, 72.8777, 'India', 'Maharashtra', 1200, 2000, 4500, 'INR', 0),
        ('Pune', 18.5204, 73.8567, 'India', 'Maharashtra', 850, 1550, 3400, 'INR', 0),
        ('Aurangabad', 19.8762, 75.3433, 'India', 'Maharashtra', 700, 1350, 3000, 'INR', 0),
        ('Nashik', 19.9975, 73.7898, 'India', 'Maharashtra', 700, 1300, 2900, 'INR', 0),

        # MANIPUR
        ('Imphal', 24.8170, 94.9080, 'India', 'Manipur', 650, 1250, 2800, 'INR', 0),

        # MEGHALAYA
        ('Cherrapunji', 25.2727, 91.7058, 'India', 'Meghalaya', 700, 1350, 3000, 'INR', 0),

        # MIZORAM
        ('Aizawl', 23.1815, 92.7789, 'India', 'Mizoram', 650, 1250, 2800, 'INR', 0),

        # NAGALAND
        ('Kohima', 25.6114, 94.1086, 'India', 'Nagaland', 650, 1250, 2800, 'INR', 0),

        # PUNJAB
        ('Amritsar', 31.6340, 74.8723, 'India', 'Punjab', 700, 1350, 3000, 'INR', 0),
        ('Chandigarh', 30.7333, 76.7794, 'India', 'Punjab', 750, 1400, 3100, 'INR', 0),
        ('Ludhiana', 30.9010, 75.8573, 'India', 'Punjab', 700, 1300, 2900, 'INR', 0),

        # RAJASTHAN
        ('Jaipur', 26.9124, 75.7873, 'India', 'Rajasthan', 700, 1400, 3200, 'INR', 0),
        ('Jodhpur', 26.2389, 73.0243, 'India', 'Rajasthan', 700, 1350, 3100, 'INR', 0),
        ('Udaipur', 24.5854, 73.7125, 'India', 'Rajasthan', 850, 1600, 3500, 'INR', 0),
        ('Ajmer', 26.4499, 74.6399, 'India', 'Rajasthan', 650, 1250, 2800, 'INR', 0),

        # SIKKIM
        ('Gangtok', 27.5330, 88.6139, 'India', 'Sikkim', 800, 1550, 3400, 'INR', 0),

        # TAMIL NADU
        ('Chennai', 13.0827, 80.2707, 'India', 'Tamil Nadu', 850, 1600, 3500, 'INR', 0),
        ('Coimbatore', 11.0066, 76.9485, 'India', 'Tamil Nadu', 750, 1400, 3100, 'INR', 0),
        ('Madurai', 9.9252, 78.1198, 'India', 'Tamil Nadu', 700, 1350, 3000, 'INR', 0),
        ('Ooty', 11.4102, 76.6955, 'India', 'Tamil Nadu', 850, 1600, 3500, 'INR', 0),

        # TELANGANA
        ('Warangal', 17.9689, 79.5941, 'India', 'Telangana', 650, 1250, 2800, 'INR', 0),

        # TRIPURA
        ('Agartala', 23.8103, 91.2787, 'India', 'Tripura', 650, 1250, 2800, 'INR', 0),

        # UTTAR PRADESH
        ('Agra', 27.1767, 78.0081, 'India', 'Uttar Pradesh', 600, 1300, 3000, 'INR', 0),
        ('Lucknow', 26.8467, 80.9462, 'India', 'Uttar Pradesh', 700, 1350, 3000, 'INR', 0),
        ('Varanasi', 25.3209, 83.0087, 'India', 'Uttar Pradesh', 700, 1300, 2900, 'INR', 0),
        ('Mathura', 27.4924, 77.6737, 'India', 'Uttar Pradesh', 650, 1250, 2800, 'INR', 0),

        # UTTARAKHAND
        ('Dehradun', 30.3165, 78.0322, 'India', 'Uttarakhand', 700, 1350, 3000, 'INR', 0),
        ('Rishikesh', 30.0894, 78.2685, 'India', 'Uttarakhand', 700, 1350, 3000, 'INR', 0),
        ('Mussoorie', 30.4618, 78.4681, 'India', 'Uttarakhand', 800, 1500, 3300, 'INR', 0),
        ('Nainital', 29.3919, 79.4504, 'India', 'Uttarakhand', 800, 1500, 3300, 'INR', 0),

        # WEST BENGAL
        ('Kolkata', 22.5726, 88.3639, 'India', 'West Bengal', 700, 1400, 3000, 'INR', 0),
        ('Darjeeling', 27.0360, 88.2560, 'India', 'West Bengal', 1000, 1800, 3500, 'INR', 0),
        ('Siliguri', 26.7271, 88.3953, 'India', 'West Bengal', 650, 1250, 2800, 'INR', 0),
        ('Sundarbans', 22.0000, 89.0000, 'India', 'West Bengal', 800, 1500, 3300, 'INR', 0),

        # DELHI (NCR)
        ('Delhi', 28.7041, 77.1025, 'India', 'Delhi', 900, 1600, 3500, 'INR', 0),

        # LADAKH
        ('Ladakh', 34.1526, 77.5770, 'India', 'Ladakh', 900, 1700, 3900, 'INR', 0),

        # FAMOUS INTERNATIONAL DESTINATIONS
        ('Paris', 48.8566, 2.3522, 'France', 'Europe', 120, 180, 350, 'USD', 1),
        ('London', 51.5074, -0.1278, 'United Kingdom', 'Europe', 130, 200, 380, 'USD', 1),
        ('Dubai', 25.2048, 55.2708, 'United Arab Emirates', 'Middle East', 150, 250, 450, 'USD', 1),
        ('Singapore', 1.3521, 103.8198, 'Singapore', 'Asia', 140, 220, 400, 'USD', 1),
        ('Bangkok', 13.7563, 100.5018, 'Thailand', 'Asia', 80, 140, 280, 'USD', 1),
        ('Bali', -8.6705, 115.2126, 'Indonesia', 'Asia', 70, 130, 250, 'USD', 1),
        ('Tokyo', 35.6762, 139.6503, 'Japan', 'Asia', 200, 350, 600, 'USD', 1),
        ('New York', 40.7128, -74.0060, 'USA', 'North America', 180, 300, 550, 'USD', 1),
        ('Los Angeles', 34.0522, -118.2437, 'USA', 'North America', 150, 280, 500, 'USD', 1),
        ('Barcelona', 41.3851, 2.1734, 'Spain', 'Europe', 110, 170, 330, 'USD', 1),
        ('Rome', 41.9028, 12.4964, 'Italy', 'Europe', 100, 160, 320, 'USD', 1),
        ('Sydney', -33.8688, 151.2093, 'Australia', 'Oceania', 160, 280, 500, 'USD', 1),
        ('Amsterdam', 52.3676, 4.9041, 'Netherlands', 'Europe', 120, 190, 360, 'USD', 1),
        ('Maldives', 4.1694, 73.5093, 'Maldives', 'Asia', 200, 400, 800, 'USD', 1),
        ('Iceland', 64.9631, -19.0208, 'Iceland', 'Europe', 180, 280, 480, 'USD', 1),
    ]

    for dest in destinations:
        try:
            cursor.execute("""
                INSERT INTO destinations 
                (name, latitude, longitude, country, category, budget_per_day, 
                 medium_per_day, luxury_per_day, currency, is_international)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, dest)
        except sqlite3.IntegrityError:
            pass  # Destination already exists

    conn.commit()
    conn.close()

