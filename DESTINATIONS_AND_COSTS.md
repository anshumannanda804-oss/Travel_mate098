
# Travel Destination Per-Day Cost Database

## Overview
This document outlines all available travel destinations with per-day accommodation costs categorized by luxury level and currency type.

---

## ODISHA DESTINATIONS (India)

| Destination | Category | Budget/Day (₹) | Medium/Day (₹) | Luxury/Day (₹) |
|---|---|---|---|---|
| **Puri** | Odisha Beach | 800 | 1500 | 3000 |
| **Bhubaneswar** | Odisha Capital | 700 | 1200 | 2800 |
| **Konark** | Odisha Heritage | 600 | 1000 | 2500 |
| **Rourkela** | Odisha Industrial | 500 | 1000 | 2200 |
| **Cuttack** | Odisha City | 600 | 1100 | 2600 |
| **Balasore** | Odisha Beach | 700 | 1300 | 2900 |
| **Chilika Lake** | Odisha Natural | 800 | 1400 | 3100 |
| **Koraput** | Odisha Tribal | 600 | 1100 | 2400 |
| **Darjeeling** | Hill Station | 1000 | 1800 | 3500 |

---

## MAJOR INDIA DESTINATIONS

### Metropolitan Cities
| Destination | Budget/Day (₹) | Medium/Day (₹) | Luxury/Day (₹) |
|---|---|---|---|
| **Delhi** | 900 | 1600 | 3500 |
| **Mumbai** | 1200 | 2000 | 4500 |
| **Bangalore** | 900 | 1700 | 3800 |
| **Hyderabad** | 800 | 1500 | 3200 |
| **Kolkata** | 700 | 1400 | 3000 |

### Heritage & Culture
| Destination | Budget/Day (₹) | Medium/Day (₹) | Luxury/Day (₹) |
|---|---|---|---|
| **Jaipur** | 700 | 1400 | 3200 |
| **Agra** (Taj Mahal) | 600 | 1300 | 3000 |
| **Varanasi** | 700 | 1300 | 2900 |
| **Taj Mahal Region** | 600 | 1300 | 3000 |

### Beach Destinations
| Destination | Budget/Day (₹) | Medium/Day (₹) | Luxury/Day (₹) |
|---|---|---|---|
| **Goa** | 1000 | 1800 | 4000 |
| **Kerala** | 1100 | 2000 | 4200 |

### Hill Stations
| Destination | Budget/Day (₹) | Medium/Day (₹) | Luxury/Day (₹) |
|---|---|---|---|
| **Shimla** | 800 | 1500 | 3500 |
| **Manali** | 900 | 1700 | 3800 |

---

## INTERNATIONAL DESTINATIONS (USD - Per Day)

### Europe
| Destination | Country | Budget/Day ($) | Medium/Day ($) | Luxury/Day ($) |
|---|---|---|---|---|
| **Paris** | France | 120 | 180 | 350 |
| **London** | United Kingdom | 130 | 200 | 380 |
| **Barcelona** | Spain | 110 | 170 | 330 |
| **Rome** | Italy | 100 | 160 | 320 |
| **Amsterdam** | Netherlands | 120 | 190 | 360 |
| **Iceland** | Iceland | 180 | 280 | 480 |

### Asia
| Destination | Country | Budget/Day ($) | Medium/Day ($) | Luxury/Day ($) |
|---|---|---|---|---|
| **Bangkok** | Thailand | 80 | 140 | 280 |
| **Bali** | Indonesia | 70 | 130 | 250 |
| **Singapore** | Singapore | 140 | 220 | 400 |
| **Tokyo** | Japan | 200 | 350 | 600 |

### Middle East & Indian Ocean
| Destination | Country | Budget/Day ($) | Medium/Day ($) | Luxury/Day ($) |
|---|---|---|---|---|
| **Dubai** | United Arab Emirates | 150 | 250 | 450 |
| **Maldives** | Maldives | 200 | 400 | 800 |

### North America
| Destination | Country | Budget/Day ($) | Medium/Day ($) | Luxury/Day ($) |
|---|---|---|---|---|
| **New York** | USA | 180 | 300 | 550 |
| **Los Angeles** | USA | 150 | 280 | 500 |

### Oceania
| Destination | Country | Budget/Day ($) | Medium/Day ($) | Luxury/Day ($) |
|---|---|---|---|---|
| **Sydney** | Australia | 160 | 280 | 500 |

---

## COST CALCULATION EXAMPLE

### Example: 5-Day Trip from Delhi to Puri

**Transportation Costs:**
- Bus: ₹3,000 (distance-based)
- Train: ₹2,000 (distance-based)
- Flight: ₹9,000 (distance-based)

**Accommodation Costs (5 days):**
- Budget Category: ₹4,000 (₹800/day)
- Medium Category: ₹7,500 (₹1,500/day)
- Luxury Category: ₹15,000 (₹3,000/day)

**Total Trip Cost (Budget Category with Train):**
Training Cost + 5 Days Budget Accommodation = ₹2,000 + ₹4,000 = **₹6,000**

---

## CURRENCY INFORMATION

- **Domestic (India):** Indian Rupees (₹)
- **International:** US Dollars ($)
  - Exchange rate basis: 1 USD ≈ 83 INR (approximate)

---

## HOW PER-DAY COSTS ARE CALCULATED

1. **Budget:** Budget accommodations, local transport, street food
2. **Medium:** Mid-range hotels, local food + restaurants, guided tours
3. **Luxury:** Premium hotels, fine dining, exclusive experiences

These are **accommodation-only costs**. Additional expenses include:
- Transportation (calculated separately based on distance)
- Activities & sightseeing
- Meals (partially covered in above)
- Shopping & miscellaneous

---

## DATABASE SCHEMA

```sql
CREATE TABLE destinations (
    id INTEGER PRIMARY KEY,
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
);
```

---

## Usage in API

**Endpoint:** `POST /api/trip-details`

**Request:**
```json
{
    "source": "Delhi",
    "destination": "Puri",
    "days": 5
}
```

**Response Includes:**
```json
{
    "accommodation_costs": {
        "budget": 4000,
        "medium": 7500,
        "luxury": 15000,
        "currency": "INR",
        "days": 5
    },
    "is_international": false
}
```

---

**Last Updated:** February 2026
