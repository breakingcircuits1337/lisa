#!/usr/bin/env python3
"""
LISA's Smart Memory System v2
Adds priority scoring to markdown memories without losing the story
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime

LISA_DIR = Path(__file__).parent.parent
MEMORY_DIR = LISA_DIR

class SmartMemory:
    def __init__(self):
        self.meta_file = MEMORY_DIR / ".memory_meta.json"
        self.memories = self.load_metadata()
        
    def load_metadata(self):
        """Load memory metadata"""
        if self.meta_file.exists():
            with open(self.meta_file) as f:
                return json.load(f)
        return {}
    
    def save_metadata(self):
        """Save memory metadata"""
        with open(self.meta_file, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def access(self, memory_name):
        """Record access to a memory"""
        if memory_name not in self.memories:
            self.memories[memory_name] = {
                "access_count": 0,
                "last_access": 0,
                "created": time.time()
            }
        self.memories[memory_name]["access_count"] += 1
        self.memories[memory_name]["last_access"] = time.time()
        self.save_metadata()
    
    def get_priority(self, memory_name):
        """Calculate priority score (0-1)"""
        if memory_name not in self.memories:
            return 0.5
        
        m = self.memories[memory_name]
        
        # Factors:
        # 1. Access count (max 10 points)
        access_score = min(m["access_count"] / 10, 1.0) * 0.3
        
        # 2. Recency (max 1 day = 1.0)
        recency = time.time() - m.get("last_access", 0)
        recency_score = max(0, 1 - (recency / 86400)) * 0.4
        
        # 3. Importance (manual + auto)
        importance = m.get("importance", 0.5) * 0.3
        
        return min(access_score + recency_score + importance, 1.0)
    
    def get_layer_priority(self):
        """Get priorities for each memory layer"""
        layers = ["LONG_TERM", "SOUL", "USER", "TOOLS", "AGENTS", "MEDIUM_TERM", "SHORT_TERM"]
        priorities = {}
        for layer in layers:
            priorities[layer] = self.get_priority(layer)
        return priorities
    
    def smart_load(self):
        """Load memories in priority order"""
        priorities = self.get_layer_priority()
        
        # Always load high-priority (>0.7)
        # Query medium (0.3-0.7)  
        # Skip low (<0.3)
        
        loaded = []
        for layer, priority in sorted(priorities.items(), key=lambda x: -x[1]):
            if priority >= 0.3:
                filepath = MEMORY_DIR / f"{layer}.md"
                if filepath.exists():
                    self.access(layer)
                    loaded.append((layer, priority, filepath.read_text()))
        
        return loaded

def main():
    sm = SmartMemory()
    
    print("=" * 60)
    print("LISA SMART MEMORY v2")
    print("=" * 60)
    
    # Show priorities
    print("\nMemory Priorities:")
    priorities = sm.get_layer_priority()
    for layer, priority in sorted(priorities.items(), key=lambda x: -x[1]):
        bar = "█" * int(priority * 20)
        print(f"  {layer:15} [{bar:20}] {priority:.2f}")
    
    # Load in priority order
    print("\n" + "=" * 60)
    print("LOADING MEMORIES (Priority Order)")
    print("=" * 60)
    
    memories = sm.smart_load()
    for layer, priority, content in memories:
        print(f"\n{'='*20} {layer} (p={priority:.2f}) {'='*20}")
        # Show first 200 chars
        print(content[:200] + "...")

if __name__ == "__main__":
    main()
