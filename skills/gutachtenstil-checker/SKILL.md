---
name: gutachtenstil-checker
description: >
  Prüft juristische Texte auf korrekten Gutachtenstil und gibt strukturiertes Feedback.
  Nutze diesen Skill bei Anfragen wie „prüf den Gutachtenstil", „ist das stilistisch korrekt",
  „schau mal drüber", „Klausur korrigieren", „Hausarbeit überarbeiten" oder wenn ein
  juristischer Text auf die korrekte Einhaltung von Obersatz, Definition, Subsumtion
  und Ergebnis geprüft werden soll.
license: CC-BY-4.0
metadata:
  author: iurskill.md
  version: "1.0"
  rechtsgebiet: Alle Rechtsgebiete
  zielgruppe: Studierende, Referendare
  sprache: Deutsch
---

# Gutachtenstil-Checker

Prüft juristische Texte auf die korrekte Einhaltung des Gutachtenstils und gibt
konkretes, lernförderndes Feedback.

## Hintergrund: Die vier Schritte des Gutachtenstils

```
1. OBERSATZ    → „Fraglich ist, ob P das Eigentum an X erworben hat."
2. DEFINITION  → „Eigentum erwirbt, wer ..."
3. SUBSUMTION  → „Hier hat P ... Damit liegt ... vor."
4. ERGEBNIS    → „P hat das Eigentum erworben."
```

**Abgrenzung zum Urteilsstil:** Der Urteilsstil nennt das Ergebnis zuerst und ist
für Urteile korrekt – in Klausuren und Gutachten ist ausschließlich der Gutachtenstil
zu verwenden.

## Prüfschema

### Strukturfehler erkennen

- Wird das Ergebnis im Obersatz vorweggenommen? (häufigster Fehler)
  - ❌ „P hat das Eigentum erworben, weil ..."
  - ✅ „Fraglich ist, ob P das Eigentum erworben hat."
- Fehlt die Definition?
- Fehlt die Subsumtion (Anwendung der Norm auf den Sachverhalt)?
- Ist das Ergebnis am Ende klar formuliert?

### Sprachliche Marker

| Schritt | Korrekte Formulierungen |
|---|---|
| Obersatz | „Fraglich ist ...", „P könnte ...", „Es könnte ..." |
| Definition | „... liegt vor, wenn ...", „Voraussetzungen sind ..." |
| Subsumtion | „Hier ...", „Im vorliegenden Fall ...", „Dies ist der Fall, da ..." |
| Ergebnis | „Somit ...", „Folglich ...", „Damit hat P ..." |

## Ausgabeformat

```
## Gutachtenstil-Analyse

**Gesamtbewertung:** [✅ Korrekt / ⚠️ Teilweise korrekt / ❌ Überarbeitung nötig]

---

### Gefundene Probleme

| # | Textstelle | Problem | Korrekturvorschlag |
|---|-----------|---------|-------------------|
| 1 | „..." | Ergebnis im Obersatz vorweggenommen | „Fraglich ist, ob ..." |

---

### Überarbeiteter Abschnitt (Beispiel)
[Einen problematischen Absatz im korrekten Gutachtenstil neu formulieren]

---

### Tipps für diese Bearbeiterin / diesen Bearbeiter
[2–3 individuelle Hinweise basierend auf den häufigsten Fehlern im Text]
```

## Anweisungen

1. Text vollständig lesen, bevor Fehler markiert werden.
2. Jeden Prüfungsschritt separat durchgehen (Obersatz, Definition, Subsumtion, Ergebnis).
3. Konkrete Textstellen zitieren – kein allgemeines Feedback.
4. Mindestens einen Abschnitt im korrekten Gutachtenstil umschreiben.
5. Ton lernfördernd halten – Fehler sind Lernchancen.

## Sonderfälle

- **Mischformen:** Wechsel zwischen Gutachten- und Urteilsstil explizit markieren.
- **Kurzgutachten:** Prüfung darf knapper ausfallen, alle vier Schritte bleiben Pflicht.
- **Strafrecht:** Aufbau I. Tatbestand → II. Rechtswidrigkeit → III. Schuld;
  Gutachtenstil gilt auf jeder Ebene.
