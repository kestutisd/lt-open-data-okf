---
type: Dataset
title: "Juridinių asmenų mokestinė nepriemoka"
description: "Svarbu: teikiami duomenys nėra vertinami pagal 2005 m. rugsėjo 16 d."
resource: "https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos"
tags: [gov, vmi, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/ja_nepriemokos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1202/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/ja_nepriemokos"
    author: "team:vda"
    last_modified: "2026-03-03T00:00:00Z"
---

# Juridinių asmenų mokestinė nepriemoka

- **Namespace:** `datasets/gov/vmi/ja_nepriemokos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/ja_nepriemokos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1202/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų mokestinė nepriemoka[^dcat]
- **Portal Title (`@en`):** Data about legal entities with tax arrears[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-03-03`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Svarbu: teikiami duomenys nėra vertinami pagal 2005 m. rugsėjo 16 d. VMI prie FM viršininko įsakymu Nr. VA-67 patvirtintas Mokesčių mokėtojų skolingumo nustatymo taisykles, skelbiami statistiniai duomenys apie juridinio asmens nepriemoką konkrečiam laikotarpiui. Duomenys apie juridinius asmenis turinčius mokestinę nepriemoką, atskirai išskiriant (neįskaitant vykdomųjų dokumentų): Pradelstą nepriemoką (JA pradelsta mokestinės nepriemokos suma), Atidėtą nepriemoką (JA pagal mokestinės paskolos sutartį, susitarimą dėl pagalbos, restruktūrizavimo planą, mokumo atkūrimo planą, taikos sutartį atidėtos nepriemokos likutis), Atidėtą pradelstą nepriemoką (JA pagal mokestinės paskolos sutartį, susitarimą dėl pagalbos, restruktūrizavimo planą, mokumo atkūrimo planą, taikos sutartį, pradelsta suma). Duomenys gaunami iš Mokesčių apskaitos informacinės sistemos apie konkretaus juridinio asmens mokėtojo nepriemoką. Atkreiptinas dėmesys, kad teikiami duomenys nėra vertinami pagal Mokesčių mokėtojų skolingumo nustatymo taisykles. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on legal entities with tax arrears, separately (excluding executive documents): Overdue arrears (the amount of overdue tax arrears is overdue), Deferred arrears (JA under tax loan agreement, aid agreement, restructuring plan, solvency restoration plan, balance of deferred arrears), Deferred overdue arrears (JA under tax loan agreement, aid agreement, restructuring plan, solvency restoration plan, settlement agreement, overdue amount). The data is obtained from the Tax Accounting Information System on the non-surcharge of a particular legal entity.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NepriemokosSuma](ja_nepriemokos/NepriemokosSuma.md) | Juridinių asmenų nepriemokos sumos | — | — | — | `10` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/ja_nepriemokos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/ja_nepriemokos (https://data.gov.lt/datasets/1202/)
