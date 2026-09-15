# CV-generator

Laver Parsey's brandede 3-siders konsulent-CV (PDF) ud fra strukturerede data i en JSON-fil.

## Opsætning (første gang)

```
pip install -r requirements.txt
playwright install chromium
```

## Brug

```
python3 render_cv.py data.json output.pdf
```

`data.json` skal følge skemaet beskrevet i skillen "parsey-konsulent-cv" (navn, rolle, profil,
kernekompetencer, projekter, joberfaring, sikkerhedsgodkendelse osv.). Skriv ALDRIG kompetencer
eller erfaring ind i data.json, som konsulenten ikke faktisk har.

Fontfilerne i `fonts/` (Space Grotesk + Inter) er Parseys brandfonte og indlejres direkte i PDF'en.
Rør dem ikke, medmindre brandbook'en ændrer typografien.

## Hvor bruges det

Skillene `parsey-konsulent-cv` og `parsey-stillingsmatch` bruger dette script til at rendere CV'er.
Ret her, når layoutet skal ændres — ikke inde i selve skill-samtalen.
