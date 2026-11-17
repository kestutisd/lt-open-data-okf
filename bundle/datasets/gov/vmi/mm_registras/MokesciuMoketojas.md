---
type: Table
title: "MokesciuMoketojas — MOKESČIŲ MOKĖTOJŲ (JURIDINIŲ ASMENŲ) KODŲ, TIPŲ, GRUPIŲ DUOMENYS"
description: "Spinta table datasets/gov/vmi/mm_registras/MokesciuMoketojas (37 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/mm_registras/MokesciuMoketojas"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/mm_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mm_registras.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MokesciuMoketojas — MOKESČIŲ MOKĖTOJŲ (JURIDINIŲ ASMENŲ) KODŲ, TIPŲ, GRUPIŲ DUOMENYS

- **Model:** `datasets/gov/vmi/mm_registras/MokesciuMoketojas`[^manifest]
- **Dataset:** [MOKESČIŲ MOKĖTOJŲ (JURIDINIŲ ASMENŲ) KODŲ, TIPŲ, GRUPIŲ DUOMENYS](../mm_registras.md) (`datasets/gov/vmi/mm_registras`)
- **Manifest CSV:** [datasets/gov/vmi/mm_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mm_registras.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/mm_registras/MokesciuMoketojas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų rinkinio eilės numeris | — |
| `klnt_tipas` | `string` | — | `4` | `open` | — | Kliento tipas | — |
| `ja_kodas` | `integer` | — | `4` | `open` | — | JA identifikacinis kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo pavadinimas | — |
| `ireg_data` | `date` | `D` | `4` | `open` | — | Kliento įregistravimo į MMR data | — |
| `isreg_data` | `date` | `D` | `4` | `open` | — | Kliento išregistravimo iš MMR data | — |
| `anul_data` | `date` | `D` | `4` | `open` | — | Įrašo anuliavimo data | — |
| `valstybe` | `string` | — | `4` | `open` | — | Triženklis valstybės kodas | — |
| `tipo_kodas` | `integer` | — | `4` | `open` | — | Kliento tipo kodas | — |
| `tipo_aprasymas` | `string` | — | `4` | `open` | — | Kliento tipo aprašymas | — |
| `tipas_nuo` | `date` | `D` | `4` | `open` | — | Duomenų tipo galiojimo pradžios data | — |
| `tipas_iki` | `date` | `D` | `4` | `open` | — | Duomenų tipo galiojimo pabaigos data | — |
| `anul_tipas` | `date` | `D` | `4` | `open` | — | Duomenų tipo anuliavimo data | — |
| `pvm_kodas_pref` | `string` | — | `4` | `open` | — | Aktualaus PVM mokėtojo kodo prefiksas | — |
| `pvm_kodas` | `string` | — | `4` | `open` | — | Aktualus PVM mokėtojo kodas be prefikso „LT“ | — |
| `pvm_iregistruota` | `date` | `D` | `4` | `open` | — | PVM mokėtojo įregistravimo data | — |
| `pvm_isregistruota` | `date` | `D` | `4` | `open` | — | PVM mokėtojo išregistravimo data | — |
| `padalinio_nr` | `integer` | — | `4` | `open` | — | Mokesčio mokėtojo padalinio numeris | — |
| `padalinio_pvd` | `string` | — | `4` | `open` | — | Mokesčio mokėtojo padalinio pavadinimas | — |
| `padalinio_savivaldybe` | `integer` | — | `4` | `open` | — | Padalinio savivaldybės kodas | — |
| `padalinio_kodas` | `integer` | — | `4` | `open` | — | Valstybės, kurioje yra padalinys, kodas | — |
| `suformuota` | `date` | `D` | `4` | `open` | — | Mokesčio mokėtojo padalinio suformavimo data | — |
| `isformuota` | `date` | `D` | `4` | `open` | — | Mokesčio mokėtojo padalinio išformavimo data | — |
| `ekonomine_veikla` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `4` | `open` | — | Ekonominės veiklos rūšies kodas | — |
| `veiklos_pradzia` | `date` | `D` | `4` | `open` | — | Veiklos galiojimo pradžios data | — |
| `veiklos_pabaiga` | `date` | `D` | `4` | `open` | — | Veiklos galiojimo pabaigos data | — |
| `veikla_anuliuota` | `date` | `D` | `4` | `open` | — | Veikla anuliuota | — |
| `pagrindine` | `integer` | — | `4` | `open` | — | Ekonominės veiklos požymis | — |
| `vv_savivaldybe` | `integer` | — | `4` | `open` | — | Vykdomos veiklos savivaldybė | — |
| `vv_adresas_nuo` | `date` | `D` | `4` | `open` | — | Vykdomos veiklos adreso įsigaliojimo pradžia | — |
| `vv_adresas_iki` | `date` | `D` | `4` | `open` | — | Vykdomos veiklos adreso įsigaliojimo pabaiga | — |
| `vv_adresas_anul` | `date` | `D` | `4` | `open` | — | Vykdomos veiklos adreso anuliavimo data | — |
| `mm_grupe` | `integer` | — | `4` | `open` | — | Mokesčių mokėtojo grupės kodas | — |
| `grup_aprasymas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo grupės aprašymas | — |
| `grupe_nuo` | `date` | `D` | `4` | `open` | — | Įrašo duomenų galiojimo pradžios data | — |
| `grupe_iki` | `date` | `D` | `4` | `open` | — | Įrašo duomenų galiojimo pabaigos data | — |
| `grupe_anul` | `date` | `D` | `4` | `open` | — | Įrašo anuliavimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `klnt_tipas` | `"LJA"` | — | — | Lietuvos juridinis asmuo | — |
| `klnt_tipas` | `"UJA"` | — | — | Užsienio juridinis asmuo | — |
| `pagrindine` | `1` | — | — | Pagrindinė | — |
| `pagrindine` | `0` | — | — | Nepagrindinė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `padalinio_savivaldybe` | `create(property: "padalinio_savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `padalinio_savivaldybe` | `update(property: "padalinio_savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `vv_savivaldybe` | `create(property: "vv_savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `vv_savivaldybe` | `update(property: "vv_savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/mm_registras.csv
