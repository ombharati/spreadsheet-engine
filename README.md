# Spreadsheet Engine

A from-scratch Python spreadsheet computation engine for learning core CS and programming concepts.

## Overview
This project implements the core logic of a spreadsheet: cell storage, formula evaluation, dependency tracking, and recalculation. Built as a learning exercise while exploring Python fundamentals, OOP, graphs, and interpreters.

**Goals**:
- Deepen Python skills (data structures, OOP, error handling)
- Understand dependency graphs and topological sorting
- Practice formula parsing and evaluation
- Experiment with software design principles (modularity, testing)

**Status**: Early MVP stage. Basics in progress; see [Progress](#progress).

## Features (Planned/Implemented)
- Cell value storage and retrieval
- Basic formula support (arithmetic, cell references)
- Dependency tracking and efficient recalculation
- Circular reference detection

## Quick Start
```bash
# Clone the repo
git clone https://github.com/yourusername/spreadsheet-engine.git
cd spreadsheet-engine

# (Optional: virtual env)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (if any, e.g., later for testing)
pip install -r requirements.txt

# Run example / tests
python -m pytest  # or python examples/basic.py
