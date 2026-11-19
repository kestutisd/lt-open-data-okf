---
type: Table
title: "Dokumentas — Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys"
description: "\"Lietuvos muitinei pateikiamų dokumentų sąrašas tvarkomas Lietuvos Respublikos integruoto tarifo (LITAR) sistemoje (https://litarweb.lrmuitine.lt/taric/web/certsearchform_LT)."
resource: "https://get.data.gov.lt/datasets/gov/muitine/dokumentu_sarasas/Dokumentas"
tags: [gov, muitine, dokumentas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/muitine/dokumentu_sarasas.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3818/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/dokumentu_sarasas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dokumentas — Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys

**Dataset Context:** "Lietuvos muitinei pateikiamų dokumentų sąrašas tvarkomas Lietuvos Respublikos integruoto tarifo (LITAR) sistemoje (https://litarweb.lrmuitine.lt/taric/web/certsearchform_LT). Sąraše pateikiama informacija apie Lietuvos muitinei pateikiamus dokumentus (dokumentų rūšis), kurių duomenys nurodomi muitinės deklaracijose. Vienoje eilutėje pateikiama tam tikru laikotarpiu galiojančio vieno dokumento informacija: dokumento rūšis, rūšies galiojimo pradžios ir pabaigos data, rūšies pavadinimas, rūšies kodas (dokumento rūšis ir 3 simolių kodas), dokumento kodo galiojimo pradžios ir pabaigos data, kodo pavadinimas, bei dokumento pavadinimo įsigaliojimo data. Paskutiniame stulpelyje nurodomas dokumento šaltinis (Taric arba National). Duomenų laikotarpis: nuo 2004 m. gegužės 1 d. Lietuvos Respublikoje galiojantys Europos Bendrijos integruoto tarifo (TARIC) duomenys apie dokumentus, papildyti nuo 2004 m. gegužės 1 d. galiojančiais nacionalinių dokumentų duomenimis. Duomenų teikėjas – Muitinės departamentas prie Lietuvos Respublikos finansų ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Model:** `datasets/gov/muitine/dokumentu_sarasas/Dokumentas`[^manifest]
- **Dataset:** [Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys](../dokumentu_sarasas.md) (`datasets/gov/muitine/dokumentu_sarasas`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/dokumentu_sarasas.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/dokumentu_sarasas/Dokumentas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | "Unikalus Valstybės duomenų agentūros eilutės identifikatorius. Eilutės unikalumą sudaro stulpeliai - rusies_kodas, dok_pav, pav_galioja_nuo" |
| `dok_rusis` | `string` | — | `4` | `open` | — | Dokumento rūšis | — |
| `rusis_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento rūšies galiojimo pradžios data | — |
| `rusis_galioja_iki` | `date` | `D` | `4` | `open` | — | Dokumento rūšies galiojimo pabaigos data | — |
| `rusies_pav` | `string` | — | `4` | `open` | — | Dokumento rūšies pavadinimas | — |
| `rusies_kodas` | `string` | — | `4` | `open` | — | Dokumento rūšies kodas | — |
| `kod_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento rūšies kodas galiojimo pradžia | — |
| `kod_galioja_iki` | `date` | `D` | `4` | `open` | — | Dokumento rūšies kodo galiojimo pabaiga | — |
| `dok_kod_pav` | `string` | — | `3` | `open` | — | Dokumento rūšies kodo pavadinimas | — |
| `kod_pav_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento rūšies kodo pavadinimo galiojimo pradžios data | — |
| `dok_saltinis` | `string` | — | `4` | `open` | — | Dokumento šaltinis | "Dokumento šaltinis. Požymis TARIC reiškia, kad dokumento įrašas gautas iš Europos Sąjungos integruoto tarifo (TARIC) duomenų bazės. Požymis National reiškia, kad dokumento įrašas yra iš dokumentų nacionalinių kodų sąrašo" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dok_saltinis` | `"Taric"` | — | — | Taric | Dokumento įrašas gautas iš Europos Sąjungos integruoto tarifo (TARIC) duomenų bazės |
| `dok_saltinis` | `"National"` | — | — | National | Dokumento įrašas yra iš dokumentų nacionalinių kodų sąrašo |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/dokumentu_sarasas.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/dokumentu_sarasas (https://data.gov.lt/datasets/3818/)
