#!/usr/bin/env python3
"""
Test script to verify the workflow runs correctly locally
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from workflow import sequential_workflow
    print("✅ Successfully imported workflow")
    
    # Run the workflow
    print("🚀 Running sequential workflow...")
    result = sequential_workflow()
    
    print("✅ Workflow completed successfully!")
    print(f"📊 Final result: {result}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 Make sure to install requirements: pip install -r requirements.txt")
    sys.exit(1)
    
except Exception as e:
    print(f"❌ Error running workflow: {e}")
    sys.exit(1)
