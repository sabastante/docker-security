# Seguridad en Docker y Kubernetes

# Introducción al Curso:

Este curso está diseñado como una introducción práctica a Docker, orientado a ingenieros, desarrolladores, analistas y personal de seguridad que necesiten comprender cómo empaquetar, distribuir y ejecutar aplicaciones en entornos modernos. El objetivo principal es que, al finalizar, puedas **construir contenedores**, **ejecutarlos**, **entender cómo funcionan internamente** y aplicar **buenas prácticas de seguridad** en el proceso.

---

## ¿Qué problema resuelve Docker?

Antes de Docker, la instalación y despliegue de aplicaciones solía generar inconsistencias entre entornos:

- “Funciona en mi máquina”.
- Dependencias diferentes entre servidores.
- Librerías y runtime distintos en cada entorno.
- Configuraciones manuales difíciles de mantener.

**Docker** permite empaquetar una aplicación junto a todas sus dependencias en una unidad estandarizada llamada **imagen**.  
Cuando se ejecuta una imagen, obtenemos un **contenedor**, que es un proceso aislado del host.

Esto permite:

- Entornos reproducibles.
- Despliegues rápidos.
- Portabilidad entre laptops, servidores y nubes.
- Versionado y control del entorno completo.

---

## Contenidos del Curso

| Módulo | Tema | Objetivo |
|-------|------|----------|
| 1.1 | ¿Qué es Docker? Contenedores vs Máquinas Virtuales | Comprender la diferencia conceptual y práctica. |
| 1.2 | Imágenes y Contenedores | Aprender a construir, listar y ejecutar contenedores. |
| 1.3 | Dockerfile | Crear imágenes propias desde código fuente. |
| 1.4 | Docker Hub y Registries | Subir, versionar y distribuir imágenes. |
| 1.5 | Multi-arch builds | Construcción de imágenes para diferentes arquitecturas. |

---

## Requisitos Previos

- Manejo básico de Linux en terminal.
- Conocimientos mínimos de programación (cualquier lenguaje).
- Permisos para instalar software en el equipo local.

No se requieren conocimientos previos de contenedores.

