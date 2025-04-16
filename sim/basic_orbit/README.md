Erklärung des Codes:

1. Gravitationskraft: Die Gravitationskraft zwischen der Erde und dem Satelliten wird mit dem Gravitationsgesetz von Newton berechnet.

2. Runge-Kutta-Integration: Diese Methode wird verwendet, um die Bewegung des Satelliten über die Zeit zu integrieren. Sie ist eine genaue Methode der numerischen Integration, die die Positionen und Geschwindigkeiten des Satelliten berechnet.

3. Simulation der Bewegung: Die Position des Satelliten wird zu jedem Zeitschritt unter Verwendung der Runge-Kutta-Methode aktualisiert, und die Bahn wird schließlich geplottet.

#######

🔬 Wissenschaftliche Grundlagen
1. Gesetz von der Erhaltung des Impulses (Translation):

    Prinzip: In einem abgeschlossenen System ohne äußere Kräfte bleibt der Gesamtimpuls konstant.

    Quelle: Newtons Bewegungsgesetze (insbesondere das 1. und 2. Gesetz)

    📚 Klassische Mechanik – Goldstein, Poole & Safko (Standardwerk)

    🤓 Bedeutet: Wenn du intern Masse verschiebst (z. B. das Gewicht im Zylinder), ändert sich der Gesamtschwerpunkt nicht, solange keine äußere Kraft wirkt.

2. Bewegung des Schwerpunkts in einem Gravitationsfeld

    Der Schwerpunkt eines ausgedehnten Körpers bewegt sich so, als wäre die gesamte Masse in diesem Punkt konzentriert.

    Voraussetzung: Das Gravitationsfeld ist homogen oder lässt sich näherungsweise als Zentralfeld betrachten (wie z. B. die Gravitation der Erde in vielen Satellitenmodellen).

    📚 Siehe: Classical Mechanics von John R. Taylor oder Mechanics von Landau & Lifshitz

3. Innere Massenverlagerung beeinflusst nicht die Bahn eines abgeschlossenen Systems

    Das kommt z. B. bei Satelliten mit beweglichen Massen oder in der Raumfahrttechnik vor.

    NASA und ESA berücksichtigen interne Massenverlagerungen in Modellen für Reaktionsräder, Treibstoffbewegungen etc., aber diese verändern nicht die Bahn des Schwerpunkts – nur z. B. die Rotationsdynamik.

        „The motion of the center of mass of a system of particles is not affected by internal forces, only by external ones.“
        – Marion & Thornton, Classical Dynamics of Particles and Systems

4. Noether-Theorem

    Das Noether-Theorem stellt den Zusammenhang zwischen Symmetrien und Erhaltungsgrößen her.

    Translation → Impulserhaltung

    Rotation → Drehimpulserhaltung

    📚 Emmy Noether, 1918 (Grundlage moderner theoretischer Physik)

🚀 Anwendung in der Raumfahrt

    In der Raumfahrt gibt es viele Beispiele, wo Satelliten intern Massen verlagern (z. B. durch Treibstoffbewegung oder rotierende Kreisel), um ihre Orientierung zu ändern (Attitude Control).

    Aber: Solange keine Masse ausgestoßen oder eine Kraft nach außen wirkt, bleibt der Orbit (die Bahn des Massenschwerpunkts) unverändert.

    Beispiel: Gravity Gradient Stabilization bei Satelliten nutzt passive Ausrichtung durch Massenverteilung – aber beeinflusst nicht die Umlaufbahn selbst.

✅ Zusammenfassung
Aktion	                      Beeinflusst Orbit?	       Begründung
Masse intern verschieben	         ❌ Nein	       Impuls bleibt gleich
Masse nach außen stoßen (z. B. Jet)	 ✅ Ja	           Impulsänderung
Energie intern umverteilen	         ❌ Nein	       Geschlossenes System
Energie nach außen abgeben	         ✅ Ja	           Offenes System
