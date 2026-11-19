---
type: Dataset
title: "Būsto kainų indekso svoriai"
description: "Rinkinyje pateikiami būsto kainų indekso svoriai."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/bki_svoriai"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/bki_svoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/bki_svoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2521/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/bki_svoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Būsto kainų indekso svoriai

- **Namespace:** `datasets/gov/lsd/statistika/bki_svoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/bki_svoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/bki_svoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/bki_svoriai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2521/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/bki_svoriai`[^dcat]
- **Portal Title (`@lt`):** Būsto kainų indekso svoriai[^dcat]
- **Portal Title (`@en`):** Housing Price Index Weights[^dcat]
- **Issued (`dct:issued`):** `2023-12-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2026-04-04` .. `2026-06-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami būsto kainų indekso svoriai. Svoris – procentais arba promilėmis išreikšta namų ūkių piniginių išlaidų lyginamoji dalis tam tikrai BKI elementariajai visumai priklausantiems būstams su žeme įsigyti. Kuo didesnis svoris, tuo didesnė tam tikro būsto su žeme klasifikavimo lygio kainų pokyčio įtaka aukštesnio būsto su žeme klasifikavimo lygio kainų pokyčiui. Svorių bazinis laikotarpis – laikotarpis, kurio duomenimis remiantis skaičiuojami indekso svoriai. Atliekamos tokios gautų statistinių duomenų tikrinimo ir redagavimo procedūros: atmetami sandoriai, kuriais įsigyti būstai dėl nepakankamo baigtumo lygio (< 80 proc.) yra netinkami gyventi, analizuojami kiekvienai elementariajai visumai priskirtų būstų pirkimo–pardavimo sandorių duomenys, palyginti su ankstesnių ketvirčių duomenimis. Duomenų redagavimas ir patvirtinimas atliekamas naudojant kompiuterinę kainų statistinių duomenų tikrinimo programą. Gautos kainų kitimo tendencijos lyginamos su nekilnojamojo turto agentūrų užfiksuotomis būsto kainų kitimo tendencijomis. Informacija apie veiksnius, turinčius įtaką būsto kainų pasikeitimui, reguliariai stebima spaudoje, kitų įmonių ir institucijų skelbiamose apžvalgose ir ataskaitose. Pagrindinis statistinių duomenų šaltinis BKI apskaičiuoti yra VĮ Registrų centro Nekilnojamojo turto registro ir Sandorių duomenų bazių duomenys. Šaltinio duomenys gaunami kas ketvirtį. BKI bazinis laikotarpis yra 2015 m. (2015 m. – 100). Kitas BKI bazinio laikotarpio keitimas numatytas 2026 m., buvusi laiko eilutė bus perskaičiuota į naują indekso bazinį laikotarpį ir paskelbta apskaičiavus 2026 m. I ketv. BKI. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes the weights of the house price index. “Weight” means the percentage or promil of the relative share of household monetary expenditure for the purchase of land-based housing belonging to the basic population of the CCI. The higher the weight, the greater the impact of a change in the price level of a land-based housing classification on the price development of a higher level of land-based housing classification. “Weight reference period” means the period during which the weight of the index is calculated. The following procedures for checking and editing the statistics received are carried out: rejecting transactions in which the purchased dwellings are unfit for life due to a lack of completion (< 80%), analysing the purchase-sale transaction data of the dwellings attributed to each basic whole compared to the previous quarters. The editing and validation of data shall be carried out using a computer program for checking price statistics. The resulting price trends are compared to the trends in house prices recorded by real estate agencies. Information on factors influencing changes in house prices is regularly monitored in the press, surveys and reports published by other companies and institutions. The main source of statistical data for the calculation of the CCI is the data of the Real Property Register of the Centre of Registers of the SE and the databases of transactions. Source data is obtained quarterly. The BKI base period is 2015 (2015: 100). Another change to the CCI base period is foreseen for 2026, the former time line will be converted into a new index base period and published after calculation in QI 2026. CCI[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S7R263M2021005](bki_svoriai/S7R263M2021005.md) | Būsto kainų indekso svoriai | `4` | `vda_id` | — | `13` | Rinkinyje pateikiami būsto kainų indekso svoriai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/bki_svoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/bki_svoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/bki_svoriai (https://data.gov.lt/datasets/2521/)
