# NotebookLM Automation

Automate creation of multiple audio overviews in Google NotebookLM with different prompts and focus areas.

## Installation

1. **Download and extract** this zip file to your server:
```bash
scp notebooklm-automation.zip your-server:~
ssh your-server
unzip notebooklm-automation.zip
cd notebooklm-automation
```

2. **Install dependencies**:
```bash
pip install playwright --break-system-packages
playwright install chromium
```

3. **Make script executable**:
```bash
chmod +x scripts/generate_audio_overviews.py
```

## Quick Start

1. **Create an input file** (`my_project.json`):
```json
{
  "sources": [
    "https://example.com/article1",
    "https://example.com/article2"
  ],
  "audio_overviews": [
    {
      "prompt": "Focus on technical concepts for developers",
      "length": "longer"
    },
    {
      "prompt": "Create executive summary for business leaders",
      "length": "default"
    }
  ]
}
```

2. **Run the automation**:
```bash
python scripts/generate_audio_overviews.py my_project.json
```

3. **Audio files download to current directory**

## Usage Options

### Basic (with visible browser for authentication)
```bash
python scripts/generate_audio_overviews.py input.json
```

### Headless mode (after initial auth)
```bash
python scripts/generate_audio_overviews.py input.json --headless
```

### Custom timeout (default is 10 minutes)
```bash
python scripts/generate_audio_overviews.py input.json --timeout 900
```

## Input File Format

```json
{
  "sources": [
    "URL1",
    "URL2"
  ],
  "audio_overviews": [
    {
      "prompt": "What the AI should focus on",
      "length": "default"  // or "longer" (never "shorter")
    }
  ]
}
```

See `references/example_input.json` for a complete example.

## How It Works

The script uses Playwright to:
1. Open NotebookLM and create a new notebook
2. Add all source URLs
3. Wait for sources to process
4. Create each audio overview with its specific prompt/length
5. Wait ~10 minutes for generation
6. Download all audio files

## For Your iOS + SSH Workflow

Since you operate from iOS via SSH:

1. **Initial setup** (one time):
```bash
ssh your-server
cd ~/notebooklm-automation
pip install playwright --break-system-packages
playwright install chromium
```

2. **Each time you need audio overviews**:
```bash
ssh your-server
cd ~/notebooklm-automation
vim input.json  # or upload via SFTP
python scripts/generate_audio_overviews.py input.json
```

3. **Files download to** `/home/claude/` on your server

4. **Retrieve files** via SFTP or set up a simple web server

## Authentication Handling

First run requires Google sign-in:
- Run without `--headless` flag
- Use X11 forwarding: `ssh -X your-server`
- Or use VNC to see the browser
- After first auth, subsequent runs can use `--headless`

## Troubleshooting

See `references/troubleshooting.md` for:
- Updating selectors if NotebookLM UI changes
- Common failure scenarios
- Debugging tips

## File Structure

```
notebooklm-automation/
├── README.md              # This file
├── SKILL.md              # Detailed skill documentation
├── INSTALL.md            # Installation guide
├── scripts/
│   └── generate_audio_overviews.py  # Main automation script
└── references/
    ├── example_input.json           # Example input file
    └── troubleshooting.md           # Troubleshooting guide
```

## Limitations

- Max ~10 audio overviews per run
- Sources must be publicly accessible websites
- Requires Google account with NotebookLM access
- Generation takes ~5-10 minutes per overview
- UI automation may break if NotebookLM updates
