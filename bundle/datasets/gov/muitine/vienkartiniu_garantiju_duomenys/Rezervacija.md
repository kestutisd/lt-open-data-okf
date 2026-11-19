---
type: Table
title: "Rezervacija — Duomenys apie vienkartinių muitinės garantijų panaudojimus"
description: "Duomenys apie vienkartinių muitinės garantijų rezervacijas ir atlaisvinimus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/vienkartiniu_garantiju_duomenys/Rezervacija"
tags: [gov, muitine, rezervacija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/vienkartiniu_garantiju_duomenys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/vienkartiniu_garantiju_duomenys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2794/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/vienkartiniu_garantiju_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rezervacija — Duomenys apie vienkartinių muitinės garantijų panaudojimus

Duomenys apie vienkartinių muitinės garantijų rezervacijas ir atlaisvinimus[^manifest]

- **Model:** `datasets/gov/muitine/vienkartiniu_garantiju_duomenys/Rezervacija`[^manifest]
- **Dataset:** [Duomenys apie vienkartinių muitinės garantijų panaudojimus](../vienkartiniu_garantiju_duomenys.md) (`datasets/gov/muitine/vienkartiniu_garantiju_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/vienkartiniu_garantiju_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/vienkartiniu_garantiju_duomenys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/vienkartiniu_garantiju_duomenys/Rezervacija` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `veiksmo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veiksmo_id` | `string` | — | `4` | `open` | — | Šifruotas garantijos rezervacijos veiksmo identifikatorius | — |
| `garantijos_id` | `string` | — | `4` | `open` | — | Šifruotas garantijos identifikatorius | — |
| `ekonomines_veiklos_vykdytojas` | `string` | — | `4` | `open` | — | Ekonominės veiklos vykdytojas | — |
| `veiksmo_data` | `date` | `D` | `4` | `open` | — | Garantijos veiksmo data | — |
| `garantijos_veiksmo_sekos_numeris` | `string` | — | `4` | `open` | — | Garantijos veiksmo sekos numeris | — |
| `veiksmas` | `string` | — | `4` | `open` | — | Garantijos rezervacijos veiksmo pavadinimas | — |
| `panaudota_suma_uzstatui_eur` | `number` | — | `4` | `open` | — | Panaudota suma užstatui eurais | — |
| `muitines_operacija` | `string` | — | `4` | `open` | — | Muitinės operacija | — |
| `garantijos_tipas` | `string` | — | `4` | `open` | — | Garantijos tipo pavadinimas | — |
| `garantijos_tipo_kodas` | `string` | — | `4` | `open` | — | Garantijos tipo kodas sistemoje | — |
| `garantijos_dydis_eur` | `number` | — | `4` | `open` | — | Garantijos dydis eurais | — |
| `nepanaudotas_garantijos_dydis_eur` | `number` | — | `4` | `open` | — | Nepanaudotas garantijos dydis eurais | — |
| `garantijos_galiojimo_pradzia` | `date` | `D` | `4` | `open` | — | Garantijos galiojimo pradžia | — |
| `garanto_identifikacinis_kodas` | `string` | — | `4` | `open` | — | Šifruotas garanto identifikacinis kodas | — |
| `garantijos_statusas` | `string` | — | `4` | `open` | — | Garantijos statusas | — |
| `garantijos_statuso_data` | `date` | `D` | `4` | `open` | — | Garantijos statuso data | — |
| `ar_visos_es_salys` | `boolean` | — | `4` | `open` | — | Požymis, ar garantija galioja visose Europos Sąjungos šalyse | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | — | `"USE"` | — | — | — |
| `veiksmas` | — | `"RELEASE"` | — | — | — |
| `veiksmas` | — | `"USE_CANCELLATION"` | — | — | — |
| `garantijos_tipas` | — | `"Garanto vienkartinis įsipareigojimas"` | — | — | — |
| `garantijos_tipo_kodas` | — | `"2"` | — | — | — |
| `garantijos_statusas` | — | `"CANCELLED"` | — | — | — |
| `garantijos_statusas` | — | `"IN_USE"` | — | — | — |
| `garantijos_statusas` | — | `"VALID"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/vienkartiniu_garantiju_duomenys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/vienkartiniu_garantiju_duomenys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/vienkartiniu_garantiju_duomenys (https://data.gov.lt/datasets/2794/)
