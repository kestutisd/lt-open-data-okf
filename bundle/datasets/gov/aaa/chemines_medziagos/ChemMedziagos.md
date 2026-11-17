---
type: Table
title: "ChemMedziagos — Cheminės medžiagos / mišiniai"
description: "Spinta table datasets/gov/aaa/chemines_medziagos/ChemMedziagos (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/chemines_medziagos/ChemMedziagos"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/chemines_medziagos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemines_medziagos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ChemMedziagos — Cheminės medžiagos / mišiniai

- **Model:** `datasets/gov/aaa/chemines_medziagos/ChemMedziagos`[^manifest]
- **Dataset:** [datasets/gov/aaa/chemines_medziagos](../chemines_medziagos.md) (`datasets/gov/aaa/chemines_medziagos`)
- **Manifest CSV:** [datasets/gov/aaa/chemines_medziagos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemines_medziagos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/chemines_medziagos/ChemMedziagos`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `cas_nr` | `string` | — | `4` | `open` | — | Medžiagos CAS numeris | Cheminių medžiagų santrumpų tarnybos suteiktas registracijos numeris |
| `pubchem` | `url` | — | `4` | `open` | — | Cheminės medžiagos informacija PubChem | PubChem duomenų bazės paieškos rezultatai pagal CAS nr. |
| `nist` | `url` | — | `4` | `open` | — | Cheminės medžiagos informacija NIST | NIST duomenų bazės paieškos rezultatai pagal CAS nr. |
| `eb_nr` | `string` | — | `4` | `open` | — | Medžiagos EB numeris | EINECS, ELINCS arba NLP numeris, oficialus cheminės medžiagos numeris Europos Sąjungoje (pagal 2008 m. gruodžio 16 d. Europos Parlamento ir Tarybos reglamento (EB) Nr. 1272/2008 dėl cheminių medžiagų ir mišinių klasifikavimo, ženklinimo ir pakavimo, iš dalies keičiančio ir panaikinančio direktyvas 67/548/EEB bei 1999/45/EB ir iš dalies keičiančio Reglamentą (EB) Nr. 1907/2006) VI priedą). EB aprašas: https://echa.europa.eu/lt/information-on-chemicals/ec-inventory |
| `pavadinimas` | `string` | — | `2` | `open` | — | Cheminės medžiagos pavadinimas | — |
| `kiekis` | `number` | `t` | `4` | `open` | — | Kiekis tonomis | — |
| `veiksmas` | `string` | — | `4` | `open` | — | Veiksmas | — |
| `pav_frazes` | `string` | — | `2` | `open` | — | Pavojingumo frazės | Pavojingumo frazės su paaiškinimais: https://ec.europa.eu/taxation_customs/dds2/SAMANCTA/LT/Safety/HP_LT.htm |
| `metai` | `integer` | — | `2` | `open` | — | Dokumento (ataskaitos) atsiskaitymo metai | Nuo 2017 m. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `"EK"` | — | — | Eksportuota | — |
| `veiksmas` | `"SU"` | — | — | Sunaudota | — |
| `veiksmas` | `"IS"` | — | — | Išplatinta (parduota) | — |
| `veiksmas` | `"PA"` | — | — | Pagaminta | — |
| `veiksmas` | `"IM"` | — | — | Importuota | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/chemines_medziagos.csv
