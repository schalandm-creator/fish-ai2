"""
Schonzeiten & Mindestmaße für Süßwasserfische in Deutschland (Stand 2024).
Angaben ohne Gewähr.
"""

BUNDESLAENDER = [
    "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen",
    "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen",
    "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen",
    "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen",
]

FISH_REGULATIONS = {
    "Hecht": {
        "default":                 {"schonzeit": "01. Februar – 30. April",   "mindestmass": "50 cm"},
        "Schleswig-Holstein":      {"schonzeit": "01. Februar – 31. März",    "mindestmass": "50 cm"},
        "Nordrhein-Westfalen":     {"schonzeit": "01. März – 30. April",      "mindestmass": "50 cm"},
        "Brandenburg":             {"schonzeit": "01. Februar – 30. April",   "mindestmass": "50 cm",
                                    "hinweis": "In manchen Gewässern bis 15. Mai verlängert."},
    },
    "Zander": {
        "default":                 {"schonzeit": "01. März – 31. Mai",        "mindestmass": "50 cm"},
        "Schleswig-Holstein":      {"schonzeit": "01. März – 31. Mai",        "mindestmass": "45 cm"},
    },
    "Barsch": {
        "default":                 {"schonzeit": "Keine allgemeine Schonzeit","mindestmass": "15 cm"},
        "Schleswig-Holstein":      {"schonzeit": "01. April – 31. Mai",       "mindestmass": "18 cm"},
        "Brandenburg":             {"schonzeit": "01. April – 31. Mai",       "mindestmass": "20 cm"},
    },
    "Forelle": {
        "default":                 {"schonzeit": "01. Oktober – 28. Februar", "mindestmass": "25 cm",
                                    "hinweis": "Regenbogenforelle meist ganzjährig angelbar."},
        "Bayern":                  {"schonzeit": "01. Oktober – 28. Februar", "mindestmass": "25 cm (Bach) / 35 cm (See)"},
        "Baden-Württemberg":       {"schonzeit": "01. November – 28. Februar","mindestmass": "25 cm"},
        "Schleswig-Holstein":      {"schonzeit": "15. Oktober – 15. Januar",  "mindestmass": "30 cm"},
    },
    "Lachs": {
        "default":                 {"schonzeit": "15. September – 31. Dezember", "mindestmass": "50 cm",
                                    "hinweis": "In vielen BL stark reguliert. Lokale Vorschriften prüfen!"},
        "Schleswig-Holstein":      {"schonzeit": "01. September – 31. Dezember", "mindestmass": "60 cm (Ostsee)"},
    },
    "Karpfen": {
        "default":                 {"schonzeit": "01. Mai – 30. Juni",        "mindestmass": "35 cm"},
    },
    "Schleie": {
        "default":                 {"schonzeit": "01. Mai – 30. Juni",        "mindestmass": "25 cm"},
    },
    "Brassen": {
        "default":                 {"schonzeit": "01. Mai – 15. Juni",        "mindestmass": "25 cm"},
        "Schleswig-Holstein":      {"schonzeit": "01. Mai – 15. Juni",        "mindestmass": "20 cm"},
    },
    "Aal": {
        "default":                 {"schonzeit": "Keine bundesweit einheitliche Schonzeit", "mindestmass": "45 cm",
                                    "hinweis": "⚠️ Aal ist stark gefährdet (IUCN critically endangered). Lokale Entnahmeverbote prüfen!"},
        "Schleswig-Holstein":      {"schonzeit": "01. Oktober – 30. November","mindestmass": "45 cm"},
        "Mecklenburg-Vorpommern":  {"schonzeit": "15. September – 15. November","mindestmass": "45 cm"},
    },
    "Wels": {
        "default":                 {"schonzeit": "01. Mai – 30. Juni",        "mindestmass": "70 cm"},
    },
    "Äsche": {
        "default":                 {"schonzeit": "01. März – 30. April",      "mindestmass": "30 cm",
                                    "hinweis": "⚠️ Äsche ist gefährdet. In manchen BL ganzjährig geschützt."},
        "Baden-Württemberg":       {"schonzeit": "01. März – 31. Mai",        "mindestmass": "30 cm"},
        "Schleswig-Holstein":      {"schonzeit": "15. Februar – 15. April",   "mindestmass": "30 cm"},
    },
    "Rotauge": {
        "default":                 {"schonzeit": "01. Mai – 15. Juni",        "mindestmass": "15 cm"},
        "Bayern":                  {"schonzeit": "Keine allgemeine Schonzeit","mindestmass": "15 cm"},
    },
    "Rotfeder": {
        "default":                 {"schonzeit": "01. Mai – 15. Juni",        "mindestmass": "15 cm"},
    },
    "Stör": {
        "default":                 {"schonzeit": "⛔ Ganzjährig geschont",    "mindestmass": "Keine Entnahme erlaubt!",
                                    "hinweis": "Europäischer Stör ist vom Aussterben bedroht – sofortiger schonender Rückwurf Pflicht!"},
    },
}
