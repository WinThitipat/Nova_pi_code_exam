# 🤖 IkazuchiBot – NovaPi Autonomous & Manual Control System

### 📘 Overview
**IkazuchiBot** is a multi-functional robot system built on the **Makeblock NovaPi + mBuild** ecosystem.  
It supports **manual control** via the gamepad and **autonomous mode** for precise movement control using **encoder motors**, **DC motors**, **smart servos**, and **brushless components**.  

This project was developed by **SUSHI_IOT / Ikazuchi** of **ROYAL PALADIN Team**, as part of a WIP competitive robotics project.

---

## ⚙️ Features

### 🚗 Movement System
- **Omni-directional control** using 4 encoder motors:
  - Move forward / backward  
  - Move sideways (left / right)  
  - Spin in place (left / right)  
- Angle-based movement for precision auto operation  

### ⚡ Conveyor & Intake System
- Independent control of **upper**, **midway**, and **lower** conveyors  
- Support for **reverse** operation  
- Integrated **intake motor** for feeding or ejecting objects  

### 🎯 Shooter System
- Brushless motor toggled with one button  
- Adjustable speed for firing mechanisms  

### 🦾 Manipulator System
- **Forklift**: Controlled by joystick axis  
- **Gripper**: Open/close via button commands  
- **Smart Servo**: 3-position toggle for lifting or adjusting levels  

### 🤖 Autonomous Mode
- **Kachidoki Auto System**:  
  Performs a predefined sequence of movements based on robot zone (`L` or `R`)  
  - Collects blocks  
  - Moves to target position using motor angle feedback  
  - Automatically stops upon reaching target rotation  

### 🎮 Gamepad Controls

| Control | Action |
|----------|--------|
| **Up / Down / Left / Right** | Move robot |
| **Rx joystick** | Spin left/right |
| **Ly joystick** | Control forklift |
| **R1 / R2** | Conveyor toggle (reverse / forward) |
| **L1 / L2** | Upper conveyor toggle (reverse / forward) |
| **+** | Toggle shooter (brushless motor) |
| **L_Thumb** | Toggle block gather system |
| **R_Thumb** | Activate Auto Mode |
| **N1 / N4** | Open / Close gripper |
| **N2** | Toggle servo position |
| **N3** | Toggle intake system |

---

## 🧠 Class Structure

### `class Ikazuchibot`
Handles all robot systems and their control logic.

#### Key Methods:
| Method | Description |
|--------|-------------|
| `logo()` | Displays ASCII startup logo |
| `set_move_degree()` | Move by encoder degree |
| `set_motor_speed()` | Set motor power directly |
| `move_forward()` / `move_backward()` | Basic movement |
| `move_left_sideway()` / `move_right_sideway()` | Strafing movement |
| `spin_left()` / `spin_right()` | Rotational movement |
| `stop_motor()` | Stop all motors |
| `brushless_speed()` | Set brushless power |
| `shooter()` | Toggle shooter system |
| `convey_system()` | Conveyor logic with toggle & reverse |
| `servo_control()` | Multi-state servo control |
| `forklift_system()` | Control forklift via joystick |
| `block_gather_system()` | Toggle block collection system |
| `intake_system()` | Toggle intake motor |
| `kachidoki_auto_system()` | Autonomous block collection + movement |
| `control_system()` | Main loop handling all gamepad input and logic |

---

## 🧩 Hardware Connections

| Component | Port | Type |
|------------|------|------|
| Upper Left Motor | M1 | Encoder Motor |
| Upper Right Motor | M2 | Encoder Motor |
| Lower Left Motor | M3 | Encoder Motor |
| Lower Right Motor | M4 | Encoder Motor |
| Servo Level Adjustment | M5 | Smart Servo |
| Block Gather Motor | M6 | Encoder Motor |
| Upper Conveyor | DC1 | DC Motor |
| Midway Conveyor | DC2 | DC Motor |
| Lower Conveyor | DC3 | DC Motor |
| Forklift | DC4 | DC Motor |
| Gripper | DC7 | DC Motor |
| Intake | DC8 | DC Motor |
| Shooter (Brushless) | BL1 | Brushless Motor |

---

## 🔁 Main Loop

```python
robot = Ikazuchibot()
Ikazuchibot.logo()

while True:
    robot.control_system()
```

This continuously checks the **gamepad input**, **auto mode**, and executes the appropriate actions.

---

## 🛠️ Requirements

- **NovaPi** firmware compatible with `mbuild` Python API  
- **mBuild modules** (encoder motors, DC motors, servos, gamepad, etc.)  
- Python environment supporting NovaPi SDK (e.g., `mblock-py`, `novapi` package)

---

## 🧑‍💻 Credits

**Developer:** SUSHI_IOT (Ikazuchi)  
**Team:** ROYAL PALADIN  
**Language:** Python (NovaPi SDK)  
**Version:** WIP Build  

> “;-; This code made by SUSHI_IOT || DEV by Ikazuchi || ROYAL PALADIN! Team [WIP]”
