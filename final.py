import time
import json
import schedule
import requests
from telegram import Bot

telegram_token = "YOUR_TELEGRAM_TOKEN"
telegram_chat_id = "YOUR_CHAT_ID"

followed_trader_nickname = "TRADER_NICKNAME"
rapidapi_key = "YOUR_RAPID_API_KEY"

bot = Bot(token=telegram_token)
async def send_telegram_message(chat_id, text):
    request = Request()
    bot = Bot(token=telegram_bot_token, request=request)
    await bot.send_message(chat_id=chat_id, text=text)


def get_trader_encrypted_uid(nickname):
    url = "https://binance-futures-leaderboard1.p.rapidapi.com/v2/searchTrader"
    querystring = {"nickname": nickname}
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "binance-futures-leaderboard1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    data = response.json()
    if "data" in data:
        for trader in data["data"]:
            if "encryptedUid" in trader:
                return trader["encryptedUid"]
    print(f"Error: Encrypted UID not found in response. Response: {data}")
    return None


def get_trader_positions(encrypted_uid):
    url = "https://binance-futures-leaderboard1.p.rapidapi.com/v2/getTraderPositions"
    querystring = {"encryptedUid": encrypted_uid}
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "binance-futures-leaderboard1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data["data"]


def monitor_trader():
    print("Sprawdzanie pozycji tradera...")
    encrypted_uid = get_trader_encrypted_uid(followed_trader_nickname)
    positions_list = get_trader_positions(encrypted_uid)

    for positions in positions_list:
        if "perpetual" in positions and "delivery" in positions:
            if positions["perpetual"] or positions["delivery"]:
                message = f"Trader {followed_trader_nickname} otworzył pozycję: {positions}"
                print(message)
                asyncio.run(send_telegram_message(chat_id=telegram_chat_id, text=message))


schedule.every(30).seconds.do(monitor_trader)

while True:
    schedule.run_pending()
    time.sleep(1)