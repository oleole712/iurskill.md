# iurskill.md

**Offene Bibliothek wiederverwendbarer Skills für KI-Tools – ausgerichtet auf deutsches Recht.**

Skills sind Markdown-Dateien, die KI-Agenten wie Claude, Open WebUI oder andere Plattformen mit juristischem Fachwissen und strukturierten Arbeitsabläufen ausstatten. Jeder Skill löst eine konkrete, wiederholbare Aufgabe – von der Fristenberechnung bis zur Urteilsanalyse.

→ **Website:** [iurskill.md](https://iurskill.md)

---

## Skills in dieser Bibliothek

| Skill | Rechtsgebiet | Beschreibung |
|---|---|---|
| [Fristenberechnung](skills/fristenberechnung/SKILL.md) | Prozessrecht | Berechnet juristische Fristen nach ZPO, VwGO, StPO, FGO, SGG und ArbGG |
| [Urteilszusammenfassung](skills/urteilszusammenfassung/SKILL.md) | Prozessrecht / Recherche | Erstellt strukturierte Zusammenfassungen von Gerichtsurteilen |
| [Gutachtenstil-Checker](skills/gutachtenstil-checker/SKILL.md) | Ausbildung / Methodik | Prüft juristische Texte auf korrekten Gutachtenstil |

---

## Einen Skill verwenden

1. Öffne den gewünschten Skill-Ordner und lade die `SKILL.md` herunter
2. Lade die Datei in deinen KI-Agenten (z. B. Claude, Open WebUI)
3. Stelle deine juristische Frage – der Agent aktiviert den Skill automatisch

Detaillierte Anleitungen für verschiedene Plattformen findest du auf der [FAQ-Seite](https://iurskill.md/faq).

---

## Eigenen Skill einreichen

Alle Informationen zum Einreichen eines Skills: [CONTRIBUTING.md](CONTRIBUTING.md)

Kurz zusammengefasst:
1. Fork dieses Repository
2. Lege einen neuen Ordner unter `skills/dein-skill-name/` an
3. Füge eine `SKILL.md` nach dem [vorgegebenen Format](#format) hinzu
4. Öffne einen Pull Request

---

## Format

Jede `SKILL.md` beginnt mit einem YAML-Frontmatter:

```yaml
---
name: skill-name
description: >
  Kurze Beschreibung, wann dieser Skill aktiviert werden soll.
  KI-Agenten nutzen dieses Feld, um zu entscheiden, ob der Skill passt.
license: CC-BY-4.0
metadata:
  author: Dein Name
  version: "1.0"
  rechtsgebiet: z. B. Prozessrecht
  sprache: Deutsch
---
```

Der Markdown-Body enthält Anweisungen, Normen, Ausgabeformate und Beispiele.

Die vollständige Spezifikation: [agentskills.io/specification](https://agentskills.io/specification)

---

## Lizenzen

- **Skills (Inhalte):** [CC-BY-4.0](LICENSE-CONTENT) – frei nutzbar mit Namensnennung
- **Code (GitHub Actions, Scripts):** [MIT](LICENSE)

---

## Hinweis

Die Skills in dieser Bibliothek ersetzen keine Rechtsberatung.
