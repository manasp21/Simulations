# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains interactive physics simulations for visualizing electric fields around high-voltage transmission lines. The simulations are educational tools for electrical engineering students and professionals to understand electromagnetic field behavior in power systems.

## Architecture

**Self-Contained HTML Simulations**: Each simulation is a complete, standalone HTML file containing embedded CSS styling and JavaScript physics engine. No external dependencies, build systems, or package managers are used.

**Core Components**:
- `ElectricFieldSimulationSimple.html` - Primary simulation with dual-panel layout featuring central arrow and distance plot analysis for ultra-low field visualization

## Technical Implementation

**Physics Engine**: Real-time electric field calculations using:
- Conducting cylindrical conductors with proper boundary conditions (E = 0 inside)
- Non-conducting ground (no image charges or ground plane effects)
- Line charge density calculations: λᵢ(t) = 2πε₀Vᵢ(t) / ln(2hᵢ/a)
- Electric field superposition: E(r,t) = Σᵢ₌₁⁶ [λᵢ(t) / (2πε₀)] · (r̂ᵢ / rᵢ)
- Time-varying voltage: Vᵢ(t) = V_peak × sin(ωt + φᵢ + θ_circuit)

**Coordinate System**:
- World coordinates: meters from tower base
- Screen coordinates: pixels with pixelsPerMeter scaling (16 px/m)
- Tower height: 35 meters (typical for 345-500 kV transmission)

**Visualization System**:
- Canvas-based vector field rendering
- Uniform blue arrow styling for field vectors
- Real-time animation with configurable update rates (5-60 Hz)
- Interactive parameter controls for voltage (115-765 kV), frequency (50-60 Hz), phase offsets

## Usage

**Running Simulations**: Open HTML files directly in any modern web browser. No installation or setup required.

**Development Workflow**: Since files are self-contained HTML, simply edit the file and refresh browser to see changes. No build process or package management needed.

**Current Implementation**:
- **Primary Simulation**: Dual-panel layout with central arrow and distance plot analysis
- **Ultra-Low Field Analysis**: Enhanced for analyzing fields in the 12m-58m range with improved sensitivity
- **Focus Areas**: Central field vector visualization and radial distance field magnitude plotting

**Key Parameters**:
- Peak Voltage: Real-world transmission line voltages in kV
- Frequency: Power system frequency (50/60 Hz)
- Phase Offset: Circuit 2 relative to Circuit 1 (0-360°)
- Vector Spacing/Scale: Visualization density and arrow size

## Development Guidelines

**Single File Architecture**: The simulation is contained in a single HTML file. When creating variations (dark/light themes), maintain identical physics calculations and control interfaces - only visual styling should differ between variants.

**Physics Accuracy**: Mathematical models must remain scientifically accurate for educational use. Key constants:
- EPSILON_0 = 8.854e-12 F/m (vacuum permittivity)
- Conductor arrangements: Hexagonal configuration with 6m radius, opposing phase arrangement

**Performance**: Simulations run real-time field calculations on vector grids. Optimize for smooth animation while maintaining calculation accuracy.

**Code Structure**: Functions are organized by purpose:
- `calculateElectricField()` - Core physics computation with method of images
- `draw*()` functions - Rendering components (tower, conductors, vectors, ground)
- `worldToScreen()` - Coordinate system conversion
- Event handlers - UI parameter controls
- `animate()` - Main render loop with configurable update rates

**Specialized Visualization Functions**:
- `drawCentralArrow()` - Single large arrow at center point showing field vector
- `drawFieldPlot()` - Real-time distance vs field magnitude plot with ultra-low field sensitivity
- `sampleFieldAtDistance()` - Averages field magnitude at 8 points around distance circle
- `drawSecondaryArrow()` - Blue E-vector at 25m distance for comparison
- `drawDistanceScale()` - Concentric circles and reference grid for distance visualization

## File Conventions

- HTML files are self-contained with embedded CSS/JS
- Current implementation uses light theme styling with gradient sky background
- When creating theme variants, maintain identical DOM structure and JavaScript functionality
- File naming convention: `ElectricFieldSimulation[Variant].html`
- Current focus: Ultra-low field analysis capabilities for educational demonstrations