---
type: Table
title: "ZpvVakcinacija — Paskiepytų ŽPV vakcinacija"
description: "Paskiepytų nuo žmogaus papilomos viruso (ŽPV) asmenų skaičius pagal įstaigas ir amžiaus grupes"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/zpv_skiepai/ZpvVakcinacija"
tags: [gov, lsd, zpvvakcinacija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/zpv_skiepai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/zpv_skiepai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3862/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/zpv_skiepai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ZpvVakcinacija — Paskiepytų ŽPV vakcinacija

Paskiepytų nuo žmogaus papilomos viruso (ŽPV) asmenų skaičius pagal įstaigas ir amžiaus grupes[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/zpv_skiepai/ZpvVakcinacija`[^manifest]
- **Dataset:** [Paskiepytų ŽPV vakcinacija](../zpv_skiepai.md) (`datasets/gov/lsd/sveikata/zpv_skiepai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/zpv_skiepai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/zpv_skiepai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/zpv_skiepai/ZpvVakcinacija` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `men_data` | `date` | `D` | `4` | `open` | — | "Vakcinacijos data, apvalinta mėnesio tikslumu" | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmenų grupės lytis | — |
| `amziaus_gr` | `string` | — | `4` | `open` | — | "Amžiaus grupės: mažiau negu 10m., 11m., 12m., 13m., 14m., 15-17 m., 18 m. ir daugiau." | — |
| `apsk_pav` | `string` | — | `4` | `open` | — | Apskritis | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `pspc_pav` | `string` | — | `4` | `open` | — | Pirminės sveikatos priežiūros įstaigos pavadinimas | — |
| `pop` | `integer` | — | `4` | `open` | — | Prisirašiusiųjų prie pirminės sveikatos priežiūros įstaigos asmenų skaičius | — |
| `dozes_nr` | `integer` | — | `4` | `open` | — | "Vakcinos dozės eiliškumas: 1, 2, 3, 4" | — |
| `count` | `integer` | — | `4` | `open` | — | Paskiepytų asmenų skaičius pagal paskutinę asmens dozės eiliškumo skiepijimo būseną | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `amziaus_gr` | `"18+"` | — | — | 18 metų ir vyresni | — |
| `amziaus_gr` | `"12"` | — | — | 12 metų | — |
| `amziaus_gr` | `"11"` | — | — | 11 metų | — |
| `amziaus_gr` | `"13"` | — | — | 13 metų | — |
| `amziaus_gr` | `"15-17"` | — | — | Nuo 15 iki 17 metų | — |
| `amziaus_gr` | `"14"` | — | — | 14 metų | — |
| `amziaus_gr` | `"<=10"` | — | — | Iki 10 metų imtinai | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/zpv_skiepai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/zpv_skiepai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/zpv_skiepai (https://data.gov.lt/datasets/3862/)
