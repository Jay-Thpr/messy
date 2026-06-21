ARCHITECTURE = """
MessyApp Architecture (updated 2017, 2019, 2021, never finished)

┌─────────────────────────────────────────────────────────────┐
│ main.py / run.py / app.py / start.py / REAL_main.py         │
└───────────────────────────┬─────────────────────────────────┘
                            │
              ┌─────────────▼─────────────┐
              │   ApplicationManager      │  (God Object)
              │   + ManagerOfManagers     │
              └─────────────┬─────────────┘
                            │
     ┌──────────────────────┼──────────────────────┐
     │                      │                      │
 UIManager            DataManager            EventManager
 (imports others)     (SQL strings)         (3 click handlers)
     │                      │                      │
     └──────────────────────┼──────────────────────┘
                            │
              ┌─────────────▼─────────────┐
              │ MainWindow + main_window  │  (duplicates)
              │ + OldMainWindow           │  (deprecated)
              └───────────────────────────┘

Global state: global_state.py + GLOBALS.py + state.py (pick one)
Config: settings.py + Settings.py + app_config.json + config_loader.py
"""
