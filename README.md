# Módulo de descuentos — Pipeline CI

Repositorio de la Actividad práctica 2 (Unidad 2 · Proceso del desarrollo del software).

## Ejecución local

```bash
pip install pytest pytest-cov
pytest -v --cov=descuentos --cov-report=term-missing --cov-fail-under=80
```

## Cómo demostrar la compilación rota y corregida en GitHub Actions

1. Para observar la primera ejecución fallida en `main`, cambia temporalmente en `descuentos.py` la línea 6 a `if cantidad > 10:` y haz push.
2. Crea la rama `fix/descuento-limite`, restaura `if cantidad >= 10:`, sube la rama y abre un Pull Request hacia `main` para validar la ejecución exitosa (10/10 pruebas y 100 % cobertura).
