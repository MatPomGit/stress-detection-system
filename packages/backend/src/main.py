#!/usr/bin/env python3
"""
System Wykrywania Stresu w Czasie Rzeczywistym - Backend FastAPI
Real-Time Stress Detection System - FastAPI Backend

To jest usługa API backendu, która dostarcza endpointy do wykrywania stresu.
This is the backend API service that provides stress detection endpoints.

===== CO TO JEST API? / WHAT IS AN API? =====

API (Application Programming Interface) to "interfejs programistyczny" - 
sposób, w jaki różne programy komunikują się ze sobą.

API (Application Programming Interface) is a way for different programs
to communicate with each other.

W naszym przypadku:
In our case:
- Frontend (interfejs użytkownika) wysyła zapytania HTTP do backendu
  (Frontend (user interface) sends HTTP requests to backend)
- Backend przetwarza dane i zwraca wyniki
  (Backend processes data and returns results)

===== CO TO JEST FastAPI? / WHAT IS FastAPI? =====

FastAPI to nowoczesny framework Python do tworzenia API.
Jest szybki, łatwy w użyciu i automatycznie generuje dokumentację.

FastAPI is a modern Python framework for creating APIs.
It's fast, easy to use, and automatically generates documentation.

===== UWAGA O PRYWATNOŚCI / PRIVACY NOTICE =====

WAŻNE: Wszystko dzieje się lokalnie!
IMPORTANT: Everything happens locally!

- Wszystkie obliczenia wykonywane są lokalnie na Twoim urządzeniu
  (All processing happens locally on your device)
- Żadne dane NIE SĄ przekazywane do zewnętrznych serwerów
  (No data is transmitted to external servers)
- Tylko dane cech (nie treść) są przechowywane, zaszyfrowane algorytmem AES-256
  (Only feature data (not content) is stored, encrypted with AES-256)
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

# ===== IMPORTY BIBLIOTEK / LIBRARY IMPORTS =====
#
# WYJAŚNIENIE DLA POCZĄTKUJĄCYCH / EXPLANATION FOR BEGINNERS:
# Importujemy narzędzia (biblioteki), których będziemy używać:
# We import tools (libraries) that we'll use:

import uvicorn  # Serwer ASGI do uruchamiania FastAPI / ASGI server to run FastAPI
from fastapi import FastAPI, WebSocket, WebSocketDisconnect  # Framework FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Obsługa CORS (Cross-Origin Resource Sharing)
from loguru import logger  # Zaawansowane logowanie / Advanced logging
from pydantic import BaseModel  # Walidacja danych / Data validation

# ===== KONFIGURACJA LOGURU / LOGURU CONFIGURATION =====
#
# Loguru to biblioteka do logowania - zapisywania informacji o działaniu programu
# Loguru is a logging library - for recording information about program operation

logger.remove()  # Usuń domyślne handlery / Remove default handlers
logger.add(sys.stderr, level="INFO")  # Dodaj output do konsoli / Add console output
logger.add("logs/stress_backend.log", rotation="10 MB", retention="7 days")
# Dodaj output do pliku z rotacją:
# Add file output with rotation:
# - rotation="10 MB": Nowy plik co 10 MB (New file every 10 MB)
# - retention="7 days": Przechowuj logi przez 7 dni (Keep logs for 7 days)

# ===== INICJALIZACJA APLIKACJI FastAPI / INITIALIZE FastAPI APPLICATION =====
#
# Tworzymy główny obiekt aplikacji FastAPI
# We create the main FastAPI application object

app = FastAPI(
    title="Stress Detection API",  # Nazwa API / API name
    version="0.1.0",  # Wersja / Version
    description="Local API for real-time stress detection system",  # Opis / Description
    docs_url="/api/docs",  # URL dla interaktywnej dokumentacji Swagger UI
    redoc_url="/api/redoc",  # URL dla alternatywnej dokumentacji ReDoc
)
# 
# CO TO DAJE? / WHAT DOES THIS GIVE?
# Po uruchomieniu serwera możesz odwiedzić:
# After starting the server you can visit:
# - http://127.0.0.1:8765/api/docs - interaktywna dokumentacja (interactive docs)
# - http://127.0.0.1:8765/api/redoc - alternatywna dokumentacja (alternative docs)

# ===== MIDDLEWARE CORS / CORS MIDDLEWARE =====
#
# CORS (Cross-Origin Resource Sharing) pozwala frontendowi (Electron)
# komunikować się z backendem, nawet jeśli działają na różnych portach.
#
# CORS allows the frontend (Electron) to communicate with the backend,
# even if they run on different ports.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:*", "http://127.0.0.1:*"],  
    # Dozwolone originy / Allowed origins
    # "*" oznacza "dowolny port" / "*" means "any port"
    
    allow_credentials=True,  # Pozwól na ciasteczka / Allow cookies
    allow_methods=["*"],  # Wszystkie metody HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Wszystkie nagłówki / All headers
)


# ===== MODELE DANYCH PYDANTIC / PYDANTIC DATA MODELS =====
#
# WYJAŚNIENIE DLA POCZĄTKUJĄCYCH / EXPLANATION FOR BEGINNERS:
# 
# Pydantic to biblioteka do walidacji danych - sprawdza czy dane mają poprawny format.
# Pydantic is a library for data validation - it checks if data has the correct format.
#
# Klasy poniżej definiują "schematy" - jak powinny wyglądać dane w API.
# Classes below define "schemas" - how data should look in the API.

class HealthResponse(BaseModel):
    """
    Model odpowiedzi dla endpointu health check.
    Response model for the health check endpoint.
    
    ===== CO TO JEST HEALTH CHECK? / WHAT IS A HEALTH CHECK? =====
    
    Health check to prosty endpoint, który mówi czy serwer działa.
    Health check is a simple endpoint that tells if the server is running.
    
    Używane przez:
    Used by:
    - Monitorowanie (Monitoring tools)
    - Load balancery (Load balancers)
    - Testy (Tests)
    """
    status: str  # Status serwera, np. "healthy" / Server status, e.g. "healthy"
    version: str  # Wersja API / API version
    timestamp: datetime  # Czas odpowiedzi / Response time


class StressScore(BaseModel):
    """
    Model wyniku poziomu stresu.
    Stress level score model.
    
    ===== CO ZAWIERA? / WHAT DOES IT CONTAIN? =====
    
    To główny model danych - wynik analizy stresu użytkownika.
    This is the main data model - the result of user stress analysis.
    """
    score: int  # Wynik 0-100 (Score 0-100)
    level: str  # Poziom: LOW, MEDIUM, HIGH, CRITICAL
    confidence: float  # Pewność predykcji 0.0-1.0 (Prediction confidence)
    timestamp: datetime  # Kiedy został obliczony (When it was calculated)
    modules: dict[str, Optional[int]]  # Wyniki z poszczególnych modułów (Scores from individual modules)
    # Przykład / Example: {"behavioral": 75, "facial": 68, "voice": 71}


class Settings(BaseModel):
    """
    Model ustawień użytkownika.
    User settings model.
    
    ===== CO MOŻNA SKONFIGUROWAĆ? / WHAT CAN BE CONFIGURED? =====
    
    Użytkownik może włączyć/wyłączyć poszczególne moduły i ustawić progi.
    User can enable/disable individual modules and set thresholds.
    """
    behavioral_enabled: bool = True  # Czy moduł behawioralny jest włączony (Is behavioral module enabled)
    facial_enabled: bool = True  # Czy moduł twarzy jest włączony (Is facial module enabled)
    voice_enabled: bool = True  # Czy moduł głosu jest włączony (Is voice module enabled)
    notification_threshold: int = 70  # Próg powiadomienia (0-100) / Notification threshold
    # Jeśli stres > 70, wyślij powiadomienie / If stress > 70, send notification


# ===== GLOBALNY STAN APLIKACJI / GLOBAL APPLICATION STATE =====
#
# UWAGA DLA POCZĄTKUJĄCYCH / NOTE FOR BEGINNERS:
# To są zmienne globalne - dostępne w całej aplikacji.
# These are global variables - accessible throughout the application.
# 
# W produkcji zastąpimy je prawdziwymi serwisami i bazą danych.
# In production, we'll replace them with real services and database.

current_stress_score = 0  # Obecny wynik stresu (testowy) / Current stress score (test)
settings = Settings()  # Obecne ustawienia użytkownika / Current user settings


# ===== TRASY API (ENDPOINTY) / API ROUTES (ENDPOINTS) =====
#
# WYJAŚNIENIE DLA POCZĄTKUJĄCYCH / EXPLANATION FOR BEGINNERS:
# 
# Endpoint to "punkt końcowy" - adres URL, pod którym można coś zrobić.
# An endpoint is an "end point" - a URL address where you can do something.
#
# Przykład / Example:
# GET /api/health -> sprawdź czy serwer działa (check if server is running)
# GET /api/stress/current -> pobierz obecny poziom stresu (get current stress level)
#
# Dekoratory (@app.get, @app.post, etc.) definiują trasy.
# Decorators (@app.get, @app.post, etc.) define routes.

@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """
    Endpoint health check - sprawdza czy serwer działa.
    Health check endpoint - checks if server is running.
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Wyślij zapytanie GET do: http://127.0.0.1:8765/api/health
    Send GET request to: http://127.0.0.1:8765/api/health
    
    Odpowiedź / Response:
    {
        "status": "healthy",
        "version": "0.1.0",
        "timestamp": "2026-02-07T20:00:00"
    }
    
    ===== CO TO JEST async? / WHAT IS async? =====
    
    'async' oznacza funkcję asynchroniczną - może wykonywać się "w tle"
    nie blokując innych operacji. Ważne w serwerach!
    
    'async' means asynchronous function - can execute "in background"
    without blocking other operations. Important in servers!
    """
    return HealthResponse(
        status="healthy",  # Status: zdrowy (healthy)
        version="0.1.0",  # Wersja API / API version
        timestamp=datetime.now()  # Obecny czas / Current time
    )


@app.get("/api/stress/current", response_model=StressScore)
async def get_current_stress():
    """
    Pobierz obecny wynik poziomu stresu.
    Get current stress score.
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Wyślij zapytanie GET do: http://127.0.0.1:8765/api/stress/current
    Send GET request to: http://127.0.0.1:8765/api/stress/current
    
    ===== CO ZWRACA? / WHAT DOES IT RETURN? =====
    
    Zwraca obiekt StressScore z:
    Returns a StressScore object with:
    - score: liczba 0-100 (number 0-100)
    - level: LOW/MEDIUM/HIGH/CRITICAL
    - confidence: pewność 0.0-1.0 (confidence 0.0-1.0)
    - modules: wyniki z każdego modułu (results from each module)
    
    UWAGA / NOTE: Obecnie zwraca dane testowe (mock data).
    W przyszłości będą to prawdziwe wyniki z modeli ML.
    Currently returns test data (mock data).
    In future, will be real results from ML models.
    """
    # Dane testowe - będą zastąpione prawdziwym wnioskowaniem ML
    # Mock data - will be replaced with actual ML inference
    return StressScore(
        score=72,  # Wynik stresu: 72/100 (Stress score: 72/100)
        level="HIGH",  # Poziom: WYSOKI (Level: HIGH)
        confidence=0.85,  # Pewność: 85% (Confidence: 85%)
        timestamp=datetime.now(),  # Czas pomiaru (Measurement time)
        modules={
            "behavioral": 75,  # Moduł behawioralny: 75/100
            "facial": 68,  # Moduł twarzy: 68/100
            "voice": 71  # Moduł głosu: 71/100
        }
    )


@app.get("/api/settings", response_model=Settings)
async def get_settings():
    """
    Pobierz ustawienia użytkownika.
    Get user settings.
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Wyślij zapytanie GET do: http://127.0.0.1:8765/api/settings
    Send GET request to: http://127.0.0.1:8765/api/settings
    
    Zwraca obecne ustawienia (które moduły są włączone, progi, etc.)
    Returns current settings (which modules are enabled, thresholds, etc.)
    """
    return settings  # Zwróć globalne ustawienia / Return global settings


@app.put("/api/settings", response_model=Settings)
async def update_settings(new_settings: Settings):
    """
    Zaktualizuj ustawienia użytkownika.
    Update user settings.
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Wyślij zapytanie PUT do: http://127.0.0.1:8765/api/settings
    Send PUT request to: http://127.0.0.1:8765/api/settings
    
    Z ciałem JSON / With JSON body:
    {
        "behavioral_enabled": true,
        "facial_enabled": false,
        "voice_enabled": true,
        "notification_threshold": 80
    }
    
    ===== CO TO JEST PUT? / WHAT IS PUT? =====
    
    PUT to metoda HTTP używana do aktualizacji zasobów.
    PUT is an HTTP method used to update resources.
    
    - GET: pobierz dane (retrieve data)
    - POST: utwórz nowe (create new)
    - PUT: zaktualizuj istniejące (update existing)
    - DELETE: usuń (delete)
    """
    global settings  # Użyj globalnej zmiennej settings / Use global settings variable
    settings = new_settings  # Zaktualizuj ustawienia / Update settings
    logger.info(f"Ustawienia zaktualizowane: {settings}")
    logger.info(f"Settings updated: {settings}")
    return settings  # Zwróć nowe ustawienia / Return new settings


@app.post("/api/baseline/start")
async def start_baseline_calibration():
    """
    Rozpocznij proces kalibracji linii bazowej.
    Start baseline calibration process.
    
    ===== CO TO JEST LINIA BAZOWA? / WHAT IS A BASELINE? =====
    
    Linia bazowa to "Twoja norma" - jak zachowujesz się normalnie,
    bez stresu. System musi się tego nauczyć przez kilka dni.
    
    Baseline is "your norm" - how you behave normally,
    without stress. System needs to learn this over several days.
    
    ===== JAK DZIAŁA KALIBRACJA? / HOW DOES CALIBRATION WORK? =====
    
    1. System zbiera dane przez 5 dni (System collects data for 5 days)
    2. Analizuje Twoje typowe wzorce (Analyzes your typical patterns)
    3. Tworzy model "normalnego stanu" (Creates "normal state" model)
    4. Potem porównuje obecne zachowanie z bazową linią
       (Then compares current behavior with baseline)
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Wyślij zapytanie POST do: http://127.0.0.1:8765/api/baseline/start
    Send POST request to: http://127.0.0.1:8765/api/baseline/start
    
    WAŻNE / IMPORTANT:
    Podczas kalibracji pracuj normalnie! Nie symuluj stresu.
    During calibration, work normally! Don't simulate stress.
    """
    logger.info("Rozpoczynanie kalibracji linii bazowej...")
    logger.info("Starting baseline calibration...")
    return {
        "status": "started",  # Status: rozpoczęto (started)
        "estimated_days": 5,  # Szacowany czas: 5 dni (Estimated time: 5 days)
        "message": "Kalibracja linii bazowej rozpoczęta. Używaj aplikacji normalnie przez 5 dni." 
                   " / Baseline calibration started. Use the app normally for 5 days."
    }


@app.get("/api/baseline/status")
async def get_baseline_status():
    """
    Pobierz status kalibracji linii bazowej.
    Get baseline calibration status.
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Wyślij zapytanie GET do: http://127.0.0.1:8765/api/baseline/status
    Send GET request to: http://127.0.0.1:8765/api/baseline/status
    
    ===== CO ZWRACA? / WHAT DOES IT RETURN? =====
    
    Zwraca informacje o postępie kalibracji:
    Returns information about calibration progress:
    - status: "not_started" / "in_progress" / "completed"
    - progress: 0-100 (procent ukończenia / completion percentage)
    - days_completed: ile dni minęło (how many days passed)
    - days_remaining: ile dni pozostało (how many days remaining)
    """
    return {
        "status": "in_progress",  # Status: w trakcie (in progress)
        "progress": 40,  # Postęp: 40% (Progress: 40%)
        "days_completed": 2,  # Ukończono: 2 dni (Completed: 2 days)
        "days_remaining": 3  # Pozostało: 3 dni (Remaining: 3 days)
    }


# ===== WEBSOCKET DLA AKTUALIZACJI W CZASIE RZECZYWISTYM =====
# ===== WEBSOCKET FOR REAL-TIME UPDATES =====
#
# WYJAŚNIENIE DLA POCZĄTKUJĄCYCH / EXPLANATION FOR BEGINNERS:
#
# WebSocket to technologia pozwalająca na dwukierunkową komunikację
# w czasie rzeczywistym między serwerem a klientem.
#
# WebSocket is a technology allowing bidirectional real-time
# communication between server and client.
#
# Różnica vs HTTP:
# Difference vs HTTP:
# - HTTP: Klient pyta -> Serwer odpowiada (request-response)
# - WebSocket: Otwarty kanał, serwer może sam wysyłać dane
#              (Open channel, server can send data on its own)
#
# Użycie w naszej aplikacji:
# Use in our application:
# - Serwer wysyła aktualizacje poziomu stresu co 30 sekund
#   (Server sends stress level updates every 30 seconds)
# - Frontend otrzymuje je natychmiast bez ciągłego odpytywania
#   (Frontend receives them immediately without constant polling)

class ConnectionManager:
    """
    Menedżer połączeń WebSocket.
    WebSocket connection manager.
    
    ===== CO ROBI TA KLASA? / WHAT DOES THIS CLASS DO? =====
    
    Zarządza wszystkimi aktywnymi połączeniami WebSocket.
    Manages all active WebSocket connections.
    
    Funkcje / Functions:
    - connect(): Dodaj nowe połączenie (Add new connection)
    - disconnect(): Usuń połączenie (Remove connection)
    - broadcast(): Wyślij wiadomość do wszystkich (Send message to all)
    """
    def __init__(self):
        """
        Konstruktor - inicjalizuje pustą listę połączeń.
        Constructor - initializes empty connection list.
        """
        self.active_connections: list[WebSocket] = []  # Lista aktywnych połączeń / List of active connections

    async def connect(self, websocket: WebSocket):
        """
        Połącz nowego klienta.
        Connect new client.
        
        Args:
            websocket: Obiekt połączenia WebSocket / WebSocket connection object
        """
        await websocket.accept()  # Zaakceptuj połączenie / Accept connection
        self.active_connections.append(websocket)  # Dodaj do listy / Add to list
        logger.info(f"Klient WebSocket połączony. Łącznie: {len(self.active_connections)}")
        logger.info(f"WebSocket client connected. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        """
        Rozłącz klienta.
        Disconnect client.
        
        Args:
            websocket: Obiekt połączenia WebSocket / WebSocket connection object
        """
        self.active_connections.remove(websocket)  # Usuń z listy / Remove from list
        logger.info(f"Klient WebSocket rozłączony. Łącznie: {len(self.active_connections)}")
        logger.info(f"WebSocket client disconnected. Total: {len(self.active_connections)}")

    async def broadcast(self, message: dict):
        """
        Wyślij wiadomość do wszystkich połączonych klientów.
        Send message to all connected clients.
        
        Args:
            message: Wiadomość w formacie słownika / Message in dictionary format
        """
        for connection in self.active_connections:  # Dla każdego połączenia / For each connection
            try:
                await connection.send_json(message)  # Wyślij JSON / Send JSON
            except Exception as e:
                logger.error(f"Błąd wysyłania do klienta: {e}")
                logger.error(f"Error broadcasting to client: {e}")


# Stwórz globalną instancję menedżera / Create global manager instance
manager = ConnectionManager()


@app.websocket("/ws/stress")
async def websocket_endpoint(websocket: WebSocket):
    """
    Endpoint WebSocket dla aktualizacji stresu w czasie rzeczywistym.
    WebSocket endpoint for real-time stress updates.
    
    ===== JAK UŻYWAĆ? / HOW TO USE? =====
    
    Z JavaScriptu (frontend):
    From JavaScript (frontend):
    
    ```javascript
    const ws = new WebSocket('ws://127.0.0.1:8765/ws/stress');
    
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log('Nowy poziom stresu:', data);
        // Zaktualizuj UI / Update UI
    };
    ```
    
    ===== CO DZIEJE SIĘ KROK PO KROKU? / WHAT HAPPENS STEP BY STEP? =====
    
    1. Klient łączy się z /ws/stress (Client connects to /ws/stress)
    2. Serwer akceptuje połączenie (Server accepts connection)
    3. Co 30 sekund serwer wysyła aktualizację (Every 30 seconds server sends update)
    4. Klient otrzymuje dane i aktualizuje UI (Client receives data and updates UI)
    5. W przypadku błędu lub rozłączenia - cleanup (On error or disconnect - cleanup)
    """
    await manager.connect(websocket)  # Połącz klienta / Connect client
    try:
        while True:  # Nieskończona pętla / Infinite loop
            # Wyślij aktualizację stresu co 30 sekund
            # Send stress update every 30 seconds
            import asyncio
            await asyncio.sleep(30)  # Czekaj 30 sekund / Wait 30 seconds

            # Przygotuj dane (obecnie testowe)
            # Prepare data (currently test data)
            stress_data = {
                "event": "stress_update",  # Typ zdarzenia / Event type
                "data": {
                    "score": 72,  # Wynik / Score
                    "level": "HIGH",  # Poziom / Level
                    "confidence": 0.85,  # Pewność / Confidence
                    "timestamp": datetime.now().isoformat(),  # Czas / Time
                    "modules": {
                        "behavioral": 75,  # Behawioralny / Behavioral
                        "facial": 68,  # Twarz / Facial
                        "voice": 71  # Głos / Voice
                    }
                }
            }
            await websocket.send_json(stress_data)  # Wyślij JSON / Send JSON
            
    except WebSocketDisconnect:
        # Klient się rozłączył normalnie / Client disconnected normally
        manager.disconnect(websocket)
    except Exception as e:
        # Wystąpił błąd / An error occurred
        logger.error(f"Błąd WebSocket: {e}")
        logger.error(f"WebSocket error: {e}")
        manager.disconnect(websocket)


# ===== ZDARZENIA CYKLU ŻYCIA APLIKACJI / APPLICATION LIFECYCLE EVENTS =====
#
# WYJAŚNIENIE DLA POCZĄTKUJĄCYCH / EXPLANATION FOR BEGINNERS:
#
# FastAPI pozwala zdefiniować funkcje, które wykonają się:
# FastAPI allows defining functions that execute:
# - Przy starcie aplikacji (@app.on_event("startup"))
# - Przy zamykaniu aplikacji (@app.on_event("shutdown"))
#
# Użyteczne do:
# Useful for:
# - Inicjalizacji zasobów (połączenia DB, modele ML)
#   (Resource initialization - DB connections, ML models)
# - Czyszczenia zasobów przy zamykaniu
#   (Resource cleanup on shutdown)

@app.on_event("startup")
async def startup_event():
    """
    Funkcja wykonywana przy starcie aplikacji.
    Function executed on app startup.
    
    ===== CO SIĘ TUTAJ DZIEJE? / WHAT HAPPENS HERE? =====
    
    Ta funkcja wykonuje się RAZ, gdy serwer się uruchamia.
    This function executes ONCE when the server starts.
    
    Obecnie tylko wyświetla powitanie, ale w przyszłości będzie:
    Currently only displays welcome, but in future will:
    - Ładować modele ML (Load ML models)
    - Łączyć się z bazą danych (Connect to database)
    - Inicjalizować moduły monitorujące (Initialize monitoring modules)
    """
    logger.info("=" * 60)
    logger.info("Backend Wykrywania Stresu w Czasie Rzeczywistym v0.1.0")
    logger.info("Real-Time Stress Detection Backend v0.1.0")
    logger.info("Prywatność | Wielomodalny | Przetwarzanie Lokalne")
    logger.info("Privacy-First | Multi-Modal | Local Processing")
    logger.info("=" * 60)
    logger.info("Dokumentacja API: http://127.0.0.1:8765/api/docs")
    logger.info("API Docs: http://127.0.0.1:8765/api/docs")
    logger.info("=" * 60)
    
    # TODO: W przyszłości dodaj tutaj / In future add here:
    # - Ładowanie modeli ML / Loading ML models
    # - Inicjalizacja połączenia z bazą danych / Database connection initialization
    # - Weryfikacja wymaganych plików i katalogów / Verification of required files and directories


@app.on_event("shutdown")
async def shutdown_event():
    """
    Funkcja wykonywana przy zamykaniu aplikacji.
    Function executed on app shutdown.
    
    ===== CO SIĘ TUTAJ DZIEJE? / WHAT HAPPENS HERE? =====
    
    Ta funkcja wykonuje się RAZ, gdy serwer się wyłącza.
    This function executes ONCE when the server shuts down.
    
    Obecnie tylko loguje wiadomość, ale w przyszłości będzie:
    Currently only logs message, but in future will:
    - Zamykać połączenia WebSocket (Close WebSocket connections)
    - Zapisywać stan aplikacji (Save application state)
    - Zwalniać zasoby (Free resources)
    """
    logger.info("Zamykanie backendu wykrywania stresu...")
    logger.info("Shutting down Stress Detection Backend...")
    
    # TODO: W przyszłości dodaj tutaj / In future add here:
    # - Bezpieczne zamknięcie wszystkich połączeń / Safe closure of all connections
    # - Zapis stanu do bazy danych / Save state to database
    # - Zwolnienie pamięci modeli ML / Free ML models memory


def main():
    """
    Główny punkt wejścia dla uruchomienia serwera.
    Main entry point for running the server.
    
    ===== CO ROBI TA FUNKCJA? / WHAT DOES THIS FUNCTION DO? =====
    
    1. Tworzy katalog 'logs' jeśli nie istnieje
       (Creates 'logs' directory if it doesn't exist)
    2. Uruchamia serwer uvicorn z aplikacją FastAPI
       (Starts uvicorn server with FastAPI application)
    
    ===== JAK URUCHOMIĆ SERWER? / HOW TO START THE SERVER? =====
    
    Z terminala / From terminal:
    ```bash
    python src/main.py
    ```
    
    Lub bezpośrednio z uvicorn / Or directly with uvicorn:
    ```bash
    uvicorn src.main:app --host 127.0.0.1 --port 8765 --reload
    ```
    
    ===== PARAMETRY UVICORN / UVICORN PARAMETERS =====
    
    - "src.main:app": Ścieżka do obiektu aplikacji (Path to app object)
      - src.main: moduł (module)
      - app: zmienna (variable)
    
    - host="127.0.0.1": Nasłuchuj tylko lokalnie (Listen only locally)
      127.0.0.1 = localhost = Twój komputer (your computer)
      Bezpieczeństwo: Serwer NIE jest dostępny z zewnątrz
      Security: Server is NOT accessible from outside
    
    - port=8765: Numer portu (Port number)
      Aplikacja będzie dostępna pod: http://127.0.0.1:8765
      Application will be available at: http://127.0.0.1:8765
    
    - reload=True: Auto-restart przy zmianach kodu (Auto-restart on code changes)
      UWAGA: Używaj tylko w development! (NOTE: Use only in development!)
      W produkcji ustaw reload=False (In production set reload=False)
    
    - log_level="info": Poziom logowania (Logging level)
      Opcje / Options: "debug", "info", "warning", "error", "critical"
    """
    # KROK 1: Stwórz katalog logs / STEP 1: Create logs directory
    Path("logs").mkdir(exist_ok=True)  
    # exist_ok=True: Nie zgłaszaj błędu jeśli katalog już istnieje
    # exist_ok=True: Don't raise error if directory already exists

    # KROK 2: Uruchom serwer / STEP 2: Run server
    uvicorn.run(
        "src.main:app",  # Aplikacja do uruchomienia / Application to run
        host="127.0.0.1",  # Host (tylko lokalny / only local)
        port=8765,  # Port
        reload=True,  # Auto-reload (development mode)
        log_level="info"  # Poziom logowania / Logging level
    )


if __name__ == "__main__":
    # ===== CO TO ZNACZY? / WHAT DOES THIS MEAN? =====
    # 
    # To sprawdza, czy plik jest uruchamiany bezpośrednio.
    # This checks if the file is run directly.
    # 
    # Jeśli tak: uruchom main() i wystartuj serwer
    # If yes: run main() and start server
    # 
    # Jeśli plik jest importowany: nie uruchamiaj serwera
    # If file is imported: don't start server
    
    main()  # Uruchom serwer / Start server
