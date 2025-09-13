#Frage 1
# Kantenlänge des Würfels in Millimeter
cube_edge_length_mm = 5.0

# Umrechnung in Zentimeter
cube_edge_length_cm = cube_edge_length_mm / 10

# Volumen des Würfels (in Kubikzentimeter)
cube_volume_cm3 = cube_edge_length_cm ** 3

# Masse des Würfels in Gramm
cube_mass_g = 2.68

# Dichte in g/cm³
cube_density_g_per_cm3 = cube_mass_g / cube_volume_cm3

print("Dichte des Platinwürfels:", cube_density_g_per_cm3, "g/cm³")
#Frage 2
# Ergebnis aus der Dichteberechnung
ergebnis = 21.44

# Umwandlung in eine Zeichenkette
lösungswort = str(ergebnis)

print("Das Lösungswort lautet:", lösungswort)
#Frage 3
# Gegebene Werte
ladung_Q_coulomb = 64.5   # in Coulomb
zeitdauer_t_sekunden = 5.5   # in Sekunden

# Stromstärke nach I = Q / t
stromstaerke_ampere = ladung_Q_coulomb / zeitdauer_t_sekunden

print("Die Stromstärke beträgt:", stromstaerke_ampere, "A")