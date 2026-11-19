---
type: Table
title: "KelioZenklas — Kelio ženklai"
description: "Šiame rinkinyje pateikti Marijampolės savivaldybės kelio ženklai bei jų lokacijos."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/keliai/KelioZenklas"
tags: [gov, marijampoles_sav, keliozenklas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/kelio_zenklas.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/kelio_zenklas.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2756/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/keliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KelioZenklas — Kelio ženklai

Šiame rinkinyje pateikti Marijampolės savivaldybės kelio ženklai bei jų lokacijos.[^manifest]

- **Model:** `datasets/gov/marijampoles_sav/keliai/KelioZenklas`[^manifest]
- **Dataset:** [Marijampolės savivaldybės techninių eismo reguliavimo priemonių informacinės sistemos duomenys](../keliai.md) (`datasets/gov/marijampoles_sav/keliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/kelio_zenklas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/kelio_zenklas.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/keliai/KelioZenklas` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_primary_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_primary_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Kelio ženklo tipas | — |
| `tipo_pavadinimas` | `string` | — | `3` | `open` | — | Ženklo tipo pavadinimas | — |
| `ket_nr` | `string` | — | `4` | `open` | — | Kelių eismo taisyklių (KET) ženklo numeris | — |
| `zenklo_tekstas` | `string` | — | `3` | `open` | — | Ženkle esantis tekstas | — |
| `galiojimo_kryptis` | `string` | — | `4` | `open` | — | Ženklo galiojimo kryptis | — |
| `pasukimo_kampas` | `integer` | — | `4` | `open` | — | Ženklo pasukimo kampas | — |
| `zenklu_grupe` | `string` | — | `4` | `open` | — | Ženklų grupė | — |
| `atspindzio_grupe` | `string` | — | `4` | `open` | — | Atspindžio grupė | — |
| `bukle` | `string` | — | `4` | `open` | — | Ženklo būklė | — |
| `statusas` | `string` | — | `4` | `open` | — | Ženklo statusas | — |
| `irengimo_data` | `datetime` | `S` | `4` | `open` | — | Įrengimo data | — |
| `galioja_nuo` | `datetime` | `S` | `4` | `open` | — | Ženklas galioja nuo | — |
| `galioja_iki` | `datetime` | `S` | `4` | `open` | — | Ženklas galioja iki | — |
| `pasal_priezastis_lt` | `string` | — | `2` | `open` | — | Ženklo pašalinimo priežastis | — |
| `pasal_data` | `datetime` | `D` | `4` | `open` | — | Ženklo pašalinimo data | — |
| `adresas` | `string` | — | `4` | `open` | — | Ženklo adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"NUR"` | — | — | Nurodomasis kelio ženklas | — |
| `tipas` | `"DRAU"` | — | — | Draudžiamasis kelio ženklas | — |
| `tipas` | `"PIR"` | — | — | Pirmumo kelio ženklas | — |
| `tipas` | `"LENT"` | — | — | Papildoma lentelė | — |
| `tipas` | `"NUK"` | — | — | Nukreipiamasis kelio ženklas | — |
| `tipas` | `"ISP"` | — | — | Įspėjamasis kelio ženklas | — |
| `tipas` | `"INF"` | — | — | Informacinis kelio ženklas | — |
| `tipas` | `"PAS"` | — | — | Paslaugų kelio ženklas | — |
| `tipas` | `"VERZ"` | — | — | Verz | — |
| `galiojimo_kryptis` | `"PIR"` | — | — | Pirmyn | — |
| `galiojimo_kryptis` | `"PRAT"` | — | — | Pagal esimą - Pirmyn / Atgal | — |
| `bukle` | `"GER"` | — | — | Gera | — |
| `bukle` | `"VID"` | — | — | Vidutinė | — |
| `bukle` | `"BLO"` | — | — | Bloga | — |
| `statusas` | `"2"` | — | — | Galioja | — |
| `statusas` | `"3"` | — | — | Negalioja | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pasal_priezastis_lt` | `update(property: "pasal_priezastis_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/kelio_zenklas.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/kelio_zenklas.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/keliai (https://data.gov.lt/datasets/2756/)
