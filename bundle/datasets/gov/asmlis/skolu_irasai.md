---
type: Dataset
title: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Asmlis” ir „Mokesta” aptarnaujančios savivaldybes ir joms pavaldžias įstaigas vartotojų skolų įrašai."
description: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Asmlis” ir „Mokesta”, aptarnaujančios savivaldybes ir joms pavaldžias įstaigas, vartotojų skolų įrašai."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai"
tags: [gov, asmlis, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skolu_irasai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2930/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/skolu_irasai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Asmlis” ir „Mokesta” aptarnaujančios savivaldybes ir joms...

Savivaldybių MOKESTA ir ASMLIS sistemų duomenys[^manifest]

- **Namespace:** `datasets/gov/asmlis/skolu_irasai`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/skolu_irasai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `11` (11 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2930/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai`[^dcat]
- **Portal Title (`@lt`):** Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta” vartotojų skolų įrašai[^dcat]
- **Portal Title (`@en`):** Debt records[^dcat]
- **Issued (`dct:issued`):** `2025-08-20`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-04` .. `2026-10-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Asmlis” ir „Mokesta”, aptarnaujančios savivaldybes ir joms pavaldžias įstaigas, vartotojų skolų įrašai. Viena eilutė atitinka vieną skolos įrašą. Duomenų rinkinį sudaro skolos įrašo ir sutarties identifikatoriai, skolos suma ir požymis, nurodantis, ar neskaičiuojami delspinigiai, skolos įrašo data, bankroto data, mokėtojo kodas, mokėtojo tipas, asmens kodas, juridinio asmens kodas, nurodoma, ar vartotojas yra PVM mokėtojas, pateikiamos sutarties įsigaliojimo ir nutraukimo datos, vartotojo gimimo / mirties metai, lytis, paslaugos teikimo vietos koordinatės ir jų tipas. Priklausomai nuo savivaldybės ar įstaigos, duomenų aprėptis gali skirtis, tačiau duomenis numatyta atnaujinti kas mėnesį. Duomenų teikėjai: UAB Telšių vandenys; UAB Kretingos šilumos tinklai; UAB Anykščių šiluma; UAB Šakių šilumos tinklai; UAB Pakruojo šiluma; SĮ Telšių butų ūkis; UAB Utenos Komunalininkas; UAB Anykščių komunalinis ūkis; UAB Raseinių šilumos tinklai; UAB Elektrėnų komunalinis ūkis; UAB Molėtų švara. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Customer debt records of Asmilis and Mokesta, the service and settlement administration system that serves municipalities and their subsidiaries. One line corresponds to one debt entry. The dataset shall comprise the identifiers of the debt record and contract, the amount of the debt and an indication of whether interest on late payment, the date of the debt entry, the date of bankruptcy, the payer's number, the payer's type, the personal number, the legal entity number, whether the consumer is a VAT payer, the dates of entry into force and termination of the contract, the year of birth/death of the consumer, the sex, the coordinates of the place of service and their type. Depending on the municipality or body, the scope of the data may vary, but the data is scheduled to be updated monthly. Data Provider: UAB Telšiai vandenys Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TelsiuvIrasas](skolu_irasai/TelsiuvIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Telšių vandenys" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [AnyksciuSilumaIrasas](skolu_irasai/AnyksciuSilumaIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Anykščių šiluma" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [KretingosSTIrasas](skolu_irasai/KretingosSTIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Kretingos šilumos tinklai" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [SakiuSilumaIrasas](skolu_irasai/SakiuSilumaIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Šakių šiluma" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [AnyksciuKUIrasas](skolu_irasai/AnyksciuKUIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Anykščių komunalinio ūkio" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [PakruojoSilumaIrasas](skolu_irasai/PakruojoSilumaIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Pakruojo šiluma" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [MoletuSvaraIrasas](skolu_irasai/MoletuSvaraIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Molėtų švaros" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [UtenosKomunalininkasIrasas](skolu_irasai/UtenosKomunalininkasIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Utenos Komunalininko" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [ElektrenuKUIrasas](skolu_irasai/ElektrenuKUIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Elektrėnų komunalinio ūkio" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [TelsiuBUIrasas](skolu_irasai/TelsiuBUIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” SĮ "Telšių butų ūkio" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |
| [RaseiniuSTIrasas](skolu_irasai/RaseiniuSTIrasas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Raseinių šilumos tinklai" vartotojų skolų įrašai. | `4` | `vda_prime_key` | — | `23` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skolu_irasai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/skolu_irasai (https://data.gov.lt/datasets/2930/)
