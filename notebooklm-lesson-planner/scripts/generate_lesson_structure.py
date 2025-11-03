#!/usr/bin/env python3
"""
Generate NotebookLM lesson plan structure from JSON input.

This script takes a JSON specification and creates a structured lesson plan
that can be processed to find sources and generate prompts.
"""

import json
import sys
import argparse
from typing import Dict, List
from pathlib import Path


def generate_lesson_plan(
    topic: str,
    learning_areas: List[str],
    listener_context: Dict[str, any] = None,
    target_sources: int = 15
) -> Dict:
    """
    Generate a lesson plan structure.
    
    Args:
        topic: Main topic for the lesson
        learning_areas: List of specific areas to cover
        listener_context: Dict with listener background info
        target_sources: Target number of sources to find (10-20)
    
    Returns:
        Structured lesson plan dict
    """
    if not listener_context:
        listener_context = {}
    
    lesson_plan = {
        'topic': topic,
        'learning_areas': learning_areas,
        'listener_context': listener_context,
        'target_sources': target_sources,
        'sources': [],  # Will be populated later
        'prompts': []   # Will be generated after sources
    }
    
    return lesson_plan


def load_batch_specification(json_path: str) -> List[Dict]:
    """
    Load a batch specification JSON file.
    
    Expected format:
    {
        "lessons": [
            {
                "topic": "Sandwich Making",
                "learning_areas": ["bread", "proteins", "cheeses", "vegetables"],
                "listener_context": {
                    "knows": ["basic cooking", "food safety"],
                    "wants_to_learn": ["gourmet techniques"],
                    "skill_level": "intermediate"
                },
                "target_sources": 15
            },
            ...
        ]
    }
    """
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    return data.get('lessons', [])


def save_lesson_plan(lesson_plan: Dict, output_path: str):
    """Save lesson plan to JSON file."""
    with open(output_path, 'w') as f:
        json.dump(lesson_plan, f, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description='Generate NotebookLM lesson plan structure'
    )
    
    # Single lesson mode
    parser.add_argument(
        '--topic',
        help='Main topic for the lesson'
    )
    parser.add_argument(
        '--areas',
        nargs='+',
        help='Learning areas to cover'
    )
    parser.add_argument(
        '--context',
        help='JSON string with listener context'
    )
    parser.add_argument(
        '--sources',
        type=int,
        default=15,
        help='Target number of sources (default: 15)'
    )
    
    # Batch mode
    parser.add_argument(
        '--batch',
        help='Path to JSON file with multiple lesson specifications'
    )
    
    # Output
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output path for lesson plan(s)'
    )
    
    args = parser.parse_args()
    
    if args.batch:
        # Batch processing
        lessons = load_batch_specification(args.batch)
        
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for i, lesson_spec in enumerate(lessons, 1):
            lesson_plan = generate_lesson_plan(
                topic=lesson_spec['topic'],
                learning_areas=lesson_spec['learning_areas'],
                listener_context=lesson_spec.get('listener_context', {}),
                target_sources=lesson_spec.get('target_sources', 15)
            )
            
            # Create filename from topic
            filename = f"lesson_{i:03d}_{lesson_spec['topic'].lower().replace(' ', '_')}.json"
            output_path = output_dir / filename
            
            save_lesson_plan(lesson_plan, str(output_path))
            print(f"Created: {output_path}")
        
        print(f"\nGenerated {len(lessons)} lesson plans in {output_dir}")
    
    else:
        # Single lesson mode
        if not args.topic or not args.areas:
            parser.error("--topic and --areas required for single lesson mode")
        
        listener_context = {}
        if args.context:
            listener_context = json.loads(args.context)
        
        lesson_plan = generate_lesson_plan(
            topic=args.topic,
            learning_areas=args.areas,
            listener_context=listener_context,
            target_sources=args.sources
        )
        
        save_lesson_plan(lesson_plan, args.output)
        print(f"Created: {args.output}")


if __name__ == '__main__':
    main()
