---
type: Table
title: "Subjektas — Maisto tvarkymo subjektai"
description: "Spinta table datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas"
tags: [gov, vmvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Maisto tvarkymo subjektai

- **Model:** `datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas`[^manifest]
- **Dataset:** [Duomenys apie maisto tvarkymo subjektus](../maisto_tvarkymo_subjektai.md) (`datasets/gov/vmvt/maisto_tvarkymo_subjektai`)
- **Manifest CSV:** [datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `0` | `open` | — | Juridinio asmens kodas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `pavadinimas` | `string` | — | `0` | `open` | — | Juridinio asmens pavadinimas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `veikla` | `string` | — | `3` | `open` | — | Pagrindinė veikla | — |
| `evrk_1` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis[kodas]](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `3` | `open` | — | Veikla pagal Ekonominės veiklos rūšių klasifikatorių | — |
| `evrk_2` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis[kodas]](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `3` | `open` | — | Papildoma veikla pagal Ekonominės veiklos rūšių klasifikatorių | — |
| `evrk_3` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis[kodas]](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `1` | `open` | — | Papildoma veikla pagal Ekonominės veiklos rūšių klasifikatorių | — |
| `produktas` | `string` | — | `1` | `open` | — | Produktas | — |
| `pk_1` | `ref` | [AsortimentoKlasifikatorius](AsortimentoKlasifikatorius.md) | `4` | `open` | — | Asortimento kodas pagal VMVT FIS sąrašą | — |
| `pk_2` | `ref` | [AsortimentoKlasifikatorius](AsortimentoKlasifikatorius.md) | `4` | `open` | — | Papildomo asortimento kodas pagal VMVT FIS sąrašą | — |
| `pk_3` | `ref` | [AsortimentoKlasifikatorius](AsortimentoKlasifikatorius.md) | `4` | `open` | — | Papildomo asortimento kodas pagal VMVT FIS sąrašą | — |
| `mt_adresas` | `string` | — | `0` | `open` | — | Maisto tvarkymo objekto adresas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `paz_isdave` | `string` | — | `2` | `open` | — | Pažymėjimą išdavė | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Pažymėjimo išdavimo data | — |
| `paz_nr` | `string` | — | `1` | `open` | — | Maisto tvarkymo pažymėjimo numeris | — |
| `riz_grupe` | `string` | — | `3` | `open` | — | Rizikos grupė | Aprašymas apie rizikos grupes: https://vmvt.lt/maisto-sauga/kontrole/ukio-subjektu-registrai/subjektai-pagal-rizikos-grupes |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv
