# Pokémon RL (Emerald + BizHawk)

Reinforcement learning environment for training agents to play Pokémon Emerald using BizHawk + Python.

---

## ⚠️ Requirements

You must install:

- Python 3.11
- BizHawk Emulator  
  https://tasvideos.org/BizHawk
- Pokémon Emerald ROM  
  Place as: `roms/Pokemon_Emerald.gba`


---

## 🧠 Architecture

- BizHawk runs the game
- Lua script handles input + frame stepping
- Python connects via socket
- Stable-Baselines3 trains PPO agent

---

## 🚀 Setup

### 1. Create environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
```
---

🎮 Run BizHawk
1. Open BizHawk
2. Load Pokémon Emerald ROM
3. Open Lua Console
4. Run: `lua/bridge.lua`

---
🧠 Train Agent
```bash
python train.py
```

This will start PPO training using screen observations.

---

📺 Record Gameplay

After training:
```bash
python record.py
```
Outputs:
```bash
recordings/run.mp4
```

---
🎯 First Milestone

The agent should learn:
- random movement
- leaving starting area
- basic exploration