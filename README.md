# Telegram Bot — Cities Game with Environment Data

## Short Description

This project is a **Telegram game bot** where users play the classic “Cities” game while receiving additional real-world data about each city.  
The bot validates city names, tracks used cities, responds with its own city, and enriches gameplay with geographic, environmental, and informational data.

---

## Core Functionality

### Game Logic
- User enters a city name (case-sensitive)
- The city must start with the last valid letter of the previous city
- Used cities are tracked to prevent repetition
- The bot responds with a valid city on the required letter

### City Validation
- Uses **geonamescache** to verify city existence
- Retrieves latitude and longitude
- Sends city location on the map

---

## External Data Integration

For each city, the bot provides:
- **Air Quality Index (AQI)** and weather data via *AirVisual API*
- Country, temperature, wind speed, air pollution level
- Short city description from **Wikipedia**
- Random city image from **Unsplash API**

---

## Database (SQLite)

A separate module demonstrates basic SQLite operations:
- Table creation
- Insert, select, update, delete queries  
Used mainly as a learning/practice component.

---

## Project Structure

- `game_cities.py` — main bot logic and gameplay
- `AQI.py` — interaction with AirVisual API
- `SQLite.py` — SQLite examples and database operations

---

## Technologies Used

- Python
- telebot (pyTelegramBotAPI)
- SQLite
- geonamescache
- Wikipedia API
- AirVisual API
- Unsplash API

---

## Purpose

This project demonstrates:
- game logic in a Telegram bot
- API integration for real-time data
- geographic data processing
- combining entertainment with educational content

