# Skill einreichen

Vielen Dank für dein Interesse, zur iurskill.md-Bibliothek beizutragen. Diese Anleitung erklärt, wie du einen neuen Skill einreichst oder einen bestehenden verbesserst.

---

## Voraussetzungen

- Ein GitHub-Konto
- Grundkenntnisse in Markdown
- Fachwissen im jeweiligen Rechtsgebiet

---

## Schritt-für-Schritt

### 1. Repository forken

Klicke oben rechts auf **Fork**, um eine eigene Kopie des Repositories zu erstellen.

### 2. Ordner anlegen

Lege unter `skills/` einen neuen Ordner an. Der Ordnername:
- ist kleingeschrieben
- enthält nur Buchstaben, Zahlen und Bindestriche
- beschreibt den Skill prägnant

**Beispiel:** `skills/vertragspruefung/`

### 3. SKILL.md erstellen

Erstelle eine `SKILL.md` im neuen Ordner. Die Datei muss mit einem YAML-Frontmatter beginnen:
```yaml
---
name: skill-name
description: >
  Kurze Beschreibung, wann dieser Skill aktiviert werden soll (max. 200 Zeichen).
  KI-Agenten nutzen dieses Feld, um zu entscheiden, ob der Skill passt.
license: CC-BY-4.0
metadata:
  author: Dein Name oder GitHub-Handle
  version: "1.0"
  rechtsgebiet: z. B. Vertragsrecht
  sprache: Deutsch
---
```

Der Markdown-Body enthält:
- Kurzbeschreibung des Skills
- Anweisungen für den Agenten
- Normen, Tabellen, Ausgabeformate
- Beispiele (empfohlen)

### 4. Pull Request öffnen

Sobald dein Skill fertig ist:
1. Committe deine Änderungen
2. Gehe zu deinem Fork auf GitHub
3. Klicke auf **Compare & pull request**
4. Fülle die Pull-Request-Vorlage aus
5. Reiche den PR ein

---

## Qualitätskriterien

Ein guter Skill:

- **löst eine konkrete, wiederholbare Aufgabe** – kein „allgemeiner Rechtsratgeber"
- **hat eine präzise `description`** – der Agent muss wissen, wann er den Skill einsetzen soll
- **benennt das Ausgabeformat** – strukturierte Ergebnisse sind besser als Fließtext
- **verweist auf Normen** – Paragraphen und Gesetze machen den Skill verlässlich
- **enthält einen Haftungshinweis** – Skills ersetzen keine Rechtsberatung

---

## Bestehenden Skill verbessern

Verbesserungen an bestehenden Skills sind ausdrücklich willkommen. Bitte beschreibe im Pull Request, was du geändert hast und warum.

Wichtig: Inhaltliche Änderungen an einem veröffentlichten Skill werden als neue Version behandelt. Das `version`-Feld im Frontmatter ist entsprechend hochzuzählen.

---

## Verhaltenskodex

Bitte bleibe sachlich und konstruktiv. Ziel ist eine Bibliothek, die Juristen praktisch nützt.

---

## Fragen?

Öffne ein [Issue](../../issues) oder schreibe über das Kontaktformular auf [iurskill.md](https://iurskill.md).
