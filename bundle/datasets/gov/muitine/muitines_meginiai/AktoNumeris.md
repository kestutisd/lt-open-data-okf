---
type: Table
title: "AktoNumeris — Informacija apie muitinės mėginių klasifikavimo aktus"
description: "informacija apie muitinio įforminimo metu paimtus prekių pavyzdžius ir pagal juos suformuotus prekių klasifikavimo aktus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_meginiai/AktoNumeris"
tags: [gov, muitine, aktonumeris, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_meginiai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_meginiai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2834/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_meginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AktoNumeris — Informacija apie muitinės mėginių klasifikavimo aktus

informacija apie muitinio įforminimo metu paimtus prekių pavyzdžius ir pagal juos suformuotus prekių klasifikavimo aktus[^manifest]

- **Model:** `datasets/gov/muitine/muitines_meginiai/AktoNumeris`[^manifest]
- **Dataset:** [Informacija apie muitinės mėginių klasifikavimo aktus](../muitines_meginiai.md) (`datasets/gov/muitine/muitines_meginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_meginiai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_meginiai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_meginiai/AktoNumeris` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `prekiu_klasifikavimo_akto_numeris`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prekiu_klasifikavimo_akto_numeris` | `string` | — | `4` | `open` | — | Šifruotas prekių klasifikavimo akto numeris | — |
| `prekiu_klasifikavimo_akto_data` | `date` | `D` | `4` | `open` | — | Prekių klasifikavimo akto data | — |
| `pazeidimu_nustatymai` | `string` | — | `4` | `open` | — | Ar prekės kodas pasikeitė | — |
| `ar_prekiu_klasifikavimo_aktas_panaikintas` | `boolean` | — | `4` | `open` | — | Požymis ar prekių klasifikavimo aktas panaikintas | — |
| `taric_kodas_akte` | `string` | — | `4` | `open` | — | Prekės kombinuotosios nomenklatūros kodas nurodytas prekės klasifikavimo akte | — |
| `prekes_kodas1_akte` | `string` | — | `4` | `open` | — | Papildomas prekės kodas nr.1 nurodytas prekių klasifikavimo akte | — |
| `prekes_kodas2_akte` | `string` | — | `4` | `open` | — | Papildomas prekės kodas nr.2 nurodytas prekių klasifikavimo akte | — |
| `prekes_kodas3_akte` | `string` | — | `4` | `open` | — | Papildomas prekės kodas nr.3 nurodytas prekių klasifikavimo akte | — |
| `prekes_kodas4_akte` | `string` | — | `4` | `open` | — | Papildomas prekės kodas nr.4 nurodytas prekių klasifikavimo akte | — |
| `deklaruotas_taric_kodas` | `string` | — | `4` | `open` | — | Deklaruotas prekės kombinuotosios nomenklatūros kodas | — |
| `deklaruotas_prekes_kodas1` | `string` | — | `4` | `open` | — | Deklaruotas papildomas prekės kodas nr.1 | — |
| `deklaruotas_prekes_kodas2` | `string` | — | `4` | `open` | — | Deklaruotas papildomas prekės kodas nr.2 | — |
| `deklaruotas_prekes_kodas3` | `string` | — | `4` | `open` | — | Deklaruotas papildomas prekės kodas nr.3 | — |
| `deklaruotas_prekes_kodas4` | `string` | — | `4` | `open` | — | Deklaruotas papildomas prekės kodas nr.4 | — |
| `meginio_emimo_priezastis` | `string` | — | `4` | `open` | — | Mėginio ėmimo priežastis | — |
| `meginio_paemimo_numeris` | `string` | — | `4` | `open` | — | Šifruotas mėginio paėmimo numeris | — |
| `teritorine_muitine` | `string` | — | `4` | `open` | — | Teritorinės muitinės, kurioje paimtas mėginys, pavadinimas | — |
| `muitines_posto_kodas` | `string` | — | `4` | `open` | — | Muitinės , kurioje paimtas mėginys, posto kodas | — |
| `muitines_procedura` | `string` | — | `4` | `open` | — | Muitinės procedūra | — |
| `eksporto_salis` | `string` | — | `4` | `open` | — | Eksporto šalis | — |
| `importo_salis` | `string` | — | `4` | `open` | — | Importo šalis | — |
| `eksportuotojas` | `string` | — | `4` | `open` | — | Šifruotas eksportuotojas | — |
| `importuotojas` | `string` | — | `4` | `open` | — | Šifruotas importuotojas | — |
| `ypatingos_salygos_meginiui_paimti` | `boolean` | — | `4` | `open` | — | Požymis, ar mėginiui paimti reikalingos ypatingos sąlygos (užšaldymas) | — |
| `meginio_paemimo_laikas` | `datetime` | — | `4` | `open` | — | Mėginio paėmimo laikas | — |
| `ar_meginys_skubus` | `boolean` | — | `4` | `open` | — | Požymis ar mėginys skubus | — |
| `isvados_numeris` | `string` | — | `4` | `open` | — | Šifruotas mėginio išvados numeris | — |
| `ar_isvada_panaikinta` | `boolean` | — | `4` | `open` | — | Požymis ar išvada panaikinta | — |
| `registravimo_isvadai_data` | `date` | `D` | `4` | `open` | — | Registravimo išvadai data | — |
| `isvados_data` | `datetime` | — | `4` | `open` | — | Išvados pateikimo data | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Prekės kilmės šalis | — |
| `sprendimo_numeris` | `string` | — | `4` | `open` | — | Šifruotas muitinės sprendimo numeris dėl prekių | — |
| `sprendimo_data` | `date` | `D` | `4` | `open` | — | Muitinės sprendimo data | — |
| `bauda` | `number` | — | `4` | `open` | — | Baudos suma iš privalomos sumokėti sumos | — |
| `baudos_valiuta` | `string` | — | `4` | `open` | — | Baudos valiuta | — |
| `mokama_suma` | `number` | — | `4` | `open` | — | Privaloma sumokėti suma muitinei | — |
| `mokejimo_valiuta` | `string` | — | `4` | `open` | — | Privalomos sumokėti sumos valiuta | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pazeidimu_nustatymai` | — | `"Prekės kodas pasikeitė"` | — | — | — |
| `pazeidimu_nustatymai` | — | `"Prekės kodas nepasikeitė"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_meginiai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_meginiai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_meginiai (https://data.gov.lt/datasets/2834/)
