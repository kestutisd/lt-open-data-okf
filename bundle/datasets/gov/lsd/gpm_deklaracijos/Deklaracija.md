---
type: Table
title: "Deklaracija — Gyventojų pajamų mokesčio deklaracijos"
description: "Gyventojų pajamų mokesčio deklaracijos"
resource: "https://get.data.gov.lt/datasets/gov/lsd/gpm_deklaracijos/Deklaracija"
tags: [gov, lsd, deklaracija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gpm_deklaracijos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gpm_deklaracijos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2924/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gpm_deklaracijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Deklaracija — Gyventojų pajamų mokesčio deklaracijos

Gyventojų pajamų mokesčio deklaracijos[^manifest]

- **Model:** `datasets/gov/lsd/gpm_deklaracijos/Deklaracija`[^manifest]
- **Dataset:** [Gyventojų pajamų mokesčio deklaracijų duomenys](../gpm_deklaracijos.md) (`datasets/gov/lsd/gpm_deklaracijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gpm_deklaracijos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gpm_deklaracijos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gpm_deklaracijos/Deklaracija` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `dk_id` | `string` | — | `4` | `open` | — | Deklaracijos identifikatorius | — |
| `mm_kodas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojas | — |
| `paj_insert_date` | `date` | `D` | `4` | `open` | — | Įrašo data | — |
| `paj_update_date` | `date` | `D` | `4` | `open` | — | Atnaujinta įrašo data | — |
| `metai` | `integer` | — | `4` | `open` | — | Mokestinio laikotarpio metai | — |
| `pajamu_suma` | `number` | — | `4` | `open` | — | Gautos pajamos | — |
| `isskaiciuotas_gpm` | `number` | — | `4` | `open` | — | Išskaičiuotas gyventojų pajamų mokestis | — |
| `paj_valst_paj` | `string` | — | `4` | `open` | — | Valstybė kurioje gautos pajamos | — |
| `pajamu_rusies_kodas` | `integer` | — | `4` | `open` | — | Pajamų rūšies kodas | — |
| `pajamu_rusis_aprasas` | `string` | — | `4` | `open` | — | Pajamų rūšies kodo aprašas | — |
| `lengvatos_kodas` | `string` | — | `4` | `open` | — | Lengvatos kodas | — |
| `lengvatos_pavadinimas` | `string` | — | `4` | `open` | — | Lengvatos pavadinimas | — |
| `pajamu_pobudis` | `string` | — | `4` | `open` | — | Pajamu pobūdis | — |
| `pajamu_pobudis_pavadinimas` | `string` | — | `4` | `open` | — | Pajamu pobūdis paaiškinimas | — |
| `verslo_ld_kodas` | `string` | — | `4` | `open` | — | Verslo liūdijomo kodas | — |
| `verslo_ld_rusiu_pav` | `string` | — | `4` | `open` | — | Verslo liūdijomo rūšies pavadinimas | — |
| `paj_suma_pap` | `number` | — | `4` | `open` | — | Su pajamomis tiesiogiai susijusi išlaidų suma | — |
| `paj_gpm_kito` | `number` | — | `4` | `open` | — | Pajamu gpm pakito | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pajamu_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `isskaiciuotas_gpm` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gpm_deklaracijos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gpm_deklaracijos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gpm_deklaracijos (https://data.gov.lt/datasets/2924/)
