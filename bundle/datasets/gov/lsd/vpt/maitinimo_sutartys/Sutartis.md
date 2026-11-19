---
type: Table
title: "Sutartis — Bendrojo ugdymo įstaigų maitinimo paslaugų viešųjų pirkimų sutarčių duomenys"
description: "Rinkinyje pateikiami Viešųjų pirkimų tarnybos (VPT) Viešųjų pirkimų monitoringo informacinės sistemos Lietuvos bendrojo ugdymo įstaigų maitinimo sutarčių, viešinamų Viešųjų pirkimų portale, duomenys nuo 2008 m. Nurodomi išsamūs maitinimo sutarčių duomenys (galiojimo..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis"
tags: [gov, lsd, sutartis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4088/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/maitinimo_sutartys"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Sutartis — Bendrojo ugdymo įstaigų maitinimo paslaugų viešųjų pirkimų sutarčių duomenys

**Dataset Context:** Rinkinyje pateikiami Viešųjų pirkimų tarnybos (VPT) Viešųjų pirkimų monitoringo informacinės sistemos Lietuvos bendrojo ugdymo įstaigų maitinimo sutarčių, viešinamų Viešųjų pirkimų portale, duomenys nuo 2008 m. Nurodomi išsamūs maitinimo sutarčių duomenys (galiojimo laikotarpis, sutarties vertė, duomenys apie perkančiąją organizaciją ir konkursą laimėjusį tiekėją). Pažymėtina, kad maitinimo paslaugų konkursą gali organizuoti ne tik mokykla, bet ir mokyklos savininkė – savivaldybės administracija. Tokiu atveju prie perkančiosios organizacijos nurodomas maitinimo konkursą organizavusios savivaldybės administracijos pavadinimas. 2025 m. pabaigoje bendro Viešųjų pirkimų tarnybos ir Valstybės duomenų agentūros projekto metu, pasitelkiant dirbtinio intelekto (DI) modelį, buvo analizuojamos galiojančios ugdymo įstaigų maitinimo sutartys. DI modelis identifikavo duomenis apie maitinimo organizavimą (ar tiekiamas ekologiškas maistas, ar už maistą galima atsiskaityti elektroninėje maitinimo užsakymų ir atsiskaitymo sistemoje (EMUAS), ar maitinimas valgyklose organizuojamas savitarnos principu) ir sutartyse nurodytus patiekalus bei jų požymius (kaina, maitinimo laikas, moksleivių amžiaus grupė, kuriai skirtas patiekalas). Atkreipiame dėmesį, jog DI modelio identifikuotų duomenų tikslumas nėra garantuojamas. Šie duomenys atnaujinami nebus. Duomenų teikėjas – Viešųjų pirkimų tarnyba Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis`[^manifest]
- **Dataset:** [Ugdymo įstaigų maitinimo sutarčių duomenys](../maitinimo_sutartys.md) (`datasets/gov/lsd/vpt/maitinimo_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys/Sutartis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Viešųjų pirkimų tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `sutarties_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `registracijos_id` | `string` | — | `4` | `open` | — | Sutarties registracijos identifikacinis numeris | — |
| `tev_registracijos_id` | `string` | — | `4` | `open` | — | Tėvinės sutarties identifikacinis numeris, susijęs su registracijos_id. | — |
| `sutarties_issiuntimas` | `date` | `D` | `4` | `open` | — | Sutarties išsiuntimo pasirašymui data | — |
| `sutarties_pradzia` | `datetime` | `S` | `4` | `open` | — | Sutarties galiojimo pradžios laiko žyma | — |
| `sutarties_pabaiga` | `datetime` | `S` | `4` | `open` | — | Sutarties galiojimo termino laiko žyma | — |
| `ar_sutartis_galioja` | `boolean` | — | `4` | `open` | — | Požymis, ar sutartis galioja paskutinio rinkinio atnaujinimo metu | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Sutarties duomenų atnaujinimo data | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties registracijos numeris | — |
| `sutarties_objektas` | `string` | — | `4` | `open` | — | Sutarties objekto pavadinimas | — |
| `verte_eur` | `number` | — | `4` | `open` | — | Sutarties vertė, nurodyta eurais | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `pirkimo_budas` | `string` | — | `4` | `open` | — | Viešojo pirkimo konkurse skelbto pirkimo būdas | — |
| `pirkimo_nr` | `string` | — | `4` | `open` | — | Viešojo pirkimo numeris | — |
| `bvpz_kodas` | `string` | — | `4` | `open` | — | Bendrojo viešųjų pirkimų žodyno kodas, naudotas viešajam pirkimui | — |
| `bvpz_pavadinimas` | `string` | — | `4` | `open` | — | Bendrojo viešųjų pirkimų žodyno kodo aprašumas, naudotas viešajam pirkimui | — |
| `tiekeju_grupe` | `string` | — | `4` | `open` | — | Nurodoma tiekėjų grupė, jeigu sutartį pasirašė keli tiekėjai | — |
| `tiekejas` | `string` | — | `4` | `open` | — | Tiekėjo pavadinimas | — |
| `tiekejo_jar` | `string` | — | `4` | `open` | — | Tiekėjo juridinio asmens kodas | — |
| `tiekejo_valstybe` | `string` | — | `4` | `open` | — | Tiekėjo valstybės pavadinimas | — |
| `tiek_adresas` | `string` | — | `4` | `open` | — | Tiekėjo adresas | — |
| `po` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos pavadinimas | Perkančioji organizacija maitinimui organizuoti gali būti ne tik mokykla, bet ir savivaldybė. |
| `po_jar` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos juridinio asmens kodas | — |
| `po_adresas` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos adresas | — |
| `po_geometrija` | `geometry(3346)` | — | `4` | `open` | — | Perkančiosios organizacijos vietos koordinatės (LKS) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tiekejo_valstybe` | `"Lietuva"` | — | — | — | — |
| `tiekejo_valstybe` | `"Lenkija"` | — | — | — | — |
| `tiekejo_valstybe` | `"Slovėnija"` | — | — | — | — |
| `tiekejo_valstybe` | `"Latvija"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.
- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L15)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/maitinimo_sutartys (https://data.gov.lt/datasets/4088/)
