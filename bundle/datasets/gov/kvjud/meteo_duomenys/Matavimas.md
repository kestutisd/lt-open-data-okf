---
type: Table
title: "Matavimas — Klaipėdos uosto šiaurinio molo meteo informacija"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys/Matavimas"
tags: [gov, kvjud, matavimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/meteo_duomenys.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2360/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/meteo_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Matavimas — Klaipėdos uosto šiaurinio molo meteo informacija

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys. Rinkinyje pateikiami nuo 2024 m. gruodžio mėnesio kaupiami šiaurinio molo meteorologiniai duomenys. Šių matavimų metu matuojamas slėgis, rasos taškas, santykinė drėgmė, temperatūra, vėjo kryptis bei greitis. Vienas įrašas atitinka vieną matavimą. Matavimo stotelės koordinatės: 55.73057 21.07975. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kvjud/meteo_duomenys/Matavimas`[^manifest]
- **Dataset:** [Klaipėdos uosto šiaurinio molo meteo informacija](../meteo_duomenys.md) (`datasets/gov/kvjud/meteo_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/meteo_duomenys.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys/Matavimas` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `matavimo_laikas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `matavimo_laikas` | `datetime` | `S` | `4` | `open` | — | Meteo sąlygų matavimo laikas | — |
| `bp_a_hpa` | `number` | `hPa` | `4` | `open` | — | Slėgis (hPa) | — |
| `dew_p_c` | `number` | `°C` | `4` | `open` | — | Rasos taškas (C) | — |
| `rel_hum_a_p` | `number` | `%` | `4` | `open` | — | Santykinė drėgmė (%) | — |
| `temp_a_c` | `number` | `°C` | `4` | `open` | — | Temperatūra (C) | — |
| `vsb_m` | `number` | `m` | `4` | `open` | — | Matomumas (m) | — |
| `wind_dir_deg` | `number` | `°` | `4` | `open` | — | Vėjo kryptis (°) | — |
| `wind_speed_a_mps` | `number` | `m/s` | `4` | `open` | — | Vėjo greitis (vidutinis) (m/s) | — |
| `wind_speed_g_mps` | `number` | `m/s` | `4` | `open` | — | Vėjo greitis (maksimalus/gūsiai) (m/s) | — |
| `wind_speed_min_mps` | `number` | `m/s` | `4` | `open` | — | Vėjo greitis (minimalus) (m/s) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/meteo_duomenys.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/meteo_duomenys (https://data.gov.lt/datasets/2360/)
