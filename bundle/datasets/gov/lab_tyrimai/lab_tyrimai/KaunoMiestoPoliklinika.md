---
type: Table
title: "KaunoMiestoPoliklinika — Kauno miesto poliklinikos pacientams atliktų laboratorinių tyrimų duomenys"
description: "VšĮ Kauno miesto poliklinikos (KMP) POLIS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/KaunoMiestoPoliklinika"
tags: [gov, lab_tyrimai, kaunomiestopoliklinika, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L105"
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L105"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2700/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-23T00:00:00Z"
---

# KaunoMiestoPoliklinika — Kauno miesto poliklinikos pacientams atliktų laboratorinių tyrimų duomenys

VšĮ Kauno miesto poliklinikos (KMP) POLIS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. Duomenys kaupiami nuo 2020 m. ir yra atnaujinami iki šiol. Duomenų rinkinio kaupiami duomenys apima paciento šifruotą identifikatorių, lytį, gimimo metus, tyrimo užsakymo datą dienos tikslumu, tyrimo pavadinimą, tyrimo rezultatus bei nurodytas apatines ir viršutines normas. Rinkinyje viena eilutė nurodo vieno asmens vieną konkretų tyrimą. PASITERIAVIMUI: Valstybės duomenų valdysenos atvėrimo komanda: atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/KaunoMiestoPoliklinika`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L105](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L105)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/KaunoMiestoPoliklinika` (`deployed`)[^manifest]
- **Provider:** `lab_tyrimai`[^manifest]
- **Primary Key (`ref`):** `vda_primary_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-23`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_primary_key` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `uzsakymo_data` | `date` | `D` | `4` | `open` | — | Užsakymo data | — |
| `asm_ak` | `string` | — | `4` | `open` | — | Asmens kodas | Paciento asmens kodas (duomenys hash'inti) |
| `vda_ak_asm_validacija` | `string` | — | `4` | `open` | — | Asmens kodo validacija | — |
| `asm_lytis` | `string` | — | `4` | `open` | — | Asmens lytis | Duomenys ateina iš tiekėjo duomenų bazės |
| `vda_lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | Lytis paimta iš asmens kodo |
| `vda_gimimo_metai` | `date` | `D` | `4` | `open` | — | Asmens gimimo metai | Gimimo metai paimti iš asmens gimimo datos. Metai triukšminti +-1 metai |
| `tyr_pavadinimas` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `rez_tyr_kodas` | `string` | — | `4` | `open` | — | Tyrimų rezultato kodas | — |
| `rez_tyr_pav` | `string` | — | `4` | `open` | — | Tyrimo rezultato pavadinimas | — |
| `rez_rezultatas` | `string` | — | `2` | `open` | — | Rezultatas | — |
| `rez_vienetai` | `string` | — | `4` | `open` | — | Rezultato vienetai | — |
| `rez_normos` | `string` | — | `3` | `open` | — | Rezultato normos | — |
| `rez_normos_apatine` | `string` | — | `4` | `open` | — | Rezultato apatinė norma | — |
| `rez_normos_virsutine` | `string` | — | `4` | `open` | — | Rezultato viršutinė norma | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vda_lytis_ak` | `"Vyras"` | — | — | Vyras | — |
| `vda_lytis_ak` | `"Moteris"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L105 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L105)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai (https://data.gov.lt/datasets/2700/)
