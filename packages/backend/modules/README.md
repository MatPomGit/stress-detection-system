# Monitoring Modules

This directory contains the core monitoring modules for stress detection:

## Structure

- **behavioral/** - Background behavioral monitoring (typing, apps, idle time)
- **facial/** - Facial stress analysis during video calls
- **voice/** - Voice stress analysis during video calls
- **fusion/** - Multi-modal signal fusion engine

## Implementation Status

All modules are currently in **planning phase**. See the [PRD](../../../docs/PRD_Stress_Detection_System.md) for detailed specifications.

### Phase 2: Behavioral Module (Weeks 3-5)
- Keyboard/mouse hooks
- Application monitoring
- Idle time detection
- Baseline learning

### Phase 3: Facial Analysis (Weeks 6-8)
- MediaPipe face detection
- OpenFace AU recognition
- Eye behavior analysis

### Phase 4: Voice Analysis (Weeks 9-10)
- Audio capture
- Pitch/tone extraction
- Voice quality features

### Phase 5: Multi-Modal Fusion (Weeks 13-14)
- Signal normalization
- Weighted fusion
- Stress score calculation
