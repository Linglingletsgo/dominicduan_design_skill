#!/usr/bin/env python3
import os
import sys

def build_tree(branches):
    base_dirs = [
        "_research_pdfs",
        "_extracted_images",
        "_inspiration_images"
    ]
    
    # Create base infra
    for d in base_dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created base dir: {d}/")
        
    # Create branches
    for idx, branch in enumerate(branches, 1):
        clean_name = "".join(c if c.isalnum() else "_" for c in branch).strip("_")
        branch_path = f"schemes/branch_{idx}_{clean_name}"
        os.makedirs(branch_path, exist_ok=True)
        print(f"Created branch path: {branch_path}/")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_project_tree.py 'Branch1' 'Branch2' ...")
        sys.exit(1)
    build_tree(sys.argv[1:])
