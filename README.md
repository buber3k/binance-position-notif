# binance-position-notif

Binance Position notif to skrypt w Pythonie, który monitoruje aktywność wybranego tradera na platformie [Binance Futures](https://www.binance.com/en/futures-activity/leaderboard/futures) i wysyła powiadomienia na Telegramie, gdy trader otwiera nową pozycję.

## Dlaczego jest przydatny?

Ten skrypt umożliwia automatyczne śledzenie działań najlepszych traderów, bez konieczności ciągłego sprawdzania platformy Binance. Otrzymujesz powiadomienia w czasie rzeczywistym, co pozwala na szybkie reagowanie na zmiany na rynku.

## Wymagania

Aby uruchomić skrypt, musisz mieć zainstalowanego Pythona 3.6 lub nowszego. Potrzebne są następujące biblioteki:

- python-binance
- python-telegram-bot
- schedule
- requests

Możesz zainstalować te biblioteki, używając polecenia:
`pip install python-binance python-telegram-bot schedule requests`

Unikalne wartości w pliku final.py:
   - telegram_token - token bota na platformie Telegram
   - telegram_chat_id - ID czatu, do którego mają być wysyłane powiadomienia
   - followed_trader_nickname - nazwa użytkownika tradera, którego chcesz śledzić do uzyskania z linku na początku pliku
   - rapidapi_key - skrypt korzysta z [następującego API](https://rapidapi.com/DevNullZero/api/binance-futures-leaderboard1)
