---
type: Dataset
title: "Pacientų, kuriems atlikta inkstų biopsija, duomenys"
description: "Rinkinyje pateikiami asmenų, kuriems nuo 2015 m. atlikta inkstų biopsija, duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientų, kuriems atlikta inkstų biopsija, duomenys

Rinkinyje pateikiami asmenų, kuriems nuo 2015 m. atlikta inkstų biopsija, duomenys.

Rinkinį sudaro:

Inkstų biopsijų duomenys. Asmenys, kuriems atlikta inkstų biopsija, gimimo data, lytis, biopsijos gavimo data, lėtinės inkstų ligos, 5 stadijos pirmo įrašo data, indikatoriai, ar pacientui nustatytos gretutinės ligos, inkstų ligų rizikos veiksniai – cukrinis diabetas ir arterinė hipertenzija, paciento mirties data ir pagrindinė mirties priežastis. Visos datos yra pateikiamos mėnesio tikslumu.

Pirmos dializės duomenys. Pacientų pirmos dializės data (mėnesio tikslumu), dializės tipas. Vienam asmeniui gali būti registruotos kelios pirmosios dializės datos, nes po atliktos inksto transplantacijos, transplantatui nustojus funkcionuoti, įrašoma nauja dializės pradžios data.

Inkstų transplantacijų duomenys. Pacientams atliktų inkstų transplantacijų (intervencijos ACHI kodas 36503-00) datos (mėnesio tikslumu).

Laboratorinių tyrimų duomenys. Pacientų inkstų funkciją apibūdinantys laboratoriniai tyrimai (kreatininas serume, glomerulų filtracijos greitis, albumino-kreatinino santykis šlapime), jų atlikimo data, tyrimo ir analitės pavadinimai, analitės rezultatai, apatiniai, viršutiniai normos rėžiai bei matavimo vienetai.

Elektroninių receptų duomenys. Pacientams išrašyti elektroniniai receptai, jų išrašymo data (mėnesio tikslumu), recepto skyrimo diagnozės kodas ir pavadinimas, vaisto ATC kodai, bendriniai pavadinimai ir stiprumas. Filtruoti tik su inkstų patologija susiję elektroniniai receptai pagal ATC kodus, t. y. renino angiotenzino sistemą veikiantys vaistai, beta adrenoblokatoriai, kalcio kanalų blokatoriai, diuretikai, ne geležies antianeminiai preparatai, geležies preparatai, imunosupresantai, sistemiškai veikiantys kortikosteroidai.

Duomenų šaltiniai: Valstybinis patologijos centras, Nacionalinis transplantacijų biuras (ŽALODRIS), Valstybinė ligonių kasa (SVEIDRA IS), Higienos instituto Mirties priežasčių registras, įvairių gydymo įstaigų informacinės sistemos bei Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistemos (ESPBI IS) E. recepto posistemis.

Atnaujinimo periodiškumas: Vieną kartą per metus.

- **Namespace:** `datasets/gov/lsd/sveikata/inkstu_biopsijos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [InkstoBiopsija](inkstu_biopsijos/InkstoBiopsija.md) | Inkstų biopsijų duomenys | `4` | `vda_prime_key` | — | 11 | Asmenys, kuriems atlikta inkstų biopsija, gimimo data, lytis, biopsijos gavimo data, lėtinės inkstų ligos, 5 stadijos pirmo įrašo data, indikatoriai, ar... |
| [PirmaDialize](inkstu_biopsijos/PirmaDialize.md) | Pirmos dializės duomenys | `4` | `vda_prime_key` | — | 5 | Pacientų pirmos dializės data (mėnesio tikslumu), dializės tipas. |
| [InkstoTransplantacija](inkstu_biopsijos/InkstoTransplantacija.md) | Inkstų transplantacijų duomenys | `4` | `vda_prime_key` | — | 4 | Pacientams atliktų inkstų transplantacijų (intervencijos ACHI kodas 36503-00) datos (mėnesio tikslumu) |
| [LaboratorinisTyrimas](inkstu_biopsijos/LaboratorinisTyrimas.md) | Laboratorinių tyrimų duomenys | `4` | `vda_prime_key` | — | 9 | Pacientų inkstų funkciją apibūdinantys laboratoriniai tyrimai (kreatininas serume, glomerulų filtracijos greitis, albumino-kreatinino santykis šlapime), jų... |
| [Receptas](inkstu_biopsijos/Receptas.md) | Elektroninių receptų duomenys | `4` | `vda_prime_key` | — | 8 | Pacientams išrašyti elektroniniai receptai, jų išrašymo data (mėnesio tikslumu), recepto skyrimo diagnozės kodas ir pavadinimas, vaisto ATC kodai... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv
