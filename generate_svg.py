#!/usr/bin/env python3

import json
import urllib.request
from datetime import datetime, timezone, timedelta

# ============================================================
# 설정
# ============================================================
NAME = "Jamse"
CITY = "Sejong, Korea"
LATITUDE = 36.524890879378766
LONGITUDE = 127.26123133804998
TIMEZONE = "Asia/Seoul"
GITHUB_URL = "https://github.com/im6705"
# ============================================================


def get_weather():
    """Open-Meteo API로 현재 날씨 가져오기"""
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}&longitude={LONGITUDE}"
        f"&current=temperature_2m,weather_code"
        f"&timezone={TIMEZONE}"
    )
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        current = data["current"]
        temp_c = current["temperature_2m"]
        temp_f = round(temp_c * 9 / 5 + 32)
        code = current["weather_code"]
        return temp_c, temp_f, wmo_to_emoji(code), wmo_to_text(code)
    except Exception as e:
        print(f"날씨 API 오류: {e}")
        return 20, 68, "☁️", "Cloudy"


def wmo_to_emoji(code):
    """WMO 날씨 코드 → 이모지"""
    mapping = {
        0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️",
        45: "🌫️", 48: "🌫️",
        51: "🌦️", 53: "🌦️", 55: "🌧️",
        61: "🌧️", 63: "🌧️", 65: "🌧️",
        71: "🌨️", 73: "🌨️", 75: "🌨️",
        80: "🌧️", 81: "🌧️", 82: "🌧️",
        95: "⛈️", 96: "⛈️", 99: "⛈️",
    }
    return mapping.get(code, "🌤️")


def wmo_to_text(code):
    """WMO 날씨 코드 → 영문 텍스트"""
    mapping = {
        0: "Clear", 1: "Mostly Clear", 2: "Partly Cloudy", 3: "Cloudy",
        45: "Foggy", 48: "Foggy",
        51: "Light Drizzle", 53: "Drizzle", 55: "Heavy Drizzle",
        61: "Light Rain", 63: "Rain", 65: "Heavy Rain",
        71: "Light Snow", 73: "Snow", 75: "Heavy Snow",
        80: "Showers", 81: "Showers", 82: "Heavy Showers",
        95: "Thunderstorm", 96: "Thunderstorm", 99: "Thunderstorm",
    }
    return mapping.get(code, "Partly Cloudy")


def get_greeting():
    """시간대별 인사말"""
    kst = timezone(timedelta(hours=9))
    hour = datetime.now(kst).hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def get_day_of_week():
    """현재 요일 (KST 기준)"""
    kst = timezone(timedelta(hours=9))
    return datetime.now(kst).strftime("%A")


def generate_svg():
    temp_c, temp_f, weather_emoji, weather_text = get_weather()
    greeting = get_greeting()
    day = get_day_of_week()

    svg = f'''<svg width="550" height="340" viewBox="0 0 550 340" fill="none"
  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <style>
    .bubble {{ fill: #e9e9eb; }}
    a {{ fill: #0079ff; }}
    text {{ fill: #242424; font-size: 18px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; letter-spacing: -0.02em; }}
    .emoji {{ font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif; }}

    .typing-1 {{ opacity: 0; animation: fade-in-out 1.5s; }}
    .msg-1    {{ animation: wait 1.7s, msg-1 0.2s 1.7s; }}

    .typing-2 {{ opacity: 0; animation: wait 2.5s, fade-in-out 1.5s 2.5s; }}
    .msg-2    {{ animation: wait 4.2s, msg-2 0.2s 4.2s; }}

    .typing-3 {{ opacity: 0; animation: wait 5s, fade-in-out 1.5s 5s; }}
    .msg-3    {{ animation: wait 6.7s, msg-3 0.2s 6.7s; }}

    .typing-4 {{ opacity: 0; animation: wait 7.5s, fade-in-out 1.5s 7.5s; }}
    .msg-4    {{ animation: wait 9.2s, msg-4 0.2s 9.2s; }}

    @keyframes wait {{ 0%,100% {{ opacity: 0; }} }}
    @keyframes fade-in-out {{ 0%,100% {{ opacity: 0; }} 25%,90% {{ opacity: 1; }} }}
    @keyframes msg-1 {{ 0% {{ opacity:0; transform:translate(10px,5px); }} 100% {{ opacity:1; transform:translate(10px,0); }} }}
    @keyframes msg-2 {{ 0% {{ opacity:0; transform:translate(10px,53px); }} 100% {{ opacity:1; transform:translate(10px,48px); }} }}
    @keyframes msg-3 {{ 0% {{ opacity:0; transform:translate(10px,125px); }} 100% {{ opacity:1; transform:translate(10px,120px); }} }}
    @keyframes msg-4 {{ 0% {{ opacity:0; transform:translate(10px,197px); }} 100% {{ opacity:1; transform:translate(10px,192px); }} }}

    @media (prefers-color-scheme: dark) {{
      .bubble {{ fill: #3b3b3d; }}
      text {{ fill: #dcdcdc; }}
      a {{ fill: #0c82f9; }}
    }}
  </style>

  <!-- typing 1 -->
  <g transform="translate(10, 0)" class="typing-1">
    <rect x="8" width="70" height="42" rx="21" class="bubble"/>
    <circle cx="14" cy="33" r="8" class="bubble"/>
    <circle cx="4" cy="42" r="4" class="bubble"/>
    <circle cx="28" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/></circle>
    <circle cx="43" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.2s" repeatCount="indefinite"/></circle>
    <circle cx="58" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.4s" repeatCount="indefinite"/></circle>
  </g>

  <!-- msg 1: greeting -->
  <g transform="translate(10, 0)" class="msg-1 bubble">
    <rect width="220" height="42" rx="18"/>
    <text x="15" y="27">{greeting}! I'm {NAME} <tspan class="emoji">👋</tspan></text>
  </g>

  <!-- typing 2 -->
  <g transform="translate(10, 48)" class="typing-2">
    <rect x="8" width="70" height="42" rx="21" class="bubble"/>
    <circle cx="14" cy="33" r="8" class="bubble"/>
    <circle cx="4" cy="42" r="4" class="bubble"/>
    <circle cx="28" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/></circle>
    <circle cx="43" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.2s" repeatCount="indefinite"/></circle>
    <circle cx="58" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.4s" repeatCount="indefinite"/></circle>
  </g>

  <!-- msg 2: location + weather -->
  <g transform="translate(10, 48)" class="msg-2">
    <rect width="440" height="66" rx="18" class="bubble"/>
    <text x="15" y="27">I'm from {CITY}, where it's currently</text>
    <text x="15" y="50">{temp_f}°F ({temp_c}°C) and <tspan class="emoji">{weather_emoji}</tspan> {weather_text} today.</text>
  </g>

  <!-- typing 3 -->
  <g transform="translate(10, 120)" class="typing-3">
    <rect x="8" width="70" height="42" rx="21" class="bubble"/>
    <circle cx="14" cy="33" r="8" class="bubble"/>
    <circle cx="4" cy="42" r="4" class="bubble"/>
    <circle cx="28" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/></circle>
    <circle cx="43" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.2s" repeatCount="indefinite"/></circle>
    <circle cx="58" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.4s" repeatCount="indefinite"/></circle>
  </g>

  <!-- msg 3: interests -->
  <g transform="translate(10, 120)" class="msg-3">
    <rect width="470" height="66" rx="18" class="bubble"/>
    <text x="15" y="27">I'm a developer who loves building things.</text>
    <text x="15" y="50">Currently working with C#, Rust &amp; Claude Code.</text>
  </g>

  <!-- typing 4 -->
  <g transform="translate(10, 192)" class="typing-4">
    <rect x="8" width="70" height="42" rx="21" class="bubble"/>
    <circle cx="14" cy="33" r="8" class="bubble"/>
    <circle cx="4" cy="42" r="4" class="bubble"/>
    <circle cx="28" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/></circle>
    <circle cx="43" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.2s" repeatCount="indefinite"/></circle>
    <circle cx="58" cy="21" r="5" fill="#999"><animate attributeName="opacity" values="0.5;1;0.5" dur="1s" begin="0.4s" repeatCount="indefinite"/></circle>
  </g>

  <!-- msg 4: closing -->
  <g transform="translate(10, 192)" class="msg-4">
    <rect width="290" height="42" rx="18" class="bubble"/>
    <text x="15" y="27">Have a great {day}! <tspan class="emoji">✨</tspan></text>
  </g>
</svg>'''

    with open("greeting.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✅ greeting.svg 생성 완료!")
    print(f"   {greeting}, {day}, {temp_c}°C/{temp_f}°F, {weather_emoji} {weather_text}")


if __name__ == "__main__":
    generate_svg()
