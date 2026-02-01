# Product Requirements Document (PRD)
## Real-Time Stress Detection System for IT & Remote Workers

**Version:** 1.0
**Date:** February 1, 2026
**Status:** Draft
**Owner:** Development Team
**Stakeholders:** End Users (IT/Remote Workers), Team Leads, HR/Wellness Teams

---

## Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [Product Vision & Goals](#2-product-vision--goals)
3. [Problem Statement](#3-problem-statement)
4. [Target Users](#4-target-users)
5. [Product Overview](#5-product-overview)
6. [Success Metrics](#6-success-metrics)
7. [Functional Requirements](#7-functional-requirements)
8. [Technical Architecture](#8-technical-architecture)
9. [User Stories & Use Cases](#9-user-stories--use-cases)
10. [Data Models & ML Requirements](#10-data-models--ml-requirements)
11. [User Interface & Experience](#11-user-interface--experience)
12. [Privacy, Security & Ethics](#12-privacy-security--ethics)
13. [Implementation Roadmap](#13-implementation-roadmap)
14. [Dependencies & Constraints](#14-dependencies--constraints)
15. [Risk Assessment](#15-risk-assessment)
16. [Future Enhancements](#16-future-enhancements)
17. [Appendix](#17-appendix)

---

## 1. Executive Summary

### 1.1 Product Overview
The Real-Time Stress Detection System is an intelligent, non-invasive desktop application that monitors IT professionals and remote workers for early signs of workplace stress using behavioral analysis, facial recognition, and voice pattern detection.

### 1.2 Key Differentiators
- **Multi-modal detection**: Combines 3 independent data streams (behavior, face, voice)
- **Baseline personalization**: Learns individual patterns vs. generic thresholds
- **Privacy-first**: All processing happens locally, no data storage
- **Proactive intervention**: Early warning system before burnout occurs
- **Non-intrusive**: No surveys, self-reporting, or workflow interruption

### 1.3 Business Value
- Reduce employee burnout rates by 30-40%
- Early intervention saves $3,000-$5,000 per employee in healthcare costs
- Improve productivity through better work-life balance awareness
- Provide data-driven insights for organizational wellness programs

---

## 2. Product Vision & Goals

### 2.1 Vision Statement
*"Empower every knowledge worker with real-time awareness of their stress levels, enabling proactive self-care before burnout occurs."*

### 2.2 Product Goals

**Primary Goals:**
1. Detect stress with ≥85% accuracy using multi-modal signals
2. Provide stress insights within 5 seconds of detection
3. Maintain <5% false positive rate
4. Ensure 100% local processing with zero data transmission

**Secondary Goals:**
1. Achieve 70% daily active user retention after 30 days
2. Generate actionable stress trend reports
3. Integrate with popular productivity tools (Slack, Teams, Calendar)
4. Support 5+ video conferencing platforms

### 2.3 Non-Goals (Out of Scope for v1.0)
- Medical diagnosis or clinical intervention
- Real-time monitoring by managers/employers
- Stress prediction beyond 2 hours
- Mobile/tablet support
- Integration with wearable devices
- Multi-user/team dashboards

---

## 3. Problem Statement

### 3.1 Current Challenges

**Problem 1: Late Detection**
- 76% of employees experience burnout symptoms before recognizing stress
- Average time from stress onset to recognition: 4-6 weeks
- Existing solutions rely on weekly/monthly self-reporting surveys

**Problem 2: Unreliable Self-Assessment**
- Survey response bias: people underreport stress by 40%
- Stigma prevents honest reporting in workplace surveys
- Self-awareness of stress is poor during high-pressure periods

**Problem 3: Single-Signal Limitations**
- Facial emotion detection has 62% accuracy for stress (too low)
- Voice analysis alone misses silent work periods
- Behavioral patterns vary widely between individuals

### 3.2 User Pain Points
- "I realize I'm stressed only after I snap at colleagues"
- "Surveys feel like extra work during busy times"
- "I don't know when to take breaks because I feel 'fine' until I crash"
- "My manager doesn't understand my workload until I'm burned out"

### 3.3 Market Gap
No existing solution combines:
- Real-time behavioral monitoring
- Multi-modal signal fusion
- Local-only processing for privacy
- Personalized baseline learning

---

## 4. Target Users

### 4.1 Primary Personas

**Persona 1: Sarah - Remote Software Developer**
- Age: 28-35
- Works from home 5 days/week
- 6-8 video meetings daily
- Struggles with work-life boundaries
- Pain points: Isolation, long hours, deadline pressure

**Persona 2: Raj - IT Support Specialist**
- Age: 30-40
- Hybrid work (3 days office, 2 days home)
- High-interrupt work environment
- Manages multiple support tickets simultaneously
- Pain points: Context switching, constant alerts, client escalations

**Persona 3: Maria - Product Manager**
- Age: 32-42
- Fully remote, manages distributed team
- Back-to-back meetings (8-10 hours/day)
- High cognitive load from decision-making
- Pain points: Meeting fatigue, stakeholder pressure, multitasking

### 4.2 Secondary Users
- Team leads (aggregate anonymized insights)
- HR/Wellness coordinators (program effectiveness data)

### 4.3 User Environment
- **Hardware**: Laptop/desktop with webcam, microphone
- **OS**: Windows 10+, macOS 12+, Linux (Ubuntu 20.04+)
- **Network**: Internet required for initial setup only
- **Workspace**: Home office, co-working space, corporate office

---

## 5. Product Overview

### 5.1 How It Works

```
┌─────────────────────────────────────────────────────────┐
│                    User Works Normally                  │
└───────────────┬─────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────┐
│           Background Monitoring (3 Modules)            │
├───────────────────────────────────────────────────────┤
│  1. Behavioral Module (always running)                │
│     - Typing patterns, app usage, idle time           │
│                                                        │
│  2. Facial Analysis (during video calls)              │
│     - Micro-expressions, eye strain, facial tension   │
│                                                        │
│  3. Voice Analysis (during video calls)               │
│     - Pitch, tone, speech rate, pauses                │
└───────────────┬───────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────┐
│        Personalized Baseline Comparison               │
│  (What's normal for THIS user vs. generic rules)      │
└───────────────┬───────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────┐
│         Multi-Modal Signal Fusion Engine              │
│  Combines all 3 sources → Confidence-weighted score   │
└───────────────┬───────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────┐
│              Stress Score (0-100)                     │
│  + Stress Level: Low / Medium / High / Critical       │
└───────────────┬───────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────┐
│                 User Dashboard                        │
│  - Real-time stress score                            │
│  - Daily/weekly trends                               │
│  - Gentle nudges ("Consider a break")                │
│  - Stress trigger insights                           │
└───────────────────────────────────────────────────────┘
```

### 5.2 Core Value Proposition
- **For users**: "Know your stress before it knows you"
- **For organizations**: "Prevent burnout with data-driven wellness"

---

## 6. Success Metrics

### 6.1 Product Metrics

**Accuracy & Performance**
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Stress detection accuracy | ≥85% | Ground truth validation via ESM (Experience Sampling Method) |
| False positive rate | <5% | User feedback on incorrect alerts |
| False negative rate | <10% | Missed stress events vs. ESM |
| Response latency | <5 seconds | Time from signal to dashboard update |
| CPU usage | <5% average | System resource monitoring |
| Memory footprint | <500 MB | RAM usage monitoring |

**User Engagement**
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Daily active users (DAU) | 70% after 30 days | App usage logs |
| Average session duration | 8+ hours | Background runtime |
| Dashboard views per day | 3-5 times | UI interaction logs |
| Alert acknowledgment rate | >60% | User response to notifications |
| Feature adoption (all 3 modules) | >80% | Module enablement status |

**Business Impact**
| Metric | Target | Timeframe |
|--------|--------|-----------|
| User-reported burnout incidents | -30% reduction | 6 months |
| Stress awareness improvement | +50% (survey) | 3 months |
| Break-taking behavior | +40% frequency | 3 months |
| User satisfaction (NPS) | >40 | Ongoing |

### 6.2 Leading Indicators
- Baseline calibration completion rate: >90% within 5 days
- Stress trend correlation with calendar density: r > 0.6
- User trust score (privacy concern survey): >4.0/5.0

---

## 7. Functional Requirements

### 7.1 Module 1: Behavioral Monitoring

#### FR-BM-001: Typing Pattern Analysis
**Priority:** P0 (Must Have)
**Description:** Monitor keyboard activity to detect stress indicators.

**Acceptance Criteria:**
- Track typing speed (WPM) with ±5 WPM accuracy
- Count backspace frequency (deletions per 100 keystrokes)
- Detect burst typing vs. continuous typing patterns
- Calculate typing error rate (deviation from user baseline)
- Identify typing-then-delete cycles (hesitation patterns)

**Technical Notes:**
- Use OS-level keyboard hooks (Windows: `pynput`, macOS: `Quartz`)
- Sample rate: 100ms for keystroke timestamps
- No keystroke content logging (only metadata)

---

#### FR-BM-002: Application Context Tracking
**Priority:** P0 (Must Have)
**Description:** Track active application usage patterns to identify work intensity.

**Acceptance Criteria:**
- Detect active window/application every 5 seconds
- Classify applications by category (IDE, browser, communication, other)
- Calculate application switch frequency (switches per hour)
- Identify prolonged single-app focus (>2 hours continuous)
- Detect rapid context switching (>10 switches in 10 minutes)

**Technical Notes:**
- Windows: `win32gui.GetForegroundWindow()`
- macOS: `NSWorkspace.sharedWorkspace()`
- Linux: `xdotool getactivewindow`
- Application whitelist for privacy (exclude browsers showing personal content)

---

#### FR-BM-003: Idle Time Detection
**Priority:** P0 (Must Have)
**Description:** Monitor user inactivity to detect prolonged staring/frustration.

**Acceptance Criteria:**
- Detect mouse/keyboard inactivity with 1-second resolution
- Classify idle periods: micro (<30s), short (30s-2m), long (2m+)
- Identify "frozen cursor" patterns (mouse stationary >30s with app active)
- Distinguish idle from genuine breaks (AFK detection)
- Track idle-to-active transitions (sudden activity bursts)

**Technical Notes:**
- Use OS idle time APIs: `GetLastInputInfo()` (Windows), `CGEventSourceSecondsSinceLastEventType()` (macOS)
- Cross-reference with screen lock status

---

#### FR-BM-004: Work Session Analysis
**Priority:** P1 (Should Have)
**Description:** Analyze continuous work periods and break patterns.

**Acceptance Criteria:**
- Define work session as active period >15 minutes
- Track session duration (start, end, total time)
- Calculate break frequency (breaks per 2-hour block)
- Identify marathon sessions (>3 hours without 10+ minute break)
- Detect micro-break patterns (<2 minutes away from desk)

**Technical Notes:**
- Use 15-minute rolling window for session detection
- Persist session data locally in SQLite

---

#### FR-BM-005: Task Repetition Detection
**Priority:** P2 (Nice to Have)
**Description:** Identify cyclic behavior indicating frustration or stuck state.

**Acceptance Criteria:**
- Detect repeated app switches (same 2-3 apps cycling)
- Identify file open-close-reopen patterns (same file >5 times in 30 min)
- Flag repetitive copy-paste actions (>10 times in 5 minutes)
- Detect tab thrashing (browser tabs opening/closing rapidly)

**Technical Notes:**
- Use sequence pattern matching algorithms
- Require >80% sequence similarity for flagging

---

### 7.2 Module 2: Facial Stress Detection

#### FR-FA-001: Face Detection & Tracking
**Priority:** P0 (Must Have)
**Description:** Detect and track user face during video calls.

**Acceptance Criteria:**
- Detect face in webcam feed with ≥95% accuracy
- Track face across frames (handle head movement)
- Support multiple face detection (identify primary user)
- Handle partial occlusion (hand on face, looking away)
- Operate at 10 FPS minimum for real-time analysis

**Technical Notes:**
- Use MediaPipe Face Mesh or Dlib for face detection
- Fallback to Haar Cascades if GPU unavailable
- Face landmark count: 68 points minimum

---

#### FR-FA-002: Facial Action Unit (AU) Recognition
**Priority:** P0 (Must Have)
**Description:** Detect specific facial muscle movements associated with stress.

**Acceptance Criteria:**
- Detect AU4 (Brow Lowerer) - frustration indicator
- Detect AU6+12 (Cheek Raiser + Lip Corner Puller) - distinguish genuine vs. forced smile
- Detect AU7 (Lid Tightener) - eye strain indicator
- Detect AU17 (Chin Raiser) - tension indicator
- Detect AU23 (Lip Tightener) - suppressed emotion indicator
- Calculate AU intensity (0-5 scale)

**Technical Notes:**
- Use OpenFace or Py-Feat for AU detection
- Temporal smoothing over 3-second window to reduce noise

---

#### FR-FA-003: Eye Behavior Analysis
**Priority:** P1 (Should Have)
**Description:** Analyze eye-related stress indicators.

**Acceptance Criteria:**
- Calculate blink rate (blinks per minute)
- Detect prolonged staring (blink rate <5/min for >2 minutes)
- Measure eye openness ratio (detect squinting)
- Track gaze direction (looking away from screen)
- Identify rapid eye movement (darting eyes)

**Technical Notes:**
- Use Eye Aspect Ratio (EAR) for blink detection
- Threshold: EAR < 0.2 for blink
- Baseline blink rate: 15-20/min (normal)

---

#### FR-FA-004: Head Pose & Movement Analysis
**Priority:** P2 (Nice to Have)
**Description:** Analyze head movement patterns for engagement and stress.

**Acceptance Criteria:**
- Calculate head pose (pitch, yaw, roll) in degrees
- Detect rigid posture (minimal head movement for >5 minutes)
- Identify frequent head tilting (confusion indicator)
- Track head nod frequency (engagement indicator)
- Detect face-hiding gestures (hand-to-face contact)

**Technical Notes:**
- Use solvePnP for head pose estimation
- Sample rate: 5 FPS sufficient

---

#### FR-FA-005: Video Call Detection
**Priority:** P0 (Must Have)
**Description:** Automatically detect when user is in a video call.

**Acceptance Criteria:**
- Detect active video conferencing apps (Zoom, Teams, Meet, Webex, Slack)
- Identify camera access by applications
- Start facial analysis only during active calls
- Pause analysis when camera is muted/turned off
- Support custom application whitelist

**Technical Notes:**
- Monitor process list for known VC apps
- Check camera device access via system APIs
- Windows: `mfplat.dll`, macOS: `AVFoundation`

---

### 7.3 Module 3: Voice Stress Detection

#### FR-VO-001: Audio Capture & Preprocessing
**Priority:** P0 (Must Have)
**Description:** Capture microphone audio during video calls for analysis.

**Acceptance Criteria:**
- Capture audio at 16kHz sample rate minimum
- Support mono channel input
- Apply noise reduction (background noise, keyboard clicks)
- Detect voice activity (VAD) to isolate speech segments
- Process audio in 3-second sliding windows

**Technical Notes:**
- Use PyAudio or SoundDevice for capture
- Apply WebRTC VAD or Silero VAD
- No audio recording/storage - real-time processing only

---

#### FR-VO-002: Pitch & Tone Analysis
**Priority:** P0 (Must Have)
**Description:** Analyze voice pitch changes as stress indicators.

**Acceptance Criteria:**
- Extract fundamental frequency (F0) from speech
- Calculate pitch variability (standard deviation)
- Detect elevated pitch (stress-induced vocal tension)
- Identify pitch monotony (flat affect indicator)
- Compare against user's baseline pitch range

**Technical Notes:**
- Use librosa or Praat for F0 extraction
- Baseline pitch range: ±20 Hz from mean
- Stress indicator: >30 Hz spike from baseline

---

#### FR-VO-003: Speech Rate & Rhythm Analysis
**Priority:** P1 (Should Have)
**Description:** Analyze speaking pace and fluency.

**Acceptance Criteria:**
- Calculate syllables per second (speech rate)
- Detect rushed speech (>6 syllables/sec)
- Identify slowed speech (<2 syllables/sec)
- Measure speech-to-pause ratio
- Detect disfluencies (um, uh, repeated words)

**Technical Notes:**
- Use phoneme segmentation for syllable counting
- Forced alignment with Montreal Forced Aligner

---

#### FR-VO-004: Voice Quality Features
**Priority:** P1 (Should Have)
**Description:** Extract voice quality indicators of stress.

**Acceptance Criteria:**
- Calculate jitter (pitch perturbation)
- Calculate shimmer (amplitude perturbation)
- Measure Harmonics-to-Noise Ratio (HNR)
- Detect vocal strain (breathy or harsh voice)
- Extract Mel-Frequency Cepstral Coefficients (MFCCs)

**Technical Notes:**
- Use Parselmouth (Praat Python wrapper)
- Stress thresholds: Jitter >1%, Shimmer >3%, HNR <20dB

---

#### FR-VO-005: Microphone Mute Detection
**Priority:** P0 (Must Have)
**Description:** Detect when user microphone is muted.

**Acceptance Criteria:**
- Detect system-level mute status
- Detect application-level mute (Zoom, Teams)
- Pause voice analysis during mute
- Resume analysis when unmuted
- Log mute duration for context

**Technical Notes:**
- Monitor audio device mixer settings
- Check VC app window for mute indicator (OCR fallback)

---

### 7.4 Module 4: Multi-Modal Fusion Engine

#### FR-MF-001: Signal Normalization
**Priority:** P0 (Must Have)
**Description:** Normalize signals from different modules to comparable scales.

**Acceptance Criteria:**
- Scale all signals to 0-100 range
- Apply z-score normalization against user baseline
- Handle missing signals gracefully (module disabled/unavailable)
- Weight signals by confidence score
- Update normalization parameters weekly

**Technical Notes:**
- Use min-max scaling with outlier clipping
- Confidence score based on signal quality metrics

---

#### FR-MF-002: Baseline Learning
**Priority:** P0 (Must Have)
**Description:** Learn individual user's normal behavior patterns.

**Acceptance Criteria:**
- Calibration period: 5 working days minimum
- Collect ≥20 hours of behavioral data
- Collect ≥2 hours of video call data
- Calculate baseline statistics (mean, std, percentiles)
- Flag insufficient data and extend calibration
- Re-calibrate monthly to adapt to changing patterns

**Technical Notes:**
- Use exponential weighted moving average for adaptation
- Store baseline in user profile (encrypted JSON)

---

#### FR-MF-003: Stress Score Calculation
**Priority:** P0 (Must Have)
**Description:** Calculate final stress score from multi-modal inputs.

**Acceptance Criteria:**
- Combine behavioral, facial, voice scores with weighted average
- Apply temporal smoothing (5-minute rolling window)
- Output stress score 0-100
- Classify into levels: Low (0-30), Medium (31-60), High (61-85), Critical (86-100)
- Update score every 30 seconds
- Confidence interval: ±10 points

**Technical Notes:**
- Weight distribution: Behavioral 50%, Face 30%, Voice 20%
- Adjust weights based on module availability
- Use Kalman filter for temporal smoothing

---

#### FR-MF-004: Trend Analysis
**Priority:** P1 (Should Have)
**Description:** Analyze stress patterns over time.

**Acceptance Criteria:**
- Calculate hourly average stress score
- Identify peak stress hours (top 3 per day)
- Detect stress trend: increasing, decreasing, stable
- Correlate stress with calendar events (meeting density)
- Generate daily stress summary report

**Technical Notes:**
- Use linear regression for trend detection
- Store 30 days of historical data

---

#### FR-MF-005: Trigger Identification
**Priority:** P2 (Nice to Have)
**Description:** Identify activities/contexts that trigger stress.

**Acceptance Criteria:**
- Correlate stress spikes with:
  - Specific applications
  - Meeting types (1:1, team, client)
  - Time of day
  - Day of week
- Rank triggers by frequency and intensity
- Present top 5 triggers in dashboard

**Technical Notes:**
- Use association rule mining (Apriori algorithm)
- Minimum support: 10 occurrences

---

### 7.5 User Interface & Notifications

#### FR-UI-001: System Tray Integration
**Priority:** P0 (Must Have)
**Description:** Provide persistent, non-intrusive system tray icon.

**Acceptance Criteria:**
- Display real-time stress level via icon color:
  - Green (Low), Yellow (Medium), Orange (High), Red (Critical)
- Show current stress score on hover tooltip
- Right-click menu with:
  - Open Dashboard
  - Pause Monitoring
  - Settings
  - Exit
- Auto-start on system boot (configurable)

**Technical Notes:**
- Use pystray for cross-platform tray icon
- Icon updates every 30 seconds

---

#### FR-UI-002: Main Dashboard
**Priority:** P0 (Must Have)
**Description:** Provide comprehensive stress visualization interface.

**Acceptance Criteria:**
- Display sections:
  1. Current stress score (large, prominent)
  2. Real-time gauge (0-100)
  3. Today's trend line chart
  4. Module status indicators (behavior/face/voice active)
  5. Recent alerts/recommendations
  6. Weekly stress heatmap (7 days)
- Update frequency: 30 seconds
- Responsive design (minimum 1024x768 resolution)

**Technical Notes:**
- Use Electron or Qt for desktop UI
- Chart library: Chart.js or Plotly
- Color scheme: Accessibility-compliant (WCAG 2.1 AA)

---

#### FR-UI-003: Gentle Alerts
**Priority:** P0 (Must Have)
**Description:** Provide non-disruptive stress notifications.

**Acceptance Criteria:**
- Trigger alert when:
  - Stress reaches High level for >30 minutes
  - Stress reaches Critical level for >10 minutes
  - No break taken in >3 hours
- Alert types:
  - System notification (native OS)
  - Dashboard banner
  - Optional sound (subtle chime)
- Alert messages:
  - Empathetic tone ("You've been working hard...")
  - Actionable suggestion ("Consider a 5-minute break")
  - Easy dismiss ("I'm fine" / "Remind me in 30 min")
- Alert frequency limit: Max 1 per hour

**Technical Notes:**
- Use plyer for cross-platform notifications
- Store dismissed alerts to prevent repeat

---

#### FR-UI-004: Historical Reports
**Priority:** P1 (Should Have)
**Description:** Provide detailed historical stress analytics.

**Acceptance Criteria:**
- Time ranges: Today, This Week, This Month, Custom
- Visualizations:
  - Stress trend line chart
  - Stress level distribution (pie chart)
  - Peak stress hours (bar chart)
  - Module contribution breakdown
  - Top stress triggers (list)
- Export options: PDF report, CSV data
- Privacy: Data stored locally only

**Technical Notes:**
- Report generation: ReportLab for PDF
- Data retention: 90 days (configurable)

---

#### FR-UI-005: Settings & Configuration
**Priority:** P0 (Must Have)
**Description:** Allow user customization of monitoring preferences.

**Acceptance Criteria:**
- Module toggles:
  - Enable/disable behavioral monitoring
  - Enable/disable facial analysis
  - Enable/disable voice analysis
- Alert preferences:
  - Alert threshold (Medium/High/Critical only)
  - Notification sound on/off
  - Do Not Disturb hours
- Privacy settings:
  - Pause monitoring (temporary)
  - Clear all data
  - View data collection summary
- Application whitelist/blacklist for behavioral monitoring

**Technical Notes:**
- Settings stored in config.json (encrypted)
- Instant apply (no restart required)

---

### 7.6 Privacy & Security Features

#### FR-PS-001: Local-Only Processing
**Priority:** P0 (Must Have)
**Description:** Ensure all data processing happens on user's device.

**Acceptance Criteria:**
- No network requests during monitoring
- No telemetry or analytics transmission
- No cloud storage of any user data
- Offline operation after initial setup
- Network usage limited to:
  - Software updates (user-initiated)
  - Model downloads (during setup)

**Technical Notes:**
- Network firewall rule verification
- Packet capture testing to confirm zero data egress

---

#### FR-PS-002: Data Encryption
**Priority:** P0 (Must Have)
**Description:** Encrypt all stored user data.

**Acceptance Criteria:**
- Encrypt baseline profile data (AES-256)
- Encrypt historical stress scores database
- Encrypt application settings
- Use OS keychain for encryption keys
- Automatic encryption of logs

**Technical Notes:**
- Use cryptography.fernet for Python
- Key derivation: PBKDF2 with device-specific salt

---

#### FR-PS-003: User Consent & Onboarding
**Priority:** P0 (Must Have)
**Description:** Obtain explicit consent before monitoring begins.

**Acceptance Criteria:**
- First-run wizard with:
  - Clear explanation of what's monitored
  - What's NOT collected (no content, no recordings)
  - Privacy policy agreement
  - Module-by-module consent (granular opt-in)
  - Camera/microphone permission requests
- Consent can be revoked anytime in settings
- Age verification (18+ requirement)

**Technical Notes:**
- Consent timestamp logged
- Re-prompt consent after major updates

---

#### FR-PS-004: Data Retention & Deletion
**Priority:** P0 (Must Have)
**Description:** Allow users to control their data lifecycle.

**Acceptance Criteria:**
- Default retention: 90 days
- Configurable retention: 7/30/90/365 days
- "Clear All Data" button in settings with confirmation
- Automatic purging of data beyond retention period
- Complete uninstallation removes all traces

**Technical Notes:**
- Daily cleanup cron job
- Secure deletion (overwrite with zeros before delete)

---

#### FR-PS-005: Transparency Dashboard
**Priority:** P1 (Should Have)
**Description:** Show users what data is being collected.

**Acceptance Criteria:**
- Display active monitoring modules
- Show data collection summary:
  - "Behavioral data points collected today: 5,432"
  - "Facial frames analyzed: 1,234"
  - "Voice segments processed: 87"
- Real-time module activity indicator
- Access to raw feature data (not interpretations)

**Technical Notes:**
- Read-only data viewer
- No user identifiers in UI

---

## 8. Technical Architecture

### 8.1 System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     User's Computer                         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │              Frontend (Electron/Qt)                   │ │
│  │  - System Tray Icon                                   │ │
│  │  - Dashboard UI (React/Vue)                           │ │
│  │  - Settings Panel                                     │ │
│  │  - Notification Manager                               │ │
│  └─────────────────────┬─────────────────────────────────┘ │
│                        │ IPC                               │
│  ┌─────────────────────▼─────────────────────────────────┐ │
│  │         Backend Service (Python 3.10+)                │ │
│  │                                                        │ │
│  │  ┌──────────────────────────────────────────────┐    │ │
│  │  │      Data Collection Layer                   │    │ │
│  │  ├──────────────────────────────────────────────┤    │ │
│  │  │ • Keyboard/Mouse Hook Manager                │    │ │
│  │  │ • Application Monitor                        │    │ │
│  │  │ • Webcam Capture (OpenCV)                    │    │ │
│  │  │ • Audio Capture (PyAudio)                    │    │ │
│  │  └──────────────────┬───────────────────────────┘    │ │
│  │                     │                                 │ │
│  │  ┌──────────────────▼───────────────────────────┐    │ │
│  │  │      Feature Extraction Layer                │    │ │
│  │  ├──────────────────────────────────────────────┤    │ │
│  │  │ • Behavioral Analyzer                        │    │ │
│  │  │ • Face Landmark Detector (MediaPipe)         │    │ │
│  │  │ • Facial AU Recognizer (OpenFace)            │    │ │
│  │  │ • Voice Feature Extractor (librosa)          │    │ │
│  │  └──────────────────┬───────────────────────────┘    │ │
│  │                     │                                 │ │
│  │  ┌──────────────────▼───────────────────────────┐    │ │
│  │  │      ML Inference Layer                      │    │ │
│  │  ├──────────────────────────────────────────────┤    │ │
│  │  │ • Baseline Model (User Profile)              │    │ │
│  │  │ • Anomaly Detector (Isolation Forest)        │    │ │
│  │  │ • Stress Classifier (Random Forest)          │    │ │
│  │  │ • Multi-Modal Fusion (Weighted Ensemble)     │    │ │
│  │  └──────────────────┬───────────────────────────┘    │ │
│  │                     │                                 │ │
│  │  ┌──────────────────▼───────────────────────────┐    │ │
│  │  │      Business Logic Layer                    │    │ │
│  │  ├──────────────────────────────────────────────┤    │ │
│  │  │ • Stress Score Calculator                    │    │ │
│  │  │ • Trend Analyzer                             │    │ │
│  │  │ • Alert Manager                              │    │ │
│  │  │ • Report Generator                           │    │ │
│  │  └──────────────────┬───────────────────────────┘    │ │
│  │                     │                                 │ │
│  │  ┌──────────────────▼───────────────────────────┐    │ │
│  │  │      Data Persistence Layer                  │    │ │
│  │  ├──────────────────────────────────────────────┤    │ │
│  │  │ • SQLite Database (encrypted)                │    │ │
│  │  │ • User Profile Store (JSON)                  │    │ │
│  │  │ • Configuration Manager                      │    │ │
│  │  └──────────────────────────────────────────────┘    │ │
│  │                                                        │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │         OS Integration Layer                          │ │
│  │  - Windows: Win32 API, WMI                            │ │
│  │  - macOS: Cocoa, Quartz, Core Audio                   │ │
│  │  - Linux: X11/Wayland, PulseAudio                     │ │
│  └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

        ▲                                  ▲
        │ (One-time only)                  │ (Updates only)
        │                                  │
        ▼                                  ▼
┌────────────────────┐          ┌────────────────────┐
│  ML Model Storage  │          │  Software Updates  │
│  (AWS S3/CDN)      │          │  (GitHub Releases) │
└────────────────────┘          └────────────────────┘
```

### 8.2 Technology Stack

#### Backend (Core Engine)
- **Language**: Python 3.10+
- **ML Framework**: scikit-learn 1.3+, TensorFlow Lite 2.13+ (for on-device inference)
- **Computer Vision**: OpenCV 4.8+, MediaPipe 0.10+
- **Audio Processing**: librosa 0.10+, PyAudio 0.2.13+
- **System Monitoring**: psutil 5.9+, pynput 1.7+
- **Database**: SQLite 3.40+ with SQLCipher for encryption
- **Task Scheduler**: APScheduler 3.10+

#### Frontend (UI)
- **Framework**: Electron 27+ (cross-platform desktop)
- **UI Library**: React 18+ with TypeScript
- **State Management**: Zustand 4+
- **Charts**: Chart.js 4+ or Recharts 2+
- **Styling**: Tailwind CSS 3+
- **IPC**: electron-ipc for frontend-backend communication

#### ML Models
- **Face Detection**: MediaPipe Face Mesh (468 landmarks)
- **Facial AU Recognition**: OpenFace 2.2.0 (pre-trained)
- **Stress Classifier**: Custom Random Forest (trained on WESAD dataset)
- **Anomaly Detection**: Isolation Forest (unsupervised)
- **Voice Stress**: Pre-trained MFCC-based SVM (calibrated per user)

#### Platform-Specific APIs
- **Windows**: pywin32 (Win32 API), WMI (process monitoring)
- **macOS**: pyobjc (Cocoa framework), Quartz (window management)
- **Linux**: python-xlib (X11), Wnck (window tracking)

### 8.3 Data Flow Architecture

```
┌──────────────┐
│   Raw Input  │
│ (Keyboard/   │
│  Mouse/      │
│  Camera/     │
│  Microphone) │
└──────┬───────┘
       │
       ▼
┌─────────────────────────┐
│  Feature Extraction     │
│  (Every 30 seconds)     │
├─────────────────────────┤
│ Behavioral:             │
│  - typing_speed: 65 WPM │
│  - error_rate: 0.12     │
│  - idle_time: 45s       │
│  - app_switches: 3      │
│                         │
│ Facial (if in call):    │
│  - AU4_intensity: 2.1   │
│  - blink_rate: 8/min    │
│  - smile_genuineness:0.3│
│                         │
│ Voice (if in call):     │
│  - pitch_mean: 180 Hz   │
│  - pitch_std: 25 Hz     │
│  - speech_rate: 4.2 syl/s│
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  Baseline Comparison    │
│  (Z-score normalization)│
├─────────────────────────┤
│ typing_speed_z: +1.8    │ <- 1.8 std dev above normal
│ error_rate_z: +2.3      │ <- Significant deviation
│ AU4_z: +1.5             │
│ pitch_mean_z: +2.1      │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  ML Inference           │
│  (Stress Classifier)    │
├─────────────────────────┤
│ behavioral_score: 72    │
│ facial_score: 65        │
│ voice_score: 78         │
│ confidence: 0.83        │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  Multi-Modal Fusion     │
│  (Weighted Average)     │
├─────────────────────────┤
│ final_score = 0.5×72 +  │
│               0.3×65 +  │
│               0.2×78    │
│             = 71.1      │
│                         │
│ Apply temporal smooth:  │
│ smoothed = 0.7×71 +     │
│            0.3×prev(68) │
│          = 70.1         │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  Stress Level           │
│  Classification         │
├─────────────────────────┤
│ Score: 70.1             │
│ Level: HIGH             │
│ Trend: ↗ Increasing     │
│ Duration: 45 minutes    │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  Alert Decision         │
├─────────────────────────┤
│ IF score > 60 AND       │
│    duration > 30 min    │
│ THEN trigger alert      │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│  UI Update + Storage    │
├─────────────────────────┤
│ • Update dashboard      │
│ • Show notification     │
│ • Log to database       │
└─────────────────────────┘
```

### 8.4 Database Schema

```sql
-- User Profile (Baseline Data)
CREATE TABLE user_profile (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    calibration_complete BOOLEAN DEFAULT 0,

    -- Behavioral baselines
    avg_typing_speed REAL,
    std_typing_speed REAL,
    avg_error_rate REAL,
    avg_app_switches_per_hour REAL,
    avg_idle_per_session REAL,

    -- Facial baselines (during calls)
    avg_blink_rate REAL,
    avg_AU4_intensity REAL,
    avg_smile_genuineness REAL,

    -- Voice baselines (during calls)
    avg_pitch REAL,
    std_pitch REAL,
    avg_speech_rate REAL,

    -- Metadata
    calibration_hours_collected REAL,
    last_updated TIMESTAMP
);

-- Stress Events (Time-series)
CREATE TABLE stress_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Scores
    behavioral_score REAL,
    facial_score REAL,
    voice_score REAL,
    final_score REAL,
    stress_level TEXT, -- LOW/MEDIUM/HIGH/CRITICAL
    confidence REAL,

    -- Context
    active_application TEXT,
    in_video_call BOOLEAN,
    calendar_event_id TEXT,

    -- Module availability
    behavioral_active BOOLEAN,
    facial_active BOOLEAN,
    voice_active BOOLEAN
);

-- Alerts
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    alert_type TEXT, -- HIGH_STRESS/CRITICAL_STRESS/NO_BREAK
    message TEXT,
    stress_score REAL,
    acknowledged BOOLEAN DEFAULT 0,
    acknowledged_at TIMESTAMP,
    user_action TEXT -- DISMISSED/TOOK_BREAK/SNOOZED
);

-- Application Usage
CREATE TABLE app_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    application_name TEXT,
    category TEXT, -- IDE/BROWSER/COMMUNICATION/OTHER
    duration_seconds INTEGER,
    stress_score REAL
);

-- Video Call Sessions
CREATE TABLE video_calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    platform TEXT, -- Zoom/Teams/Meet/etc
    avg_stress_score REAL,
    max_stress_score REAL,
    facial_data_points INTEGER,
    voice_data_points INTEGER
);

-- User Settings
CREATE TABLE settings (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 8.5 ML Model Pipeline

#### 8.5.1 Baseline Learning (Calibration Phase)

```python
# Pseudocode for baseline calculation

def calibrate_baseline(user_data, days=5):
    """
    Learn user's normal behavior over 5 days
    """
    features = [
        'typing_speed', 'error_rate', 'app_switches',
        'idle_time', 'blink_rate', 'pitch_mean'
    ]

    baseline = {}
    for feature in features:
        values = user_data[feature]

        # Remove outliers (>3 std dev)
        clean_values = remove_outliers(values, threshold=3)

        # Calculate statistics
        baseline[feature] = {
            'mean': np.mean(clean_values),
            'std': np.std(clean_values),
            'p10': np.percentile(clean_values, 10),
            'p90': np.percentile(clean_values, 90)
        }

    return baseline
```

#### 8.5.2 Stress Classification

```python
# Pseudocode for stress detection

def calculate_stress_score(current_features, baseline):
    """
    Multi-modal stress detection
    """
    # Step 1: Normalize features
    normalized = {}
    for feature, value in current_features.items():
        if feature in baseline:
            z_score = (value - baseline[feature]['mean']) / baseline[feature]['std']
            normalized[feature] = z_score

    # Step 2: Behavioral stress score
    behavioral_indicators = [
        'typing_speed_z',  # High typing speed = stress
        'error_rate_z',     # High errors = stress
        'app_switches_z'    # Frequent switches = stress
    ]
    behavioral_score = calculate_module_score(
        normalized,
        behavioral_indicators,
        weights=[0.4, 0.4, 0.2]
    )

    # Step 3: Facial stress score (if available)
    facial_score = None
    if in_video_call():
        facial_indicators = ['AU4_z', 'blink_rate_z', 'smile_genuineness_z']
        facial_score = calculate_module_score(normalized, facial_indicators)

    # Step 4: Voice stress score (if available)
    voice_score = None
    if in_video_call() and microphone_active():
        voice_indicators = ['pitch_z', 'speech_rate_z', 'jitter_z']
        voice_score = calculate_module_score(normalized, voice_indicators)

    # Step 5: Fusion
    scores = [behavioral_score]
    weights = [0.5]

    if facial_score:
        scores.append(facial_score)
        weights.append(0.3)

    if voice_score:
        scores.append(voice_score)
        weights.append(0.2)

    # Normalize weights to sum to 1
    weights = [w / sum(weights) for w in weights]

    final_score = sum(s * w for s, w in zip(scores, weights))

    # Step 6: Temporal smoothing
    smoothed_score = 0.7 * final_score + 0.3 * get_previous_score()

    return {
        'behavioral': behavioral_score,
        'facial': facial_score,
        'voice': voice_score,
        'final': smoothed_score,
        'level': classify_level(smoothed_score)
    }

def classify_level(score):
    if score < 30:
        return 'LOW'
    elif score < 60:
        return 'MEDIUM'
    elif score < 85:
        return 'HIGH'
    else:
        return 'CRITICAL'
```

### 8.6 Performance Optimization

#### Resource Constraints
| Component | CPU Usage | Memory | GPU (Optional) |
|-----------|-----------|--------|----------------|
| Behavioral Monitor | <1% | 50 MB | N/A |
| Facial Analysis | 3-5% | 200 MB | 10% (if available) |
| Voice Analysis | 2-3% | 100 MB | N/A |
| UI (Electron) | 1-2% | 150 MB | N/A |
| **Total** | **<10%** | **500 MB** | **10% (optional)** |

#### Optimization Strategies
1. **Frame Skipping**: Process facial analysis at 10 FPS (not 30 FPS)
2. **Model Quantization**: Use TensorFlow Lite INT8 models (4x smaller, faster)
3. **Lazy Loading**: Load facial/voice modules only when video call detected
4. **Batch Processing**: Process behavioral data in 30-second batches
5. **Efficient Hooks**: OS-level hooks with minimal callback overhead
6. **Incremental Baseline**: Update baseline statistics incrementally (no full recalculation)

---

## 9. User Stories & Use Cases

### 9.1 Primary User Stories

#### US-001: First-Time Setup
**As a** new user
**I want to** easily set up the application with clear privacy explanations
**So that** I understand what's monitored and feel comfortable using it

**Acceptance Criteria:**
- Setup wizard completes in <5 minutes
- Privacy policy shown in simple, non-legal language
- Can opt in/out of each module individually
- Camera/microphone permissions requested with clear justification
- Calibration period explained with progress indicator

---

#### US-002: Daily Stress Awareness
**As a** remote worker
**I want to** see my current stress level at a glance
**So that** I can take breaks before burnout

**Acceptance Criteria:**
- System tray icon shows stress level via color
- Tooltip shows numerical score on hover
- Dashboard opens in <2 seconds
- Stress score updates within 30 seconds of change

---

#### US-003: Break Reminders
**As an** IT professional who gets absorbed in work
**I want to** receive gentle reminders when stress is high
**So that** I remember to take breaks

**Acceptance Criteria:**
- Alert triggers after 30 min of high stress
- Message is empathetic, not alarming
- Can snooze for 30 minutes
- Can dismiss with "I'm fine" option
- Max 1 alert per hour to avoid annoyance

---

#### US-004: Understanding Stress Triggers
**As a** product manager with many meetings
**I want to** see which activities cause my stress
**So that** I can restructure my day

**Acceptance Criteria:**
- Dashboard shows top 5 stress triggers
- Correlation with calendar events visible
- Can filter by date range
- Triggers ranked by frequency and intensity

---

#### US-005: Privacy Control
**As a** privacy-conscious user
**I want to** pause monitoring and clear data easily
**So that** I feel in control of my information

**Acceptance Criteria:**
- "Pause Monitoring" button in system tray
- "Clear All Data" button with confirmation in settings
- Data deletion is immediate and irreversible
- Transparency dashboard shows what's collected

---

### 9.2 Use Case Scenarios

#### Scenario 1: Detecting Meeting Fatigue
**Context:** Sarah has 6 back-to-back Zoom meetings (10 AM - 4 PM)

**Flow:**
1. 10:00 AM - First meeting starts
   - System detects Zoom process
   - Activates facial + voice modules
   - Baseline stress: 25 (Low)

2. 12:00 PM - Third meeting
   - Facial AU4 (brow furrow) increasing
   - Voice pitch elevated by 20 Hz
   - Stress score: 55 (Medium)

3. 2:30 PM - Fifth meeting
   - Forced smile detected (AU6+12 low genuineness)
   - Blink rate drops to 6/min (eye strain)
   - Stress score: 72 (High)

4. 2:35 PM - Alert triggered
   - Notification: "You've been in meetings for 4 hours. Consider a short break after this call."
   - Sarah dismisses ("Remind me in 30 min")

5. 3:15 PM - Follow-up reminder
   - Sarah takes a 10-minute walk
   - Stress score drops to 45 upon return

**Outcome:** Early intervention prevented late-afternoon burnout

---

#### Scenario 2: Debugging Frustration
**Context:** Raj is stuck on a bug for 2 hours

**Flow:**
1. 2:00 PM - Starts debugging
   - Switches between IDE, browser, Stack Overflow
   - Baseline stress: 30 (Low)

2. 2:45 PM - Frustration builds
   - App switches: 25 in 10 minutes (high thrashing)
   - Typing-then-delete cycles: 8 occurrences
   - Stress score: 58 (Medium)

3. 3:30 PM - Peak frustration
   - Idle periods: 3x 45-second "staring at screen"
   - Error rate: 18% (3x baseline)
   - Stress score: 78 (High)

4. 3:35 PM - Alert
   - "You've been working intensely on the same task. A short break might help you see it fresh."
   - Raj realizes he's stuck, posts question on team Slack

5. 3:50 PM - Teammate helps
   - Bug fixed collaboratively
   - Stress score returns to 35

**Outcome:** Alert prompted help-seeking behavior

---

#### Scenario 3: False Positive Prevention
**Context:** Maria is excited, not stressed, during product launch

**Flow:**
1. 4:00 PM - Product launch meeting
   - High energy presentation
   - Voice pitch elevated (excitement)
   - Facial animation high
   - Voice module: 65 (would indicate stress)
   - Facial module: 60 (would indicate stress)

2. Behavioral module shows:
   - Typing speed normal
   - App usage: Single app (presentation mode)
   - No error spikes
   - Behavioral score: 25 (Low)

3. Multi-modal fusion:
   - Weighted average: 0.5×25 + 0.3×60 + 0.2×65 = 43.5
   - Level: MEDIUM (not HIGH)
   - No alert triggered due to behavioral contradiction

**Outcome:** Multi-modal approach prevented false alarm

---

## 10. Data Models & ML Requirements

### 10.1 Feature Vectors

#### Behavioral Feature Vector (Collected every 30 seconds)
```json
{
  "timestamp": "2026-02-01T14:30:00Z",
  "typing_speed_wpm": 65,
  "typing_error_rate": 0.12,
  "backspace_frequency": 8.5,
  "typing_pauses_count": 3,
  "app_switches_last_10min": 12,
  "active_app_duration_sec": 420,
  "idle_time_sec": 45,
  "cursor_stationary_time_sec": 30,
  "repeated_actions": ["copy-paste:5", "file-reopen:2"],
  "work_session_duration_min": 125,
  "time_since_last_break_min": 95
}
```

#### Facial Feature Vector (Collected every 3 seconds during calls)
```json
{
  "timestamp": "2026-02-01T14:30:00Z",
  "face_detected": true,
  "face_confidence": 0.95,
  "landmarks_count": 68,
  "action_units": {
    "AU1": 0.2,  // Inner Brow Raiser
    "AU4": 2.1,  // Brow Lowerer (stress indicator)
    "AU6": 1.5,  // Cheek Raiser
    "AU7": 1.8,  // Lid Tightener (eye strain)
    "AU12": 1.2, // Lip Corner Puller
    "AU17": 0.8, // Chin Raiser
    "AU23": 1.5  // Lip Tightener
  },
  "blink_rate_per_min": 8,
  "eye_aspect_ratio": 0.22,
  "smile_genuineness": 0.35,  // Low = forced smile
  "head_pose": {
    "pitch": -5.2,
    "yaw": 2.1,
    "roll": 0.8
  },
  "head_movement_variance": 0.15  // Low = rigid posture
}
```

#### Voice Feature Vector (Collected every 3 seconds during calls)
```json
{
  "timestamp": "2026-02-01T14:30:00Z",
  "voice_detected": true,
  "speech_duration_sec": 2.4,
  "fundamental_freq_hz": 185,
  "pitch_std_hz": 28,
  "pitch_range_hz": 95,
  "speech_rate_syllables_per_sec": 4.5,
  "pause_count": 2,
  "pause_total_duration_sec": 1.2,
  "jitter_percent": 0.8,
  "shimmer_percent": 2.5,
  "harmonics_to_noise_ratio_db": 18,
  "mfcc_coefficients": [12.3, -5.4, 3.2, ...],  // 13 coefficients
  "voice_quality": "strained"  // normal/breathy/strained/harsh
}
```

### 10.2 ML Model Specifications

#### Model 1: Baseline Anomaly Detector
**Algorithm:** Isolation Forest (unsupervised)
**Purpose:** Detect when user behavior deviates from personal baseline
**Input:** Normalized behavioral feature vector
**Output:** Anomaly score (0-1, higher = more anomalous)
**Training:** First 5 days of user data (20+ hours)
**Re-training:** Weekly incremental update

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,  # Expect 10% anomalous points
    random_state=42
)
```

---

#### Model 2: Stress Classifier (Supervised)
**Algorithm:** Random Forest Classifier
**Purpose:** Classify stress level from features
**Input:** Combined behavioral + facial + voice features
**Output:** Stress probability (0-1)
**Training Data:** WESAD dataset (wrist/chest sensors) + custom labeled data
**Classes:** Binary (stressed/not-stressed), then mapped to 0-100 scale

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=10,
    class_weight='balanced'
)

# Features importance ranking
# 1. typing_error_rate_z: 0.18
# 2. AU4_intensity_z: 0.15
# 3. pitch_std_z: 0.12
# ...
```

---

#### Model 3: Facial AU Recognizer
**Algorithm:** OpenFace 2.2.0 (pre-trained CNN)
**Purpose:** Extract facial action units from video frames
**Input:** 224x224 RGB face image
**Output:** 18 AU intensities (0-5 scale)
**Model Size:** 98 MB
**Inference Time:** 45 ms per frame (on CPU)

---

#### Model 4: Voice Stress Detector
**Algorithm:** SVM with RBF kernel
**Purpose:** Classify voice stress from acoustic features
**Input:** 13 MFCCs + pitch + jitter + shimmer
**Output:** Stress probability (0-1)
**Training Data:** SAVEE, RAVDESS emotion datasets (filtered for stress/tension)
**Calibration:** Fine-tuned with user's first 2 hours of call audio

---

### 10.3 Model Performance Requirements

| Model | Accuracy Target | Latency | Model Size | Hardware |
|-------|-----------------|---------|------------|----------|
| Anomaly Detector | 80% precision | <10 ms | 5 MB | CPU |
| Stress Classifier | 85% accuracy | <50 ms | 20 MB | CPU |
| Facial AU | 90% AU accuracy | <50 ms | 98 MB | GPU (optional) |
| Voice Stress | 75% accuracy | <100 ms | 15 MB | CPU |

---

### 10.4 Training Data Requirements

#### Initial Model Training (Pre-deployment)
- **WESAD Dataset**: Wearable stress detection (15 subjects, 5+ hours each)
- **SEWA Dataset**: Facial/vocal emotion in-the-wild
- **Custom Dataset**: 50 beta users, 2 weeks each, labeled via ESM

#### Per-User Calibration Data
- **Baseline**: 5 working days, 20+ hours of passive monitoring
- **Labels**: Optional user feedback ("Was this stressful? Yes/No")
- **Validation**: Ground truth from random ESM prompts (3x per day)

---

## 11. User Interface & Experience

### 11.1 UI Wireframes (Text Description)

#### System Tray Icon States
```
┌─────────────────────────────────────┐
│ Icon States (16x16 px):             │
├─────────────────────────────────────┤
│ 🟢 Green  = Stress: 0-30 (Low)      │
│ 🟡 Yellow = Stress: 31-60 (Medium)  │
│ 🟠 Orange = Stress: 61-85 (High)    │
│ 🔴 Red    = Stress: 86-100 (Critical)│
│ ⚪ Gray   = Monitoring paused       │
│ ⚫ Black  = Calibrating (first 5 days)│
└─────────────────────────────────────┘

Right-Click Menu:
├── Open Dashboard
├── Current Stress: 65 (High)
├────────────────
├── Pause Monitoring
├── Settings
├── About
└── Exit
```

---

#### Main Dashboard Layout
```
┌──────────────────────────────────────────────────────────┐
│  Stress Monitor Dashboard                    [_][□][×]  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │         CURRENT STRESS LEVEL                       │ │
│  │                                                    │ │
│  │              ┌─────────────┐                       │ │
│  │              │     65      │  🟠 HIGH              │ │
│  │              │   ━━━━━━━   │                       │ │
│  │              └─────────────┘                       │ │
│  │                                                    │ │
│  │         "You've been under high load for           │ │
│  │          the past 45 minutes"                      │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  TODAY'S TREND                                     │ │
│  │  ┌────────────────────────────────────────────┐   │ │
│  │  │   Stress                                   │   │ │
│  │  │ 100 ┤                                       │   │ │
│  │  │  80 ┤          ╭─╮                         │   │ │
│  │  │  60 ┤      ╭──╯ ╰─╮ ←You are here          │   │ │
│  │  │  40 ┤   ╭──╯       ╰────                   │   │ │
│  │  │  20 ┤───╯                                  │   │ │
│  │  │   0 └────────────────────────────────      │   │ │
│  │  │     9am  11am  1pm  3pm  5pm               │   │ │
│  │  └────────────────────────────────────────────┘   │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌──────────────┬──────────────┬──────────────────────┐ │
│  │  BEHAVIORAL  │   FACIAL     │      VOICE           │ │
│  │      72      │     65       │       78             │ │
│  │   🟢 Active  │  🟡 In Call  │   🟡 In Call        │ │
│  └──────────────┴──────────────┴──────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  STRESS TRIGGERS (This Week)                       │ │
│  │  1. 🎥 Video meetings (avg stress: 68)             │ │
│  │  2. 💻 IDE (long sessions) (avg: 62)               │ │
│  │  3. 📧 Email (context switching) (avg: 58)         │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  RECOMMENDATIONS                                   │ │
│  │  • Consider a 5-10 minute break                    │ │
│  │  • You haven't taken a break in 95 minutes         │ │
│  │  • Tomorrow: Try scheduling breaks between meetings│ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│         [View Weekly Report]  [Settings]                │
└──────────────────────────────────────────────────────────┘
```

---

#### Settings Panel
```
┌──────────────────────────────────────────────────────┐
│  Settings                                  [×]       │
├──────────────────────────────────────────────────────┤
│                                                      │
│  MONITORING MODULES                                  │
│  ☑ Behavioral Monitoring (Always active)            │
│  ☑ Facial Analysis (During video calls)             │
│  ☑ Voice Analysis (During video calls)              │
│                                                      │
│  ────────────────────────────────────────────────   │
│                                                      │
│  ALERTS                                              │
│  Alert Threshold: [Medium] [High] [●Critical Only]  │
│  ☑ Show desktop notifications                       │
│  ☐ Play sound with alerts                           │
│  Do Not Disturb Hours: [9:00 PM] to [8:00 AM]       │
│                                                      │
│  ────────────────────────────────────────────────   │
│                                                      │
│  PRIVACY                                             │
│  • All data stored locally on your computer         │
│  • No videos or audio recordings saved              │
│  • Only feature data (numbers) stored                │
│                                                      │
│  [View Data Summary]                                 │
│  [Clear All Data] ⚠️                                 │
│                                                      │
│  ────────────────────────────────────────────────   │
│                                                      │
│  APPLICATION FILTERS                                 │
│  Exclude from monitoring:                            │
│  [+ Add Application]                                 │
│  • Personal Browser (Firefox Personal Profile)      │
│  • Spotify                                           │
│                                                      │
│  ────────────────────────────────────────────────   │
│                                                      │
│  DATA RETENTION                                      │
│  Keep history for: [○ 7 days] [● 30 days]           │
│                    [○ 90 days] [○ 1 year]           │
│                                                      │
│               [Cancel]  [Save Changes]               │
└──────────────────────────────────────────────────────┘
```

---

### 11.2 Notification Examples

#### Alert 1: High Stress Duration
```
┌────────────────────────────────────────┐
│  🟠 Stress Monitor                     │
├────────────────────────────────────────┤
│  You've been under high load for       │
│  the past 45 minutes.                  │
│                                        │
│  Consider taking a 5-minute break      │
│  to reset.                             │
│                                        │
│  [I'm Fine]  [Remind Me in 30min]     │
└────────────────────────────────────────┘
```

#### Alert 2: No Break Reminder
```
┌────────────────────────────────────────┐
│  🟡 Stress Monitor                     │
├────────────────────────────────────────┤
│  You haven't taken a break in 3 hours. │
│                                        │
│  Even a 2-minute walk can help!        │
│                                        │
│  [Dismiss]  [Start 5-min Timer]       │
└────────────────────────────────────────┘
```

#### Alert 3: Meeting Fatigue
```
┌────────────────────────────────────────┐
│  🟠 Stress Monitor                     │
├────────────────────────────────────────┤
│  You've been in video calls for        │
│  4 hours today.                        │
│                                        │
│  Your stress level: 68 (High)          │
│                                        │
│  Try to schedule a buffer after this   │
│  meeting.                              │
│                                        │
│  [Got It]                              │
└────────────────────────────────────────┘
```

---

### 11.3 Onboarding Flow

#### Step 1: Welcome
```
Welcome to Stress Monitor!

Your personal wellness companion for work.

We help you:
✓ Detect stress before burnout
✓ Understand your work patterns
✓ Take breaks at the right time

[Get Started]
```

#### Step 2: Privacy Explanation
```
Your Privacy is Our Priority

What we monitor:
✓ Typing patterns (speed, errors)
✓ Application usage (duration, switches)
✓ Facial expressions (during video calls only)
✓ Voice patterns (during video calls only)

What we DON'T collect:
✗ Keystroke content (what you type)
✗ Screen content (what you see)
✗ Video or audio recordings
✗ Browsing history or personal data

Everything stays on YOUR computer.
No cloud. No sharing. Period.

[I Understand] [Read Full Privacy Policy]
```

#### Step 3: Module Selection
```
Choose Monitoring Modules

We recommend enabling all modules for best accuracy,
but you can customize:

☑ Behavioral Monitoring (Recommended)
   Track typing, app usage, breaks

☑ Facial Analysis (Recommended)
   Detect stress during video calls
   Requires: Webcam permission

☑ Voice Analysis (Optional)
   Analyze voice patterns in calls
   Requires: Microphone permission

You can change these anytime in Settings.

[Continue]
```

#### Step 4: Permissions
```
Grant Permissions

To monitor your stress, we need:

📷 Camera Access
   To analyze facial expressions during video calls
   [Grant Permission]

🎤 Microphone Access
   To analyze voice patterns during calls
   [Grant Permission]

⌨️ Accessibility Access (macOS/Linux)
   To monitor typing and app usage
   [Grant Permission]

[Skip This Step] [Continue]
```

#### Step 5: Calibration
```
Learning Your Baseline

For the next 5 working days, we'll learn
what's "normal" for you.

Everyone works differently, so we need to
understand YOUR patterns before detecting stress.

During this time:
• Work as you normally would
• We'll collect baseline data
• No alerts will be sent
• Progress: Day 1 of 5

You can use the app anytime, but stress detection
accuracy improves after calibration completes.

[Start Monitoring]
```

---

## 12. Privacy, Security & Ethics

### 12.1 Privacy Principles

#### Principle 1: Data Minimization
**Policy:** Collect only what's necessary for stress detection.

**Implementation:**
- ❌ Do NOT collect: Keystroke content, screenshots, video recordings, audio files
- ✅ DO collect: Keystroke metadata (timing, speed), facial landmarks (coordinates), audio features (pitch, no content)
- Example: Instead of storing "password123", we store "8 keystrokes in 1.2 seconds with 0 errors"

---

#### Principle 2: Local-First Processing
**Policy:** All computation happens on user's device.

**Implementation:**
- No API calls during monitoring
- No telemetry or analytics transmission
- Network used ONLY for:
  - Initial model download (one-time)
  - Software updates (user-initiated)
- Firewall rules to block unauthorized egress

**Verification:**
- Wireshark packet capture testing
- Network monitor dashboard in UI

---

#### Principle 3: User Control
**Policy:** Users own their data and can delete it anytime.

**Implementation:**
- "Pause Monitoring" button (instant stop)
- "Clear All Data" button (irreversible deletion)
- Granular module toggles
- No "required" modules (all optional)
- Export data in CSV format

---

#### Principle 4: Transparency
**Policy:** Users know exactly what's collected and why.

**Implementation:**
- Plain-language privacy policy (no legal jargon)
- Onboarding wizard explains each module
- "Data Summary" page shows collection stats
- Open-source codebase (planned for v2.0)

---

### 12.2 Security Measures

#### Data Encryption
- **At Rest**: AES-256 encryption for all databases
- **Key Storage**: OS keychain (Windows Credential Manager, macOS Keychain, Linux Secret Service)
- **Algorithm**: Fernet symmetric encryption (Python `cryptography` library)

```python
from cryptography.fernet import Fernet
import keyring

# Generate key (once per user)
key = Fernet.generate_key()
keyring.set_password("StressMonitor", "db_key", key.decode())

# Encrypt data
cipher = Fernet(key)
encrypted_data = cipher.encrypt(sensitive_data.encode())
```

---

#### Access Control
- **File Permissions**: User-only read/write (chmod 600 on Linux/macOS)
- **Process Isolation**: Run as user-level process (no admin/root required)
- **Camera/Mic Access**: Request permissions via OS dialogs
- **Application Signing**: Code-signed binaries (prevents tampering)

---

#### Secure Updates
- **HTTPS Only**: Download updates over TLS 1.3
- **Signature Verification**: GPG-signed releases
- **Auto-update**: Optional (user can disable)
- **Rollback**: Keep previous version for 7 days

---

### 12.3 Ethical Guidelines

#### Guideline 1: No Employer Surveillance
**Commitment:** This tool is for individual use only.

**Implementation:**
- No "admin dashboard" or team view
- No export to manager/HR
- License agreement prohibits employer-mandated use
- Warning during installation: "This tool is for YOUR wellness only"

---

#### Guideline 2: Non-Diagnostic Tool
**Commitment:** Not a medical device or clinical diagnosis tool.

**Implementation:**
- Disclaimers in UI: "Not a substitute for professional help"
- Recommendations link to mental health resources
- No use of clinical terms (e.g., "burnout" → "high stress")
- Encourage seeking professional help if needed

---

#### Guideline 3: Informed Consent
**Commitment:** Users must explicitly opt in.

**Implementation:**
- No default "yes" checkboxes
- Clear explanations before each permission request
- Can withdraw consent anytime
- Re-consent required after major updates

---

#### Guideline 4: Bias Mitigation
**Commitment:** Fair detection across demographics.

**Implementation:**
- Test facial recognition across skin tones (using Pilot Parliaments Benchmark)
- Validate voice analysis across accents/languages
- Behavioral baseline adapts to individual (no generic thresholds)
- Diverse beta testing cohort (50+ users, varied backgrounds)

---

### 12.4 Compliance & Legal

#### GDPR Compliance (EU)
- ✅ Right to access data (export feature)
- ✅ Right to deletion ("Clear All Data")
- ✅ Data minimization (only necessary data)
- ✅ Purpose limitation (stress detection only)
- ✅ No cross-border transfer (local-only)

#### CCPA Compliance (California)
- ✅ Right to know what's collected (transparency dashboard)
- ✅ Right to delete data
- ✅ No sale of personal information (N/A - no data leaves device)

#### HIPAA (NOT applicable)
- This is NOT a medical device
- Not covered under HIPAA
- Disclaimer: "For wellness awareness only, not medical diagnosis"

#### Accessibility (ADA/WCAG 2.1)
- Color-blind friendly UI (not relying solely on color)
- Keyboard navigation support
- Screen reader compatibility
- High-contrast mode

---

## 13. Implementation Roadmap

### 13.1 Development Phases

#### Phase 0: Foundation (Weeks 1-2)
**Goal:** Set up development environment and architecture

**Tasks:**
- [ ] Set up Git repository with .gitignore
- [ ] Initialize Python project (poetry/pip)
- [ ] Set up Electron boilerplate
- [ ] Configure CI/CD pipeline (GitHub Actions)
- [ ] Create database schema (SQLite)
- [ ] Design directory structure
- [ ] Write technical specification document
- [ ] Set up testing framework (pytest)

**Deliverables:**
- Working dev environment
- Project skeleton
- Tech spec document

---

#### Phase 1: Behavioral Module (Weeks 3-5)
**Goal:** Implement background behavioral monitoring

**Tasks:**
- [ ] Implement keyboard hook (pynput)
  - Typing speed calculation
  - Error rate tracking
  - Backspace frequency
- [ ] Implement application monitoring
  - Active window detection (OS-specific)
  - App categorization
  - Context switching tracking
- [ ] Implement idle time detection
  - Mouse/keyboard inactivity
  - Screen lock detection
- [ ] Build data collection pipeline
  - 30-second aggregation
  - Store to SQLite
- [ ] Create baseline learning module
  - 5-day calibration
  - Statistical baseline calculation
- [ ] Unit tests (80% coverage)

**Deliverables:**
- Functional behavioral module
- Database with behavioral data
- Test suite

---

#### Phase 2: Facial Analysis Module (Weeks 6-8)
**Goal:** Implement video call facial stress detection

**Tasks:**
- [ ] Integrate MediaPipe Face Mesh
  - Face detection
  - Landmark extraction (68 points)
- [ ] Integrate OpenFace for AU recognition
  - Install and test OpenFace
  - Extract AU intensities
- [ ] Implement eye behavior analysis
  - Blink detection (Eye Aspect Ratio)
  - Blink rate calculation
- [ ] Implement head pose estimation
  - solvePnP algorithm
  - Pitch/yaw/roll calculation
- [ ] Build video call detector
  - Process monitoring (Zoom, Teams, etc.)
  - Camera access detection
- [ ] Optimize performance
  - Frame rate limiting (10 FPS)
  - GPU acceleration (optional)
- [ ] Unit tests

**Deliverables:**
- Functional facial module
- Tested with sample videos
- Performance benchmarks

---

#### Phase 3: Voice Analysis Module (Weeks 9-10)
**Goal:** Implement voice stress detection

**Tasks:**
- [ ] Set up audio capture (PyAudio)
  - 16kHz sampling
  - Noise reduction
- [ ] Implement Voice Activity Detection (Silero VAD)
- [ ] Extract pitch features (librosa)
  - Fundamental frequency (F0)
  - Pitch variability
- [ ] Extract voice quality features (Parselmouth)
  - Jitter
  - Shimmer
  - Harmonics-to-Noise Ratio
- [ ] Implement speech rate analysis
  - Syllable counting
  - Pause detection
- [ ] Build microphone mute detector
- [ ] Unit tests

**Deliverables:**
- Functional voice module
- Tested with sample audio
- Feature extraction validated

---

#### Phase 4: ML Model Training (Weeks 11-12)
**Goal:** Train and validate stress detection models

**Tasks:**
- [ ] Acquire training datasets
  - Download WESAD, SAVEE, RAVDESS
  - Label custom data from beta users
- [ ] Train baseline anomaly detector (Isolation Forest)
  - Feature engineering
  - Hyperparameter tuning
  - Validation (80/20 split)
- [ ] Train stress classifier (Random Forest)
  - Feature importance analysis
  - Cross-validation
  - Threshold calibration
- [ ] Validate facial AU model (OpenFace)
  - Test on diverse faces
  - Benchmark accuracy
- [ ] Train voice stress SVM
  - MFCC feature extraction
  - RBF kernel tuning
- [ ] Export models (pickle/joblib)
- [ ] Model performance testing

**Deliverables:**
- Trained models (accuracy ≥85%)
- Model evaluation reports
- Serialized model files

---

#### Phase 5: Multi-Modal Fusion (Weeks 13-14)
**Goal:** Combine all modules into unified stress score

**Tasks:**
- [ ] Implement signal normalization
  - Z-score transformation
  - Min-max scaling
- [ ] Build fusion engine
  - Weighted averaging
  - Confidence scoring
- [ ] Implement temporal smoothing (Kalman filter)
- [ ] Build stress level classifier (0-100 → Low/Med/High/Critical)
- [ ] Implement trend analysis
  - Linear regression for trend
  - Peak stress hour detection
- [ ] Build trigger identification
  - Correlation analysis
  - Association rule mining
- [ ] Integration testing (all modules working together)

**Deliverables:**
- Working multi-modal system
- Unified stress score output
- Integration test suite

---

#### Phase 6: User Interface (Weeks 15-17)
**Goal:** Build desktop application UI

**Tasks:**
- [ ] Set up Electron + React project
- [ ] Build system tray icon
  - Color-coded stress levels
  - Right-click menu
- [ ] Build main dashboard
  - Current stress gauge
  - Trend line chart (Chart.js)
  - Module status indicators
- [ ] Build notification system
  - Native OS notifications (plyer)
  - Alert logic implementation
- [ ] Build settings panel
  - Module toggles
  - Alert preferences
  - Privacy controls
- [ ] Build historical reports
  - Weekly stress heatmap
  - Trigger analysis view
  - PDF export (ReportLab)
- [ ] Implement onboarding wizard
  - 5-step setup flow
  - Permission requests
- [ ] UI/UX testing

**Deliverables:**
- Functional desktop app
- Polished UI
- User testing feedback

---

#### Phase 7: Privacy & Security (Weeks 18-19)
**Goal:** Implement encryption and privacy features

**Tasks:**
- [ ] Implement AES-256 database encryption
- [ ] Integrate OS keychain for key storage
- [ ] Build "Clear All Data" functionality
  - Secure deletion (overwrite)
- [ ] Build "Pause Monitoring" feature
- [ ] Implement data retention policies
  - Auto-purge old data
- [ ] Build transparency dashboard
  - Data collection summary
- [ ] Add privacy policy to app
- [ ] Security audit (penetration testing)
- [ ] Network traffic verification (Wireshark)

**Deliverables:**
- Encrypted data storage
- Privacy controls working
- Security audit report

---

#### Phase 8: Testing & Optimization (Weeks 20-22)
**Goal:** Comprehensive testing and performance tuning

**Tasks:**
- [ ] Performance profiling
  - CPU usage optimization (<10%)
  - Memory footprint reduction (<500 MB)
- [ ] Battery impact testing (laptops)
- [ ] Cross-platform testing
  - Windows 10/11
  - macOS 12/13/14
  - Ubuntu 20.04/22.04
- [ ] Edge case testing
  - Multiple monitors
  - External webcams
  - Bluetooth headsets
- [ ] Load testing (24-hour continuous run)
- [ ] Accuracy validation
  - Ground truth labeling (ESM)
  - Calculate precision/recall
- [ ] Bug fixing sprint
- [ ] Code refactoring
- [ ] Documentation (README, user guide)

**Deliverables:**
- Performance benchmarks
- Bug-free application
- User documentation

---

#### Phase 9: Beta Testing (Weeks 23-26)
**Goal:** Real-world validation with beta users

**Tasks:**
- [ ] Recruit 50 beta testers (diverse backgrounds)
- [ ] Distribute beta builds
- [ ] Set up feedback collection (surveys, bug reports)
- [ ] Monitor usage analytics (crash reports)
- [ ] Conduct user interviews (5-10 users)
- [ ] Iterate based on feedback
- [ ] Address critical bugs
- [ ] Refine UI based on usability feedback
- [ ] Validate accuracy with ESM ground truth
- [ ] Calculate final metrics (NPS, retention, accuracy)

**Deliverables:**
- Beta testing report
- User feedback summary
- Product improvements

---

#### Phase 10: Launch Preparation (Weeks 27-28)
**Goal:** Prepare for public release

**Tasks:**
- [ ] Finalize branding (logo, colors)
- [ ] Create marketing website
- [ ] Write blog post/press release
- [ ] Create demo video (2-3 minutes)
- [ ] Prepare app store listings
  - Windows Store (optional)
  - macOS App Store (optional)
- [ ] Set up support channels (email, Discord)
- [ ] Final QA pass
- [ ] Create installers (.exe, .dmg, .deb)
- [ ] Sign code (Windows Authenticode, macOS notarization)
- [ ] Prepare launch announcement

**Deliverables:**
- Production-ready build
- Marketing materials
- Support infrastructure

---

#### Phase 11: Launch (Week 29)
**Goal:** Public release v1.0

**Tasks:**
- [ ] Deploy website
- [ ] Publish installers (GitHub Releases)
- [ ] Submit to app stores (if applicable)
- [ ] Announce on social media, Reddit, HN
- [ ] Monitor launch metrics (downloads, crashes)
- [ ] Respond to user feedback
- [ ] Hotfix critical bugs (if any)

**Deliverables:**
- Live product
- Launch analytics

---

### 13.2 Milestone Summary

| Milestone | Week | Deliverable | Success Criteria |
|-----------|------|-------------|------------------|
| M1: Foundation | 2 | Dev environment ready | All developers can build project |
| M2: Behavioral Module | 5 | Background monitoring works | 20+ hours of data collected |
| M3: Facial Module | 8 | Video call analysis works | AU detection accuracy >90% |
| M4: Voice Module | 10 | Voice stress detection works | Pitch extraction working |
| M5: ML Models | 12 | Models trained | Stress classifier accuracy ≥85% |
| M6: Fusion Engine | 14 | Unified stress score | All modules integrated |
| M7: UI Complete | 17 | Desktop app functional | Dashboard displays real-time data |
| M8: Privacy Features | 19 | Encryption implemented | Security audit passed |
| M9: Testing Complete | 22 | Performance optimized | CPU <10%, Memory <500MB |
| M10: Beta Launch | 26 | 50 users testing | Feedback collected |
| M11: Public Launch | 29 | v1.0 released | Product live |

---

### 13.3 Resource Allocation

#### Team Composition (Recommended)
- **Backend Engineer** (Python, ML): 1 FTE
- **Frontend Engineer** (Electron, React): 1 FTE
- **ML Engineer** (Model training, optimization): 0.5 FTE
- **UI/UX Designer**: 0.5 FTE
- **QA Engineer**: 0.5 FTE
- **Product Manager**: 0.25 FTE

**Total:** ~3.75 FTE for 29 weeks

---

#### Technology Costs
- **ML Datasets**: Free (WESAD, SAVEE, RAVDESS are public)
- **Cloud Storage**: $0 (local-only)
- **CI/CD**: $0 (GitHub Actions free tier)
- **Code Signing Certificates**: $200/year (Windows + macOS)
- **Domain + Hosting**: $50/year

**Total:** ~$250/year

---

## 14. Dependencies & Constraints

### 14.1 Technical Dependencies

#### External Libraries
| Library | Version | Purpose | License | Risk |
|---------|---------|---------|---------|------|
| Python | 3.10+ | Backend runtime | PSF | Low |
| OpenCV | 4.8+ | Video processing | Apache 2.0 | Low |
| MediaPipe | 0.10+ | Face detection | Apache 2.0 | Medium (Google maintained) |
| OpenFace | 2.2.0 | Facial AU recognition | Apache 2.0 | Medium (academic project) |
| librosa | 0.10+ | Audio analysis | ISC | Low |
| scikit-learn | 1.3+ | ML models | BSD-3 | Low |
| Electron | 27+ | Desktop UI | MIT | Low |
| React | 18+ | UI framework | MIT | Low |
| SQLite | 3.40+ | Database | Public Domain | Low |

**Mitigation:**
- Pin exact versions in requirements.txt
- Monthly security updates
- Fallback algorithms if dependency unavailable (e.g., Haar Cascades if MediaPipe fails)

---

### 14.2 Hardware Constraints

#### Minimum System Requirements
- **CPU**: Dual-core 2.0 GHz (Intel i5 or equivalent)
- **RAM**: 4 GB (8 GB recommended)
- **Storage**: 500 MB available
- **Camera**: 720p webcam (for facial module)
- **Microphone**: Any (for voice module)
- **GPU**: Optional (improves facial analysis speed by 2-3x)

#### Supported Operating Systems
- Windows 10 (1903+), Windows 11
- macOS 12 Monterey, 13 Ventura, 14 Sonoma
- Ubuntu 20.04 LTS, 22.04 LTS, Fedora 36+

**Constraint:** Older OS versions may lack required APIs (e.g., macOS <12 has limited camera permission controls)

---

### 14.3 Privacy Constraints

#### What We CANNOT Do
1. **Store raw video/audio**: Privacy violation, also large storage footprint
2. **Transmit data to cloud**: Defeats "local-only" promise
3. **Access browser content**: No screen scraping or DOM inspection
4. **Read file contents**: Only track file names, not content
5. **Track personal apps**: Must have whitelist/blacklist

---

### 14.4 Legal Constraints

#### Age Restriction
- **18+ only**: Monitoring minors raises consent issues
- Verify during onboarding (not foolproof, but due diligence)

#### Employment Law
- Cannot be mandated by employers (violates autonomy)
- Must include license clause: "For personal use only, not workplace surveillance"

#### Medical Device Regulations (FDA/CE)
- NOT a medical device (no diagnosis/treatment)
- Disclaimers required to avoid liability

---

### 14.5 Scalability Constraints

#### v1.0 Limitations
- **Single user per machine**: No multi-user profiles
- **Local-only data**: No cross-device sync
- **90-day history max**: Avoid database bloat
- **No mobile support**: Desktop-only

**Rationale:** Keep v1.0 scope manageable, add features in v2.0+

---

## 15. Risk Assessment

### 15.1 Technical Risks

#### Risk 1: Facial Recognition Accuracy Across Skin Tones
**Probability:** Medium
**Impact:** High (bias, user distrust)
**Mitigation:**
- Test on diverse dataset (Pilot Parliaments Benchmark)
- Use MediaPipe (Google's model has been tested for fairness)
- Fallback to behavioral-only detection if facial fails
- Provide opt-out for facial module

---

#### Risk 2: Battery Drain on Laptops
**Probability:** Medium
**Impact:** Medium (user dissatisfaction)
**Mitigation:**
- Aggressive performance optimization (target <5% CPU)
- Use TensorFlow Lite INT8 models (lower power)
- Allow users to disable modules
- Provide "Power Saver" mode (reduced sampling rate)

---

#### Risk 3: Model Overfitting to WESAD Dataset
**Probability:** Medium
**Impact:** Medium (poor real-world accuracy)
**Mitigation:**
- Supplement with custom labeled data (50 beta users)
- Cross-validate on multiple datasets
- Per-user calibration (personalized baseline)
- A/B test models during beta

---

#### Risk 4: OS API Changes (Breaking Updates)
**Probability:** Low
**Impact:** High (app stops working)
**Mitigation:**
- Pin OS versions in testing
- Monitor Apple/Microsoft developer forums
- Maintain fallback methods (e.g., accessibility API + legacy API)
- Fast patch release cycle (within 7 days of OS update)

---

### 15.2 Privacy Risks

#### Risk 5: Data Breach (Local Database Stolen)
**Probability:** Low
**Impact:** High (privacy violation)
**Mitigation:**
- AES-256 encryption at rest
- No PII stored (only feature vectors)
- Secure key storage (OS keychain)
- Educate users on physical security

---

#### Risk 6: Unauthorized Access by Malware
**Probability:** Low
**Impact:** Medium (data exfiltration)
**Mitigation:**
- Code signing (prevents tampering)
- Regular security audits
- No network access during monitoring (firewall rules)
- Recommend users run antivirus

---

### 15.3 User Experience Risks

#### Risk 7: Alert Fatigue (Too Many Notifications)
**Probability:** High
**Impact:** Medium (users disable app)
**Mitigation:**
- Limit to 1 alert per hour
- Provide snooze option
- Allow customization of alert threshold
- Use gentle, non-alarming language

---

#### Risk 8: Calibration Period Too Long (5 Days)
**Probability:** Medium
**Impact:** Low (user impatience)
**Mitigation:**
- Show progress bar ("Day 2 of 5")
- Provide partial functionality during calibration
- Explain why calibration is necessary
- Allow "Quick Start" with generic baseline (lower accuracy warning)

---

### 15.4 Market Risks

#### Risk 9: Low User Adoption (Trust Issues)
**Probability:** Medium
**Impact:** High (product failure)
**Mitigation:**
- Emphasize "local-only" in marketing
- Provide open-source roadmap (v2.0)
- Transparent privacy policy
- Beta testimonials
- Partner with mental health organizations for endorsement

---

#### Risk 10: Competing Products Launch First
**Probability:** Low
**Impact:** Medium (reduced novelty)
**Mitigation:**
- Fast development cycle (29 weeks)
- Differentiation: Multi-modal + privacy-first
- Strong UX focus
- Community building (Discord, Reddit)

---

## 16. Future Enhancements (v2.0+)

### 16.1 Post-Launch Features

#### Feature 1: Calendar Integration
**Description:** Correlate stress with calendar events (meetings, deadlines)
**Effort:** Medium
**Value:** High
**Priority:** P0 for v2.0

**Implementation:**
- Integrate with Google Calendar, Outlook, iCal APIs
- Tag stress events with calendar context
- Provide insights: "Your 1:1s with John correlate with 20% higher stress"

---

#### Feature 2: Team Insights (Anonymous Aggregation)
**Description:** Anonymized team-level stress trends for managers
**Effort:** High
**Value:** Medium
**Priority:** P1 for v2.0

**Implementation:**
- Opt-in only (user consent required)
- Aggregate data from ≥10 users (k-anonymity)
- No individual identification
- Show team trends, peak stress hours
- **Ethical guardrail:** Cannot tie stress to performance reviews

---

#### Feature 3: Wearable Integration (Heart Rate, HRV)
**Description:** Enhance detection with physiological data
**Effort:** High
**Value:** High
**Priority:** P0 for v3.0

**Implementation:**
- Integrate with Apple Watch, Fitbit, Garmin APIs
- Heart Rate Variability (HRV) as stress indicator
- Combine with behavioral/facial/voice for 4-modal detection
- Increase accuracy to 90%+

---

#### Feature 4: Mobile Companion App
**Description:** View dashboard on phone, receive alerts
**Effort:** High
**Value:** Medium
**Priority:** P2 for v2.0

**Implementation:**
- React Native app (iOS, Android)
- Sync data via local WiFi (no cloud)
- Read-only view (no data collection on mobile)
- Push notifications for stress alerts

---

#### Feature 5: Stress Mitigation Suggestions (AI Coach)
**Description:** Personalized recommendations based on triggers
**Effort:** Medium
**Value:** High
**Priority:** P0 for v2.0

**Implementation:**
- If trigger = "long meetings", suggest: "Try 25-min Pomodoro meetings"
- If trigger = "email context switching", suggest: "Batch process emails 2x/day"
- Use GPT-4 API (local LLM in v3.0) for natural language suggestions

---

#### Feature 6: Posture & Ergonomics Monitoring
**Description:** Detect poor posture using webcam
**Effort:** Medium
**Value:** Medium
**Priority:** P2 for v2.0

**Implementation:**
- Use MediaPipe Pose to detect slouching
- Alert if hunched over for >30 minutes
- Combine with stress detection (poor posture + stress = alert priority)

---

#### Feature 7: Open-Source Release
**Description:** Make codebase public for transparency
**Effort:** Low
**Value:** High (trust building)
**Priority:** P0 for v2.0

**Implementation:**
- Clean up code, add comments
- MIT or Apache 2.0 license
- Publish on GitHub
- Community contributions welcome

---

## 17. Appendix

### 17.1 Glossary

- **Action Unit (AU):** Facial muscle movement defined by Facial Action Coding System (FACS)
- **Baseline:** User's normal behavior patterns learned during calibration
- **Calibration:** 5-day learning period to establish baseline
- **ESM (Experience Sampling Method):** Research technique where users report feelings at random intervals (ground truth)
- **False Positive:** System incorrectly flags stress when user is not stressed
- **False Negative:** System misses stress when user is actually stressed
- **HRV (Heart Rate Variability):** Variation in time between heartbeats (stress indicator)
- **Jitter:** Short-term variation in pitch (voice quality measure)
- **MFCC (Mel-Frequency Cepstral Coefficients):** Audio features representing voice timbre
- **Multi-modal:** Using multiple data sources (behavior, face, voice)
- **Shimmer:** Short-term variation in amplitude (voice quality measure)
- **Stress Score:** Numerical value 0-100 representing stress level
- **Temporal Smoothing:** Averaging over time to reduce noise

---

### 17.2 References

#### Research Papers
1. "Realtime Face Speech Emotion Recognition in Worker Stress Analysis" (IEEE 2024/25) - Base paper
2. "WESAD: A Multimodal Dataset for Wearable Stress and Affect Detection" (UbiComp 2018)
3. "OpenFace 2.0: Facial Behavior Analysis Toolkit" (FG 2018)
4. "Automatic Stress Detection in Working Environments From Smartphones" (Pervasive Computing 2015)

#### Datasets
- **WESAD:** Wrist and chest sensor stress data (15 subjects)
- **SAVEE:** Speech emotion dataset (British English, 4 speakers)
- **RAVDESS:** Audio-visual emotion dataset (24 actors)
- **Pilot Parliaments:** Facial recognition fairness benchmark (diverse demographics)

#### Tools & Frameworks
- **MediaPipe:** https://google.github.io/mediapipe/
- **OpenFace:** https://github.com/TadasBaltrusaitis/OpenFace
- **librosa:** https://librosa.org/
- **Electron:** https://www.electronjs.org/

---

### 17.3 Frequently Asked Questions

**Q: Will this slow down my computer?**
A: No. Target CPU usage is <10% and memory <500 MB. Most users won't notice any impact.

**Q: Can my employer see my stress data?**
A: No. All data stays on your computer. There's no "export to manager" feature.

**Q: What if I don't have a webcam?**
A: The behavioral module works without a webcam. Facial/voice modules only activate during video calls.

**Q: Does this record my video calls?**
A: No. We analyze video frames in real-time and discard them immediately. Nothing is recorded.

**Q: Can I use this on multiple computers?**
A: v1.0 is single-device only. Cross-device sync planned for v2.0.

**Q: Is this open-source?**
A: Not initially. Open-source release planned for v2.0 after stability improvements.

**Q: How accurate is the stress detection?**
A: Target accuracy is ≥85%. Accuracy improves after the 5-day calibration period.

**Q: Will this work with all video conferencing apps?**
A: We support Zoom, Teams, Google Meet, Webex, Slack Huddles, and Discord. Others can be added via settings.

---

### 17.4 Contact & Support

**During Development:**
- GitHub Issues: (repo TBD)
- Email: dev-team@stressmonitor.io (placeholder)

**Post-Launch:**
- User Guide: https://stressmonitor.io/docs
- Discord Community: (invite link TBD)
- Email Support: support@stressmonitor.io
- Bug Reports: GitHub Issues

---

## Document Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-02-01 | Initial PRD creation | Development Team |

---

**END OF DOCUMENT**

---

**Total Word Count:** ~12,500 words
**Estimated Reading Time:** 50 minutes
**Status:** Ready for stakeholder review
