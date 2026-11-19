---
type: Table
title: "Registras — Tiekiamų paslaugų registras"
description: "Šiaulių energijos teikiamų paslaugų ir suvartotų kiekių registras."
resource: "https://get.data.gov.lt/datasets/gov/se/billingas/Registras"
tags: [gov, se, registras, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/se/registras.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2886/"
    title: "data.gov.lt DCAT-AP — datasets/gov/se/billingas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Registras — Tiekiamų paslaugų registras

Šiaulių energijos teikiamų paslaugų ir suvartotų kiekių registras. Rinkinys apima Šiaulių energijos teikiamų paslaugų teritoriją, duomenys nuo 2017 metų iki dabar. Rinkinyje pateikiama paslaugos pavadinimas ir kategorija, kiekis ir matavimo vienetas, periodo mėnuo ir patalpos ID (referuoja į lentelę Patalpos).[^manifest]

- **Model:** `datasets/gov/se/billingas/Registras`[^manifest]
- **Dataset:** [Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo...](../billingas.md) (`datasets/gov/se/billingas`)[^manifest]
- **Manifest CSV:** [datasets/gov/se/registras.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/se/billingas/Registras` (`deployed`)[^manifest]
- **Provider:** `se` — AB Šiaulių energija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identitfikatorius | — |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos unikalus identifikatorius | — |
| `periodo_menuo` | `date` | `M` | `4` | `open` | — | Suteiktų paslaugų laikotarpio mėnuo | — |
| `kiekis` | `number` | — | `4` | `open` | — | Suteiktų paslaugų kiekis | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Suteiktų paslaugų kiekio matavimo vienetas | — |
| `pirkejo_kodas` | `string` | — | `4` | `open` | — | Pirkėjo kodas | — |
| `juridinis` | `string` | — | `4` | `open` | — | Požymis ar juridinis pirkėjas | — |
| `paslaugos_pavadinimas` | `string` | — | `4` | `open` | — | Paslaugos pavadinimas | — |
| `paslaugos_kategorija` | `string` | — | `4` | `open` | — | Paslaugos kategorija | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/se/registras.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/se/billingas (https://data.gov.lt/datasets/2886/)
