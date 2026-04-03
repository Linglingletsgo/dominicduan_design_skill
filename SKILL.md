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

**CRITICAL RULE: FULL AUTOMATION & DEEP THINKING**
You must execute all 6 steps continuously and produce markdown artifacts at each step. **DO NOT stop and ask the user for permission to proceed to the next step.** (Pause only in Step 2 if you need the user to manually bypass anti-bot mechanisms). 
In every step, you MUST use extensive `<thinking>` blocks to guarantee **deep philosophical reasoning and maximum branch divergence** before outputting your findings. 

### Step 1: Context Building & Radical Divergence (语境构建与发散)
- **Action**: Conduct keyword divergence based strictly on the user's defined theme and the philosophical context.
- **Divergence**: You MUST deduce 3 to 5 mutually exclusive, radical scheme branches (exploring different extremes of the theory).
- **Structure**: Execute `python scripts/build_project_tree.py "Branch1" "Branch2" ...` substituting your deduced branches. This script guarantees the core directories and multi-branch infrastructure are built instantly and accurately.
- **Document**: Output to `01_brainstorming_and_divergence.md`.

### Step 2: Academic Research & Multimodal Literature Analysis (学术调研与多模态文献解析)
- **Action (Web Search)**: Use your `browser_subagent` to navigate to **https://sci-bot.ru/** for academic literature (theory, philosophy) search and locate specific DOIs based on Step 1. 
- **Action (Automated Web Download)**: 
  - For books: Use the `browser_subagent` to navigate to **https://z-library.sk/**. Log in using the credentials from initialization, simulate manual clicks to search for and download target books.
  - For papers: Use the `browser_subagent` to navigate to **https://www.sci-hub.st/**, enter the DOIs, and download the PDFs.
  - Save all files to `_research_pdfs/`.
- **Fault Tolerance**: If the `browser_subagent` completely fails due to unconquerable captchas, stop, list the required URLs, ask the user to manually download them into `_research_pdfs/`. Pause only for this action.
- **Image Extraction**: Execute `python scripts/extract_pdf_vision.py _research_pdfs _extracted_images` to bulk-extract all graphics from the PDFs automatically. Do NOT hand-write extraction code.
- **Action (Multimodal Analysis)**: Once PDFs are read textually, use `view_file` to directly view the extracted images. Analyze the visual semantics, textures, and structural logic. 
- **Document**: Output to `02_literature_analysis.md`.

### Step 3: Deep Philosophical Deduction & System Architecture (深层哲学推论与系统架构)
- **Deep Thinking**: Spend extensive computational cycles explicitly connecting the literature from Step 2 to the core philosophy (e.g., Posthumanism, Deleuze).
- **Deduction**: Establish the rigorous **Philosophical Deduction (哲学推论)**.
- **Methodology**: Construct the precise **Research Methodology (研究方法论)**.
- **Purpose**: Define the definitive **Research Purpose and Significance (研究目的与意义)**.
- **Document**: Output to `03_philosophical_deduction_and_methodology.md`.

### Step 4: Visual Research & Artist Critique (视觉化调研与艺术家批判)
- **Action**: Investigate existing related art/design projects utilizing the research from Step 3.
- **Critique**: Analyze what exact problems they solved, identify their theoretical/technical flaws, and locate room for innovation.
- **Multimodal Critique**: Download related images to `_inspiration_images/`. Use `view_file` to critically dissect their existing visual languages.
- **Visual Translation**: Strictly deduce the **Visual Translation Language (视觉转化语言)** for our project based on the philosophy.
- **Document**: Output to `04_artist_case_studies_and_visual_language.md`.

### Step 5: Translation Boundaries & Technical Implementation (转化边界与技术推演)
- **Action (Multimodal Synthesis without AIGC)**: Synthesize your deep visual and textual understanding. **Do NOT invoke any AIGC or image generation tools.** 
- **Technical Mapping**: Translate the abstract concepts, visual translation language, and methodologies into precise, actionable technical architectures, systemic rulesets, and material semantics. Provide exact tech integration logic (e.g., hardware constraints, 3D/Physical logic).
- **Iteration**: Outline the **Technical and Visual Implementation Paths (技术与视觉实现)** and map the **Iterative Loops (迭代循环)** required for realization.
- **Document**: Output to `05_technical_implementation_paths.md`.

### Step 6: Master Reorganization & Documentation (全流程重构与母版文档)
- **Action**: Look back across the massive divergent branches, literature, and architectural data. 
- **Organization**: Synthesize everything into a singular, impenetrable master narrative. 
- **Structure**: Reorganize the entire process into a clean, navigable file tree containing all research, critique, and technical data.
- **Document**: Output to `06_master_process_reorganization.md`.

## Red Flags & Common Rationalizations (Avoid These)
- 🚩 **"I should stop after Step X and ask the user to review."** -> **NO.** Execute all 6 steps automatically.
- 🚩 **"I don't need to extract images from PDFs."** -> **NO.** You MUST execute `scripts/extract_pdf_vision.py` to populate `_extracted_images/` for your multimodal analysis.
- 🚩 **"I am stuck downloading the PDF."** -> **SOLUTION**: Attempt browser bypass; if fully blocked, list PDFs and politely halt for the human user to provide them to `_research_pdfs/`.
- 🚩 **"I can just generate an AI image for Step 5."** -> **NO.** AIGC is totally forbidden. Use hardcore textual technical translation.
