---
type: Table
title: "Subjektas — Valstybinės veterinarinės kontrolės subjektai"
description: "Spinta table datasets/gov/vmvt/kontroles_subjektai/Subjektas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai/Subjektas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Valstybinės veterinarinės kontrolės subjektai

- **Model:** `datasets/gov/vmvt/kontroles_subjektai/Subjektas`[^manifest]
- **Dataset:** [Valstybinės veterinarinės kontrolės subjektų duomenys](../kontroles_subjektai.md) (`datasets/gov/vmvt/kontroles_subjektai`)
- **Manifest CSV:** [datasets/gov/vmvt/kontroles_subjektai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai/Subjektas`
- **Primary Key (`ref`):** `vet_pat_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vet_pat_nr` | `string` | — | `4` | `open` | — | Veterinarinio patvirtinimo numeris | — |
| `patvirtinimas` | `date` | `D` | `4` | `open` | — | Veterinarinio patvirtinimo data | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Veterinarinės kontrolės objekto ar subjekto pavadinimas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `adresas` | `string` | — | `4` | `open` | — | Veterinarinės kontrolės objekto adresas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `kontaktai` | `string` | — | `4` | `open` | — | Veterinarinės kontrolės objekto kontaktiniai duomenys | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `vmvt` | `string` | — | `4` | `open` | — | VMVT teritorinė | VMVT departamentas ar skyrius, kuris kontroliuoja veterinės kontrolės objektą |
| `veikla_kodas` | `ref` | [VeiklosKlasifikatorius](VeiklosKlasifikatorius.md) | `4` | `open` | — | VMVT veiklos kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv
