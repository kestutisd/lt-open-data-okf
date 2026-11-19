---
type: Dataset
title: "Pastatų ir jo elementų nusidėvėjimas ir rizikos"
description: "Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas"
tags: [gov, ssva, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4143/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pastatu_duomenu_bankas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pastatų ir jo elementų nusidėvėjimas ir rizikos

Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę.[^manifest]

- **Namespace:** `datasets/gov/ssva/pastatu_duomenu_bankas`[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4143/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Pastatų ir jų elementų rizikos bei nusidėvėjimo duomenų rinkiniai[^dcat]
- **Portal Title (`@en`):** Sets of risk and depreciation data for buildings and their elements[^dcat]
- **Issued (`dct:issued`):** `2026-02-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie pastatų techninę būklę, riziką ir nusidėvėjimą rengiami vadovaujantis Statinio techninės būklės vertinimo taisyklėmis (ASR) ir sudaro tris tarpusavyje susijusius, tačiau savarankiškus duomenų rinkinius. Tokia struktūra leidžia atskirai analizuoti bendrą pastato būklę ir detaliai vertinti kiekvieno elemento techninę būklę bei riziką. Pirmąjį rinkinį sudaro pastato rizikos ir nusidėvėjimo agreguotu lygmeniu duomenys. Jame pateikiamas bendras objekto nusidėvėjimo balas, bendras rizikos balas, statybos metai, adresas, savivaldybė bei geografinė padėtis. Šie rodikliai apskaičiuojami įvertinus visų pastato elementų būklę pagal ASR metodiką ir leidžia nustatyti bendrą statinio techninę būklę bei prioritetus priežiūrai ar renovacijai. Antrasis rinkinys skirtas pastato elementų rizikos duomenims. Jame detalizuojama atskirų elementų (pvz., pamatų, sienų, stogo, inžinerinių sistemų, balkonų, laiptinių ir kt.) rizika pagal atitinkamas saugos ir esminių statinio reikalavimų kategorijas, tokias kaip mechaninis atsparumas, gaisrinė sauga, higiena, energinis efektyvumas ar kiti reglamente nustatyti kriterijai. Kiekvienam elementui priskiriamas rizikos balas, vertinimo balas, didžiausia galima balo reikšmė bei požymis, nurodantis, ar nustatyta kritinė rizika. Tai leidžia identifikuoti konkrečias problemines vietas pastate. Trečiasis rinkinys apima pastato elementų nusidėvėjimo duomenis. Jame pateikiama informacija apie kiekvieno elemento tarnavimo trukmę, faktinį nusidėvėjimo procentą, statybos metus, objekto adresą bei kitus identifikavimo duomenis. Nusidėvėjimo vertinimas atliekamas pagal ASR nustatytus kriterijus, atsižvelgiant į fizinę būklę, eksploatacijos laiką ir kitus techninius parametrus. Duomenų rinkiniai atnaujinami kiekvieną savaitę. Visi duomenys pateikiami atsižvelgiant į teisės aktų keliamus duomenų atvėrimo reikalavimus. Duomenų teikėjas – Statybos sektoriaus vystymo agentūra. Reglamento tekstas prieinamas: https://www.e-tar.lt/portal/lt/legalAct/f5109e80ce8811e69e09f35d37acd719/asr Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PastatoElementoRizika](pastatu_duomenu_bankas/PastatoElementoRizika.md) | — | `4` | `rizikos_vertinimo_id` | — | `14` | — |
| [PastatoElementoNusidevejimas](pastatu_duomenu_bankas/PastatoElementoNusidevejimas.md) | — | `4` | `elemento_id` | — | `9` | — |
| [PastatoRizikaNusidevejimas](pastatu_duomenu_bankas/PastatoRizikaNusidevejimas.md) | — | — | `objekto_id` | — | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pastatu_duomenu_bankas (https://data.gov.lt/datasets/4143/)
