---
type: Table
title: "IplaukuSuma — Mokesčių ir kitų įmokų į biudžetus apyskaitos (forma 1-VP) VMI duomenys"
description: "Spinta table datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma"
tags: [gov, vmi, iplaukusuma, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/imokos_forma1_vp.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/imokos_forma1_vp.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1203/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/imokos_forma1_vp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IplaukuSuma — Mokesčių ir kitų įmokų į biudžetus apyskaitos (forma 1-VP) VMI duomenys

- **Model:** `datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma`[^manifest]
- **Dataset:** [Mokesčių ir kitų įmokų į biudžetus apyskaitos (forma 1-VP) VMI duomenys](../imokos_forma1_vp.md) (`datasets/gov/vmi/imokos_forma1_vp`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/imokos_forma1_vp.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/imokos_forma1_vp.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo ID | — |
| `imokos_pavadinimas` | `string` | — | `1` | `open` | — | 1-VP formos eilutės pavadinimas | — |
| `eil_nr` | `integer` | — | `4` | `open` | — | 1-VP pagrindinės formos stulpelis Eil. Nr. | — |
| `mm_apskritis` | `ref` | [Apskritis](../../rc/ar/apskritis/Apskritis.md) (`level=3`: `mm_apskritis.adm_kodas`) | `3` | `open` | — | Apskrities kodas, kurioje yra registruotas mokesčių mokėtojas | — |
| `mm_savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=3`: `mm_savivaldybe.sav_kodas`) | `3` | `open` | — | Savivaldybės kodas, kurioje registruotas mokesčių mokėtojas | — |
| `metai` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Ataskaitinis metų mėnuo | — |
| `visa_suma` | `number` | — | `2` | `open` | — | Auganti įplaukų suma už ataskaitinius metus nuo metų pradžios iki ataskaitinio mėnesio pabaigos | — |
| `valst_biudzetui` | `number` | — | `2` | `open` | — | Auganti įplaukų suma valstybės biudžetui už ataskaitinius metus nuo metų pradžios iki ataskaitinio mėnesio pabaigos | — |
| `sav_biudzetui` | `number` | — | `2` | `open` | — | Auganti įplaukų suma savivaldybių biudžetams už ataskaitinius metus nuo metų pradžios iki ataskaitinio mėnesio pabaigos | — |
| `fondams` | `number` | — | `2` | `open` | — | Auganti įplaukų suma fondams už ataskaitinius metus nuo metų pradžios iki ataskaitinio mėnesio pabaigos | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo (būsenos pasikeitimo) data | — |
| `suformuota` | `date` | `D` | `4` | `open` | — | Duomenų suformavimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `visa_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `valst_biudzetui` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sav_biudzetui` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `fondams` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/imokos_forma1_vp.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/imokos_forma1_vp.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/imokos_forma1_vp (https://data.gov.lt/datasets/1203/)
