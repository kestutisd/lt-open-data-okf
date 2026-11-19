---
type: Table
title: "LaboratorinisTyrimas — LSMU Kauno Klinikų laboratorijoje pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMULKK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai/LaboratorinisTyrimas"
tags: [gov, lsmu, laboratorinistyrimas, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/lab_tyrimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3864/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsmu/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LaboratorinisTyrimas — LSMU Kauno Klinikų laboratorijoje pacientams atliktų laboratorinių tyrimų rezultatai

**Dataset Context:** Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMULKK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys. Rinkinyje pateikiama pacientų informacija: pseudonimizuotas asmens kodas, gimimo metai, lytis, tyrimų duomenys – tyrimo grupė, užsakymo laikas, pavadinimas, trumpinys; taip pat tyrimų atsakymai – rezultato reikšmė, tipas, matavimo vienetai, normos ir jų ribos. Duomenyse asmenų gimimo metai „triukšminti“ (gimimo metai nurodomi su +-1 metų paklaida). Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lsmu/lab_tyrimai/LaboratorinisTyrimas`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lsmu/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/lab_tyrimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai/LaboratorinisTyrimas` (`deployed`)[^manifest]
- **Provider:** `lsmu` — Lietuvos sveikatos mokslų universitetas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Užsakymo identifikatorius | — |
| `uzsakymo_laikas` | `datetime` | `N` | `4` | `open` | — | Užsakymo tikslus laikas | — |
| `asm_id` | `string` | — | `4` | `open` | — | Paciento eilutės identifikatorius | — |
| `asm_identifikatorius` | `string` | — | `4` | `open` | — | Pacientui priskirtas identifikatorius | — |
| `identifikatoriaus_tipas` | `string` | — | `4` | `open` | — | Identifikatoriaus tipas | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Paciento asmens kodo trūkumai | — |
| `ak_lytis` | `string` | — | `4` | `open` | — | Asmens kode nurodyta paciento lytis | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis (Angliškos reikšmės) | — |
| `gim_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `ak_gim_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai nurodyti asmens kode | — |
| `tyr_grupe` | `string` | — | `4` | `open` | — | Tyrimo grupe | — |
| `tyr_trumpas_pav` | `string` | — | `4` | `open` | — | Tyrimo pavadinimo trumpinys | — |
| `tyr_pav` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `rez_tipas` | `string` | — | `4` | `open` | — | Rezultato tipas | — |
| `rez_rezultatas` | `string` | — | `4` | `open` | — | Rezultatato reikšmė | — |
| `rez_vienetai` | `string` | — | `4` | `open` | — | Rezultato matavimo vienetai | — |
| `rez_normos` | `string` | — | `4` | `open` | — | Rezultato normos reikšmė | — |
| `rez_normos_apatine` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato minimali norma | — |
| `rez_normos_virsutine` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato maksimali norma | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `identifikatoriaus_tipas` | `"LTU"` | — | — | Lietuviškas asmens kodas | — |
| `identifikatoriaus_tipas` | `"ORGANIZATION"` | — | — | LSMU Kauno klinikų unikalus identifikatorius | — |
| `identifikatoriaus_tipas` | `"DIK_CODE"` | — | — | Draudžiamojo identifikacinis kodas | — |
| `identifikatoriaus_tipas` | `"ESI_CODE"` | — | — | E-sveikatos identifikacinis kodas | — |
| `identifikatoriaus_tipas` | `"living_subject_link"` | — | — | Kitas vidinis unikalus asmens identifikatorius | — |
| `identifikatoriaus_tipas` | `"UNDEF"` | — | — | Neatpažintas kodas | — |
| `ak_validacija` | `"Tinkamas"` | — | — | Asmens kodas atitinka LT asmens kodo sudarymo taisykles | — |
| `ak_validacija` | `"Netinkamas ilgis"` | — | — | Asmens kodas netinkamo ilgio | — |
| `ak_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Asmens kode nurodytas netinkamas paskutinis skaitmuo | — |
| `ak_validacija` | `"Netinkama gimimo data"` | — | — | Asmens kode nurodyta netinkama gimimo data | — |
| `ak_lytis` | `"Moteris"` | — | — | Moteris | — |
| `ak_lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"F"` | — | — | Moteris (Female) | — |
| `lytis` | `"M"` | — | — | Vyras (Male) | — |
| `rez_tipas` | `"QN"` | — | — | Skaitinės reikšmės rezultatas | — |
| `rez_tipas` | `"CODED"` | — | — | Rezultato reikšmė pateikta iš žodyno | — |
| `rez_tipas` | `"NAR"` | — | — | Tekstinės rezultato reikšmės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/lab_tyrimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsmu/lab_tyrimai (https://data.gov.lt/datasets/3864/)
