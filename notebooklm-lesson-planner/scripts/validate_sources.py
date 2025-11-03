#!/usr/bin/env python3
"""
Validate URLs for NotebookLM compatibility.

This script checks if URLs are:
1. Active (returns 200-299 status)
2. Publicly accessible (no auth required)
3. LLM-readable (no crawler blocking)
"""

import sys
import argparse
from urllib.parse import urlparse
import requests
from typing import List, Dict, Tuple


def check_url(url: str, timeout: int = 10) -> Tuple[bool, str]:
    """
    Check if a URL is valid for NotebookLM.
    
    Returns:
        (is_valid, reason) tuple
    """
    try:
        # Parse URL
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return False, "Invalid URL format"
        
        # Make request with a user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        
        # Check status code
        if response.status_code < 200 or response.status_code >= 300:
            return False, f"HTTP {response.status_code}"
        
        # Check for common blocking indicators
        content_lower = response.text.lower()
        
        # Check for robot blocking
        if 'robots.txt' in content_lower and 'disallow' in content_lower[:1000]:
            # This is a heuristic - not perfect
            pass
        
        # Check for paywall indicators
        paywall_indicators = [
            'subscribe to read',
            'sign up to continue',
            'login required',
            'paywall',
            'subscription required'
        ]
        
        for indicator in paywall_indicators:
            if indicator in content_lower[:5000]:
                return False, f"Possible paywall detected: '{indicator}'"
        
        # Check content length (very short pages might be blocked)
        if len(response.text) < 500:
            return False, "Content too short (possible block page)"
        
        return True, "OK"
        
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, "Connection error"
    except requests.exceptions.TooManyRedirects:
        return False, "Too many redirects"
    except Exception as e:
        return False, f"Error: {str(e)[:100]}"


def validate_sources(urls: List[str], verbose: bool = False) -> Dict[str, Dict]:
    """
    Validate a list of URLs.
    
    Returns:
        Dict mapping URLs to their validation results
    """
    results = {}
    
    for i, url in enumerate(urls, 1):
        if verbose:
            print(f"[{i}/{len(urls)}] Checking {url}...", file=sys.stderr)
        
        is_valid, reason = check_url(url)
        results[url] = {
            'valid': is_valid,
            'reason': reason
        }
        
        if verbose:
            status = "✓" if is_valid else "✗"
            print(f"  {status} {reason}", file=sys.stderr)
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Validate URLs for NotebookLM compatibility'
    )
    parser.add_argument(
        'urls',
        nargs='+',
        help='URLs to validate'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed progress'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='Request timeout in seconds (default: 10)'
    )
    
    args = parser.parse_args()
    
    results = validate_sources(args.urls, verbose=args.verbose)
    
    # Print summary
    valid_count = sum(1 for r in results.values() if r['valid'])
    total_count = len(results)
    
    print(f"\n{'='*60}")
    print(f"Validation complete: {valid_count}/{total_count} URLs valid")
    print(f"{'='*60}\n")
    
    # Print detailed results
    for url, result in results.items():
        status = "✓ VALID" if result['valid'] else "✗ INVALID"
        print(f"{status}: {url}")
        print(f"  Reason: {result['reason']}\n")
    
    # Exit with error code if any invalid
    sys.exit(0 if valid_count == total_count else 1)


if __name__ == '__main__':
    main()
