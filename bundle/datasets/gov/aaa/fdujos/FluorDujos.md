---
type: Table
title: "FluorDujos — Fluorintų šiltnamio efektą sukeliančių dujų ir ozono sluoksnį ardančių medžiagų duomenys"
description: "https://aaa.lrv.lt/lt/veiklos-sritys/klimato-kaita/fluorintos-siltnamio-efekta-sukeliancios-dujos"
resource: "https://get.data.gov.lt/datasets/gov/aaa/fdujos/FluorDujos"
tags: [gov, aaa, fluordujos, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/fdujos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/fdujos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1671/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/fdujos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# FluorDujos — Fluorintų šiltnamio efektą sukeliančių dujų ir ozono sluoksnį ardančių medžiagų duomenys

https://aaa.lrv.lt/lt/veiklos-sritys/klimato-kaita/fluorintos-siltnamio-efekta-sukeliancios-dujos[^manifest]

- **Model:** `datasets/gov/aaa/fdujos/FluorDujos`[^manifest]
- **Dataset:** [Fluorintų šiltnamio efektą sukeliančių dujų duomenys](../fdujos.md) (`datasets/gov/aaa/fdujos`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/fdujos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/fdujos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/fdujos/FluorDujos` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `kodas` | `string` | — | `2` | `open` | — | Fluorintų dujų ir ozono sluoksnį ardančių medžiagų (OAM) mišinio kodas | — |
| `trumpinys` | `string` | — | `2` | `open` | — | Fluorintų dujų ar ozono sluoksnį ardančių medžiagų (OAM) trumpas pavadinimas | — |
| `salis` | `string` | — | `3` | `open` | — | Pasaulio šalies pavadinimas | — |
| `veiksmas` | `string` | — | `4` | `open` | — | Veiksmas, atliktas su f-dujomis ar OAM | — |
| `kiekis` | `number` | `kg` | `4` | `open` | — | F-dujų ar OAM, su kuriais buvo atlikta veikla (importas, eksportas) | — |
| `atsiskaityta` | `integer` | — | `2` | `open` | — | Atsiskaitymo data (metai) | — |
| `prigimtis` | `string` | — | `4` | `open` | — | F-dujų ar OAM medžiagos ar mišinio prigimtis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `"IV"` | — | — | Įvežta AM1I.3 | — |
| `veiksmas` | `"IS"` | — | — | Išvežta AM1I.3 | — |
| `veiksmas` | `"IM"` | — | — | Importuota AM1E.2 | — |
| `veiksmas` | `"EK"` | — | — | Eksportuota AM1E.2 | — |
| `veiksmas` | `"PA"` | — | — | Pagaminta AM1E.2 | — |
| `prigimtis` | `"RC"` | — | — | Recirkuliuota | — |
| `prigimtis` | `"RG"` | — | — | Regeneruota | — |
| `prigimtis` | `"NA"` | — | — | Naudota (išsiurbta) | — |
| `prigimtis` | `"NE"` | — | — | Nenaudota | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atsiskaityta` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/fdujos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/fdujos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/fdujos (https://data.gov.lt/datasets/1671/)
