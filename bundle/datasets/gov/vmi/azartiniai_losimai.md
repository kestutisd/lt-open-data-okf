---
type: Dataset
title: "Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys"
description: "Deklaraciją pildo juridiniai asmenys, organizuojantys azartinius lošimus pagal Azartinių lošimų įstatymą."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai"
tags: [gov, vmi, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1923/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/azartiniai_losimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys

Deklaraciją pildo juridiniai asmenys, organizuojantys azartinius lošimus pagal Azartinių lošimų įstatymą. Daugiau informacijos apie mokestį galite rasti Lietuvos Respublikos loterijų ir lošimų mokesčio įstatyme[^manifest]

- **Namespace:** `datasets/gov/vmi/azartiniai_losimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1923/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai`[^dcat]
- **Portal Title (`@lt`):** Azartinių lošimų verslo loterijų ir lošimų mokesčio duomenys[^dcat]
- **Portal Title (`@en`):** Gambling business lotteries and gambling tax data[^dcat]
- **Issued (`dct:issued`):** `2023-10-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-03-09` .. `2025-12-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Azartinių lošimų organizatorių deklaruotų šios veiklos mokesčių (formų FR0584) duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on income declared by gambling operators from this activity and tax to the budget (forms FR0584)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bendrieji](azartiniai_losimai/Bendrieji.md) | Bendrieji azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų duomenys | `3` | — | — | `4` | — |
| [ADalis](azartiniai_losimai/ADalis.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų A dalies duomenys | `3` | — | — | `4` | Iki 2022-06-30 deklaracijos A dalis naudota azartiniams lošimams, bet be lošimų įrenginių. |
| [BDalis](azartiniai_losimai/BDalis.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų B dalies duomenys | `3` | — | — | `7` | Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje. |
| [LosimoTipas](azartiniai_losimai/LosimoTipas.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų lošimo tipai | `3` | — | — | `4` | — |
| [IrenginioTipas](azartiniai_losimai/IrenginioTipas.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų įrenginio tipai | `3` | — | — | `7` | Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/azartiniai_losimai (https://data.gov.lt/datasets/1923/)
