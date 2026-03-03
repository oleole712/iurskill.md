#!/usr/bin/env python3
"""
Validiert alle SKILL.md-Dateien unter skills/ auf korrektes YAML-Frontmatter.
Pflichtfelder: name, description, license, metadata.author, metadata.version
"""

import os
import sys
import yaml

SKILLS_DIR = "skills"
REQUIRED_TOP = ["name", "description", "license", "metadata"]
REQUIRED_META = ["author", "version"]
MAX_DESCRIPTION_LENGTH = 200
ERRORS = []


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return None, "Kein YAML-Frontmatter gefunden (Datei muss mit '---' beginnen)"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Frontmatter nicht korrekt geschlossen (fehlendes '---')"

    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"Ungültiges YAML: {e}"

    return data, None


def validate_skill(path):
    errors = []
    data, parse_error = parse_frontmatter(path)

    if parse_error:
        errors.append(parse_error)
        return errors

    for field in REQUIRED_TOP:
        if field not in data or not data[field]:
            errors.append(f"Pflichtfeld fehlt oder leer: '{field}'")

    if "description" in data and data["description"]:
        desc = str(data["description"]).strip()
        if len(desc) > MAX_DESCRIPTION_LENGTH:
            errors.append(
                f"'description' zu lang: {len(desc)} Zeichen (max. {MAX_DESCRIPTION_LENGTH})"
            )

    if "metadata" in data and isinstance(data["metadata"], dict):
        for field in REQUIRED_META:
            if field not in data["metadata"] or not data["metadata"][field]:
                errors.append(f"Pflichtfeld fehlt oder leer: 'metadata.{field}'")
    elif "metadata" in data:
        errors.append("'metadata' muss ein Objekt sein (key: value Paare)")

    if "license" in data and data["license"] != "CC-BY-4.0":
        errors.append(
            f"Lizenz '{data['license']}' nicht erlaubt – nur 'CC-BY-4.0' wird akzeptiert"
        )

    return errors


def main():
    if not os.path.isdir(SKILLS_DIR):
        print(f"Ordner '{SKILLS_DIR}' nicht gefunden.")
        sys.exit(1)

    skill_files = []
    for root, _, files in os.walk(SKILLS_DIR):
        for file in files:
            if file == "SKILL.md":
                skill_files.append(os.path.join(root, file))

    if not skill_files:
        print("Keine SKILL.md-Dateien gefunden.")
        sys.exit(0)

    all_valid = True
    for path in sorted(skill_files):
        errors = validate_skill(path)
        if errors:
            all_valid = False
            print(f"\n❌ {path}")
            for error in errors:
                print(f"   • {error}")
        else:
            print(f"✅ {path}")

    if not all_valid:
        print("\nValidierung fehlgeschlagen. Bitte die obigen Fehler beheben.")
        sys.exit(1)
    else:
        print(f"\nAlle {len(skill_files)} SKILL.md-Datei(en) sind gültig.")


if __name__ == "__main__":
    main()
