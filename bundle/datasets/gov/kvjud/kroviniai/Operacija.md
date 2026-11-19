---
type: Table
title: "Operacija — Krovininių laivų operacijos Klaipėdos valstybinio jūrų uoste"
description: "Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/kroviniai/Operacija"
tags: [gov, kvjud, operacija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/kroviniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Operacija — Krovininių laivų operacijos Klaipėdos valstybinio jūrų uoste

**Dataset Context:** Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste. Rinkinio objektas - atvykimo arba išvykimo operacija. Duomenys pateikiami nuo 2002m. iki šių dienų. Nurodoma operacijos rūšis, laivo savininko atstovas, su laivo atvykimu/išvykimu (išvykimo ir atvykimo uostas, faktiniai išvykimo laikai) bei su laivu (pavadinimas, tipas, vėliava, IMO numeris, dedveitas ir bendroji talpa) susijusi informacija. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kvjud/kroviniai/Operacija`[^manifest]
- **Dataset:** [Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste](../kroviniai.md) (`datasets/gov/kvjud/kroviniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/kroviniai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/kroviniai/Operacija` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-sa/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agenūros įrašo unikalus identifikatorius | — |
| `operacijos_id` | `string` | — | `4` | `open` | — | Operacijos identifikatorius | — |
| `op_tipas` | `string` | — | `4` | `open` | — | Operacijos tipas | — |
| `op_rusis` | `string` | — | `4` | `open` | — | Operacijos rūšis | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Operacijos data | — |
| `agentas` | `string` | — | `4` | `open` | — | Laivo savininko atstovas uoste | — |
| `imo_kodas` | `string` | — | `4` | `open` | — | Laivo IMO numeris | — |
| `laivas` | `string` | — | `4` | `open` | — | Laivo pavadinimas | — |
| `dedveitas_t` | `number` | `t` | `4` | `open` | — | Laivo dedveitas, išreikštas tonomis. | Dedveitas - tai dydis, nurodantis, kokios masės krovinį laivas gali saugiai gabenti. |
| `bendroji_talpa` | `number` | — | `4` | `open` | — | Laivo bendroji talpa | — |
| `laivo_tipas` | `string` | — | `4` | `open` | — | Laivo tipas | — |
| `veliava` | `string` | — | `4` | `open` | — | Laivo registravimo valstybė | — |
| `atvykimo_reg_nr` | `string` | — | `4` | `open` | — | Atvykimo registracijos numeris | — |
| `atvykimo_uostas` | `string` | — | `4` | `open` | — | Laivo atvykimo uostas | — |
| `faktinis_atvykimas` | `datetime` | `S` | `4` | `open` | — | Laivo faktinis atvykimo laikas | — |
| `isvykimo_loc` | `string` | — | `4` | `open` | — | Laivo išvykimo uosto LOC kodas | LOC kodas - tai penkiaženklis raidinis kodas |
| `isvykimo_mca` | `string` | — | `4` | `open` | — | Laivo išvykimo uosto MCA kodas | MCA - tai keturženklis jūrų pakrančių zonos kodas. |
| `isvykimo_uostas` | `string` | — | `4` | `open` | — | Laivo išvykimo uostas | — |
| `faktinis_isvykimas` | `datetime` | `S` | `4` | `open` | — | Laivo faktinis išvykimo laikas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `op_tipas` | `"ATV"` | — | — | Atvykimas | — |
| `op_tipas` | `"ISV"` | — | — | Išvykimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/kroviniai (https://data.gov.lt/datasets/2857/)
