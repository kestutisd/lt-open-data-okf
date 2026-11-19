---
type: Dataset
title: "Vaistinių preparatų pakuočių pardavimai"
description: "\"Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie mėnesinius vaistinių preparatų pakuočių pardavimus vaistinėse, asmens sveikatos priežiūros įstaigose, mažmenoje ir pavieniams asmenims."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai"
tags: [gov, vvkt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2941/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/pakuociu_pardavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vaistinių preparatų pakuočių pardavimai

"Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie mėnesinius vaistinių preparatų pakuočių pardavimus vaistinėse, asmens sveikatos priežiūros įstaigose, mažmenoje ir pavieniams asmenims. Lentelėje pateikiami nuo 2017 m. kaupiami duomenys. Kiekviena eilutė nurodo, kiek konkrečios vaistų pakuotės vienetų buvo parduota atitinkamą mėnesį. Taip pat nurodoma papildoma informacija apie pakuotę: bendrinis vaisto pavadinimas, stiprumas, farmacinė forma, pakuotės aprašymas, pakuotės pirminis ir antrinis dydis bei jų matavimo vienetai, vaistinio preparato pakuotės pardavimo vietos tipas ir pardavimų skaičių vienetais. Duomenų teikėjas – Valstybinė vaistų kontrolės tarnyba. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/vvkt/pakuociu_pardavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/pakuociu_pardavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2941/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai`[^dcat]
- **Portal Title (`@lt`):** Vaistinių preparatų pakuočių pardavimai[^dcat]
- **Portal Title (`@en`):** Sales of packaging of medicinal products[^dcat]
- **Issued (`dct:issued`):** `2025-03-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-03-20` .. `2026-10-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami didmeninio platinimo įmonių kas mėnesį Valstybinei vaistų kontrolės tarnybai (VVKT) teikiami duomenys apie parduotus vaistinių preparatų pakuočių kiekius vaistinėms, asmens sveikatos priežiūros įstaigoms, mažmenai ir pavieniams asmenims. Lentelėje pateikiami nuo 2017 m. kaupiami duomenys. Kiekviena eilutė nurodo, kiek konkrečios vaistų pakuotės vienetų buvo parduota atitinkamą mėnesį. Taip pat nurodoma papildoma informacija apie pakuotę: bendrinis vaisto pavadinimas, stiprumas, farmacinė forma, pakuotės aprašymas, pakuotės pirminis ir antrinis dydis bei jų matavimo vienetai, vaistinio preparato pakuotės pardavimo vietos tipas ir pardavimų skaičių vienetais. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall provide monthly data of wholesale distribution companies to the State Medicines Control Agency (LPT) on the quantities of packages of medicinal products sold to pharmacies, personal health care institutions, retailers and individuals. Each row shall indicate the number of units of a specific package of medicinal products sold in a given month. Additional packaging information shall also be provided: ATC code, generic name, strength, pharmaceutical form, description of packaging, initial and secondary size of packaging, quantity of component, daily dose determined (DDD) and translating factor of the product component and DDD content into grams. The last two columns indicate the type of product packaging sales point and the number of sales in units. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ParduotaPakuote](pakuociu_pardavimai/ParduotaPakuote.md) | Vaistinių preparatų pakuočių pardavimai | `4` | `vda_prime_key` | — | `14` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/pakuociu_pardavimai (https://data.gov.lt/datasets/2941/)
