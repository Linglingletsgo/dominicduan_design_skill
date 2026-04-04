#!/usr/bin/env python3
import os
import sys

def build_tree(theme, branches):
    clean_theme = "".join(c if c.isalnum() else "_" for c in theme).strip("_")
    if not clean_theme:
        clean_theme = "Project_Root"
        
    base_dirs = [
        f"{clean_theme}/_research_pdfs",
        f"{clean_theme}/_extracted_images",
        f"{clean_theme}/_inspiration_images"
    ]
    
    # Create base infra
    for d in base_dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created base dir: {d}/")
        
    # Create branches
    for idx, branch in enumerate(branches, 1):
        clean_name = "".join(c if c.isalnum() else "_" for c in branch).strip("_")
        branch_path = f"{clean_theme}/schemes/branch_{idx}_{clean_name}"
        os.makedirs(branch_path, exist_ok=True)
        print(f"Created branch path: {branch_path}/")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/build_project_tree.py 'ProjectTheme' 'Branch1' 'Branch2' ...")
        sys.exit(1)
        
    theme = sys.argv[1]
    branches = sys.argv[2:]
    build_tree(theme, branches)
