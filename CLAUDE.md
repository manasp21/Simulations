# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains interactive physics simulations for visualizing electric fields around high-voltage transmission lines. The simulations are educational tools for electrical engineering students and professionals to understand electromagnetic field behavior in power systems.

## Architecture

**Self-Contained HTML Simulations**: Each simulation is a complete, standalone HTML file containing embedded CSS styling and JavaScript physics engine. No external dependencies, build systems, or package managers are used.

**Core Components**:
- `ElectricFieldSimulationSimple.html` - Primary simulation with dual-panel layout featuring central arrow and distance plot analysis for ultra-low field visualization
- `transmission_line_animation.py` - Manim animation script for educational visualization of electric field physics
- `test_manim_basic.py` - Basic compatibility test script for Manim setup
- `README_manim.md` - Documentation for Manim animation setup and usage

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

**Development Workflow**: 
- **HTML Simulations**: Edit the file and refresh browser to see changes. No build process needed.
- **Manim Animations**: Test with `manim test_manim_basic.py BasicTest -p`, then render with `manim transmission_line_animation.py TransmissionLineFieldAnimation -qh`

**Current Implementation**:
- **Primary Simulation**: Dual-panel layout with central arrow and distance plot analysis
- **Ultra-Low Field Analysis**: Enhanced for analyzing fields in the 12m-58m range with improved sensitivity
- **Focus Areas**: Central field vector visualization and radial distance field magnitude plotting

**Key Parameters**:
- Peak Voltage: 0-250 kV (was 115-765 kV, updated for educational range)
- Frequency: 0-60 Hz (includes static field analysis at 0 Hz)
- Phase Offset: Circuit 2 relative to Circuit 1 (0-360°)
- Vector Spacing/Scale: Visualization density and arrow size

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
- `drawCentralArrow()` - Single large arrow at center point showing field vector
- `drawFieldPlot()` - Real-time distance vs field magnitude plot with ultra-low field sensitivity
- `sampleFieldAtDistance()` - Averages field magnitude at above-ground points only (fixed underground sampling issue)
- `drawSecondaryArrow()` - Blue E-vector at 25m distance for comparison
- `drawDistanceScale()` - Concentric circles and reference grid for distance visualization
- Distance labels (10m, 20m, 30m, 40m, 50m) positioned consistently in bottom-right direction

## File Conventions

- HTML files are self-contained with embedded CSS/JS
- Current implementation uses light theme styling with gradient sky background
- When creating theme variants, maintain identical DOM structure and JavaScript functionality
- File naming convention: `ElectricFieldSimulation[Variant].html`
- Current focus: Ultra-low field analysis capabilities for educational demonstrations

## Git Workflow

**Current State**: Repository tracks a single active simulation file (`ElectricFieldSimulationSimple.html`) with periodic cleanup of outdated variants.

**Development Pattern**: 
- Make incremental improvements to the active simulation
- Test changes by opening HTML file in browser
- Commit functional enhancements with descriptive messages
- Remove obsolete simulation variants to maintain repository cleanliness

**No Build System**: Since simulations are self-contained HTML files, there are no build commands, test runners, or package management scripts to execute.

## Manim Animation Development

**Setup Requirements**:
```bash
pip install manim numpy
```

**Common Commands**:
- **Test compatibility**: `manim test_manim_basic.py BasicTest -p`
- **Quick preview**: `manim transmission_line_animation.py TransmissionLineFieldAnimation -ql`
- **High quality render**: `manim transmission_line_animation.py TransmissionLineFieldAnimation -qh`
- **Check syntax**: `manim transmission_line_animation.py TransmissionLineFieldAnimation --dry_run`

**Animation Architecture**:
- 5 educational scenes: system setup, voltage phasors, field animation, field plotting, parameter studies
- Converts HTML simulation physics into dynamic educational visualization
- Uses same electric field calculations with conducting cylinders above non-conducting ground

**Known Compatibility Issues**:
- Color constants (CYAN, GRAY, YELLOW, ORANGE) defined as hex values for compatibility
- Avoid modifying `self.time` property (Manim read-only)
- Use `DEGREES = PI/180` for angle conversions

## Physics Model Details

**Critical Implementation Notes**:
- **Conducting Boundary Condition**: Field calculation returns zero inside conductor radius (E = 0)
- **Non-Conducting Ground**: No image charges or artificial ground effects
- **Fixed Field Sampling**: Underground points excluded from distance averaging to prevent artificial discontinuities
- **Natural 1/r Physics**: No artificial exponential attenuation or field limiting that creates unphysical kinks
- **Conductor Labels**: A1, B1, C1, A2, B2, C2 positioned outside conductor circles with black outlines for visibility