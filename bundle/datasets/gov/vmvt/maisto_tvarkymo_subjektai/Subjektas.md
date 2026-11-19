---
type: Table
title: "Subjektas — Maisto tvarkymo subjektai"
description: "Spinta table datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas"
tags: [gov, vmvt, subjektas, deployed, level-3, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/maisto_tvarkymo_subjektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Subjektas — Maisto tvarkymo subjektai

- **Model:** `datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas`[^manifest]
- **Dataset:** [Duomenys apie maisto tvarkymo subjektus](../maisto_tvarkymo_subjektai.md) (`datasets/gov/vmvt/maisto_tvarkymo_subjektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=0` scalar) | `0` | `open` | — | Juridinio asmens kodas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `pavadinimas` | `string` | — | `0` | `open` | — | Juridinio asmens pavadinimas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `veikla` | `string` | — | `3` | `open` | — | Pagrindinė veikla | — |
| `evrk_1` | `ref` | [EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) (`level=3`: `evrk_1.kodas`) | `3` | `open` | — | Veikla pagal Ekonominės veiklos rūšių klasifikatorių | — |
| `evrk_2` | `ref` | [EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) (`level=3`: `evrk_2.kodas`) | `3` | `open` | — | Papildoma veikla pagal Ekonominės veiklos rūšių klasifikatorių | — |
| `evrk_3` | `ref` | [EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) (`level=1` scalar) | `1` | `open` | — | Papildoma veikla pagal Ekonominės veiklos rūšių klasifikatorių | — |
| `produktas` | `string` | — | `1` | `open` | — | Produktas | — |
| `pk_1` | `ref` | [AsortimentoKlasifikatorius](AsortimentoKlasifikatorius.md) (`level=4 UUID`: `pk_1._id`) | `4` | `open` | — | Asortimento kodas pagal VMVT FIS sąrašą | — |
| `pk_2` | `ref` | [AsortimentoKlasifikatorius](AsortimentoKlasifikatorius.md) (`level=4 UUID`: `pk_2._id`) | `4` | `open` | — | Papildomo asortimento kodas pagal VMVT FIS sąrašą | — |
| `pk_3` | `ref` | [AsortimentoKlasifikatorius](AsortimentoKlasifikatorius.md) (`level=4 UUID`: `pk_3._id`) | `4` | `open` | — | Papildomo asortimento kodas pagal VMVT FIS sąrašą | — |
| `mt_adresas` | `string` | — | `0` | `open` | — | Maisto tvarkymo objekto adresas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `paz_isdave` | `string` | — | `2` | `open` | — | Pažymėjimą išdavė | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Pažymėjimo išdavimo data | — |
| `paz_nr` | `string` | — | `1` | `open` | — | Maisto tvarkymo pažymėjimo numeris | — |
| `riz_grupe` | `string` | — | `3` | `open` | — | Rizikos grupė | Aprašymas apie rizikos grupes: https://vmvt.lt/maisto-sauga/kontrole/ukio-subjektu-registrai/subjektai-pagal-rizikos-grupes |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/maisto_tvarkymo_subjektai (https://data.gov.lt/datasets/802/)
