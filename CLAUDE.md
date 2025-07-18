# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains interactive physics simulations for visualizing electric fields around high-voltage transmission lines. The simulations are educational tools for electrical engineering students and professionals to understand electromagnetic field behavior in power systems.

## Architecture

**Self-Contained HTML Simulations**: Each simulation is a complete, standalone HTML file containing embedded CSS styling and JavaScript physics engine. No external dependencies, build systems, or package managers are used.

**Core Components**:
- `ElectricFieldSimulationDark.html` - Dark theme simulation
- `ElectricFieldSimulationLight.html` - Light theme simulation (identical functionality, different visual styling)

## Technical Implementation

**Physics Engine**: Real-time electric field calculations using:
- Method of images for ground plane effects
- Line charge density calculations: λᵢ(t) = 2πε₀Vᵢ(t) / ln(2h/a)
- Electric field superposition: E(r,t) = Σᵢ₌₁⁶ [λᵢ(t) / (2πε₀)] · (r̂ᵢ / rᵢ)
- Time-varying voltage: Vᵢ(t) = V_peak × sin(ωt + φᵢ + θ_circuit)

**Coordinate System**:
- World coordinates: meters from tower base
- Screen coordinates: pixels with pixelsPerMeter scaling (16 px/m)
- Tower height: 35 meters (typical for 345-500 kV transmission)

**Visualization System**:
- Canvas-based vector field rendering
- Color-coded field magnitude mapping (blue→cyan→green→yellow→red)
- Real-time animation with configurable update rates (1-30 Hz)
- Interactive parameter controls for voltage (115-765 kV), frequency (50-60 Hz), phase offsets

## Usage

**Running Simulations**: Open HTML files directly in any modern web browser. No installation or setup required.

**Key Parameters**:
- Peak Voltage: Real-world transmission line voltages in kV
- Frequency: Power system frequency (50/60 Hz)
- Phase Offset: Circuit 2 relative to Circuit 1 (0-360°)
- Vector Spacing/Scale: Visualization density and arrow size

## Development Guidelines

**Theme Synchronization**: When modifying functionality, ensure both Dark and Light variants maintain identical physics calculations and control interfaces. Only visual styling should differ between themes.

**Physics Accuracy**: Mathematical models must remain scientifically accurate for educational use. Key constants:
- EPSILON_0 = 8.854e-12 F/m (vacuum permittivity)
- Conductor arrangements: Inner/outer equilateral triangles (4m/8m radius)

**Performance**: Simulations run real-time field calculations on vector grids. Optimize for smooth animation while maintaining calculation accuracy.

**Code Structure**: Functions are organized by purpose:
- `calculateElectricField()` - Core physics computation
- `draw*()` functions - Rendering components (tower, conductors, vectors, ground)
- Event handlers - UI parameter controls
- `animate()` - Main render loop

## File Conventions

- HTML files are self-contained with embedded CSS/JS
- Dark theme uses darker color schemes for backgrounds and UI elements
- Light theme uses brighter, more traditional color schemes
- Both themes use identical DOM structure and JavaScript functionality