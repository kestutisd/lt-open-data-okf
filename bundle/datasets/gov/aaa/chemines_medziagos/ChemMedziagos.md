---
type: Table
title: "ChemMedziagos — Cheminės medžiagos / mišiniai"
description: "Spinta table datasets/gov/aaa/chemines_medziagos/ChemMedziagos (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/chemines_medziagos/ChemMedziagos"
tags: [gov, aaa, chemmedziagos, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemines_medziagos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/chemines_medziagos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1560/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/chemines_medziagos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ChemMedziagos — Cheminės medžiagos / mišiniai

- **Model:** `datasets/gov/aaa/chemines_medziagos/ChemMedziagos`[^manifest]
- **Dataset:** [Lietuvos rinkoje esančios pavojingos cheminės medžiagos](../chemines_medziagos.md) (`datasets/gov/aaa/chemines_medziagos`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/chemines_medziagos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemines_medziagos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/chemines_medziagos/ChemMedziagos` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/chemines_medziagos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemines_medziagos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/chemines_medziagos (https://data.gov.lt/datasets/1560/)
