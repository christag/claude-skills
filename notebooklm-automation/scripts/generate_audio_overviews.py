#!/usr/bin/env python3
"""
NotebookLM Automation - Audio Overview Generator

Automates the creation of multiple audio overviews in Google NotebookLM using Playwright.
"""

import argparse
import json
import sys
import time
from pathlib import Path
from typing import List, Dict
from playwright.sync_api import sync_playwright, Page, TimeoutError as PlaywrightTimeout


def parse_input_file(file_path: str) -> Dict[str, List]:
    """
    Parse the input file containing sources and audio overview prompts.
    
    Expected JSON format:
    {
        "sources": ["url1", "url2", ...],
        "audio_overviews": [
            {
                "prompt": "Focus on X",
                "length": "default"  // or "longer"
            },
            ...
        ]
    }
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    if 'sources' not in data or 'audio_overviews' not in data:
        raise ValueError("Input file must contain 'sources' and 'audio_overviews' keys")
    
    return data


def wait_for_sources_to_load(page: Page, timeout: int = 120):
    """Wait for sources to finish processing in NotebookLM"""
    print("⏳ Waiting for sources to load...")
    # Wait for any loading indicators to disappear
    # This is a heuristic - adjust selectors based on actual NotebookLM UI
    time.sleep(5)  # Initial wait for processing to start
    
    # Check for completion - adjust selector as needed
    max_wait = timeout
    elapsed = 0
    while elapsed < max_wait:
        try:
            # Look for indicators that sources are still loading
            # You may need to adjust this selector based on NotebookLM's actual UI
            loading = page.locator('[role="progressbar"]').count()
            if loading == 0:
                print("✅ Sources loaded successfully")
                return
        except:
            pass
        
        time.sleep(2)
        elapsed += 2
    
    print("⚠️  Timeout waiting for sources to load, proceeding anyway...")


def wait_for_audio_generation(page: Page, timeout: int = 600):
    """Wait for all audio overviews to finish generating"""
    print(f"⏳ Waiting up to {timeout//60} minutes for audio generation to complete...")
    
    max_wait = timeout
    elapsed = 0
    check_interval = 15  # Check every 15 seconds
    
    while elapsed < max_wait:
        try:
            # Look for generating indicators
            # Adjust selectors based on actual NotebookLM UI
            generating = page.locator('text=/Generating|Processing/i').count()
            
            if generating == 0:
                print("✅ All audio overviews generated successfully")
                time.sleep(5)  # Brief pause to ensure UI is stable
                return True
            
            if elapsed % 60 == 0:  # Log every minute
                print(f"   Still generating... ({elapsed//60} minutes elapsed)")
                
        except Exception as e:
            print(f"   Error checking status: {e}")
        
        time.sleep(check_interval)
        elapsed += check_interval
    
    print(f"⏰ Timeout after {timeout//60} minutes. Some overviews may still be generating.")
    return False


def create_audio_overview(page: Page, prompt: str, length: str):
    """Create a single audio overview with specified parameters"""
    print(f"📝 Creating audio overview with prompt: '{prompt[:50]}...'")
    
    try:
        # Click the pencil/edit icon on the audio overview button
        # Adjust selector based on actual NotebookLM UI
        edit_button = page.locator('button:has-text("Audio overview")').or_(
            page.locator('[aria-label*="Audio overview"]')
        ).locator('..').locator('button[aria-label*="edit"], button[aria-label*="customize"]')
        
        if edit_button.count() > 0:
            edit_button.first.click()
        else:
            # Alternative: look for pencil icon
            page.locator('button:has([data-icon="edit"]), button:has([data-icon="pencil"])').first.click()
        
        time.sleep(1)
        
        # Select length (default or longer)
        if length.lower() == "longer":
            print("   Selecting 'Longer' length")
            page.locator('button:has-text("Longer"), [role="radio"]:has-text("Longer")').click()
        else:
            print("   Selecting 'Default' length")
            # Default may already be selected, but click it to be sure
            page.locator('button:has-text("Default"), [role="radio"]:has-text("Default")').click()
        
        time.sleep(0.5)
        
        # Find and fill the prompt text area
        prompt_input = page.locator('textarea[placeholder*="focus"], textarea[aria-label*="focus"]').or_(
            page.locator('textarea').last
        )
        prompt_input.fill(prompt)
        
        time.sleep(0.5)
        
        # Click generate button
        generate_btn = page.locator('button:has-text("Generate")').first
        generate_btn.click()
        
        print("   ✅ Audio overview generation started")
        time.sleep(2)  # Wait for dialog to close
        
    except PlaywrightTimeout as e:
        print(f"   ⚠️  Timeout: {e}")
        raise
    except Exception as e:
        print(f"   ❌ Error creating audio overview: {e}")
        raise


def download_audio_overview(page: Page, index: int) -> bool:
    """Download a single audio overview"""
    print(f"💾 Downloading audio overview #{index + 1}...")
    
    try:
        # Find all audio overview entries
        audio_entries = page.locator('[data-testid="audio-overview"], .audio-overview-item').all()
        
        if index >= len(audio_entries):
            print(f"   ⚠️  Audio overview #{index + 1} not found")
            return False
        
        entry = audio_entries[index]
        
        # Click the more/hamburger menu
        more_button = entry.locator('button[aria-label*="More"], button[aria-label*="menu"]').or_(
            entry.locator('button:has([data-icon="more"])').or_(
                entry.locator('button').last
            )
        )
        more_button.click()
        
        time.sleep(0.5)
        
        # Click download button
        download_button = page.locator('button:has-text("Download"), [role="menuitem"]:has-text("Download")').first
        
        # Set up download handler
        with page.expect_download() as download_info:
            download_button.click()
        
        download = download_info.value
        filename = download.suggested_filename
        download.save_as(f"/home/claude/{filename}")
        
        print(f"   ✅ Downloaded: {filename}")
        return True
        
    except Exception as e:
        print(f"   ❌ Error downloading audio overview #{index + 1}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Generate multiple audio overviews in NotebookLM'
    )
    parser.add_argument(
        'input_file',
        help='JSON file containing sources and audio overview prompts'
    )
    parser.add_argument(
        '--headless',
        action='store_true',
        help='Run browser in headless mode'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=600,
        help='Timeout in seconds for audio generation (default: 600 = 10 minutes)'
    )
    
    args = parser.parse_args()
    
    # Parse input file
    try:
        data = parse_input_file(args.input_file)
        sources = data['sources']
        audio_overviews = data['audio_overviews']
        
        print(f"📋 Loaded {len(sources)} sources and {len(audio_overviews)} audio overview prompts")
    except Exception as e:
        print(f"❌ Error parsing input file: {e}")
        sys.exit(1)
    
    # Launch browser
    with sync_playwright() as p:
        print("🌐 Launching browser...")
        browser = p.chromium.launch(headless=args.headless)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Navigate to NotebookLM
            print("📂 Opening NotebookLM...")
            page.goto('https://notebooklm.google.com')
            page.wait_for_load_state('networkidle')
            
            # You may need to handle Google sign-in here
            # The script assumes you're already signed in or will handle it manually
            time.sleep(3)
            
            # Click create new notebook
            print("➕ Creating new notebook...")
            create_button = page.locator('button:has-text("New"), button:has-text("Create")').first
            create_button.click()
            time.sleep(2)
            
            # Add sources
            print(f"📎 Adding {len(sources)} sources...")
            
            # Click website/URL button
            website_button = page.locator('button:has-text("Website"), button:has-text("URL")').first
            website_button.click()
            time.sleep(1)
            
            # Add each source
            for i, source in enumerate(sources):
                print(f"   Adding source {i+1}/{len(sources)}: {source}")
                url_input = page.locator('input[type="url"], input[placeholder*="URL"], textarea').first
                url_input.fill(source)
                
                # Submit/add the source
                add_button = page.locator('button:has-text("Add"), button:has-text("Insert")').first
                add_button.click()
                time.sleep(1)
                
                # If not the last source, may need to click add again
                if i < len(sources) - 1:
                    try:
                        website_button = page.locator('button:has-text("Website"), button:has-text("URL")').first
                        website_button.click(timeout=2000)
                        time.sleep(0.5)
                    except:
                        pass
            
            # Wait for sources to finish loading
            wait_for_sources_to_load(page, timeout=120)
            
            # Create audio overviews
            print(f"\n🎙️  Creating {len(audio_overviews)} audio overviews...")
            for i, overview in enumerate(audio_overviews):
                prompt = overview.get('prompt', '')
                length = overview.get('length', 'default')
                
                # Validate length
                if length.lower() not in ['default', 'longer']:
                    print(f"   ⚠️  Invalid length '{length}', using 'default'")
                    length = 'default'
                
                try:
                    create_audio_overview(page, prompt, length)
                except Exception as e:
                    print(f"   ⚠️  Failed to create audio overview {i+1}: {e}")
                    continue
                
                time.sleep(2)  # Brief pause between creations
            
            # Wait for all audio overviews to generate
            print(f"\n⏳ Waiting for audio generation to complete...")
            generation_complete = wait_for_audio_generation(page, timeout=args.timeout)
            
            if not generation_complete:
                print("⚠️  Proceeding to download despite timeout...")
            
            # Download all audio overviews
            print(f"\n💾 Downloading {len(audio_overviews)} audio overviews...")
            successful_downloads = 0
            
            for i in range(len(audio_overviews)):
                if download_audio_overview(page, i):
                    successful_downloads += 1
                time.sleep(2)  # Brief pause between downloads
            
            print(f"\n✅ Complete! Downloaded {successful_downloads}/{len(audio_overviews)} audio overviews")
            print(f"📁 Files saved to: /home/claude/")
            
        except Exception as e:
            print(f"\n❌ Error during execution: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
        
        finally:
            # Keep browser open briefly in case manual intervention is needed
            if not args.headless:
                print("\n⏸️  Browser will close in 5 seconds...")
                time.sleep(5)
            
            browser.close()


if __name__ == '__main__':
    main()
