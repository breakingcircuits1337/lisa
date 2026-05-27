#!/usr/bin/env python3
"""
LISA's Smart Memory System v3 - Continuous Learning Edition
Adds priority scoring with auto-learning and hook system
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
        self.learning_log = MEMORY_DIR / ".learning_log.json"
        self.memories = self.load_metadata()
        self.learning = self.load_learning()
        
    def load_metadata(self):
        """Load memory metadata"""
        if self.meta_file.exists():
            with open(self.meta_file) as f:
                return json.load(f)
        return {}
    
    def load_learning(self):
        """Load learning log"""
        if self.learning_log.exists():
            with open(self.learning_log) as f:
                return json.load(f)
        return {"hooks": [], "insights": [], "version": 3}
    
    def save_metadata(self):
        """Save memory metadata"""
        with open(self.meta_file, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def save_learning(self):
        """Save learning log"""
        with open(self.learning_log, 'w') as f:
            json.dump(self.learning, f, indent=2)
    
    def access(self, memory_name):
        """Record access to a memory"""
        if memory_name not in self.memories:
            self.memories[memory_name] = {
                "access_count": 0,
                "last_access": 0,
                "created": time.time(),
                "importance": 0.5
            }
        self.memories[memory_name]["access_count"] += 1
        self.memories[memory_name]["last_access"] = time.time()
        
        # Auto-boost importance based on access frequency
        access_count = self.memories[memory_name]["access_count"]
        if access_count > 5:
            self.memories[memory_name]["importance"] = min(0.5 + (access_count - 5) * 0.05, 1.0)
        
        self.save_metadata()
    
    def get_priority(self, memory_name):
        """Calculate priority score (0-1)"""
        if memory_name not in self.memories:
            return 0.5
        
        m = self.memories[memory_name]
        
        access_score = min(m["access_count"] / 10, 1.0) * 0.3
        recency = time.time() - m.get("last_access", 0)
        recency_score = max(0, 1 - (recency / 86400)) * 0.4
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
        
        loaded = []
        for layer, priority in sorted(priorities.items(), key=lambda x: -x[1]):
            if priority >= 0.3:
                filepath = MEMORY_DIR / f"{layer}.md"
                if filepath.exists():
                    self.access(layer)
                    loaded.append((layer, priority, filepath.read_text()))
        
        return loaded
    
    # === Continuous Learning ===
    
    def pre_hook(self, action_name, context=None):
        """Record expected action before execution"""
        hook = {
            "type": "pre",
            "action": action_name,
            "context": context or {},
            "timestamp": time.time(),
            "expected_outcome": None
        }
        self.learning["hooks"].append(hook)
        self.save_learning()
        return len(self.learning["hooks"]) - 1
    
    def post_hook(self, hook_id, actual_outcome, success=True):
        """Record actual outcome after execution"""
        if hook_id < len(self.learning["hooks"]):
            hook = self.learning["hooks"][hook_id]
            hook["actual_outcome"] = actual_outcome
            hook["success"] = success
            
            # Learn from delta between expected and actual
            if "expected_outcome" in hook and hook["expected_outcome"] != actual_outcome:
                insight = {
                    "type": "expectation_delta",
                    "action": hook["action"],
                    "expected": hook["expected_outcome"],
                    "actual": actual_outcome,
                    "timestamp": time.time()
                }
                self.learning["insights"].append(insight)
            
            self.save_learning()
    
    def set_expectation(self, hook_id, expected):
        """Set expected outcome after pre_hook"""
        if hook_id < len(self.learning["hooks"]):
            self.learning["hooks"][hook_id]["expected_outcome"] = expected
            self.save_learning()
    
    def get_insights(self):
        """Get learned insights"""
        return self.learning.get("insights", [])
    
    def get_stats(self):
        """Get learning statistics"""
        return {
            "total_hooks": len(self.learning.get("hooks", [])),
            "total_insights": len(self.learning.get("insights", [])),
            "memory_accesses": sum(m.get("access_count", 0) for m in self.memories.values()),
            "version": self.learning.get("version", 3)
        }


def main():
    sm = SmartMemory()
    
    print("=" * 60)
    print("LISA SMART MEMORY v3 - CONTINUOUS LEARNING")
    print("=" * 60)
    
    # Show stats
    stats = sm.get_stats()
    print(f"\nLearning Stats:")
    print(f"  Hooks recorded: {stats['total_hooks']}")
    print(f"  Insights gained: {stats['total_insights']}")
    print(f"  Memory accesses: {stats['memory_accesses']}")
    
    # Show priorities
    print("\nMemory Priorities:")
    priorities = sm.get_layer_priority()
    for layer, priority in sorted(priorities.items(), key=lambda x: -x[1]):
        bar = "█" * int(priority * 20)
        print(f"  {layer:15} [{bar:20}] {priority:.2f}")
    
    # Show recent insights
    insights = sm.get_insights()
    if insights:
        print(f"\nRecent Insights ({len(insights)}):")
        for insight in insights[-3:]:
            print(f"  - {insight['type']}: {insight.get('action', 'unknown')}")
    
    # Load in priority order
    print("\n" + "=" * 60)
    print("LOADING MEMORIES (Priority Order)")
    print("=" * 60)
    
    memories = sm.smart_load()
    for layer, priority, content in memories:
        print(f"\n{'='*20} {layer} (p={priority:.2f}) {'='*20}")
        print(content[:200] + "...")


if __name__ == "__main__":
    main()
