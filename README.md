# Sleep-Analysis

DATA3800 – Mandatory assignment 2. How is sleep deprivation related to lifestyle choices?
Data: NHIS 2025 Sample Adult file (CDC).

## Setup

```bash
python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (Git Bash):    source .venv/Scripts/activate
# macOS/Linux:           source .venv/bin/activate
pip install -r requirements.txt
```

## Data
Download the NHIS 2025 Sample Adult CSV from the CDC and place it in `data/raw/`.
The data is not stored in git.

## Structure
- `data/raw/` – original data (not tracked)
- `data/processed/` – cleaned data (not tracked)
- `src/` – reusable code (cleaning, analysis)
- `notebooks/` – EDA and analysis notebooks (one per person to avoid merge conflicts)
- `reports/figures/` – exported figures

## Enkel plan for Assignment 2
**Frist: 25. oktober 2026 kl. 23:59.**

Oppgaven: bygg og presenter en data analysis pipeline i Python (laste, rense, EDA, analysere, konkludere) på NHIS-dataene fra Assignment 1.

### Uke 1 (7.–13. okt): Forberedelse og lasting
- [ ] Spør Jawad hva «presentere» betyr, og om GenAI-verktøy er lov å bruke
- [ ] Last ned NHIS-filen og legg den i `data/raw/`
- [ ] Sett opp mappestruktur og virtuelt miljø (se Setup)
- [ ] Velg 3–5 spørsmål
- [ ] Velg ut 15–25 variabler av de 630
- [ ] Last inn i pandas og sjekk `shape` og `info()`

### Uke 2 (14.–20. okt): Rensing og EDA
- [ ] Rens dataene: gjør «Refused» og «Don't know» til manglende, fjern urealistiske verdier
- [ ] Skriv ned hver beslutning (hva og hvorfor)
- [ ] Lag 4–6 figurer og skriv 1–2 setninger under hver
- [ ] Sammenlign grupper med `groupby`, og regn ut noen betingede sannsynligheter

### Uke 3 (21.–25. okt): Konklusjon og innlevering
- [ ] Valgfritt: enkel modell som predikerer kort søvn
- [ ] Skriv svar på spørsmålene (4–5 setninger) og en «hva dette ikke viser»-del
- [ ] Rydd koden: funksjoner, kommentarer, kjører fra start til slutt
- [ ] Forbered presentasjonen
- [ ] Lever før 25. oktober kl. 23:59

### Arbeidsdeling (3–5 personer)
- Lasting og rensing
- EDA og figurer
- Analyse og modell
- Alle: tekst og presentasjon

### Forslag til spørsmål
1. Hvor mange timer sover voksne i snitt, og hvor mange sover under 7 timer?
2. Sover de som trener ofte mer enn de som trener sjelden?
3. Er kort søvn vanligere blant de som rapporterer angst eller depresjon?
4. Sover folk med lav inntekt eller utdanning mindre enn andre?
5. Kan vi forutsi kort søvn ut fra livsstil, helse og økonomi?

Husk: dataene viser sammenheng, ikke årsak. Bruk «er knyttet til», ikke «fører til». NHIS er et vektet utvalg, så husk sample weights.
