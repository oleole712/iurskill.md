---
name: urteilszusammenfassung
description: >
  Erstellt eine strukturierte, juristisch präzise Zusammenfassung eines deutschen Gerichtsurteils
  oder Beschlusses. Nutze diesen Skill bei Anfragen wie „fass das Urteil zusammen",
  „was hat das Gericht entschieden", „Leitsatz erstellen" oder wenn ein PDF oder Text
  einer gerichtlichen Entscheidung vorliegt und analysiert werden soll.
license: CC-BY-4.0
metadata:
  author: iurskill.md
  version: "1.0"
  rechtsgebiet: Alle Rechtsgebiete
  sprache: Deutsch
---

# Urteilszusammenfassung

Erstellt strukturierte Zusammenfassungen von Gerichtsurteilen und -beschlüssen für
deutschsprachige Juristinnen und Juristen.

## Ausgabeformat

```
## Urteilszusammenfassung

**Gericht & Aktenzeichen:** [z. B. BGH, Az. XII ZR 123/22]
**Datum:** [Entscheidungsdatum]
**Rechtsgebiet:** [z. B. Familienrecht, Mietrecht, Strafrecht]

---

### 1. Leitsatz (selbst formuliert)
[1–3 prägnante Sätze, die den Kern der Entscheidung erfassen]

### 2. Tatbestand
[Sachverhalt: Wer hat wen wegen was verklagt? Welche Vorinstanzen gab es?]

### 3. Entscheidungsgründe
[Zentrale rechtliche Argumentation; welche Normen wurden angewandt?]

### 4. Tenor
[Was hat das Gericht konkret entschieden?]

### 5. Praktische Bedeutung
[Warum ist dieses Urteil relevant? Auswirkungen auf die Rechtspraxis?]

### 6. Einschlägige Normen
[Liste der zitierten Gesetze und Paragraphen]
```

## Anweisungen

1. Liegt das Urteil als PDF vor, extrahiere zunächst den Text vollständig.
2. Identifiziere das Rechtsgebiet und passe die Fachterminologie an.
3. Formuliere den Leitsatz eigenständig in 1–3 Sätzen – kein wörtliches Zitat.
4. Nenne alle einschlägigen Paragraphen mit Gesetz (z. B. § 242 BGB, § 823 Abs. 1 BGB).
5. Halte die Zusammenfassung auf 300–600 Wörter, je nach Komplexität.
6. Trenne Tatbestand und Entscheidungsgründe klar voneinander.

## Qualitätskriterien

- Leitsatz ist eigenständig formuliert
- Tatbestand und Entscheidungsgründe sind klar getrennt
- Alle relevanten Rechtsnormen sind genannt
- Praktische Bedeutung ist bewertet, nicht nur beschrieben

## Zu vermeiden

- Den Tatbestand wörtlich wiederholen
- Entscheidungsgründe und Tenor vermischen
- Normen nennen ohne Erklärung ihrer Relevanz
