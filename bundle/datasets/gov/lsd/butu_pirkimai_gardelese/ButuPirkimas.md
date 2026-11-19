---
type: Table
title: "ButuPirkimas — Agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties (butų) objektų pirkimų sandorių duomenys 1 km stačiakampėse gardelėse."
description: "Lentelėje pateikiami agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties (butų) objektų pirkimų sandorių duomenys 1 km stačiakampėse gardelėse."
resource: "https://get.data.gov.lt/datasets/gov/lsd/butu_pirkimai_gardelese/ButuPirkimas"
tags: [gov, lsd, butupirkimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/butu_pirkimai_gardelese.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/butu_pirkimai_gardelese.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2559/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/butu_pirkimai_gardelese"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ButuPirkimas — Agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties (butų) objektų pirkimų sandorių...

Lentelėje pateikiami agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties (butų) objektų pirkimų sandorių duomenys 1 km stačiakampėse gardelėse. Laiko aprėptis - nuo 1998 m. Duomenys šiame rinkinyje apima ne visus gyvenamosios (butų) paskirties objektų pirkimų aibės sandorius, bet tik tuos sandorius, kurių metu įsigytas tik vienas objektas. Informacija apie sandorius, kurių metu buvo perkami keli objektai (pvz.: butas ir sandėliukas arba butas ir žemės skypas) šioje lentelėje nepateikiami. Geografinė informacija (gardelės) gauta iš VĮ Registrų centro Adresų registro.[^manifest]

- **Model:** `datasets/gov/lsd/butu_pirkimai_gardelese/ButuPirkimas`[^manifest]
- **Dataset:** [Nekilnojamojo turto registro butų pirkimų sandorių informacija gardelėse](../butu_pirkimai_gardelese.md) (`datasets/gov/lsd/butu_pirkimai_gardelese`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/butu_pirkimai_gardelese.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/butu_pirkimai_gardelese.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/butu_pirkimai_gardelese/ButuPirkimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `sq_grid_id` | `ref` | [Grid1KmSq](../grid/Grid1KmSq.md) (`level=4 UUID`: `sq_grid_id._id`) | `4` | `open` | — | Stačiakampės 1km gardelės unikalus identifikatorius | — |
| `data_nuo` | `date` | `Y` | `4` | `open` | — | Laikotarpio (metų) pradžios data | — |
| `data_iki` | `date` | `Y` | `4` | `open` | — | Laikotarpio (metų) pabaigos data | — |
| `sandoriu_sk` | `number` | `U` | `4` | `open` | — | Unikalių sandorių skaičius | — |
| `objektu_sk` | `number` | `U` | `4` | `open` | — | Unikalių nekilnojamojo turto objektų (butų) skaičius | — |
| `vid_sandorio_verte` | `number` | — | `4` | `open` | — | Sandorių verčių vidurkis (Eur) | — |
| `min_sandorio_verte` | `number` | — | `4` | `open` | — | Sandorių verčių mažiausia vertė (Eur) | — |
| `sandorio_verte_p10` | `number` | — | `4` | `open` | — | Sandorių verčių 10-asis procentilis (Eur) | — |
| `sandorio_verte_p20` | `number` | — | `4` | `open` | — | Sandorių verčių 20-asis procentilis (Eur) | — |
| `sandorio_verte_p30` | `number` | — | `4` | `open` | — | Sandorių verčių 30-asis procentilis (Eur) | — |
| `sandorio_verte_p40` | `number` | — | `4` | `open` | — | Sandorių verčių 40-asis procentilis (Eur) | — |
| `sandorio_verte_p50` | `number` | — | `4` | `open` | — | Sandorių verčių 50-asis procentilis (Eur) | — |
| `sandorio_verte_p60` | `number` | — | `4` | `open` | — | Sandorių verčių 60-asis procentilis (Eur) | — |
| `sandorio_verte_p70` | `number` | — | `4` | `open` | — | Sandorių verčių 70-asis procentilis (Eur) | — |
| `sandorio_verte_p80` | `number` | — | `4` | `open` | — | Sandorių verčių 80-asis procentilis (Eur) | — |
| `sandorio_verte_p90` | `number` | — | `4` | `open` | — | Sandorių verčių 90-asis procentilis (Eur) | — |
| `maks_sandorio_verte` | `number` | — | `4` | `open` | — | Sandorių verčių didžiausia vertė (Eur) | — |
| `vid_isigytas_plotas` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių vidurkis (m2) | — |
| `min_isigytas_plotas` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių mažiausia vertė (m2) | — |
| `isigytas_plotas_p10` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 10-asis procentilis (m2) | — |
| `isigytas_plotas_p20` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 20-asis procentilis (m2) | — |
| `isigytas_plotas_p30` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 30-asis procentilis (m2) | — |
| `isigytas_plotas_p40` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 40-asis procentilis (m2) | — |
| `isigytas_plotas_p50` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 50-asis procentilis (m2) | — |
| `isigytas_plotas_p60` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 60-asis procentilis (m2) | — |
| `isigytas_plotas_p70` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 70-asis procentilis (m2) | — |
| `isigytas_plotas_p80` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 80-asis procentilis (m2) | — |
| `isigytas_plotas_p90` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių 90-asis procentilis (m2) | — |
| `maks_isigytas_plotas` | `number` | `m^2` | `4` | `open` | — | Įsigytų plotų verčių didžiausia vertė (m2) | — |
| `vid_buto_verte` | `number` | — | `4` | `open` | — | Butų verčių vidurkis (Eur/m2) | — |
| `min_buto_verte` | `number` | — | `4` | `open` | — | Butų verčių mažiausia vertė (Eur/m2) | — |
| `buto_verte_p10` | `number` | — | `4` | `open` | — | Butų verčių 10-asis procentilis (Eur/m2) | — |
| `buto_verte_p20` | `number` | — | `4` | `open` | — | Butų verčių 20-asis procentilis (Eur/m2) | — |
| `buto_verte_p30` | `number` | — | `4` | `open` | — | Butų verčių 30-asis procentilis (Eur/m2) | — |
| `buto_verte_p40` | `number` | — | `4` | `open` | — | Butų verčių 40-asis procentilis (Eur/m2) | — |
| `buto_verte_p50` | `number` | — | `4` | `open` | — | Butų verčių 50-asis procentilis (Eur/m2) | — |
| `buto_verte_p60` | `number` | — | `4` | `open` | — | Butų verčių 60-asis procentilis (Eur/m2) | — |
| `buto_verte_p70` | `number` | — | `4` | `open` | — | Butų verčių 70-asis procentilis (Eur/m2) | — |
| `buto_verte_p80` | `number` | — | `4` | `open` | — | Butų verčių 80-asis procentilis (Eur/m2) | — |
| `buto_verte_p90` | `number` | — | `4` | `open` | — | Butų verčių 90-asis procentilis (Eur/m2) | — |
| `maks_buto_verte` | `number` | — | `4` | `open` | — | Butų verčių didžiausia vertė (Eur/m2) | — |
| `vid_visuotinio_vertinimo_verte` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių vidurkis (Eur) | — |
| `min_visuotinio_vertinimo_verte` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių mažiausia vertė (Eur) | — |
| `visuotinio_vertinimo_verte_p10` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 10-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p20` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 20-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p30` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 30-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p40` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 40-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p50` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 50-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p60` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 60-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p70` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 70-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p80` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 80-asis procentilis (Eur) | — |
| `visuotinio_vertinimo_verte_p90` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių 90-asis procentilis (Eur) | — |
| `maks_visuotinio_vertinimo_verte` | `number` | — | `4` | `open` | — | Butų visuotinio vertinimo verčių didžiausia vertė (Eur) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/butu_pirkimai_gardelese.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/butu_pirkimai_gardelese.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/butu_pirkimai_gardelese (https://data.gov.lt/datasets/2559/)
