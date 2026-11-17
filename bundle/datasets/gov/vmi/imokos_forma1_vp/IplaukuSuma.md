---
type: Table
title: "IplaukuSuma — Mokesčių ir kitų įmokų į biudžetus apyskaitos (forma 1-VP) VMI duomenys"
description: "Spinta table datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/imokos_forma1_vp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/imokos_forma1_vp.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# IplaukuSuma — Mokesčių ir kitų įmokų į biudžetus apyskaitos (forma 1-VP) VMI duomenys

- **Model:** `datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma`[^manifest]
- **Dataset:** [datasets/gov/vmi/imokos_forma1_vp](../imokos_forma1_vp.md) (`datasets/gov/vmi/imokos_forma1_vp`)
- **Manifest CSV:** [datasets/gov/vmi/imokos_forma1_vp.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/imokos_forma1_vp.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/imokos_forma1_vp/IplaukuSuma`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo ID | — |
| `imokos_pavadinimas` | `string` | — | `1` | `open` | — | 1-VP formos eilutės pavadinimas | — |
| `eil_nr` | `integer` | — | `4` | `open` | — | 1-VP pagrindinės formos stulpelis Eil. Nr. | — |
| `mm_apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis[adm_kodas]](../../rc/ar/apskritis/Apskritis.md) | `3` | `open` | — | Apskrities kodas, kurioje yra registruotas mokesčių mokėtojas | — |
| `mm_savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[sav_kodas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `3` | `open` | — | Savivaldybės kodas, kurioje registruotas mokesčių mokėtojas | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/imokos_forma1_vp.csv
