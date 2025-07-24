# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains interactive physics simulations for visualizing electric fields around high-voltage transmission lines. The simulations are educational tools for electrical engineering students and professionals to understand electromagnetic field behavior in power systems.

## Architecture

**Self-Contained HTML Simulations**: Each simulation is a complete, standalone HTML file containing embedded CSS styling and JavaScript physics engine. No external dependencies, build systems, or package managers are used.

**Core Components**:
- `ElectricFieldSimulationSimple.html` - Complete simulation with dual-panel layout featuring central arrow and distance plot analysis for ultra-low field visualization
- `README.md` - Basic repository description

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

**Running Simulation**: Open `ElectricFieldSimulationSimple.html` directly in any modern web browser. No installation or setup required.

**Development Workflow**: 
- Edit the HTML file and refresh browser to see changes. No build process needed.

**Current Implementation**:
- **Primary Simulation**: Dual-panel layout with central arrow and distance plot analysis
- **Multi-Scale Field Visualization**: Three arrows with amplification factors - Red (1x), Blue (10x), Green (100x)
- **Ultra-High Resolution Plotting**: 5000-point sampling with pure Y-axis scaling control
- **Southeast Plot Path**: 315° diagonal sampling to avoid conductor interference
- **Fixed Time Analysis**: Plot uses t=0 for consistent field data regardless of animation state

**Key Parameters**:
- Peak Voltage: Fixed at 30kV for educational demonstrations
- Frequency: 0-60 Hz (includes static field analysis at 0 Hz) 
- Phase Offset: Circuit 2 relative to Circuit 1 (0-360°)
- Plot Max Field: Pure Y-axis scaling slider (0.1-5 kV/m, default 2 kV/m)
- Plot Range: Configurable distance sampling (0-50m default)

## Development Guidelines

**Single File Architecture**: The simulation is contained in a single HTML file. When creating variations (dark/light themes), maintain identical physics calculations and control interfaces - only visual styling should differ between variants.

**Physics Accuracy**: Mathematical models must remain scientifically accurate for educational use. Key constants:
- EPSILON_0 = 8.854e-12 F/m (vacuum permittivity)
- Conductor arrangements: Hexagonal configuration with 9m radius (increased for label visibility), opposing phase arrangement
- Tower height: 50m with conductors at 44m height
- Conductor radius: 1.5cm for realistic transmission line modeling

**Performance**: Simulations run real-time field calculations on vector grids. Optimize for smooth animation while maintaining calculation accuracy.

**Code Structure**: Functions are organized by purpose:
- `calculateElectricField()` - Core physics computation with method of images
- `draw*()` functions - Rendering components (tower, conductors, vectors, ground)
- `worldToScreen()` - Coordinate system conversion
- Event handlers - UI parameter controls
- `animate()` - Main render loop with configurable update rates

**Specialized Visualization Functions**:
- `drawCentralArrow()` - Red arrow at center showing field magnitude × 1x amplification
- `drawSecondaryArrow()` - Blue arrow at 25m lateral position with 10x amplification  
- `drawGroundLevelArrow()` - Green arrow at 48.7m ground position with 100x amplification
- `drawFieldPlot()` - Ultra-high resolution distance vs field plot (5000 points) with fixed t=0 sampling
- `sampleFieldAtDistance()` - Single-point sampling along 315° diagonal path to avoid conductors
- `drawPlotPath()` - Visual indicator showing southeast sampling trajectory
- `drawScalingLegend()` - Arrow amplification reference (Red:1x, Blue:10x, Green:100x)
- `drawDistanceScale()` - Concentric circles with consistent 45° labeling

## File Conventions

- The simulation is self-contained in a single HTML file with embedded CSS/JS
- Uses light theme styling with gradient sky background
- When creating variants, maintain identical DOM structure and JavaScript functionality
- Focus: Ultra-low field analysis capabilities for educational demonstrations

## Git Workflow

**Current State**: Repository contains a single simulation file (`ElectricFieldSimulationSimple.html`).

**Development Pattern**: 
- Make incremental improvements to the simulation
- Test changes by opening HTML file in browser
- Commit functional enhancements with descriptive messages

**No Build System**: Since simulations are self-contained HTML files, there are no build commands, test runners, or package management scripts to execute.


## Physics Model Details

**Critical Implementation Notes**:
- **Conducting Boundary Condition**: Field calculation returns zero inside conductor radius (E = 0)
- **Non-Conducting Ground**: No image charges or artificial ground effects - clearly labeled in simulation
- **Plot Max Field Slider**: Pure Y-axis scaling control - NEVER calls `render()` to avoid disrupting arrow animation
- **Time Independence**: Plot sampling uses fixed t=0 to prevent data changes during slider adjustments
- **Arrow Amplification**: Each arrow uses local field value with specific amplification (1x, 10x, 100x) for multi-scale analysis
- **Southeast Plot Path**: 315° diagonal sampling avoids conductor peaks while maintaining physics accuracy
- **Ultra-High Resolution**: 5000-point sampling eliminates visual artifacts during Y-axis scaling
- **Conductor Labels**: A1, B1, C1, A2, B2, C2 positioned outside conductor circles with black outlines for visibility