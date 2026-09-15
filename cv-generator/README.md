# CV-generator

Bygger Parseys brandede 3-siders konsulent-CV som PDF ud fra strukturerede data.

## Opsætning

```
pip install -r requirements.txt
playwright install chromium
```

## Brug

```
python3 render_cv.py data.json output.pdf
```

`data.json` skal indeholde konsulentens fulde, faktiske CV-indhold — scriptet må aldrig bruges til at tilføje kompetencer eller erfaring, konsulenten ikke reelt har.

Fontene i `fonts/` er Parseys brand-skrifttyper (Inter og Space Grotesk) — undgå at ændre dem, medmindre det er aftalt med hvem der ejer brandbogen.

Denne skabelon bruges af flere interne værktøjer til at generere CV'er — rediger layoutet her, så alle der bruger det, automatisk får opdateringen med.
