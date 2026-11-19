---
type: Table
title: "AtvejaiPagalDarbovietes — COVID-19 atvejai pagal darbovietes"
description: "Pateikta paskutinių 14 dienų naujų COVID-19 atvejų istorija anonimizuotose įstaigose (su veiklos pobūdžio aprašymu)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/AtvejaiPagalDarbovietes"
tags: [gov, lsd, atvejaipagaldarbovietes, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AtvejaiPagalDarbovietes — COVID-19 atvejai pagal darbovietes

Pateikta paskutinių 14 dienų naujų COVID-19 atvejų istorija anonimizuotose įstaigose (su veiklos pobūdžio aprašymu)[^manifest]

- **Model:** `datasets/gov/lsd/covid19/AtvejaiPagalDarbovietes`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/AtvejaiPagalDarbovietes` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitine_para` | `string` | — | `2` | `open` | — | Vakardienos para | — |
| `apskritis` | `string` | — | `2` | `open` | — | Apskritis (iš dešimties Lietuvos apskričių), kurioje registruota įstaiga | — |
| `jau_tirta_nvsc` | `string` | — | `2` | `open` | — | Rodo, kada NVSC paskutinį kartą pateikė duomenis apie šioje įstaigoje galimai | — |
| `darbuotojai` | `integer` | `U` | `4` | `open` | — | Apytikslis apskaičiavimas, kiek įstaigoje dirba darbuotojų | — |
| `atvejai_viso` | `integer` | `U` | `4` | `open` | — | Kiek šioje įstaigoje dirbančių asmenų yra gavę teigiamą diagnostinio COVID testo | — |
| `atvejai_14d` | `integer` | `U` | `4` | `open` | — | Kiek per paskutines 14 dienų iš šioje įstaigoje dirbančių asmenų pirmą kartą savo | — |
| `norma_14d` | `integer` | `U` | `4` | `open` | — | Remiantis bendru populiacijos užsikrėtimų dažniu, kiek būtų galima tokioje įstaigoje | — |
| `atveju_istorija` | `string` | — | `2` | `open` | — | Atvejų istorija | — |
| `testavimo_istorija` | `string` | — | `2` | `open` | — | Tas pats kaip ir atvejų istorija, tačiau atvaizduoja testavimų apimtis (teigiamus ir neigiamus diagnostinius COVID testus) | — |
| `testai_14d` | `integer` | `U` | `4` | `open` | — | Kiek iš viso įstaigos darbuotojams buvo atlikta diagnostinių COVID testų per paskutines 14 d. | — |
| `aliarmas` | `string` | — | `3` | `open` | — | Informuoja, ar naujų atvejų skaičius įstaigoje per 14 d. neviršija normos | — |
| `imones_pavadinimas` | `string` | — | `2` | `open` | — | Neskelbiamas, kol nėra aiškus poreikis ir nauda visuomenei | — |
| `veiklos_pobudis` | `string` | — | `2` | `open` | — | Apytikslis veiklos, kuria užsiima įstaiga, pobūdžio aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)
