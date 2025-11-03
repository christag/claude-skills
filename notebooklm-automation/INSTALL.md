# NotebookLM Automation - Installation Guide

## Download & Install

1. **[Download notebooklm-automation.zip](computer:///mnt/user-data/outputs/notebooklm-automation.zip)**

2. **Upload to your server**:
```bash
scp notebooklm-automation.zip your-server:~
```

3. **SSH in and extract**:
```bash
ssh your-server
unzip notebooklm-automation.zip
cd notebooklm-automation
```

4. **Install dependencies** (one time):
```bash
pip install playwright --break-system-packages
playwright install chromium
```

## Quick Start

### Create input file (`my_audio.json`):
```json
{
  "sources": [
    "https://example.com/article1",
    "https://example.com/article2"
  ],
  "audio_overviews": [
    {
      "prompt": "Focus on technical details for developers",
      "length": "longer"
    },
    {
      "prompt": "Executive summary for business leaders",
      "length": "default"
    }
  ]
}
```

### Run the generator:
```bash
./generate.sh my_audio.json
```

That's it! The script will:
- Open NotebookLM
- Create notebook with your sources
- Generate all audio overviews
- Download them automatically

## Usage Options

**Basic usage** (visible browser):
```bash
./generate.sh input.json
```

**Headless mode** (after first auth):
```bash
./generate.sh input.json --headless
```

**Custom timeout** (default 10 min):
```bash
./generate.sh input.json --timeout 900
```

## For iOS + SSH Workflow

Since you work from iOS:

1. **Setup** (one time):
   - Download zip on iOS
   - Upload to server via SFTP app (Termius, etc.)
   - SSH in and extract

2. **Each use**:
   - Create/edit input.json on server or upload it
   - Run: `./generate.sh input.json`
   - Files download to `/home/claude/`
   - Retrieve via SFTP or access via web server

## What's Included

```
notebooklm-automation/
├── generate.sh                      # Easy wrapper script
├── README.md                        # Full documentation
├── SKILL.md                         # Detailed skill info
├── scripts/
│   └── generate_audio_overviews.py # Main Python script
└── references/
    ├── example_input.json          # Example input
    └── troubleshooting.md          # Help guide
```

## First Run Authentication

First time requires Google sign-in:
- Run without `--headless`
- Use `ssh -X your-server` for X11 forwarding
- Or connect with VNC to see browser
- After initial auth, can use headless mode

## Common Issues

**"Playwright not found"**
```bash
pip install playwright --break-system-packages
playwright install chromium
```

**"Permission denied"**
```bash
chmod +x generate.sh scripts/generate_audio_overviews.py
```

**Timeout errors**
- Increase timeout: `./generate.sh input.json --timeout 1200`
- Each audio overview takes ~5-10 minutes

**Selectors not found**
- NotebookLM UI changed
- See `references/troubleshooting.md` for updating selectors
- Run without `--headless` to debug

## Tips

- Start with 2-3 audio overviews to test
- "longer" creates ~15-20 min episodes vs ~10 min "default"
- More specific prompts = better targeted content
- Sources must be publicly accessible URLs
- Max ~10 audio overviews per run

Full documentation in the README.md file inside the zip.
