---
type: Dataset
title: "Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų klasifikatorius"
description: "Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys su prašomų įforminti procedūrų klasifikatoriumi"
resource: "https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema"
tags: [gov, muitine, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/deklaraciju_apdorojimo_sistema"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų klasifikatorius

Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys su prašomų įforminti procedūrų klasifikatoriumi[^manifest]

- **Namespace:** `datasets/gov/muitine/deklaraciju_apdorojimo_sistema`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3996/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema`[^dcat]
- **Portal Title (`@lt`):** Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijose nurodytoms prekėms prašomų įforminti procedūrų klasifikatorius[^dcat]
- **Portal Title (`@en`):** Data on customs import and export declarations and classification of the procedures requested for regularisation[^dcat]
- **Issued (`dct:issued`):** `2025-12-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2025-12-11` .. `2026-10-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje „Deklaracija“ pateikiama Išmaniojoje muitinės deklaracijų apdorojimo sistemoje nuo 2021 m. įformintų importo ir eksporto (reeksporto) deklaracijų nuasmeninta informacija. Rinkinio eilutėje pateikiami deklaracijos prekių rūšies lygmens duomenys: šifruotas deklaracijos numeris, šifruota informacija apie eksportuotoją ar importuotoją, eksportuotojo ar importuotojo šalis, deklaracijos įforminimo metai, deklaracijos rūšis, prekės kilmės šalis, prekės kombinuotos nomenklatūros kodas, svoris ir kita informacija. Duomenų rinkinyje “Procedūra“ pateikiamas klasifikatorius, skirtas aprašyti deklaracijoje nurodytoms prekėms prašomas įforminti procedūros reikšmes. Duomenų teikėjas – Lietuvos Respublikos muitinė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Duomenų rinkinyje pateikiama informacija apie LR Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenis. Rinkinį sudaro kiekvienos deklaruojamos prekės ir jos deklaracijos duomenys: šifruotas deklaracijos numeris, šifruota informacija apie eksportuotoją ar importuotoją, eksportuotojo ar importuotojo šalis, deklaracijos įforminimo metai, deklaracijos rūšis, prekės kilmės šalis, prekės kombinuotos nomenklatūros kodas, svoris ir kita informacija. Duomenys apie deklaracijas renkami nuo 2021 metų. Rinkinyje papildomai atvertas klasifikatorius, skirtas aprašyti deklaracijoje nurodytoms prekėms prašomas įforminti procedūros reikšmes. Duomenų teikėjas – Lietuvos Respublikos Muitinė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracija](deklaraciju_apdorojimo_sistema/Deklaracija.md) | Muitinės importo ir eksporto deklaracijų duomenys | `4` | `vda_prime_key` | — | `19` | Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys |
| [Procedura](deklaraciju_apdorojimo_sistema/Procedura.md) | Prašomos įforminti procedūros aprašymai pagal kodus | `4` | `vda_prime_key` | — | `8` | Prašomos įforminti procedūros aprašymų klasifikatorius pagal kodus, naudojamas muitinės deklaracijų duomenyse nurodytoms procedūroms aprašyti |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/deklaraciju_apdorojimo_sistema (https://data.gov.lt/datasets/3996/)
