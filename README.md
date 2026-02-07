# System Wykrywania Stresu w Czasie Rzeczywistym
# Real-Time Stress Detection System

> Inteligentna aplikacja desktopowa, która dba o prywatność użytkownika i monitoruje profesjonalistów IT oraz pracowników zdalnych w celu wczesnego wykrywania oznak stresu zawodowego przy użyciu wielomodalnej analizy sztucznej inteligencji.
>
> An intelligent, privacy-first desktop application that monitors IT professionals and remote workers for early signs of workplace stress using multi-modal AI analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status: In Development](https://img.shields.io/badge/status-in%20development-orange.svg)]()

---

## 🎯 Przegląd projektu / Overview

**System Wykrywania Stresu** (Stress Detection System) to zaawansowany projekt, który łączy trzy różne metody analizy:
1. **Analizę behawioralną** - śledzi sposób, w jaki pracujesz przy komputerze
2. **Rozpoznawanie mimiki twarzy** - analizuje Twoje wyrazy twarzy podczas pracy
3. **Wykrywanie wzorców głosu** - bada Twój głos podczas rozmów wideo

Wszystkie te metody działają razem, aby dostarczyć świadomość poziomu stresu w miejscu pracy w czasie rzeczywistym—zanim dojdzie do wypalenia zawodowego.

The **Stress Detection System** combines behavioral analysis, facial recognition, and voice pattern detection to provide real-time awareness of workplace stress levels—before burnout occurs.

### Kluczowe cechy / Key Features

- **🔐 Prywatność przede wszystkim (Privacy-First)**: 
  - Wszystkie obliczenia wykonywane są lokalnie na Twoim komputerze
  - Żadne dane nie są wysyłane przez Internet
  - 100% przetwarzania lokalnego, zero transmisji danych
  - All processing happens on your computer, zero data transmission

- **🤖 Wielomodalna sztuczna inteligencja (Multi-Modal AI)**: 
  - System łączy 3 niezależne sygnały analizy
  - Osiąga dokładność powyżej 85%
  - Combines 3 independent signals for 85%+ accuracy

- **📊 Spersonalizowane linie bazowe (Personalized Baselines)**: 
  - System uczy się TWOICH normalnych wzorców zachowania
  - Nie stosuje ogólnych progów dla wszystkich
  - Learns YOUR normal patterns, not generic thresholds

- **⚡ Monitorowanie w czasie rzeczywistym (Real-Time Monitoring)**: 
  - Wyniki analizy stresu w ciągu 5 sekund
  - Natychmiastowa informacja zwrotna
  - Stress insights within 5 seconds

- **🎨 Nieintru zywny (Non-Intrusive)**: 
  - Brak ankiet do wypełniania
  - Brak przerw w Twojej pracy
  - No surveys, no workflow interruption

---

## 🚀 Dlaczego ten projekt? / Why This Project?

### Problem / The Problem

**Wypalenie zawodowe to poważny problem w dzisiejszym świecie pracy:**
Workplace burnout is a serious problem in today's work environment:

- 76% pracowników doświadcza symptomów wypalenia zawodowego, zanim w ogóle rozpozna stres
  (76% of employees experience burnout symptoms before recognizing stress)
- Istniejące rozwiązania opierają się na zawodnych ankietach samooceny
  (Existing solutions rely on unreliable self-reporting surveys)
- Wykrywanie emocji na podstawie jednego sygnału ma tylko 60-65% dokładności
  (Single-signal emotion detection has only 60-65% accuracy)
- Średni czas od pojawienia się stresu do jego rozpoznania: **4-6 tygodni** ⏰
  (Average time from stress onset to recognition: 4-6 weeks)

### Nasze rozwiązanie / Our Solution

**Wielomodalne wykrywanie stresu** łączące trzy niezależne metody analizy:
**Multi-modal stress detection** combining three independent analysis methods:

1. **Monitorowanie behawioralne (Behavioral Monitoring)** - waga 50%
   - **Co analizujemy:** wzorce pisania na klawiaturze, używanie aplikacji, czas bezczynności
     (What we analyze: typing patterns, app usage, idle time)
   - **Jak to działa:** System obserwuje, jak szybko piszesz, ile robisz błędów, jak często przełączasz się między aplikacjami
     (How it works: The system observes your typing speed, error rate, and app switching behavior)
   - **Działanie w tle:** Pracuje cicho w tle, nie przeszkadzając w Twojej pracy
     (Works silently in background without interrupting your work)

2. **Analiza twarzy (Facial Analysis)** - waga 30%
   - **Co analizujemy:** mikroekspresje, zmęczenie oczu, napięcie mięśni twarzy
     (What we analyze: micro-expressions, eye strain, facial tension)
   - **Kiedy działa:** Aktywna tylko podczas rozmów wideo
     (Active during video calls only)
   - **Ochrona prywatności:** System NIE nagrywa wideo, analizuje tylko punkty orientacyjne twarzy (współrzędne)
     (Privacy protection: Does NOT record video, only analyzes facial landmarks)

3. **Analiza głosu (Voice Analysis)** - waga 20%
   - **Co analizujemy:** wysokość dźwięku, ton, tempo mowy, pauzy
     (What we analyze: pitch, tone, speech rate, pauses)
   - **Kiedy działa:** Aktywna tylko podczas rozmów wideo
     (Active during video calls only)
   - **Ochrona prywatności:** System NIE nagrywa audio, wyodrębnia tylko cechy liczbowe
     (Privacy protection: Does NOT record audio, only extracts numerical features)

**Wynik / Result**: Wczesna interwencja, która zapobiega wypaleniu zawodowemu w późnych godzinach popołudniowych
(Early intervention that prevents late-afternoon burnout)

---

## 📐 Architektura systemu / Architecture

**Schemat działania systemu (krok po kroku):**
**System workflow (step by step):**

```
┌─────────────────────────────────────────────────────┐
│  KROK 1: Użytkownik pracuje normalnie               │
│  STEP 1: User Works Normally                        │
└───────────────┬─────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  KROK 2: Monitorowanie w tle (3 moduły)           │
│  STEP 2: Background Monitoring (3 Modules)        │
├────────────────────────────────────────────────────┤
│  Moduł 1 (Module 1): Behawioralny → Pisanie,     │
│          aplikacje, czas bezczynności              │
│          Behavioral → Typing, apps, idle time      │
│  Moduł 2 (Module 2): Twarz → Ekspresje podczas    │
│          rozmów wideo                              │
│          Facial → Expressions during video calls   │
│  Moduł 3 (Module 3): Głos → Wysokość, ton         │
│          podczas rozmów                            │
│          Voice → Pitch, tone during calls          │
└───────────────┬────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  KROK 3: Porównanie ze spersonalizowaną linią     │
│          bazową                                    │
│  STEP 3: Personalized Baseline Comparison         │
│  (Twoje normalne zachowanie vs. obecne)           │
│  (Your normal vs. current behavior)                │
└───────────────┬────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  KROK 4: Silnik fuzji wielomodalnej               │
│  STEP 4: Multi-Modal Fusion Engine                │
│  Średnia ważona: 50% + 30% + 20%                  │
│  Weighted average: 50% + 30% + 20%                │
└───────────────┬────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  KROK 5: Wynik - Poziom stresu (0-100)            │
│  STEP 5: Stress Score (0-100)                     │
│  Niski / Średni / Wysoki / Krytyczny              │
│  Low / Medium / High / Critical                   │
└───────────────┬────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  KROK 6: Dashboard i delikatne powiadomienia      │
│  STEP 6: Dashboard + Gentle Alerts                │
│  "Rozważ przerwę" (nie "JESTEŚ ZESTRESOWANY!")    │
│  "Consider a break" (not "YOU ARE STRESSED!")     │
└────────────────────────────────────────────────────┘
```

**Wyjaśnienie krok po kroku / Step-by-step explanation:**

1. **Praca normalna:** Używasz komputera jak zwykle - piszesz kod, czytasz dokumentację, uczestniczysz w spotkaniach
   (Normal work: You use your computer as usual)

2. **Zbieranie danych:** System dyskretnie zbiera dane z trzech źródeł jednocześnie
   (Data collection: System discretely collects data from three sources)

3. **Analiza wzorców:** Twoje obecne wzorce są porównywane z Twoją osobistą "normą"
   (Pattern analysis: Your current patterns are compared to your personal "normal")

4. **Kombinacja sygnałów:** Wszystkie trzy sygnały są łączone zgodnie z wagami (50%, 30%, 20%)
   (Signal combination: All three signals are combined according to weights)

5. **Obliczenie wyniku:** System generuje pojedynczą liczbę (0-100) reprezentującą poziom stresu
   (Score calculation: System generates a single number representing stress level)

6. **Wyświetlenie rezultatu:** Widzisz wynik na delikatnym, nieintru zywnym dashboardzie
   (Display result: You see the result on a gentle, non-intrusive dashboard)

---

## 🛠️ Stos technologiczny / Technology Stack

### Backend (Silnik główny / Core Engine)

**Czym jest backend?** To "mózg" aplikacji - część odpowiedzialna za przetwarzanie danych i wykonywanie obliczeń.
(What is backend? It's the "brain" of the application - the part responsible for data processing and computations.)

- **Python 3.10+** - Główny język programowania (prosty i potężny)
  (Main programming language - simple yet powerful)
- **OpenCV 4.8+** - Biblioteka do przetwarzania wideo i obrazów
  (Library for video and image processing)
- **MediaPipe 0.10+** - Detekcja twarzy i punktów orientacyjnych (stworzona przez Google)
  (Face detection and landmarks - created by Google)
- **OpenFace 2.2.0** - Rozpoznawanie jednostek akcji mimicznej (Facial Action Units)
  (Facial Action Unit recognition)
- **librosa 0.10+** - Ekstrakcja cech audio (analiza dźwięku)
  (Audio feature extraction - sound analysis)
- **scikit-learn 1.3+** - Modele uczenia maszynowego (Machine Learning)
  (Machine learning models)
- **SQLite 3.40+** - Lokalna baza danych (zaszyfrowana dla bezpieczeństwa)
  (Local database - encrypted for security)

### Frontend (Interfejs użytkownika / Desktop UI)

**Czym jest frontend?** To część aplikacji, którą widzisz i z którą współdziałasz - okna, przyciski, wykresy.
(What is frontend? It's the part of the application you see and interact with - windows, buttons, charts.)

- **Electron 27+** - Framework do tworzenia aplikacji desktopowych z technologii webowych
  (Cross-platform desktop framework using web technologies)
- **React 18+** - Biblioteka do budowania interfejsu użytkownika (stworzona przez Facebook)
  (UI component library - created by Facebook)
- **Chart.js 4+** - Wizualizacja danych (tworzenie wykresów i grafów)
  (Data visualization - creating charts and graphs)
- **Tailwind CSS 3+** - Framework CSS do stylizacji (czyni aplikację ładną)
  (CSS framework for styling - makes the app look good)

### Modele ML (Uczenie maszynowe / Machine Learning)

**Czym jest ML?** Uczenie maszynowe to technika, która pozwala komputerom "uczyć się" z danych i podejmować decyzje.
(What is ML? Machine learning is a technique that allows computers to "learn" from data and make decisions.)

- **Isolation Forest** - Wykrywanie anomalii (odchyleń od normy)
  (Anomaly detection - finding deviations from normal)
- **Random Forest** - Klasyfikacja stresu (cel: dokładność 85%+)
  (Stress classification - target: 85%+ accuracy)
- **OpenFace CNN** - Sieć neuronowa do ekstrakcji jednostek akcji mimicznej
  (Convolutional Neural Network for Facial Action Unit extraction)
- **SVM** - Wykrywanie stresu w głosie (oparty na MFCC)
  (Voice stress detection - MFCC-based)

---

## 📂 Struktura projektu / Project Structure

**Wyjaśnienie struktury katalogów (dla początkujących):**
**Directory structure explanation (for beginners):**

```
stress-detection-system/          # Główny katalog projektu (Main project directory)
│
├── docs/                          # 📚 DOKUMENTACJA (DOCUMENTATION)
│   │                              # Tutaj znajdują się wszystkie dokumenty opisujące projekt
│   │                              # Here you'll find all documents describing the project
│   ├── PRD_Stress_Detection_System.md    # Dokument wymagań produktu (Product Requirements)
│   ├── architecture.md            # Architektura techniczna (Technical architecture)
│   ├── user-guide.md              # Dokumentacja dla użytkowników (End-user documentation)
│   └── api-reference.md           # Dokumentacja API dla programistów (Developer API docs)
│
├── src/                           # 💻 KOD ŹRÓDŁOWY (SOURCE CODE)
│   │                              # Cały kod aplikacji znajduje się tutaj
│   │                              # All application code is here
│   ├── backend/                   # ⚙️ Backend w Pythonie (Python backend)
│   │   │                          # Część odpowiedzialna za logikę i przetwarzanie
│   │   │                          # Part responsible for logic and processing
│   │   ├── modules/               # Główne moduły monitorujące (Core monitoring modules)
│   │   │   ├── behavioral/        # Monitorowanie behawioralne (typing, apps)
│   │   │   ├── facial/            # Analiza twarzy (Facial analysis)
│   │   │   ├── voice/             # Analiza głosu (Voice analysis)
│   │   │   └── fusion/            # Fuzja wielomodalna (Multi-modal fusion)
│   │   ├── ml/                    # 🤖 Uczenie maszynowe (Machine learning)
│   │   │   ├── models/            # Wytrenowane modele (Trained models)
│   │   │   ├── training/          # Skrypty treningowe (Training scripts)
│   │   │   └── inference/         # Wnioskowanie w czasie rzeczywistym (Real-time inference)
│   │   ├── database/              # Przechowywanie danych (Data persistence)
│   │   ├── utils/                 # Narzędzia pomocnicze (Utilities)
│   │   └── main.py                # 🚀 Punkt wejścia (Entry point)
│   │
│   ├── frontend/                  # 🎨 Interfejs użytkownika Electron/React (Electron/React UI)
│   │   │                          # Część wizualna aplikacji, którą widzisz
│   │   │                          # Visual part of the app that you see
│   │   ├── src/
│   │   │   ├── components/        # Komponenty React (przyciski, wykresy, itp.)
│   │   │   │                      # React components (buttons, charts, etc.)
│   │   │   ├── pages/             # Strony (Dashboard, Settings)
│   │   │   ├── hooks/             # Własne hooki React (Custom React hooks)
│   │   │   └── App.tsx            # Główna aplikacja (Main app)
│   │   ├── public/                # Zasoby statyczne (obrazki, ikony)
│   │   │                          # Static assets (images, icons)
│   │   └── electron/              # Główny proces Electron (Electron main process)
│   │
│   └── shared/                    # Współdzielone narzędzia (Shared utilities)
│                                  # Kod używany zarówno przez backend jak i frontend
│                                  # Code used by both backend and frontend
│
├── tests/                         # 🧪 TESTY (TEST SUITES)
│   │                              # Testy sprawdzające poprawność kodu
│   │                              # Tests verifying code correctness
│   ├── unit/                      # Testy jednostkowe (Unit tests)
│   │                              # Testują pojedyncze funkcje
│   │                              # Test individual functions
│   ├── integration/               # Testy integracyjne (Integration tests)
│   │                              # Testują współpracę modułów
│   │                              # Test module interactions
│   └── e2e/                       # Testy end-to-end (End-to-end tests)
│                                  # Testują całą aplikację
│                                  # Test entire application
│
├── datasets/                      # 📊 DANE TRENINGOWE (TRAINING DATA) - NIE W REPOZYTORIUM
│   │                              # Dane do uczenia modeli (nie znajdują się w Git)
│   │                              # Data for training models (not in Git)
│   ├── WESAD/                     # Zbiór danych stres z urządzeń noszonych (Wearable stress dataset)
│   ├── SAVEE/                     # Zbiór danych emocji w mowie (Speech emotion dataset)
│   └── custom/                    # Własne dane oznaczone (Custom labeled data)
│
├── scripts/                       # 🔧 SKRYPTY DEWELOPERSKIE (DEVELOPMENT SCRIPTS)
│   │                              # Narzędzia pomocnicze do rozwoju projektu
│   │                              # Helper tools for project development
│   ├── setup.sh                   # Konfiguracja środowiska (Environment setup)
│   ├── train_models.py            # Trenowanie modeli (Model training)
│   └── build.sh                   # Budowanie aplikacji (Build application)
│
├── .github/                       # ⚙️ KONFIGURACJA GITHUB (GITHUB CONFIGURATION)
│   ├── workflows/                 # Pipeline CI/CD (automatyczne testy)
│   │                              # CI/CD pipelines (automated tests)
│   └── ISSUE_TEMPLATE/            # Szablony zgłoszeń (Issue templates)
│
├── .gitignore                     # Lista plików ignorowanych przez Git
│                                  # List of files ignored by Git
├── LICENSE                        # Licencja MIT (MIT License)
├── README.md                      # Ten plik! (This file!)
├── CONTRIBUTING.md                # Wytyczne dla kontrybutorów (Contribution guidelines)
├── requirements.txt               # Zależności Python (Python dependencies)
├── package.json                   # Zależności Node.js (Node.js dependencies)
└── pyproject.toml                 # Konfiguracja projektu Python (Python project config)
```

**Najważniejsze katalogi do nauki / Most important directories for learning:**
1. **`src/backend/main.py`** - zacznij tutaj! (start here!)
2. **`docs/`** - przeczytaj dokumentację (read documentation)
3. **`tests/`** - zobacz przykłady użycia (see usage examples)

---

## 🚦 Pierwsze kroki / Getting Started

### Wymagania wstępne / Prerequisites

**Co musisz mieć zainstalowane na swoim komputerze:**
**What you need to have installed on your computer:**

- **Python 3.10 lub nowszy (or newer)**
  - Sprawdź wersję: `python --version` lub `python3 --version`
  - Pobierz z: https://www.python.org/downloads/
  - **Ważne dla początkujących:** Podczas instalacji zaznacz "Add Python to PATH"!
  
- **Node.js 18+ i npm**
  - Sprawdź wersję: `node --version` i `npm --version`
  - Pobierz z: https://nodejs.org/
  - npm instaluje się automatycznie z Node.js
  
- **Git** - system kontroli wersji (version control system)
  - Sprawdź wersję: `git --version`
  - Pobierz z: https://git-scm.com/downloads
  
- **Kamera internetowa (Webcam)** - do modułu analizy twarzy (for facial module)
- **Mikrofon (Microphone)** - do modułu analizy głosu (for voice module)

### Instalacja krok po kroku / Step-by-step Installation

**KROK 1: Sklonuj repozytorium (pobierz kod projektu)**
**STEP 1: Clone the repository (download project code)**

```bash
# Otwórz terminal/wiersz poleceń (Open terminal/command prompt)
# Przejdź do katalogu, gdzie chcesz mieć projekt (Navigate to where you want the project)
cd ~/Documents  # Przykład (Example): folder Dokumenty

# Sklonuj repozytorium (Clone repository)
git clone https://github.com/Nuvai/stress-detection-system.git

# Przejdź do katalogu projektu (Enter project directory)
cd stress-detection-system

# Co się stało? Git pobrał wszystkie pliki projektu na Twój komputer
# What happened? Git downloaded all project files to your computer
```

**KROK 2: Skonfiguruj środowisko Python (izolowane od systemu)**
**STEP 2: Set up Python environment (isolated from system)**

```bash
# Utwórz wirtualne środowisko Python (Create Python virtual environment)
# Dlaczego? Aby nie mieszać zależności projektu z systemem
# Why? To not mix project dependencies with your system
python -m venv venv

# Aktywuj wirtualne środowisko (Activate virtual environment)
# Na Linux/Mac:
source venv/bin/activate

# Na Windows:
venv\Scripts\activate

# Jak poznasz, że jest aktywne? Zobaczysz (venv) przed promptem w terminalu
# How to know it's active? You'll see (venv) before the prompt in terminal

# Zainstaluj zależności Python z pliku requirements.txt
# Install Python dependencies from requirements.txt file
pip install -r requirements.txt

# Co się stało? pip zainstalował wszystkie potrzebne biblioteki Python
# What happened? pip installed all necessary Python libraries
```

**KROK 3: Skonfiguruj frontend (interfejs użytkownika)**
**STEP 3: Set up frontend (user interface)**

```bash
# Przejdź do katalogu frontend (Navigate to frontend directory)
cd src/frontend

# Zainstaluj zależności Node.js z pliku package.json
# Install Node.js dependencies from package.json file
npm install

# Co się stało? npm pobrał wszystkie biblioteki JavaScript potrzebne do UI
# What happened? npm downloaded all JavaScript libraries needed for UI

# Wróć do głównego katalogu (Go back to main directory)
cd ../..
```

**KROK 4: Pobierz modele ML (jednorazowo)**
**STEP 4: Download ML models (one-time)**

```bash
# Uruchom skrypt pobierający modele (Run script to download models)
python scripts/download_models.py

# Co się stało? Skrypt pobrał wstępnie wytrenowane modele AI
# What happened? Script downloaded pre-trained AI models
# Uwaga: Ten krok może jeszcze nie działać, jeśli modele nie są gotowe
# Note: This step might not work yet if models aren't ready
```

**KROK 5: Uruchom aplikację**
**STEP 5: Run the application**

**Opcja A: Tryb deweloperski (dla programistów)**
**Option A: Development mode (for developers)**

Potrzebujesz DWÓCH okien terminala (You need TWO terminal windows):

```bash
# TERMINAL 1: Uruchom backend (silnik przetwarzający)
# TERMINAL 1: Start backend (processing engine)
python src/backend/main.py

# Zobaczysz logi informacyjne o uruchamianiu modułów
# You'll see info logs about module startup

# TERMINAL 2 (nowe okno terminala): Uruchom frontend (interfejs)
# TERMINAL 2 (new terminal window): Start frontend (interface)
cd src/frontend
npm run dev

# Aplikacja otworzy się w przeglądarce lub w oknie Electron
# Application will open in browser or Electron window
```

**Opcja B: Tryb produkcyjny (dla użytkowników końcowych)**
**Option B: Production mode (for end users)**

```bash
# Zbuduj aplikację (Build application)
npm run build --prefix src/frontend

# Uruchom aplikację (Run application)
npm start --prefix src/frontend
```

### Weryfikacja instalacji / Verify Installation

**Jak sprawdzić, czy wszystko działa poprawnie:**
**How to check if everything works correctly:**

```bash
# Test 1: Sprawdź wersję Python (Check Python version)
python --version
# Powinno wyświetlić: Python 3.10.x lub wyżej (Should show: Python 3.10.x or higher)

# Test 2: Sprawdź zainstalowane pakiety Python (Check installed Python packages)
pip list
# Powinny być widoczne: opencv-python, mediapipe, fastapi, itp.
# Should see: opencv-python, mediapipe, fastapi, etc.

# Test 3: Sprawdź Node.js (Check Node.js)
node --version
npm --version

# Test 4: Sprawdź Git (Check Git)
git --version
```

### Częste problemy i rozwiązania / Common Issues and Solutions

**Problem 1: "python nie jest rozpoznawany jako polecenie"**
**Problem 1: "python is not recognized as a command"**

```bash
# Rozwiązanie (Solution):
# 1. Upewnij się, że Python jest zainstalowany
# 2. Dodaj Python do zmiennej PATH
# 3. Spróbuj użyć `python3` zamiast `python`

# Na Windows może potrzebować reinstalacji Python z opcją "Add to PATH"
# On Windows you might need to reinstall Python with "Add to PATH" option
```

**Problem 2: "ModuleNotFoundError: No module named 'XXX'"**

```bash
# Rozwiązanie (Solution):
# Upewnij się, że wirtualne środowisko jest aktywne (venv)
# i zainstaluj brakujący moduł:
pip install nazwa-modułu
```

**Problem 3: "npm: command not found"**

```bash
# Rozwiązanie (Solution):
# Zainstaluj Node.js z https://nodejs.org/
# npm instaluje się automatycznie razem z Node.js
```

**Problem 4: Kamera/mikrofon nie działa**
**Problem 4: Camera/microphone doesn't work**

```bash
# Rozwiązanie (Solution):
# 1. Sprawdź, czy inne aplikacje mają dostęp do kamery/mikrofonu
# 2. Nadaj uprawnienia w ustawieniach systemu
# 3. Na Linux może wymagać instalacji dodatkowych sterowników
```

---

## 📊 Metryki sukcesu / Success Metrics

**Jak mierzymy, czy projekt się udał:**
**How we measure if the project succeeded:**

| Metryka / Metric | Cel / Target | Status |
|--------|--------|--------|
| Dokładność wykrywania stresu<br>Stress detection accuracy | ≥85% | 🟡 W trakcie / In Progress |
| Wskaźnik fałszywych alarmów<br>False positive rate | <5% | 🟡 W trakcie / In Progress |
| Opóźnienie odpowiedzi<br>Response latency | <5 sekund / seconds | 🟡 W trakcie / In Progress |
| Zużycie CPU<br>CPU usage | <10% średnio / average | 🟡 W trakcie / In Progress |
| Zużycie pamięci<br>Memory footprint | <500 MB | 🟡 W trakcie / In Progress |
| Aktywni użytkownicy (30 dni)<br>Daily active users (30d) | 70% retention | 🔴 Nie rozpoczęte / Not Started |

**Wyjaśnienie metryk dla początkujących:**
**Metrics explanation for beginners:**

- **Dokładność wykrywania**: Jak często system poprawnie rozpoznaje poziom stresu
  (How often the system correctly recognizes stress level)
- **Fałszywe alarmy**: Jak często system myli się mówiąc, że jesteś zestresowany
  (How often the system mistakenly says you're stressed)
- **Opóźnienie**: Jak szybko dostajesz wynik po zmianie stanu
  (How quickly you get results after state change)
- **CPU/Pamięć**: Ile zasobów komputera zużywa aplikacja
  (How much computer resources the app uses)

---

## 🗺️ Mapa drogowa rozwoju / Development Roadmap

**Plan rozwoju projektu (co i kiedy robimy):**
**Project development plan (what and when we do it):**

### Faza 1: Fundamenty (Tygodnie 1-2) ✅ / Phase 1: Foundation (Weeks 1-2) ✅
**Co to znaczy:** Przygotowanie podstaw projektu
**What it means:** Preparing project basics

- [x] Konfiguracja projektu / Project setup
- [x] Stworzenie dokumentu PRD / PRD creation
- [x] Repozytorium GitHub / GitHub repository
- [ ] Pipeline CI/CD / CI/CD pipeline

### Faza 2: Moduł behawioralny (Tygodnie 3-5) 🟡 / Phase 2: Behavioral Module (Weeks 3-5) 🟡
**Co to znaczy:** Tworzenie systemu monitorującego zachowanie użytkownika
**What it means:** Creating system that monitors user behavior

- [ ] Implementacja przechwytywania klawiszy / Keyboard hook implementation
- [ ] Monitorowanie aplikacji / Application monitoring
- [ ] Wykrywanie czasu bezczynności / Idle time detection
- [ ] Uczenie linii bazowej / Baseline learning

### Faza 3: Analiza twarzy (Tygodnie 6-8) 🔴 / Phase 3: Facial Analysis (Weeks 6-8) 🔴
**Co to znaczy:** Dodanie rozpoznawania emocji z twarzy
**What it means:** Adding facial emotion recognition

- [ ] Integracja MediaPipe / MediaPipe integration
- [ ] Rozpoznawanie AU przez OpenFace / OpenFace AU recognition
- [ ] Analiza zachowania oczu / Eye behavior analysis
- [ ] Wykrywanie rozmów wideo / Video call detection

### Faza 4: Analiza głosu (Tygodnie 9-10) 🔴 / Phase 4: Voice Analysis (Weeks 9-10) 🔴
**Co to znaczy:** Dodanie analizy stresu w głosie
**What it means:** Adding voice stress analysis

- [ ] Przechwytywanie audio i VAD / Audio capture & VAD
- [ ] Ekstrakcja wysokości dźwięku / Pitch extraction
- [ ] Cechy jakości głosu / Voice quality features
- [ ] Wykrywanie wyciszenia mikrofonu / Microphone mute detection

### Faza 5: Modele ML (Tygodnie 11-12) 🔴 / Phase 5: ML Models (Weeks 11-12) 🔴
**Co to znaczy:** Trenowanie sztucznej inteligencji
**What it means:** Training artificial intelligence

- [ ] Pozyskanie zbiorów danych / Dataset acquisition
- [ ] Trenowanie modeli / Model training
- [ ] Walidacja i dostrajanie / Validation & tuning

### Faza 6: Fuzja wielomodalna (Tygodnie 13-14) 🔴 / Phase 6: Multi-Modal Fusion (Weeks 13-14) 🔴
**Co to znaczy:** Łączenie wszystkich 3 sygnałów w jeden wynik
**What it means:** Combining all 3 signals into one result

- [ ] Normalizacja sygnałów / Signal normalization
- [ ] Silnik fuzji / Fusion engine
- [ ] Wygładzanie czasowe / Temporal smoothing

### Faza 7: Interfejs użytkownika (Tygodnie 15-17) 🔴 / Phase 7: User Interface (Weeks 15-17) 🔴
**Co to znaczy:** Tworzenie wizualnej części aplikacji
**What it means:** Creating visual part of the application

- [ ] Konfiguracja Electron / Electron setup
- [ ] Komponenty dashboardu / Dashboard components
- [ ] Integracja z zasobnikiem systemowym / System tray integration
- [ ] System powiadomień / Notification system

### Faza 8: Prywatność i bezpieczeństwo (Tygodnie 18-19) 🔴 / Phase 8: Privacy & Security (Weeks 18-19) 🔴
**Co to znaczy:** Zapewnienie bezpieczeństwa danych użytkownika
**What it means:** Ensuring user data security

- [ ] Szyfrowanie AES-256 / AES-256 encryption
- [ ] Kontrole prywatności / Privacy controls
- [ ] Audyt bezpieczeństwa / Security audit

### Faza 9: Testowanie (Tygodnie 20-22) 🔴 / Phase 9: Testing (Weeks 20-22) 🔴
**Co to znaczy:** Sprawdzanie czy wszystko działa poprawnie
**What it means:** Checking if everything works correctly

- [ ] Testy jednostkowe / Unit tests
- [ ] Testy integracyjne / Integration tests
- [ ] Optymalizacja wydajności / Performance optimization

### Faza 10: Beta (Tygodnie 23-26) 🔴 / Phase 10: Beta Launch (Weeks 23-26) 🔴
**Co to znaczy:** Testowanie z prawdziwymi użytkownikami
**What it means:** Testing with real users

- [ ] 50 testerów beta / 50 beta testers
- [ ] Zbieranie feedbacku / Feedback collection
- [ ] Naprawianie błędów / Bug fixes

### Faza 11: Publiczne wydanie (Tydzień 29) 🔴 / Phase 11: Public Release (Week 29) 🔴
**Co to znaczy:** Oficjalne uruchomienie dla wszystkich
**What it means:** Official launch for everyone

- [ ] Wydanie wersji 1.0 / v1.0 launch
- [ ] Strona marketingowa / Marketing website
- [ ] Dokumentacja / Documentation

---

## 🤝 Wkład w projekt / Contributing

Witamy wkład od społeczności! Zobacz [CONTRIBUTING.md](CONTRIBUTING.md) po szczegółowe wytyczne.
We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Jak możesz pomóc / How to Contribute

**Dla początkujących programistów:**
**For beginner programmers:**

1. **Fork** - Stwórz własną kopię repozytorium (Create your own copy of the repository)
2. **Stwórz gałąź** - `git checkout -b feature/amazing-feature`
   (Create a branch for your feature)
3. **Commituj zmiany** - `git commit -m 'Add amazing feature'`
   (Commit your changes with descriptive message)
4. **Push** - `git push origin feature/amazing-feature`
   (Push to your forked repository)
5. **Pull Request** - Otwórz prośbę o włączenie zmian (Open a pull request)

### Wytyczne deweloperskie / Development Guidelines

**Dla początkujących - na co zwrócić uwagę:**
**For beginners - what to pay attention to:**

- **Python**: Stosuj PEP 8 (przewodnik stylu Pythona)
  (Follow PEP 8 - Python style guide)
- **JavaScript/TypeScript**: Używaj ESLint/Prettier (narzędzia formatujące kod)
  (Use ESLint/Prettier - code formatting tools)
- **Testy**: Pisz testy jednostkowe dla nowych funkcji
  (Write unit tests for new features)
- **Dokumentacja**: Aktualizuj dokumentację gdy trzeba
  (Update documentation as needed)
- **Prywatność**: Szanuj zasady prywatności (brak transmisji danych)
  (Respect privacy principles - no data transmission)

---

## 🔐 Prywatność i etyka / Privacy & Ethics

### Zasady prywatności / Privacy Principles

**Co gwarantujemy użytkownikom:**
**What we guarantee to users:**

✅ **Przetwarzanie tylko lokalnie (Local-Only Processing)**
   - Brak chmury, brak serwerów zewnętrznych
   - Wszystko dzieje się na Twoim komputerze
   - No cloud, no servers - everything happens on your computer

✅ **Minimalizacja danych (Data Minimization)**
   - Zbieramy tylko to, co jest niezbędne
   - Nie przechowujemy niepotrzebnych informacji
   - Only collect what's necessary, nothing more

✅ **Kontrola użytkownika (User Control)**
   - Możesz zatrzymać/usunąć dane w każdej chwili
   - Pełna kontrola nad swoimi danymi
   - Pause/delete anytime - full control over your data

✅ **Przejrzystość (Transparency)**
   - Jesteśmy otwarci co do tego, co zbieramy
   - Żadnych ukrytych funkcji
   - Open about what's collected - no hidden features

✅ **Szyfrowanie (Encryption)**
   - Dane szyfrowane algorytmem AES-256
   - Najwyższy standard bezpieczeństwa
   - AES-256 encryption - highest security standard

### Co zbieramy / What We Collect

**Bardzo ważne dla zrozumienia systemu:**
**Very important for understanding the system:**

| ✅ ZBIERAMY / COLLECTED | ❌ NIE ZBIERAMY / NOT COLLECTED |
|-------------|-----------------|
| Szybkość pisania, wskaźnik błędów<br>Typing speed, error rate | Treść wpisywanych tekstów<br>Keystroke content (what you type) |
| Nazwy aplikacji, czas użytkowania<br>App names, usage duration | Zawartość ekranu, zrzuty ekranu<br>Screen content, screenshots |
| Punkty orientacyjne twarzy (współrzędne X,Y)<br>Facial landmarks (X,Y coordinates) | Nagrania wideo<br>Video recordings |
| Wysokość głosu, ton (liczby)<br>Voice pitch, tone (numbers) | Nagrania audio<br>Audio recordings |
| Czas trwania spotkań<br>Meeting duration | Treść spotkań<br>Meeting content |

**Wyjaśnienie dla początkujących:**
**Explanation for beginners:**

- **Zbieramy METADANE** (informacje "o" czymś), nie ZAWARTOŚĆ
  (We collect METADATA - information "about" something, not CONTENT)
- **Przykład**: Wiemy, że piszesz szybko (70 słów/min), ale NIE WIEMY co piszesz
  (Example: We know you type fast (70 words/min), but we DON'T KNOW what you type)

### Zobowiązania etyczne / Ethical Commitments

**Nasze obietnice:**
**Our promises:**

- **Brak nadzoru pracodawcy (No employer surveillance)**
  - Tylko do użytku indywidualnego
  - Individual use only

- **To nie urządzenie medyczne (Not a medical device)**
  - Świadomość dobrego samopoczucia, nie diagnoza
  - Wellness awareness, not medical diagnosis

- **Świadoma zgoda (Informed consent)**
  - Wymaga wyraźnego opt-in (zgody)
  - Explicit opt-in required

- **Mitygacja stronniczości (Bias mitigation)**
  - Testowane na różnych grupach demograficznych
  - Tested across demographics

---

## 📄 Licencja / License

Ten projekt jest licencjonowany na **licencji MIT** - zobacz plik [LICENSE](LICENSE) po szczegóły.
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Kluczowe punkty / Key Points

**Co możesz zrobić z tym kodem:**
**What you can do with this code:**

- ✅ **Darmowe użytkowanie, modyfikacja, dystrybucja**
  (Free to use, modify, distribute)
- ✅ **Użytek komercyjny dozwolony**
  (Commercial use allowed)
- ✅ **Brak gwarancji**
  (No warranty provided)
- ⚠️ **Musisz załączyć oryginalną licencję w pochodnych**
  (Must include original license in derivatives)

**Wyjaśnienie dla początkujących:**
**Explanation for beginners:**

Licencja MIT to jedna z najbardziej liberalnych licencji open-source:
MIT License is one of the most permissive open-source licenses:
- Możesz robić prawie wszystko z tym kodem (You can do almost anything with this code)
- Jedyny wymóg: zachować informację o oryginalnej licencji (Only requirement: keep original license info)
- Świetna dla nauki i projektów komercyjnych (Great for learning and commercial projects)

---

## 📚 Dokumentacja / Documentation

**Gdzie znaleźć więcej informacji:**
**Where to find more information:**

- **[Dokument Wymagań Produktu (PRD)](docs/PRD_Stress_Detection_System.md)**
  - Kompletna specyfikacja produktu (Complete product specification)
  - Najlepsze miejsce aby zrozumieć wizję projektu (Best place to understand project vision)

- **[Architektura Techniczna](docs/architecture.md)**
  - Szczegóły projektowania systemu (System design details)
  - Dla programistów chcących zrozumieć jak wszystko działa (For developers wanting to understand how everything works)

- **[Przewodnik Użytkownika](docs/user-guide.md)**
  - Dokumentacja dla użytkowników końcowych (End-user documentation)
  - Jak używać aplikacji (How to use the application)

- **[Dokumentacja API](docs/api-reference.md)**
  - Dokumentacja API dla programistów (Developer API docs)
  - Jeśli chcesz budować integracje (If you want to build integrations)

---

## 🙏 Podziękowania / Acknowledgments

### Prace badawcze / Research Papers

**Projekty naukowe, na których się opieramy:**
**Scientific projects we build upon:**

- **WESAD Dataset** - Wykrywanie stresu z urządzeń noszonych (Wearable stress detection) (UbiComp 2018)
- **OpenFace** - Zestaw narzędzi do analizy zachowań twarzy (Facial behavior analysis toolkit) (FG 2018)
- **"Realtime Face Speech Emotion Recognition"** - Artykuł bazowy IEEE 2024/25 (IEEE 2024/25 base paper)

### Narzędzia Open Source / Open Source Tools

**Biblioteki, które wykorzystujemy:**
**Libraries we use:**

- [MediaPipe](https://google.github.io/mediapipe/) - Framework ML od Google (Google's ML framework)
- [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) - Analiza twarzy (Facial analysis)
- [librosa](https://librosa.org/) - Analiza audio (Audio analysis)
- [Electron](https://www.electronjs.org/) - Framework desktopowy (Desktop framework)

---

## 📞 Kontakt i wsparcie / Contact & Support

**Jak się z nami skontaktować:**
**How to contact us:**

- **GitHub Issues**: [Zgłoś błędy lub poproś o funkcje](https://github.com/Nuvai/stress-detection-system/issues)
  (Report bugs or request features)
- **Email**: dev-team@nuvai.io (dla kwestii bezpieczeństwa / for security concerns)
- **Discord**: Wkrótce (Coming soon)

**Dla początkujących - jak prosić o pomoc:**
**For beginners - how to ask for help:**

1. **Najpierw szukaj**: Sprawdź czy ktoś nie zadał już podobnego pytania
   (Search first: Check if someone already asked a similar question)
2. **Opisz problem dokładnie**: Co próbujesz zrobić? Co się dzieje? Co oczekujesz?
   (Describe the problem precisely: What are you trying to do? What happens? What do you expect?)
3. **Załącz informacje o systemie**: System operacyjny, wersja Python, wersja Node.js
   (Include system information: OS, Python version, Node.js version)

---

## 🌟 Historia gwiazdek / Star History

Jeśli ten projekt jest dla Ciebie przydatny, rozważ danie mu gwiazdki! ⭐
If you find this project useful, please consider giving it a star! ⭐

**Co to znaczy "dać gwiazdkę"?**
**What does "give a star" mean?**
- To sposób pokazania, że projekt Ci się podoba (It's a way to show you like the project)
- Pomaga innym odkryć projekt (Helps others discover the project)
- Motywuje twórców (Motivates creators)

[![Star History Chart](https://api.star-history.com/svg?repos=Nuvai/stress-detection-system&type=Date)](https://star-history.com/#Nuvai/stress-detection-system&Date)

---

## 📈 Status projektu / Project Status

**Obecna faza**: Fundamenty i planowanie
**Current Phase**: Foundation & Planning

**Wersja**: 0.1.0-alpha
**Version**: 0.1.0-alpha

**Ostatnia aktualizacja**: 1 lutego 2026
**Last Updated**: February 1, 2026

**Aktywność deweloperska:**
**Development Activity:**
- Aktywny rozwój w toku (Active development in progress)
- Oczekiwane cotygodniowe aktualizacje (Weekly updates expected)
- Planowane wydanie beta: Czerwiec 2026 (Beta launch planned: June 2026)
- Planowane wydanie v1.0: Sierpień 2026 (v1.0 release planned: August 2026)

**Co oznacza "alpha"?**
**What does "alpha" mean?**
- Projekt jest we wczesnej fazie rozwoju (Project is in early development stage)
- Wiele funkcji jeszcze nie działa (Many features don't work yet)
- Może zawierać błędy (May contain bugs)
- Świetny czas aby się uczyć i przyczyniać! (Great time to learn and contribute!)

---

**Zbudowano z ❤️ przez zespół Nuvai**
**Built with ❤️ by the Nuvai Team**

*"Poznaj swój stres, zanim on pozna ciebie"*
*"Know your stress before it knows you"*
