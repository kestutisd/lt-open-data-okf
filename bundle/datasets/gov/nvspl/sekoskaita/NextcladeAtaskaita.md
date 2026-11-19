---
type: Table
title: "NextcladeAtaskaita — SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita"
description: "\"Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita/NextcladeAtaskaita"
tags: [gov, nvspl, nextcladeataskaita, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nvspl/sekoskaita"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NextcladeAtaskaita — SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita

"Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus. Viena eilutė yra vieno SARS-CoV-2 mėginio sekoskaitos rezultatas. Seskoskaitos rezultatai generuojami naudojant Nextclade programinę įrangą. Vienos eilutės informaciją sudaro laboratorijos priskirtas mėginio identifikacinis numeris, tiriamam virusui priskirti klado (virusų grupės) pavadinimai pagal atitinkamą kriterijų, nurodomos nukleotidų ir aminorūgščių pakaitos, iškritos ir insercijos, taip pat sekoskaitos kokybės kontrolės įverčiai."[^manifest]

- **Model:** `datasets/gov/nvspl/sekoskaita/NextcladeAtaskaita`[^manifest]
- **Dataset:** [SARS-CoV-2 viruso sekoskaitos duomenys](../sekoskaita.md) (`datasets/gov/nvspl/sekoskaita`)[^manifest]
- **Manifest CSV:** [datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita/NextcladeAtaskaita` (`deployed`)[^manifest]
- **Provider:** `nvspl` — Nacionalinė visuomenės sveikatos priežiūros laboratorija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `meg_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `meg_id` | `string` | — | `4` | `open` | — | Mėginio identifikacinis numeris | — |
| `kladas` | `string` | — | `4` | `open` | — | Priskirtas kladas | — |
| `nextstrain_kladas` | `string` | — | `4` | `open` | — | Priskirtas kladas pagal Nextstrain programinę įrangą | — |
| `pso_kladas` | `string` | — | `4` | `open` | — | Priskirtas kladas pagal Pasaulinę sveikatos organizaciją | — |
| `filog_linija` | `string` | — | `4` | `open` | — | Pilnas filogenetinės linijos pavadinimas | — |
| `sutrump_filog_linija` | `string` | — | `4` | `open` | — | Sutrumpintas filogenetinės linijos pavadinimas | — |
| `klado_padetis` | `string` | — | `4` | `open` | — | Padėtis kladogramoje arba filogenetiniame medyje | — |
| `kokybes_balas` | `number` | — | `4` | `open` | — | Bendras kokybės kontrolės balas | — |
| `kokybes_statusas` | `string` | — | `4` | `open` | — | Bendras kokybės kontrolės statusas | — |
| `viso_nk_pakaitu` | `integer` | — | `4` | `open` | — | Visuminis/bendras pakaitų kiekis nukleotidinėje sekoje | — |
| `viso_nk_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų nukleotidų sekų pakeitimų | — |
| `viso_nk_iskr` | `integer` | — | `4` | `open` | — | Visuminis/bendras iškritų kiekis nukleotidinėje sekoje | — |
| `viso_nk_iskr_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų nukleotidų iškritų | — |
| `viso_nk_inser` | `integer` | — | `4` | `open` | — | Visuminis/bendras insercijų kiekis nukleotidinėje sekoje | — |
| `viso_nk_inser_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų nukleotidų insercijų | — |
| `viso_nk_trukstamu` | `integer` | — | `4` | `open` | — | Visuminis/bendras trūkstamų nukleotidų kiekis | — |
| `viso_nusk_posl` | `integer` | — | `4` | `open` | — | Sąrašas aptiktų rėmelio poslinkio pokyčių | — |
| `viso_nusk_posl_sar` | `string` | — | `4` | `open` | — | Visuminis/bendras skaitymo rėmelio poslinkis | — |
| `neidentifikuoti_nk` | `integer` | — | `4` | `open` | — | Visuminis/bendras neidentifikuotų nukleotidų kiekis | — |
| `viso_ar_pakaitu` | `integer` | — | `4` | `open` | — | Visuminis/bendras aminorūgščių pakaitų kiekis a. r. sekoje | — |
| `viso_ar_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų aminorūgščių pakeitimų | — |
| `viso_ar_iskr` | `integer` | — | `4` | `open` | — | Visuminis/bendras aminorūgščių iškritų kiekis sekoje | — |
| `viso_ar_iskr_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų aminorūgščių iškritų | — |
| `viso_ar_inser` | `integer` | — | `4` | `open` | — | Visuminis/bendras aminorūgščių insercijų kiekis sekoje | — |
| `viso_ar_inser_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų aminorūgščių insercijų | — |
| `viso_neidentifikuotu_ar` | `integer` | — | `4` | `open` | — | Bendras kiekis neidentifikuotų aminorūgščių | — |
| `nk_lygiavimo_ivertis` | `integer` | — | `4` | `open` | — | Nukleotidų sekos lygiavimo įvertis | — |
| `lygiavimo_sek_prad` | `integer` | — | `4` | `open` | — | Nukleotidų lygiavimo sekos pradžia | — |
| `lygiavimo_sek_pab` | `integer` | — | `4` | `open` | — | Nukleotidų lygiavimo sekos pabaiga | — |
| `padeng` | `number` | — | `4` | `open` | — | Nusekvenuotos sekos padengimas | — |
| `kod_sek_padeng` | `string` | — | `4` | `open` | — | Koduojančių sekų padengimas | — |
| `transform_seka` | `boolean` | — | `4` | `open` | — | Transformuota seka | Požymis nurodantis ar seka buvo transformuota naudojant atvirkštinio komplemento operaciją prieš atliekant sekų lyginimą |
| `viso_unik_nk_klad_transform_pakaitu` | `integer` | — | `4` | `open` | — | Unikalių konkrečiam kladui priskiriamų reversinių pakeitimų mutacijų kiekis nukleotidų sekoje | — |
| `unik_nk_klad_transform_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas unikalių konkrečiam kladui priskiriamų atvirkštinių mutacijų pakeitimų nukleotidų sekoje | — |
| `viso_unik_nk_klad_pakaitu` | `integer` | — | `4` | `open` | — | Pakeitimų mutacijų būdingų specifiniam kladui kiekis nukleotidų sekoje | — |
| `unik_nk_klad_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas pakeitimų mutacijų būdingų specifiniam kladui nukleotidų sekoje | — |
| `viso_ne_unik_nk_klad_pakaitu` | `integer` | — | `4` | `open` | — | Pakeitimų mutacijų kurios nėra būdingos atitinkamam kladui ir nėra reversinės kiekis nukleotidų sekoje | — |
| `ne_unik_nk_klad_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas pakeitimų mutacijų kurios nėra būdingos atitinkamam kladui ir nėra atvirkštinės nukleotidų sekoje | — |
| `viso_nk_klad_pakaitu` | `integer` | — | `4` | `open` | — | Bendras kiekis unikalių mutacijų nukleotidų sekoje priskiriamų specifiniam kladui | — |
| `viso_unik_ar_klad_transform_pakaitu` | `integer` | — | `4` | `open` | — | Unikalių konkrečiam kladui priskiriamų atvirkštinių pakaitinių mutacijų kiekis aminorūgščių sekoje | — |
| `unik_ar_klad_transform_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas unikalių konkrečiam kladui priskiriamų atvirkštinių pakeitimų mutacijų aminorūgščių sekoje | — |
| `viso_unik_ar_klad_pakaitu` | `integer` | — | `4` | `open` | — | Pakaitinių mutacijų būdingų specifiniam kladui kiekis aminorūgščių sekoje | — |
| `unik_ar_klad_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas pakaitinių mutacijų būdingų specifiniam kladui aminorūgščių sekoje | — |
| `viso_ne_unik_ar_klad_pakaitu` | `integer` | — | `4` | `open` | — | Pakaitinių mutacijų kurios nėra būdingos atitinkamam kladui ir nėra atvirkštinės kiekis aminorūgščių sekoje | — |
| `ne_unik_ar_klad_pakaitu_sar` | `string` | — | `4` | `open` | — | Sąrašas pakaitinių mutacijų kurios nėra būdingos atitinkamam kladui ir nėra reversinės aminorūgščių sekoje | — |
| `viso_ar_klad_pakaitu` | `integer` | — | `4` | `open` | — | Bendras kiekis unikalių mutacijų aminorūgščių sekoje priskiriamų specifiniam kladui | — |
| `trukstamu_nk_sar` | `string` | — | `4` | `open` | — | Sąrašas aptiktų trūkstamų nukleotidų | — |
| `sakos_pirmtk_pav` | `string` | — | `4` | `open` | — | Šakos pirmtako pavadinimas referenciniame filogenetiniame medyje | — |
| `sakos_pirmtk_nk_pakaitu_sar` | `string` | — | `4` | `open` | — | "Aptiktų nukleotidų pakaitų sąrašas, palyginus su šakos pirmtako genotipu" | — |
| `sakos_pirmtk_nk_iskr_sar` | `string` | — | `4` | `open` | — | "Aptiktų nukleotidų iškritų sąrašas, palyginus su šakos pirmtako genotipu" | — |
| `sakos_pirmtk_ar_pakaitu_sar` | `string` | — | `4` | `open` | — | "Aptiktų aminorūgščių pakaitų sąrašas, palyginus su šakos pirmtako genotipu" | — |
| `sakos_pirmtk_ar_iskr_sar` | `string` | — | `4` | `open` | — | "Aptiktų aminorūgščių iškritų sąrašas, palyginus su šakos pirmtako genotipu" | — |
| `pango_pirmtk_pav` | `string` | — | `4` | `open` | — | Pirmtako pavadinimas atskaitos filogenetiniame medyje pagal Pango liniją | — |
| `pango_pirmtk_nk_pakaitu_sar` | `string` | — | `4` | `open` | — | "Nukleotidų pakaitų sąrašas, būdingas Pango linijos pirmtako sekai, su kuria lyginama tiriamoji seka" | — |
| `pango_pirmtk_nk_iskr_sar` | `string` | — | `4` | `open` | — | "Nukleotidų iškritų sąrašas, būdingas Pango linijos pirmtako sekai, su kuria lyginama tiriamoji seka" | — |
| `pango_pirmtk_ar_pakaitu_sar` | `string` | — | `4` | `open` | — | "Aminorūgščių pakaitų sąrašas, būdingas Pango linijos pirmtako sekai, su kuria lyginama tiriamoji seka" | — |
| `pango_pirmtk_ar_iskr_sar` | `string` | — | `4` | `open` | — | "Aminorūgščių iškritų sąrašas, būdingas Pango linijos pirmtako sekai, su kuria lyginama tiriamoji seka" | — |
| `ar_jn1` | `string` | — | `4` | `open` | — | "Požymis, nurodantis, ar lyginama su JN.1 koronaviruso variantu" | — |
| `jn1_nk_pakaitu_sar` | `string` | — | `4` | `open` | — | "Aptiktų nukleotidų pakeitimų, susijusių su JN.1 variantu, sąrašas" | — |
| `jn1_nk_iskrit_sar` | `string` | — | `4` | `open` | — | "Aptiktų nukleotidų iškritų sąrašas, palyginti JN.1 variantu, sąrašas" | — |
| `jn1_ar_pakait_sar` | `string` | — | `4` | `open` | — | "Aptiktų aminorūgščių pakeitimų, susijusių su JN.1 variantu, sąrašas" | — |
| `jn1_ar_iskr_sar` | `string` | — | `4` | `open` | — | "Aptiktų aminorūgščių iškritų sąrašas, palyginti su JN.1 variantu, sąrašas" | — |
| `ar_xbb15` | `string` | — | `4` | `open` | — | "Požymis, nurodantis, ar lyginama su XBB.1.5 koronaviruso variantu" | — |
| `xbb15_nk_pakaitu_sar` | `string` | — | `4` | `open` | — | "Aptiktų nukleotidų pakeitimų, susijusių su XBB.1.5 variantu, sąrašas" | — |
| `xbb15_nk_iskr_sar` | `string` | — | `4` | `open` | — | "Aptiktų nukleotidų iškritų sąrašas, palyginti XBB.1.5 variantu, sąrašas" | — |
| `xbb15_ar_pakait_sar` | `string` | — | `4` | `open` | — | "Aptiktų aminorūgščių pakeitimų, susijusių su XBB.1.5 variantu, sąrašas" | — |
| `xbb15_ar_iskr_sar` | `string` | — | `4` | `open` | — | "Aptiktų aminorūgščių iškritų sąrašas, palyginti su XBB.1.5 variantu, sąrašas" | — |
| `nezinomos_ar_sritys` | `string` | — | `4` | `open` | — | Aptiktų gretimų nežinomos aminorūgšties sričių sąrašas (aminorūgšties simbolis X) | — |
| `dviprasmiu_nk_sar` | `string` | — | `4` | `open` | — | "Aptiktų dviprasmių nukleotidų sąrašas (nukleotidų simboliai, kurie nėra A, C, G, T, N)" | — |
| `kokybes_kontrl_slenkstis` | `integer` | — | `4` | `open` | — | "Slenkstis, kuris buvo naudojamas kokybės kontrolės (QC) taisyklei „Trūkstami duomenys“ (angl. Missing data)" | — |
| `kk_ivertis` | `number` | — | `4` | `open` | — | "Įvertis pagal kokybės kontrolės taisyklę „Trūkstami duomenys“ (angl. Missing data)" | — |
| `kk_statusas` | `string` | — | `4` | `open` | — | "Statusas pagal kokybės kontrolės taisyklę „Trūkstami duomenys“ (angl. Missing data)" | — |
| `kk_trukstami_nk` | `integer` | — | `4` | `open` | — | "Bendras trūkstamų nukleotidų skaičius, panaudotas kokybės kontrolės taisyklėje „Trūkstami duomenys“ (angl. Missing data)" | — |
| `kk_misriu_vietu_riba` | `integer` | — | `4` | `open` | — | "Slenkstinė riba naudota „mišrių vietų“ (angl. Mixed sites) kokybės kontrolei" | — |
| `misriu_vietu_kk_ivert` | `integer` | — | `4` | `open` | — | "„Mišrių vietų“ (angl. Mixed sites) kokybės kontrolės įvertinimas" | — |
| `misriu_vietu_kk_busena` | `string` | — | `4` | `open` | — | "„Mišrių vietų“ (angl. Mixed sites) kokybės kontrolės būsena" | — |
| `viso_misriu_vietu_dviprasmisku_nk` | `integer` | — | `4` | `open` | — | "Bendras dviprasmiškų nukleotidų skaičius, naudotų „mišrių vietų“ (angl. Mixed sites) kokybės kontrolei" | — |
| `kk_privacios_mutacijos_riba` | `integer` | — | `4` | `open` | — | "Ribinis parametras, naudojamas kokybės kontrolei unikalioms mėginiui būdingoms mutacijoms (angl. private mutations)" | — |
| `kk_privacios_mutacijos_param` | `integer` | — | `4` | `open` | — | "Perteklinis parametras, naudojamas kokybės kontrolei unikalioms mėginiui būdingoms mutacijoms (angl. private mutations)" | — |
| `kk_privaciu_mutaciju_balas` | `number` | — | `4` | `open` | — | Unikalių mėginiui būdingų mutacijų (angl. private mutations) kokybės kontrolės balas | — |
| `kk_privaciu_mutaciju_busena` | `string` | — | `4` | `open` | — | Unikalių mėginiui būdingų mutacijų (angl. private mutations) kokybės kontrolės būsena | — |
| `svertine_privaciu_mutaciju_riba` | `integer` | — | `4` | `open` | — | "Svertinė unikalios mėginiui būdingų mutacijų (angl. private mutations) suma, naudojama kokybės kontrolei unikalioms mėginiui būdingoms mutacijoms" | — |
| `kk_remelio_posl_sar` | `string` | — | `4` | `open` | — | "Aptiktų rėmelių poslinkių sąrašas „Rėmelių poslinkių“ (angl. Frame shifts) kokybės kontrolėje (išskyrus ignoruojamus)" | — |
| `viso_kk_remelio_posl` | `integer` | — | `4` | `open` | — | "Bendras aptiktų rėmelių poslinkių skaičius pagal kokybės kontrolę „Rėmelių poslinkiai“ (angl. Frame shifts) (išskyrus ignoruojamus)" | — |
| `kk_ignor_remelio_posl_sar` | `string` | — | `4` | `open` | — | "Rėmelio poslinkio sąrašas, kuris neraportuojamas dėl ​​ignoruojamo sąrašo" | — |
| `viso_kk_ignor_remelio_posl` | `integer` | — | `4` | `open` | — | "Bendras aptiktų rėmelio poslinkių, bet neraportuojamų dėl ignoruojamų rėmalio poslinkio sąrašo" | — |
| `kk_remelio_posl_balas` | `integer` | — | `4` | `open` | — | "„Rėmelio poslinkio“ (angl. frame shift) kokybės kontrolės balas" | — |
| `kk_remelio_posl_statusas` | `string` | — | `4` | `open` | — | "„Rėmelio poslinkio“ (angl. frame shift) kokybės kontrolės būsena" | — |
| `kk_stop_kodonai_sar` | `string` | — | `4` | `open` | — | "Sąrašas aptiktų stop kodonų QC taisyklėje „Stop kodonai“ (angl. stop codons)" | — |
| `viso_kk_stop_kodonai` | `integer` | — | `4` | `open` | — | "Bendras aptiktų stop kodonų skaičius „Stop kodonų“ kokybės kontrolės taisyklėje" | — |
| `kk_stop_kodonai_balas` | `integer` | — | `4` | `open` | — | "„Stop kodonų“ kokybės kontrolės balas" | — |
| `kk_stop_kodonai_busena` | `string` | — | `4` | `open` | — | "„Stop kodonų“ kokybės kontrolės būsena" | — |
| `viso_pgr_pradmenu_nk_mut` | `integer` | — | `4` | `open` | — | "Bendras nukleotidų mutacijų, aptiktų PGR pradmenų regionuose, skaičius" | — |
| `pgr_pradmenu_pakaitu_sar` | `string` | — | `4` | `open` | — | Aptiktų PGR pradmenų pakeitimų sąrašas | — |
| `nepavyk_kds_sar` | `string` | — | `4` | `open` | — | Nepavykusio vertimo CDS sąrašas | — |
| `ispejimai` | `string` | — | `4` | `open` | — | Įspėjimai | — |
| `klaidos` | `string` | — | `4` | `open` | — | Klaidos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nvspl/sekoskaita (https://data.gov.lt/datasets/3899/)
