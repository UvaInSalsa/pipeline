# Hoja de seguimiento — Módulo de descuentos

- **Alumno:** Pablo Omar Martínez Uvario (`10-IDGS-1`)
- **Materia:** Proceso del desarrollo del software
- **Docente:** Juan Carlos Rosales Quintero
- **Repositorio:** https://github.com/UvaInSalsa/pipeline

## Casos de prueba (límites 9, 10 y 11)

| Caso | Escenario / Regla | Entradas (precio, cantidad, frecuente) | Esperado |
| :--- | :--- | :--- | ---: |
| CP-01 | Precio cero (inválido) | `0, 5, False` | `ValueError` |
| CP-02 | Cantidad negativa (inválido) | `100, -1, False` | `ValueError` |
| CP-03 | Límite 9 · R1 (0 %) | `100, 9, False` | `$900.00` |
| CP-04 | Límite 9 · R2 (5 %) | `100, 9, True` | `$855.00` |
| CP-05 | Límite 10 · R3 (10 %) | `100, 10, False` | `$900.00` |
| CP-06 | Límite 10 · R4 (15 %) | `100, 10, True` | `$850.00` |
| CP-07 | Límite 11 · R3 (10 %) | `100, 11, False` | `$990.00` |
| CP-08 | Límite 11 · R4 (15 %) | `100, 11, True` | `$935.00` |
| CP-09 | Estándar · R1 (0 %) | `50, 4, False` | `$200.00` |
| CP-10 | Estándar · R4 (máx. 15 %) | `80, 20, True` | `$1,360.00` |
