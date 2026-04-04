---
name: dominicduan-design-skill
description: Use when initiating a rigorous identity related art project, when requiring full conceptual deduction from theoretical bases to technical implementation, or when explicitly asked to invoke dominicduan_design_skill.
---

# Dominic Duan Design Skill

## Overview
A rigorous, fully-automated modern art design workflow. It bridges deep theoretical/philosophical contexts (defaulting to Posthumanism, Deleuze/Guattari, Haraway, Zuboff, Harari) with conceptual deduction, preliminary visualization, and technical implementation.

## When to Use
- When explicitly asked to use `dominicduan_design_skill` or `dominicduan-design-skill`.
- When starting an identity related interdisciplinary art design project requiring deep academic grounding.
- When you need to deduce an artistic design workflow systematically based on philosophical literature.

## Initialization & Default Parameters
Before executing the workflow, you MUST present the defaults and ask the user for required inputs:
1. Present the default philosophical parameters: *Deleuze and Guattari's "A Thousand Plateaus", Donna J. Haraway's "Staying with the Trouble", Shoshana Zuboff's "The Age of Surveillance Capitalism", and Yuval Noah Harari's "Homo Deus" focusing on Identity and Subjectivity in a Posthumanism context.*
2. Ask the user three mandatory questions: 
   - **"What is the specific theme or limitation for the current project?"** (Crucial for bounding the design).
   - **"Do you want to modify any of the default philosophical parameters?"**
   - **"Please provide your Z-Library username and password so I can automatically download reference materials for me."**
3. Once the user replies with the theme, credentials, and optional modifications, **proceed immediately** into the automated workflow.

## The 6-Step Fully Automated Workflow

**CRITICAL RULE: TREE-STRUCTURED DOCUMENTATION MATRIX**
From Step 2 onwards, you MUST NOT write generic global documents. You must loop over each branch deduced in Step 1, executing deep reasoning and generating specific outputs documents **INSIDE each respective `schemes/branch_{X}/` folder**. This creates a massive, divergent matrix of research files. Ensure absolutely **no empty folders** remain at the end of the project. Do not pause execution unless requiring human fallback.

### Step 1: Context Building & Radical Divergence (语境构建与发散)
- **Action**: Conduct keyword divergence based strictly on the defined theme and philosophy.
- **Divergence**: You MUST deduce 3 to 5 mutually exclusive, radical scheme branches.
- **Structure**: Execute `python scripts/build_project_tree.py "[Branch1]" "[Branch2]" ...` substituting your deduced names. This automatically scaffolds the exact `schemes/branch_X/` architecture.
- **Document**: Output `01_brainstorming_and_divergence.md` at the root directory.

### Step 2: Academic Research (Shared) & Branch-Specific Multimodal Analysis
- **Action (Shared Research)**: Use `browser_subagent` to download DOIs/books to `_research_pdfs/`. Pause ONLY if captchas completely block you, asking the user to manually provide the PDFs.
- **Image Extraction (Shared)**: Execute `python scripts/extract_pdf_vision.py _research_pdfs _extracted_images`.
- **Branch-Specific Analysis**: For EVERY branch deduced in Step 1, use `view_file` to read the global PDFs and extracted images precisely through the theoretical lens of *that specific branch*.
- **Document**: Output `02_literature_analysis.md` **INSIDE each respective branch's folder** (e.g., `schemes/branch_1_A/02_literature_analysis.md`).

### Step 3: Branch-Specific Deep Philosophical Deduction & System Architecture
- **Deep Thinking**: Provide extensive `<thinking>` reasoning for each branch independently. 
- **Deduction**: Establish the rigorous Philosophical Deduction, Research Methodology, and Research Purpose specifically tailored to the divergent bounds of each branch.
- **Document**: Output `03_philosophical_deduction_and_methodology.md` **INSIDE each branch's folder**.

### Step 4: Branch-Specific Visual Research & Artist Critique
- **Action**: For each branch, investigate existing related art projects.
- **Multimodal Critique**: Download shared inspiration to `_inspiration_images/`. Critique them (`view_file`) based on the specific branch's philosophical angle.
- **Visual Translation**: Deduce a unique **Visual Translation Language (视觉转化语言)** for each branch individually.
- **Document**: Output `04_artist_case_studies_and_visual_language.md` **INSIDE each branch's folder**.

### Step 5: Branch-Specific Translation Boundaries & Technical Implementation
- **Action**: Synthesize the visual/textual understanding for each branch. **NO AIGC allowed.** 
- **Technical Mapping**: Translate each branch into exact, actionable technical architectures, systemic rulesets, and physical/3D logic separately.
- **Iteration Paths**: Provide detailed iterative implementation loops specific to each branch's logic.
- **Document**: Output `05_technical_implementation_paths.md` **INSIDE each branch's folder**.

### Step 6: Master Reorganization & Root Finalization
- **Action**: Look backward across the fully populated tree matrix (`schemes/`).
- **Organization**: Ensure NO empty folders were created. If any directory lacks documents, populate them.
- **Synthesis**: Compare the branches and synthesize everything into a singular master narrative describing the holistic divergent logic of the project.
- **Document**: Output `06_master_process_reorganization.md` at the root directory.

## Red Flags & Common Rationalizations (Avoid These)
- 🚩 **"I should stop after Step X and ask the user to review."** -> **NO.** Execute all 6 steps automatically.
- 🚩 **"I don't need to extract images from PDFs."** -> **NO.** You MUST execute `scripts/extract_pdf_vision.py` to populate `_extracted_images/` for your multimodal analysis.
- 🚩 **"I am stuck downloading the PDF."** -> **SOLUTION**: Attempt browser bypass; if fully blocked, list PDFs and politely halt for the human user to provide them to `_research_pdfs/`.
- 🚩 **"I can just generate an AI image for Step 5."** -> **NO.** AIGC is totally forbidden. Use hardcore textual technical translation.
