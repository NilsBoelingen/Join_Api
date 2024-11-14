Dies ist das Backend für ein Kanban-Board zur Aufgabenverwaltung. Es bietet eine REST-API, um Kontakte und Aufgaben zu erstellen, Aufgaben Kontakten zuzuweisen und Subtasks zu verwalten. Es enthält auch eine Startseite mit einer Übersicht aller Tasks und Statistiken.

## Features
- **Kontaktverwaltung**: API-Endpunkte zur Erstellung und Verwaltung von Kontakten.
- **Aufgabenverwaltung**: Endpunkte zur Erstellung, Bearbeitung und Verwaltung von Aufgaben.
- **Subtasks**: Subtasks werden Aufgaben zugeordnet und können nicht unabhängig existieren.
- **Dashboard**: Statistiken zur Anzahl und Status der Aufgaben.

## Tech Stack
- **Backend-Framework**: Django & Django REST Framework
- **Datenbank**: SQLite
- **Authentifizierung**: Token-basierte Authentifizierung für sichere API-Zugriffe

## Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/dein-benutzername/kanban-board-backend.git
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
