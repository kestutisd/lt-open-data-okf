---
type: Table
title: "GyventojuPajamuMokestis — Gyventojų pajamų mokesčio suma"
description: "Spinta table datasets/gov/vmi/gpm/GyventojuPajamuMokestis (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/gpm/GyventojuPajamuMokestis"
tags: [gov, vmi, gyventojupajamumokestis, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gpm.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vmi/gpm.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1182/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/gpm"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GyventojuPajamuMokestis — Gyventojų pajamų mokesčio suma

- **Model:** `datasets/gov/vmi/gpm/GyventojuPajamuMokestis`[^manifest]
- **Dataset:** [Gyventojų pajamų mokestis](../gpm.md) (`datasets/gov/vmi/gpm`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/gpm.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gpm.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/gpm/GyventojuPajamuMokestis` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `3` | `open` | — | Mokestinio laikotarpio metai | — |
| `sav_kodas` | `string` | — | `3` | `open` | — | Sistemos subjekto savivaldybes kodas | — |
| `sav_pavadinimas` | `string` | — | `3` | `open` | — | Sistemos subjekto savivaldybes pavadinimas | — |
| `mm_kodas` | `string` | — | `3` | `open` | — | Mokesčių mokėtojo identifikacinis numeris | — |
| `apskaiciuotas_gpm` | `number` | — | `3` | `open` | — | Apskaičiuota pajamų mokesčio suma (visa) | — |
| `isskaiciuotas_gpm` | `number` | — | `3` | `open` | — | Išskaičiuota pajamų mokesčio suma | — |
| `kitu_gpm` | `number` | — | `3` | `open` | — | Kitų asmenų lėšomis sumokėta pajamų mokesčio suma | — |
| `sumoketas_gpm` | `number` | — | `3` | `open` | — | Pajamų mokesčio suma sumokėta iki deklaracijos pateikimo dienos | — |
| `gpm_prievole` | `number` | — | `3` | `open` | — | Pajamų mokesčio prievolė | — |
| `gpm_moketina_grazintina` | `number` | — | `3` | `open` | — | Pajamų mokesčio suma mokėtina / grąžintina suma | — |
| `kreditas_30_proc` | `number` | — | `3` | `open` | — | Pajamų mokesčio kredito suma, apskaičiuota nuo pajamų taikant 30 proc. atskaitymus | — |
| `kreditas_fakt` | `number` | — | `3` | `open` | — | Pajamų mokesčio kredito suma, apskaičiuota nuo pajamų taikant 30 faktinius atskaitymus | — |
| `atleista` | `number` | — | `3` | `open` | — | Pajamų mokesčio suma (atleista dėl užsienyje sumokėto mokesčio) | — |
| `atskaityta` | `number` | — | `3` | `open` | — | Pajamų mokesčio suma (atskaityta dėl užsienyje sumokėto mokesčio) | — |
| `grazinta_t` | `number` | — | `3` | `open` | — | Pajamų mokesčio suma grąžinta pagal prašymo formą FR0464 | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/gpm.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gpm.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/gpm (https://data.gov.lt/datasets/1182/)
