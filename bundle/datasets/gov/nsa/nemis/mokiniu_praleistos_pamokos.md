---
type: Dataset
title: "Mokyklos nelankančių mokinių praleistos pamokos"
description: "Lentelėje pateikti Nesimokančių vaikų ir mokyklos nelankančių mokinių informacinėje sistemoje (NEMIS) registruojami mokyklos nelankančių mokinių praleistų pamokų skaičiai konkrečiais mėnesiais."
resource: "https://get.data.gov.lt/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos"
tags: [gov, nsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2863/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mokyklos nelankančių mokinių praleistos pamokos

- **Namespace:** `datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2863/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos`[^dcat]
- **Portal Title (`@lt`):** Mokyklos nelankančių mokinių praleistos pamokos[^dcat]
- **Portal Title (`@en`):** Lessons spent by non-school pupils[^dcat]
- **Issued (`dct:issued`):** `2024-11-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-11-21` .. `2026-10-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Nesimokančių vaikų ir mokyklos nelankančių mokinių informacinėje sistemoje (NEMIS) registruojami mokyklos nelankančių mokinių praleistų pamokų skaičiai konkrečiais mėnesiais. Mokyklos nelankantis mokinys – Mokinių registre įregistruotas vaikas, kurio deklaruota gyvenamoji vieta yra atitinkamoje savivaldybėje, arba vaikas, įrašytas į gyvenamosios vietos neturinčių asmenų apskaitą pagal savivaldybę, kurioje gyvena, tačiau be pateisinamos priežasties neatvykęs į mokyklą, praleidęs daugiau kaip pusę pamokų ar ugdymui skirtų valandų per mėnesį. Duomenys pateikiami nuo jų kaupimo sistemoje pradžios (2010 m.) atnaujinant kas mėnesį. Duomenų teikėjas – Nacionalinė švietimo agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table shows the number of lessons spent by non-school pupils for specific months from the National Education Agency (NESA) Information System for NEETs and non-school pupils (NEMIS). Data shall be provided from the beginning of their accumulation in the system (2010) by monthly updating. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PamokuNelankymas](mokiniu_praleistos_pamokos/PamokuNelankymas.md) | Mokyklos nelankančių mokinių praleistos pamokos | `4` | `iraso_id` | — | `10` | Lentelėje pateikti mokyklos nelankančių mokinių praleistų pamokų skaičiai konkretiems mėnesiams iš Nacionalinės švietimo agentūros (NŠA) Nesimokančių vaikų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos (https://data.gov.lt/datasets/2863/)
