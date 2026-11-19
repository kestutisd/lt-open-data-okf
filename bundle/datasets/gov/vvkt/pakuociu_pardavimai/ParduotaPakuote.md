---
type: Table
title: "ParduotaPakuote — Vaistinių preparatų pakuočių pardavimai"
description: "\"Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie mėnesinius vaistinių preparatų pakuočių pardavimus vaistinėse, asmens sveikatos priežiūros įstaigose, mažmenoje ir pavieniams asmenims."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote"
tags: [gov, vvkt, parduotapakuote, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2941/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/pakuociu_pardavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ParduotaPakuote — Vaistinių preparatų pakuočių pardavimai

**Dataset Context:** "Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie mėnesinius vaistinių preparatų pakuočių pardavimus vaistinėse, asmens sveikatos priežiūros įstaigose, mažmenoje ir pavieniams asmenims. Lentelėje pateikiami nuo 2017 m. kaupiami duomenys. Kiekviena eilutė nurodo, kiek konkrečios vaistų pakuotės vienetų buvo parduota atitinkamą mėnesį. Taip pat nurodoma papildoma informacija apie pakuotę: bendrinis vaisto pavadinimas, stiprumas, farmacinė forma, pakuotės aprašymas, pakuotės pirminis ir antrinis dydis bei jų matavimo vienetai, vaistinio preparato pakuotės pardavimo vietos tipas ir pardavimų skaičių vienetais. Duomenų teikėjas – Valstybinė vaistų kontrolės tarnyba. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Model:** `datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote`[^manifest]
- **Dataset:** [Vaistinių preparatų pakuočių pardavimai](../pakuociu_pardavimai.md) (`datasets/gov/vvkt/pakuociu_pardavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/pakuociu_pardavimai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | "Unikalus Valstybės duomenų agentūros sugeneruotas eilutės identifikatorius. Eilutės unikalumą sudaro pakid, data, pardavimai" |
| `pakid` | `string` | — | `4` | `open` | — | Pakuotės identifikacinis numeris | — |
| `npakid` | `string` | — | `4` | `open` | — | Nacionalinis vaistinio preparato pakuotės identifikatorius | — |
| `vid` | `string` | — | `4` | `open` | — | Vaistinio preparato identifikacinis numeris | — |
| `data` | `date` | `M` | `4` | `open` | — | Pardavimų data | "Data, nurodanti pardavimų ataskaitą už konkretų mėnesį" |
| `bendrinis_pavadinimas` | `string` | — | `4` | `open` | — | Vaistinio preparato bendrinis pavadinimas | — |
| `farmacine_forma` | `string` | — | `4` | `open` | — | Vaisto fizinė forma | — |
| `pakuote` | `string` | — | `4` | `open` | — | Pakuotės aprašymas | — |
| `pakuotes_pirminis_dydis` | `string` | — | `3` | `open` | — | Pakuotės pirminis dydis | "Pirminis pakuotės dydis, nurodantis vaistinio preparato dozės skaitinę talpą" |
| `pakuotes_matav_vnt` | `string` | — | `4` | `open` | — | Pakuotės pirminio dydžio matavimo vienetai | — |
| `pakuotes_antrinis_dydis` | `string` | — | `3` | `open` | — | Pakuotės antrinis dydis | "Antrinis pakuotės dydis, nurodantis dozių skaičių pakuotėje" |
| `stiprumas` | `string` | — | `4` | `open` | — | Vaistinio preparato stiprumas | — |
| `pardavimai` | `string` | — | `4` | `open` | — | Vaistų pardavimo tipai | — |
| `parduota_vnt` | `integer` | — | `4` | `open` | — | Parduotas vaistinių preparatų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pardavimai` | — | `"Mažmenai"` | — | — | — |
| `pardavimai` | — | `"Vaistinėms"` | — | — | — |
| `pardavimai` | — | `"Pavieniams pacientams"` | — | — | — |
| `pardavimai` | — | `"ASPĮ"` | — | Asmens sveikatos priežiūros įstaigoms | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/pakuociu_pardavimai (https://data.gov.lt/datasets/2941/)
