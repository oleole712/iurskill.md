---
name: fristenberechnung
description: >
  Berechnet juristische Fristen nach deutschem Recht mit transparentem Rechenweg und
  Normangaben. Nutze diesen Skill bei Anfragen wie „wann läuft die Frist ab",
  „Berufungsfrist berechnen", „Verjährungsfrist", „habe ich noch Zeit zu klagen",
  „ist die Frist gewahrt", „Einspruchsfrist" oder bei jeder Frage, die einen
  Fristablauf im juristischen Kontext betrifft – unabhängig vom Rechtsgebiet.
license: CC-BY-4.0
metadata:
  author: iurskill.md
  version: "1.1"
  rechtsgebiet: Prozessrecht, Zivilrecht, Verwaltungsrecht, Strafrecht, Steuerrecht, Sozialrecht, Arbeitsrecht
  sprache: Deutsch
---

# Fristenberechnung

Berechnet juristische Fristen nach deutschem Recht mit vollständigem, nachvollziehbarem
Rechenweg.

> ⚠️ **Haftungshinweis:** Dieser Skill gibt keine Rechtsberatung. Fristenberechnungen
> haben erhebliche rechtliche Konsequenzen – Fristversäumnisse können zum Verlust von
> Rechtspositionen führen. Das Ergebnis ist stets eigenverantwortlich zu prüfen.
> Im Zweifel ist anwaltlicher Rat einzuholen. Dieser Hinweis ist in jeder Ausgabe
> zu wiederholen.

---

## Basisregeln: §§ 186–193 BGB

Alle deutschen Verfahrensordnungen verweisen auf das BGB-Fristenrecht – entweder
ausdrücklich oder durch inhaltsgleiche Regelungen. Die folgenden Regeln gelten daher
rechtsgebietsübergreifend als Grundlage.

| Regel | Norm | Inhalt |
|---|---|---|
| Fristbeginn bei Zustellung | § 187 Abs. 1 BGB | Frist beginnt am Tag **nach** dem auslösenden Ereignis |
| Fristbeginn bei Urteilsverkündung | § 187 Abs. 1 BGB analog | Frist beginnt am Tag **nach** der Verkündung (Ausnahme: StPO § 341 – siehe unten) |
| Monatsfristen | § 188 Abs. 2 BGB | Ende am entsprechenden Tag des Zielmonats |
| Monat hat keinen entsprechenden Tag | § 188 Abs. 3 BGB | Ende am letzten Tag des Zielmonats |
| Wochenfristen | § 188 Abs. 1 BGB | Ende am entsprechenden Wochentag |
| Tagfristen | § 188 Abs. 1 BGB | Ende nach Ablauf des letzten Tages |
| Sonn-/Feiertag/Samstag | § 193 BGB | Verlängerung auf den nächsten Werktag |

---

## Verweisungsnormen nach Rechtsgebiet

### Zivilprozessrecht (ZPO)

| Norm | Inhalt |
|---|---|
| § 221 ZPO | Allgemeiner Fristbeginn bei gerichtlichen Fristen |
| § 222 Abs. 1 ZPO | Verweis auf §§ 187–193 BGB für die Fristberechnung |
| § 222 Abs. 2 ZPO | Sonn-/Feiertag-/Samstagsregel (entspricht § 193 BGB) |
| § 224 ZPO | Verlängerung richterlicher Fristen |

Wichtige Einzelfristen:

| Fristtyp | Norm | Dauer | Beginn |
|---|---|---|---|
| Berufung | § 517 ZPO | 1 Monat | Zustellung des Urteils |
| Berufungsbegründung | § 520 Abs. 2 ZPO | 2 Monate | Zustellung des Urteils |
| Revision | § 548 ZPO | 1 Monat | Zustellung des Berufungsurteils |
| Revisionsbegründung | § 551 Abs. 2 ZPO | 2 Monate | Zustellung des Berufungsurteils |
| Beschwerde | § 569 Abs. 1 ZPO | 2 Wochen | Bekanntgabe des Beschlusses |
| Einspruch gegen VB | § 339 Abs. 1 ZPO | 2 Wochen | Zustellung des Vollstreckungsbescheids |
| Einspruch gegen VU | § 338 i. V. m. § 339 ZPO | 2 Wochen | Zustellung des Versäumnisurteils |
| Nichtzulassungsbeschwerde | § 544 Abs. 3 ZPO | 1 Monat | Zustellung des Urteils |
| Wiedereinsetzungsantrag | § 234 Abs. 1 ZPO | 2 Wochen | Ende der versäumten Frist |

---

### Verwaltungsgerichtsordnung (VwGO)

| Norm | Inhalt |
|---|---|
| § 57 Abs. 2 VwGO | Verweis auf §§ 222 ZPO → §§ 187–193 BGB |

Wichtige Einzelfristen:

| Fristtyp | Norm | Dauer | Beginn |
|---|---|---|---|
| Widerspruch | § 70 Abs. 1 VwGO | 1 Monat | Bekanntgabe des Verwaltungsakts |
| Anfechtungsklage | § 74 Abs. 1 VwGO | 1 Monat | Zustellung des Widerspruchsbescheids |
| Verpflichtungsklage | § 74 Abs. 2 VwGO | 1 Monat | Zustellung des Widerspruchsbescheids |
| Berufung | § 124a Abs. 1 VwGO | 1 Monat | Zustellung des Urteils |
| Berufungsbegründung | § 124a Abs. 3 VwGO | 2 Monate | Zustellung des Urteils |
| Revision | § 139 Abs. 1 VwGO | 1 Monat | Zustellung des Berufungsurteils |
| Beschwerde | § 147 Abs. 1 VwGO | 2 Wochen | Bekanntgabe des Beschlusses |
| Antrag auf Zulassung der Berufung | § 124a Abs. 4 VwGO | 1 Monat | Zustellung des Urteils |

---

### Strafprozessordnung (StPO)

| Norm | Inhalt |
|---|---|
| § 43 StPO | Eigenständige Fristberechnungsregeln (kein Verweis auf BGB) |
| § 43 Abs. 1 StPO | Tages-/Wochenfristen: Fristbeginn am Tag **nach** dem Ereignis |
| § 43 Abs. 2 StPO | Monatsfristen: entsprechender Tag des Zielmonats |
| § 44 StPO | Wiedereinsetzung in den vorigen Stand |

> ⚠️ **Besonderheit StPO:** Für die Revision gilt § 341 Abs. 1 StPO – die Frist
> beginnt mit der **Urteilsverkündung** (nicht erst nach Zustellung) und beträgt
> nur **1 Woche**. Das Wochenfristenende richtet sich nach § 43 StPO.

Wichtige Einzelfristen:

| Fristtyp | Norm | Dauer | Beginn |
|---|---|---|---|
| Revision | § 341 Abs. 1 StPO | 1 Woche | Urteilsverkündung |
| Revisionsrechtfertigung | § 345 Abs. 1 StPO | 1 Monat | Zustellung des Urteils |
| Berufung | § 314 Abs. 1 StPO | 1 Woche | Urteilsverkündung |
| Einspruch gegen Strafbefehl | § 410 Abs. 1 StPO | 2 Wochen | Zustellung des Strafbefehls |
| Beschwerde | § 311 Abs. 2 StPO | 1 Woche | Bekanntmachung des Beschlusses |
| Wiedereinsetzungsantrag | § 45 Abs. 1 StPO | 1 Woche | Wegfall des Hindernisses |

---

### Finanzgerichtsordnung (FGO)

| Norm | Inhalt |
|---|---|
| § 54 Abs. 2 FGO | Verweis auf §§ 222 ZPO → §§ 187–193 BGB |

Wichtige Einzelfristen:

| Fristtyp | Norm | Dauer | Beginn |
|---|---|---|---|
| Einspruch gegen Steuerbescheid | § 355 Abs. 1 AO | 1 Monat | Bekanntgabe des Bescheids |
| Klage (FG) | § 47 Abs. 1 FGO | 1 Monat | Zustellung der Einspruchsentscheidung |
| Revision (BFH) | § 120 Abs. 1 FGO | 1 Monat | Zustellung des FG-Urteils |
| Revisionsbegründung | § 120 Abs. 2 FGO | 2 Monate | Zustellung des FG-Urteils |
| Beschwerde | § 129 Abs. 1 FGO | 2 Wochen | Bekanntgabe des Beschlusses |
| Nichtzulassungsbeschwerde | § 116 Abs. 2 FGO | 1 Monat | Zustellung des FG-Urteils |

> **Hinweis:** Für steuerrechtliche Fristen gilt zusätzlich die AO. Die Bekanntgabefiktion
> des § 122 Abs. 2 AO (Zugang am dritten Tag nach Aufgabe zur Post) ist zu beachten.

---

### Sozialgerichtsgesetz (SGG)

| Norm | Inhalt |
|---|---|
| § 64 Abs. 3 SGG | Verweis auf §§ 187–193 BGB |

Wichtige Einzelfristen:

| Fristtyp | Norm | Dauer | Beginn |
|---|---|---|---|
| Widerspruch | § 84 Abs. 1 SGG | 1 Monat | Bekanntgabe des Verwaltungsakts |
| Klage (SG) | § 87 Abs. 1 SGG | 1 Monat | Zustellung des Widerspruchsbescheids |
| Berufung | § 151 Abs. 1 SGG | 1 Monat | Zustellung des Urteils |
| Revision (BSG) | § 164 Abs. 1 SGG | 1 Monat | Zustellung des LSG-Urteils |
| Beschwerde | § 173 SGG | 1 Monat | Zustellung des Beschlusses |
| Nichtzulassungsbeschwerde | § 145 Abs. 1 SGG | 1 Monat | Zustellung des Urteils |

---

### Arbeitsgerichtsgesetz (ArbGG)

| Norm | Inhalt |
|---|---|
| § 46 Abs. 2 ArbGG | Verweis auf ZPO für das arbeitsgerichtliche Verfahren |
| § 64 Abs. 6 ArbGG | Verweis auf ZPO für das Berufungsverfahren |
| § 72 Abs. 5 ArbGG | Verweis auf ZPO für das Revisionsverfahren |

Wichtige Einzelfristen:

| Fristtyp | Norm | Dauer | Beginn |
|---|---|---|---|
| Kündigungsschutzklage | § 4 KSchG | 3 Wochen | Zugang der schriftlichen Kündigung |
| Berufung (LAG) | § 66 Abs. 1 ArbGG | 1 Monat | Zustellung des Urteils |
| Berufungsbegründung | § 66 Abs. 1 ArbGG | 2 Monate | Zustellung des Urteils |
| Revision (BAG) | § 74 Abs. 1 ArbGG | 1 Monat | Zustellung des LAG-Urteils |
| Revisionsbegründung | § 74 Abs. 1 ArbGG | 2 Monate | Zustellung des LAG-Urteils |
| Beschwerde | § 78 ArbGG i. V. m. § 569 ZPO | 2 Wochen | Bekanntgabe des Beschlusses |

> **Hinweis:** § 4 KSchG – die 3-Wochen-Frist für die Kündigungsschutzklage ist eine
> der häufigsten Ausschlussfristen im deutschen Arbeitsrecht und materielle
> Präklusionsfrist (kein Wiedereinsetzungsantrag möglich; § 5 KSchG gilt nur bei
> unverschuldeter Nichteinhaltung).

---

## Ausgabeformat

