---
type: Table
title: "Patikrinimas — Pateikiama informacija apie šviežių vaisių ir daržovių atitikties prekybos standartams patikrinimus (produkcijos pavadinimas; kilmės šalis; paskirties šalis; patikrintas partijų skaičius, vnt.; patikrintas produkcijos..."
description: "Spinta table datasets/gov/vat/vaisiu_darzoviu_suvestine/Patikrinimas (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/vaisiu_darzoviu_suvestine/Patikrinimas"
tags: [gov, vat, patikrinimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r7_vaisiu_darzoviu_suvestine.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r7_vaisiu_darzoviu_suvestine.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1863/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/vaisiu_darzoviu_suvestine"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Patikrinimas — Pateikiama informacija apie šviežių vaisių ir daržovių atitikties prekybos standartams patikrinimus (produkcijos...

- **Model:** `datasets/gov/vat/vaisiu_darzoviu_suvestine/Patikrinimas`[^manifest]
- **Dataset:** [Šviežių vaisių ir daržovių atitikties prekybos standartams patikrinimų suvestinė](../vaisiu_darzoviu_suvestine.md) (`datasets/gov/vat/vaisiu_darzoviu_suvestine`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r7_vaisiu_darzoviu_suvestine.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r7_vaisiu_darzoviu_suvestine.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/vaisiu_darzoviu_suvestine/Patikrinimas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `dok_patikra` | `string` | — | `4` | `open` | — | Dokumentų patikra | — |
| `tapat_patikra` | `boolean` | — | `4` | `open` | — | Tapatumo patikrinimas | — |
| `fiz_patikra` | `boolean` | — | `4` | `open` | — | Fizinė patikra | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `dokumentas` | `string` | — | `4` | `open` | — | Dokumento tipas | — |
| `produkcija` | `string` | — | `1` | `open` | — | Produkcijos pavadinimas | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Kilmės šalis | — |
| `paskirties_salis` | `string` | — | `4` | `open` | — | Paskirties šalis | — |
| `patikr_produkcija` | `number` | `t` | `4` | `open` | — | Patikrintas produkcijos kiekis tonomis | — |
| `neatitik_produkcija` | `number` | `t` | `4` | `open` | — | Neatitikusios produkcijos kiekis tonomis | — |
| `pazeidimai` | `string` | — | `4` | `open` | — | Pažeidimų neatitikimų kodai | — |
| `sunaikinta` | `number` | `t` | `4` | `open` | — | Taikytos priemonės produkcijos kiekiui tonomis: sunaikinta | — |
| `viso` | `number` | `t` | `4` | `open` | — | Bendras kiekis tonomis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dok_patikra` | `"patenkinama"` | — | — | — | — |
| `dok_patikra` | `"nepatenkinama"` | — | — | — | — |
| `dokumentas` | `"atitikties_europos_sajungos_prekybos_svieziais_vaisiais_ir_darzovemis_standartams_sertifikatas"` | — | — | — | — |
| `dokumentas` | `"pazyma_apie_svieziu_vaisiu_ir_darzoviu_neatitikti"` | — | — | — | — |
| `pazeidimai` | `"ligos_ir_puviniai"` | — | — | — | — |
| `pazeidimai` | `"netinkamas_zenklinimas"` | — | — | — | — |
| `pazeidimai` | `"kita"` | — | — | — | — |
| `pazeidimai` | `"pakavimo_trukumai"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r7_vaisiu_darzoviu_suvestine.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r7_vaisiu_darzoviu_suvestine.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/vaisiu_darzoviu_suvestine (https://data.gov.lt/datasets/1863/)
