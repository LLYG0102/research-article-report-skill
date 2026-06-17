#!/usr/bin/env python3
"""Lightweight repository checks for the research-article-report skill."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/model-report-style.md",
    "references/reproducibility-extraction.md",
    "templates/reading_report_template.md",
    "templates/figure_summary_template.md",
    "templates/method_extraction_template.md",
    "templates/wetlab_cost_template.md",
    "checklists/report_quality_checklist.md",
    "checklists/cost_estimation_checklist.md",
    "checklists/figure_location_checklist.md",
    "prompts/user_prompt_template.md",
    "schemas/report_outline.yaml",
    "metadata.json",
]

REQUIRED_SKILL_PHRASES = [
    "逐图",
    "复现",
    "成本估计",
    "references/model-report-style.md",
    "references/reproducibility-extraction.md",
    "binding",
    "experimental structure",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    missing_phrases = [phrase for phrase in REQUIRED_SKILL_PHRASES if phrase not in skill]
    if missing_phrases:
        print("SKILL.md is missing required phrases:")
        for phrase in missing_phrases:
            print(f"- {phrase}")
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8").strip()
    if len(readme.splitlines()) > 6:
        print("README.md should stay concise.")
        return 1

    print("Skill project validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
