---
type: Table
title: "StudVakcPagalIstaigasIrProgramas — Studentų vakcinacija ir imunizacija pagal įstaigas ir studijų programas"
description: "Studentų vakcinaciją ir bendrą imunizaciją nuo SARS‑CoV-2 pagal aukštąsias mokymosi įstaigas ir studijų programas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/StudVakcPagalIstaigasIrProgramas"
tags: [gov, lsd, studvakcpagalistaigasirprogramas, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L222"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L222"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# StudVakcPagalIstaigasIrProgramas — Studentų vakcinacija ir imunizacija pagal įstaigas ir studijų programas

Studentų vakcinaciją ir bendrą imunizaciją nuo SARS‑CoV-2 pagal aukštąsias mokymosi įstaigas ir studijų programas[^manifest]

- **Model:** `datasets/gov/lsd/covid19/StudVakcPagalIstaigasIrProgramas`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L222](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L222)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/StudVakcPagalIstaigasIrProgramas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ins_pav` | `string` | — | `2` | `open` | — | Aukštosios mokyklos pavadinimas | — |
| `prg_pavad_lt` | `string` | — | `2` | `open` | — | Studijų programos pavadinimas | — |
| `n_all` | `integer` | `U` | `4` | `open` | — | Šiuo metu aktyvūs studijuojantys studentai | Ne sustabdę studijas ar pašalinti. Įtraukti tiek lietuviai, tiek užsieniečiai. |
| `n_lt` | `integer` | `U` | `4` | `open` | — | Aktyvūs studentai, kurie turi lietuvišką asmens kodą | Aktyvūs studentai, kurie turi lietuvišką asmens kodą ir gali būti randami medicininiuose registruose. Šis skaičius naudojamas kaip vardiklis kituose procentiniuose stulpeliuose |
| `n_vac` | `number` | `U` | `4` | `open` | — | Bent viena doze vakcinuotų aktyvių studentų skaičius | Tik lietuviai (tiksliau, turintieji lietuvišką asmens kodą) |
| `n_vac_imm` | `number` | `U` | `4` | `open` | — | Abiem vakcinos dozėmis paskiepyti studentai | Abiem vakcinos dozėmis paskiepytų aktyvių studentų, kurie jau oficialiai turi imunitetą (14 d. nuo paskiepijimo antra vakcinos doze datos), skaičius. Tik lietuviai |
| `n_any_imm` | `number` | `U` | `4` | `open` | — | Aktyvūs studentai, kurie galimai turi imunitetą | Studentų turinčių imunitetą skaičius arba neseniai gavę (per 180 d. laikotarpį) teigiamą diagnostinio tyrimo atsakymą, arba paskiepyti abiem vakcinos dozėmis ir praėjo 14 d. nuo paskiepijimo antra vakcinos doze datos. Tik lietuviai |
| `p_vac` | `number` | `%` | `4` | `open` | — | Procentas bent viena doze vakcinuotų | Skaičiuojama pagal: (n_vac / n_lt * 100%) |
| `p_vac_imm` | `number` | `%` | `4` | `open` | — | Procentas turinčiųjų oficialų imunitetą po vakcinacijos | Skaičiuojama pagal: (n_vac_imm / n_lt * 100%) |
| `p_any_imm` | `number` | `%` | `4` | `open` | — | Procentas turinčiųjų oficialų imunitetą po vakcinacijos arba užsikrėtimo | Skaičiuojama pagal: (n_any_imm / n_lt * 100%) |
| `confidentiality` | `string` | — | `2` | `open` | — | Konfidencialumo taisyklė | Žymi, ar buvo pritaikyta konfidencialumo taisyklė, modifikuojanti absoliučius ir procentinius skaičius, kad būtų neįmanoma sužinoti, kas konkrečiai yra vakcinuotas ir kas ne. Taisyklė: mažiausiame pogrupyje negali būti mažiau nei 5 asmenys. Jei yra – tokiu atveju laikoma, kad tame pogrupyje yra 5 asmenys ir procentai skaičiuojami atitinkamai. |
| `data_freshness` | `date` | `D` | `4` | `open` | — | Duomenų "šviežumas" | Mažiausia iš dviejų datų: paskutinės įtrauktos vakcinacijos datos ir paskutinio įtraukto teigiamo testo datos. |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L222 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L222)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)
