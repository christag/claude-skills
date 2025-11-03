# NotebookLM UI Selectors and Troubleshooting

This document provides guidance for updating selectors if NotebookLM's UI changes.

## Common Selector Patterns

The script uses multiple fallback strategies to locate elements:

### Audio Overview Edit Button
```python
# Primary: Look for edit button near "Audio overview" text
page.locator('button:has-text("Audio overview")').locator('button[aria-label*="edit"]')

# Fallback: Look for pencil icon
page.locator('button:has([data-icon="edit"])')
```

### Length Selection
```python
# Look for radio buttons or buttons with "Default" or "Longer" text
page.locator('button:has-text("Longer")')
page.locator('[role="radio"]:has-text("Default")')
```

### Prompt Input Field
```python
# Look for textarea with focus-related placeholder or aria-label
page.locator('textarea[placeholder*="focus"]')
page.locator('textarea[aria-label*="focus"]')
```

### More/Hamburger Menu
```python
# Look for menu button with appropriate aria-label or icon
page.locator('button[aria-label*="More"]')
page.locator('button:has([data-icon="more"])')
```

## Debugging Tips

### Enable Visual Mode
Run without `--headless` to see what the browser is doing:
```bash
python scripts/generate_audio_overviews.py input.json
```

### Inspect Element Selectors
If the script fails to find an element:

1. Open browser DevTools (F12)
2. Use the element picker to inspect the target element
3. Check the element's:
   - Text content
   - ARIA labels
   - Data attributes
   - CSS classes
   - Role attributes

### Common Failure Points

**Sources not loading**: 
- Check that URLs are valid and accessible
- Increase timeout in `wait_for_sources_to_load()`
- Look for error messages in the NotebookLM UI

**Audio overview creation fails**:
- Verify selectors for edit button, length selection, and prompt input
- Check that Google account has NotebookLM access
- Ensure sources have finished loading before creating overviews

**Download fails**:
- Verify selector for more/menu button
- Check that audio overview has finished generating
- Ensure download permissions are set in browser context

## Updating Selectors

When NotebookLM's UI changes, update selectors in `generate_audio_overviews.py`:

1. Identify which function is failing
2. Run in non-headless mode to observe the UI
3. Use DevTools to find new selectors
4. Update the locator code with new selectors
5. Keep fallback strategies for robustness

## Wait Times

The script uses several wait times that may need adjustment:

- `wait_for_sources_to_load()`: Default 120 seconds
- `wait_for_audio_generation()`: Default 600 seconds (10 minutes)
- Various `time.sleep()` calls: 0.5-5 seconds for UI transitions

Increase these if you experience timeout errors.
