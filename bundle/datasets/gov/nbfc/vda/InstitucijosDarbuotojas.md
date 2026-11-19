---
type: Table
title: "InstitucijosDarbuotojas — Valstybės duomenų agentūros darbuotojai"
description: "Institucijų darbuotojų informacija pagal gimimo metus, lytį, darbo pradžią, pabaigą, skyrių, instituciją."
resource: "https://get.data.gov.lt/datasets/gov/nbfc/vda/InstitucijosDarbuotojas"
tags: [gov, nbfc, institucijosdarbuotojas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/vda.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/nbfc/vda.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# InstitucijosDarbuotojas — Valstybės duomenų agentūros darbuotojai

Institucijų darbuotojų informacija pagal gimimo metus, lytį, darbo pradžią, pabaigą, skyrių, instituciją. Gimimo metai apvalinami iki dešimties. Priimti ir atleisti iki 2022-01-01 dienos į rinkinį nepatenka. Priimti prieš 2022-01-01, ir atleisti po 2022-01-01 arba dirbantys iki dabar - yra rinkinyje.[^manifest]

- **Model:** `datasets/gov/nbfc/vda/InstitucijosDarbuotojas`[^manifest]
- **Dataset:** [Valstybės duomenų agentūros darbuotojai](../vda.md) (`datasets/gov/nbfc/vda`)[^manifest]
- **Manifest CSV:** [datasets/gov/nbfc/vda.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/vda.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/vda/InstitucijosDarbuotojas` (`deployed`)[^manifest]
- **Provider:** `nbfc` — Nacionalinis bendrųjų funkcijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `tabelio_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tabelio_nr` | `string` | — | `4` | `open` | — | Darbuotojo unikalus tabelio numeris šifruotas šiam rinkiniui (su kitais rinkiniais nesijungia) | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas unikaliai šifruotas šiam rinkiniui (su kitais rinkiniais nesijungia) | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Ar asmens kodas validus | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gim_desimtm_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gim_desimtm` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `darbo_pradzia` | `date` | `D` | `4` | `open` | — | Darbo pradžos data | — |
| `darbo_pabaiga` | `date` | `D` | `4` | `open` | — | Darbo pabaigos data | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyriaus Pavadinimas | — |
| `institucija` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/vda.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/vda.csv#L7)
