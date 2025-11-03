#!/bin/bash
# Simple wrapper for NotebookLM Automation

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ $# -eq 0 ]; then
    echo "Usage: ./generate.sh <input.json> [options]"
    echo ""
    echo "Options:"
    echo "  --headless       Run browser in headless mode"
    echo "  --timeout SECS   Set timeout in seconds (default: 600)"
    echo ""
    echo "Example:"
    echo "  ./generate.sh my_project.json"
    echo "  ./generate.sh my_project.json --headless"
    echo "  ./generate.sh my_project.json --timeout 900"
    exit 1
fi

python "$SCRIPT_DIR/scripts/generate_audio_overviews.py" "$@"
