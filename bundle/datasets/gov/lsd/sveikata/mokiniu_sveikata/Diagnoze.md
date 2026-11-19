---
type: Table
title: "Diagnoze — Mokinių sveikatos patikrinimų metu nustatytos diagnozės. Lentelės objektas - mokinio sveikatos tikrinimo metu išrašyta diagnozė."
description: "Kaip numato įstatymai, pagal Lietuvos Respublikos bendrojo ugdymo programas darželiuose ir mokyklose besimokantys vaikai iki 18 metų kartą per metus turi pasitikrinti sveikatą."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze"
tags: [gov, lsd, diagnoze, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4067/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/mokiniu_sveikata"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Diagnoze — Mokinių sveikatos patikrinimų metu nustatytos diagnozės. Lentelės objektas - mokinio sveikatos tikrinimo metu išrašyta diagnozė.

**Dataset Context:** Kaip numato įstatymai, pagal Lietuvos Respublikos bendrojo ugdymo programas darželiuose ir mokyklose besimokantys vaikai iki 18 metų kartą per metus turi pasitikrinti sveikatą. Vaikų sveikatos patikrinimai leidžia laiku nustatyti sveikatos sutrikimus, ragina keisti gyvenimo būdą ir atsižvelgti į mokinio sveikatos poreikius ugdymo procese. Sveikatos patikra susideda iš dviejų dalių: šeimos, vidaus ligų ar vaikų ligų gydytojas arba slaugytojas įvertina vaiko sveikatą, o gydytojas odontologas, gydytojas odontologas specialistas arba burnos higienistas įvertina dantų ir burnos higienos būklę. Rinkinyje pateikiami išsamūs Lietuvos bendrojo ugdymo darželių ir mokyklų mokinių sveikatos patikrinimo duomenys nuo 2019m. iki šių dienų. Atvėrime panaudoti duomenys iš ESPBĮ, SVEIDRA informacinių sistemų ir Gyventojų registro. Pažymima, jog rinkinio lentelių duomenys tarpusavyje nesijungia. Rinkinys susideda iš trijų lentelių: 1. Mokinio sveikatos pažymėjimas: I. Sveikatos būklės įvertinimas. Pateikiami E027-1 formos pirmos dalies duomenys. Lentelės objektas - moksleivio sveikatos patikrinimas. Pateikiami duomenys apie tikrinimą atlikusią asmens sveikatos priežiūros įstaigą (ASPĮ), prie kurios prirašytas mokinys, nuasmeninti mokinio asmens ir jo sveikatos duomenys (ūgis, svoris) bei vertinimo išvada. 2. Mokinio sveikatos pažymėjimas: II. Dantų ir žandikaulių būklės įvertinimas. Pateikiami E027-1 formos antros dalies duomenys. Lentelės objektas - moksleivio sveikatos patikrinimas. Pateikiami nuasmeninti mokinio asmens ir jo gyvenamosios vietos duomenys bei patikrinimo metu užfiksuota dantų ir žandikaulio duomenys (pieninių ir nuolatinių dantų būklė ir skaičius). 3. Mokinių sveikatos patikrinimų metu įrašytos diagnozės. Lentelėje skelbiamos sveikatos tikrinimų metu užfiksuotos diagnozės su tarptautinės ligų klasifikacijos (TLK) kodais. Lentelės objektas - tikrinimo metu įrašyta diagnozė. Duomenų teikėjas: Registrų centras Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze`[^manifest]
- **Dataset:** [Kasmetinės vaikų sveikatos patikros duomenys](../mokiniu_sveikata.md) (`datasets/gov/lsd/sveikata/mokiniu_sveikata`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `tikrinimo_id` | `string` | — | `4` | `open` | — | Sveikatos tikrinimo vizito identifikatorius | Visos patikrinimo metu surašytos diagnozės susietos pagal tikrinimo_id stulpelį. |
| `diagnoze` | `string` | — | `4` | `open` | — | Diagnozės pavadinimas | — |
| `tlk_kodas` | `string` | — | `4` | `open` | — | Tarptautinės ligų klasifikacijos (TLK) kodas | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/mokiniu_sveikata (https://data.gov.lt/datasets/4067/)
