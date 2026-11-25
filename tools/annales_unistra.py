# -*- coding: utf-8 -*-
"""Génère les blocs « Annales Université de Strasbourg » (CC1 nov. 2022, CC2 déc. 2022)
et les insère dans src/ entre des marqueurs. Usage : python3 tools/annales_unistra.py
Les énoncés sont recopiés tels quels (fautes comprises) ; seule la correction est ajoutée."""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')

def fr(a, b):
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'

CHAP = {
 'a1': "1.1–1.2 L'énergie du Soleil", 'a2': "1.3 Bilan radiatif & effet de serre",
 'a3': "1.4 Effets des activités humaines", 'a4': "2.1 Orbite & cycles de Milankovic",
 'a5': "2.2–2.4 Latitude, saisons, incidence", 'a6': "2.5–2.7 Redistribution & climats",
 'b0': "0. La Terre en couches", 'b1': "1. La forme de la Terre",
 'b3': "2b. Ondes sismiques & croûte", 'b4': "2c. Manteau, noyau, rais", 'b5': "3. Masse & densité",
}

E = '10<sup>{}</sup>'
rho = 'ρ'

CC1 = [  # (num, énoncé, [options], bonne réponse, explication, chapitre)
 ("1.", "En première approximation, on peut considérer que la Terre est une sphère. Quelle est son rayon ?",
  ["6731 km", "7631 km", "6371 km", "7163 km"], "C",
  "Le rayon moyen de la Terre est <b>R<sub>T</sub> = 6371 km</b>. Les autres réponses mélangent les mêmes chiffres : c'est un piège de lecture. Moyen mnémotechnique : « 63-71 ».", 'b1'),
 ("2.", "La Terre peut en fait être assimilée à un ellipsoïde de révolution. Quelle est approximativement la valeur de son aplatissement ?",
  ["1/200", "1/300", "1/400", "1/500"], "B",
  "Aplatissement f = (a − c)/a = (6378 − 6357)/6378 ≈ 21/6378 ≈ <b>1/298 ≈ 1/300</b>. La Terre est à peine aplatie : 21 km d'écart entre rayon équatorial et rayon polaire.", 'b1'),
 ("3.", "Comment définit-on la valeur du rayon de la Terre dans l’approximation sphérique ?",
  ["On prend le rayon équatorial de l’ellipsoïde approximant au mieux la Terre.",
   "On prend le rayon polaire de l’ellipsoïde approximant au mieux la Terre.",
   "On prend la moyenne des rayons équatorial et polaire de l’ellipsoïde approximant au mieux la Terre",
   "On prend la valeur qui donne à la sphère le même volume que celui de l’ellipsoïde approximant au mieux la Terre"], "D",
  "On cherche la sphère <b>de même volume</b> que l'ellipsoïde : R = (a²·c)<sup>1/3</sup> = (6378² × 6357)<sup>1/3</sup> ≈ 6371 km. Vérification : la moyenne simple (a + c)/2 donnerait 6367,5 km, ce n'est donc pas C. Le rayon équatorial (6378 km) et le rayon polaire (6357 km) ne donnent pas 6371 km non plus.", 'b1'),
 ("4.", "Quelle est la masse volumique moyenne de la Terre ?",
  ["5500 kg/m3", "7500 kg/m3", "9500 kg/m3", "11500 kg/m3"], "A",
  "ρ = M / V = 5,97×10<sup>24</sup> / (4/3 π × (6,371×10<sup>6</sup>)³) = 5,97×10<sup>24</sup> / 1,083×10<sup>21</sup> ≈ <b>5500 kg/m³</b> (5515). C'est 2 fois plus que les roches de surface (≈ 2700) : il y a donc des matériaux très denses en profondeur (le noyau de fer).", 'b5'),
 ("5.", "Quelle est la masse de la Terre ?",
  ["5.97 10<sup>22</sup> kg", "5.97 10<sup>23</sup> kg", "5.97 10<sup>24</sup> kg", "5.97 10<sup>25</sup> kg"], "C",
  "M<sub>T</sub> = <b>5,97×10<sup>24</sup> kg</b>, à connaître par cœur. Vérification : V × ρ = 1,083×10<sup>21</sup> m³ × 5515 kg/m³ ≈ 5,97×10<sup>24</sup> kg.", 'b5'),
 ("6.", "Qu’appelle-t-on le Moho ?",
  ["La limite entre la croute et le manteau", "La limite entre la lithosphère et l’asthénosphère",
   "La limite entre le manteau et le noyau", "La limite entre le noyau interne et le noyau externe"], "A",
  "Le <b>Moho</b> (Mohorovičić, 1909) = limite <b>croûte / manteau</b>, vers 30-35 km sous les continents et 7 km sous les océans. Les 3 discontinuités : Moho (croûte/manteau), Gutenberg (manteau/noyau), Lehmann (noyau externe/graine).", 'b0'),
 ("7.", "Qu’appelle-t-on la limite de Lehmann ?",
  ["La limite entre la croute et le manteau", "La limite entre la lithosphère et l’asthénosphère",
   "La limite entre le manteau et le noyau", "La limite entre le noyau interne et le noyau externe"], "D",
  "Inge <b>Lehmann</b> (1936) a découvert la <b>graine</b> : la limite de Lehmann sépare le <b>noyau externe liquide</b> du <b>noyau interne (graine) solide</b>, vers 5150 km de profondeur.", 'b0'),
 ("8.", "Quelle est la profondeur de la limite de Gutenberg ?",
  ["410 km", "700 km", "2885 km", "5155 km"], "C",
  "Gutenberg = limite <b>manteau / noyau</b> à environ <b>2885-2900 km</b>. 410 km et ≈ 670-700 km sont des discontinuités <i>à l'intérieur</i> du manteau ; 5155 km, c'est la limite de Lehmann.", 'b0'),
 ("9.", "Quelle est le rayon du noyau interne ?",
  ["616 km", "916 km", "1216 km", "1516 km"], "C",
  "Rayon de la graine = R<sub>T</sub> − profondeur de Lehmann = 6371 − 5155 = <b>1216 km</b>. Astuce : on retrouve la réponse avec les valeurs de la question 8.", 'b0'),
 ("10.", "Quelle est le volume du noyau interne ?",
  ["7.53 10<sup>18</sup> m3", "7.53 10<sup>19</sup> m3", "7.53 10<sup>20</sup> m3", "7.53 10<sup>21</sup> m3"], "A",
  "V = 4/3 π r³ avec r en <b>mètres</b> : r = 1216 km = 1,216×10<sup>6</sup> m. r³ = 1,798×10<sup>18</sup> m³ ; V = 4,189 × 1,798×10<sup>18</sup> ≈ <b>7,53×10<sup>18</sup> m³</b>. Piège : oublier de passer les km en m, ou se tromper dans les puissances de 10 (seul l'exposant change entre les réponses).", 'b5'),
 ("11.", "Quelle est la masse du noyau interne ?",
  ["9.79 10<sup>21</sup> kg", "9.79 10<sup>22</sup> kg", "9.79 10<sup>23</sup> kg", "9.79 10<sup>24</sup> kg"], "B",
  "m = ρ × V avec ρ(graine) ≈ 13 000 kg/m³ : 13 000 × 7,53×10<sup>18</sup> = <b>9,79×10<sup>22</sup> kg</b>. Contrôle de bon sens : c'est moins de 2 % de la masse de la Terre (5,97×10<sup>24</sup>), cohérent pour une petite boule centrale.", 'b5'),
 ("12.", "Quelle est le volume du noyau externe ?",
  ["1.69 10<sup>18</sup> m3", "1.69 10<sup>19</sup> m3", "1.69 10<sup>20</sup> m3", "1.69 10<sup>21</sup> m3"], "C",
  "Le noyau externe est une <b>coquille</b> : V = volume de la boule de rayon R<sub>noyau</sub> − volume de la graine. R<sub>noyau</sub> = 6371 − 2885 = 3486 km = 3,486×10<sup>6</sup> m → 4/3 π (3,486×10<sup>6</sup>)³ = 1,774×10<sup>20</sup> m³. On retire la graine : 1,774×10<sup>20</sup> − 0,0075×10<sup>20</sup> ≈ <b>1,69×10<sup>20</sup> m³</b>.", 'b5'),
 ("13.", "Quelle est la masse du noyau externe ?",
  ["1.86 10<sup>21</sup> kg", "1.86 10<sup>22</sup> kg", "1.86 10<sup>23</sup> kg", "1.86 10<sup>24</sup> kg"], "D",
  "m = ρ × V avec ρ(noyau externe) ≈ 11 000 kg/m³ : 11 000 × 1,69×10<sup>20</sup> ≈ <b>1,86×10<sup>24</sup> kg</b>. Ordre de grandeur : 1,69×10<sup>20</sup> × 10<sup>4</sup> = 10<sup>24</sup>.", 'b5'),
 ("14.", "Quelle est la masse relative du noyau (par rapport à la masse de la Terre) ?",
  ["33%", "38%", "43%", "48%"], "A",
  "Masse du noyau = graine + noyau externe = 0,098×10<sup>24</sup> + 1,86×10<sup>24</sup> ≈ 1,96×10<sup>24</sup> kg. Rapport : 1,96 / 5,97 ≈ <b>0,33 = 33 %</b>. À retenir : le noyau, c'est environ 1/6 du volume mais 1/3 de la masse.", 'b5'),
 ("15.", "Quelle est la densité moyenne de la croûte continentale ?",
  ["2.0", "2.7", "3.3", "4.6"], "B",
  "Croûte continentale (granite) : <b>d ≈ 2,7</b>. Croûte océanique (basalte) : ≈ 2,9-3,0. Manteau (péridotite) : ≈ 3,3. Une densité n'a pas d'unité (ρ / ρ<sub>eau</sub>).", 'b0'),
 ("16.", "Quelle est la densité juste en dessous du Moho ?",
  ["2.0", "2.7", "3.3", "4.6"], "C",
  "Sous le Moho, on est dans le <b>manteau</b> (péridotite) : <b>d ≈ 3,3</b>. Le saut 2,7 → 3,3 au Moho explique que les ondes sismiques y accélèrent (≈ 6 → 8 km/s).", 'b0'),
 ("17.", "Est ce qu’on peut dire que la croûte et la lithosphère, c’est la même chose ?",
  ["Oui", "Non", "Peut-être"], "B",
  "<b>Non</b>. La croûte est définie par sa <b>chimie</b> (roches, limite = Moho). La lithosphère est définie par son <b>comportement mécanique</b> (rigide) : elle comprend la croûte <b>+</b> le haut du manteau supérieur.", 'b0'),
 ("18.", "Est ce qu’on peut dire que le manteau supérieur et la lithosphère, c’est la même chose ?",
  ["Oui", "Non", "Peut-être"], "B",
  "<b>Non</b>. La lithosphère ne contient que la <b>partie supérieure</b> du manteau supérieur (le manteau lithosphérique). En dessous, le reste du manteau supérieur est ductile : c'est l'asthénosphère.", 'b0'),
 ("19.", "La lithosphère comprend :",
  ["La croûte et le manteau", "La croûte et le manteau supérieur", "La croûte et la partie supérieure du manteau supérieur"], "C",
  "Lithosphère = <b>croûte + partie supérieure (rigide) du manteau supérieur</b>, sur ≈ 100 km d'épaisseur en moyenne. A et B en mettent trop.", 'b0'),
 ("20.", "Si la masse volumique augmente linéairement au centre de la Terre et si elle vaut 2600 kg.m<sup>-3</sup> en surface et 12500 kg.m<sup>-3</sup> au centre de la Terre, quelle est la valeur de la masse volumique à 1000km de profondeur ? On prendra le rayon de la Terre égal à 6371 km.",
  ["4154 kg.m<sup>-3</sup>", "6154 kg.m<sup>-3</sup>", "8154 kg.m<sup>-3</sup>", "10154 kg.m<sup>-3</sup>"], "A",
  "La masse volumique gagne (12500 − 2600) = 9900 kg/m³ sur 6371 km de profondeur. À 1000 km : ρ = 2600 + 9900 × 1000/6371 = 2600 + 1554 = <b>4154 kg/m³</b>.", 'b5'),
 ("21.", f"Si on considère que la densité à l’intérieur de la Terre varie linéairement avec la profondeur, si ρ<sub>s</sub> et ρ<sub>c</sub> sont respectivement les densités à la surface et au centre de la Terre, R<sub>T</sub> le rayon de la Terre et r la distance au centre de la Terre, alors on peut écrire :",
  [f"ρ(r) = {fr('ρ<sub>s</sub>+ρ<sub>c</sub>','R<sub>T</sub>')} r + ρ<sub>c</sub>",
   f"ρ(r) = {fr('ρ<sub>s</sub>+ρ<sub>c</sub>','R<sub>T</sub>')} r − ρ<sub>c</sub>",
   f"ρ(r) = {fr('ρ<sub>s</sub>−ρ<sub>c</sub>','R<sub>T</sub>')} r + ρ<sub>c</sub>",
   f"ρ(r) = {fr('ρ<sub>s</sub>−ρ<sub>c</sub>','R<sub>T</sub>')} r − ρ<sub>c</sub>"], "C",
  "On teste les deux bouts. Au centre (r = 0) il faut ρ = ρ<sub>c</sub> : seules A et C conviennent. En surface (r = R<sub>T</sub>) il faut ρ = ρ<sub>s</sub> : avec C, (ρ<sub>s</sub> − ρ<sub>c</sub>) + ρ<sub>c</sub> = ρ<sub>s</sub> ✔ ; avec A on obtiendrait ρ<sub>s</sub> + 2ρ<sub>c</sub> ✘. Réponse <b>C</b>. Méthode à retenir : toujours vérifier r = 0 et r = R<sub>T</sub>.", 'b5'),
 ("22.", "Alors on peut écrire la masse de la Terre :",
  ["M = ∫<sub>O</sub><sup>R<sub>T</sub></sup> ρ(r)πr<sup>2</sup>dr", "M = ∫<sub>O</sub><sup>R<sub>T</sub></sup> ρ(r)4πr<sup>2</sup>dr",
   "M = ∫<sub>O</sub><sup>R<sub>T</sub></sup> ρ(r)πr<sup>3</sup>dr", "M = ∫<sub>O</sub><sup>R<sub>T</sub></sup> ρ(r)πrdr"], "B",
  "On découpe la Terre en <b>pelures d'oignon</b> : une coquille de rayon r et d'épaisseur dr a pour volume (surface de la sphère) × épaisseur = <b>4πr² dr</b>, et pour masse ρ(r)·4πr² dr. On additionne de 0 à R<sub>T</sub>. Vérification : si ρ est constant, on retrouve ρ × 4/3 π R<sub>T</sub>³ ✔.", 'b5'),
 ("23.", "La constante solaire vaut 1370 W.m<sup>-2</sup>. En déduire parmi les valeurs proposées ci-dessous, la puissance moyenne du rayonnement reçu par une surface de 1 m<sup>2</sup> située au sommet de l’atmosphère et orthogonale à un rayon terrestre",
  ["1370 W.m<sup>-2</sup>", "1000 W.m<sup>-2</sup>", "685 W.m<sup>-2</sup>", "342 W.m<sup>-2</sup>"], "D",
  "La Terre intercepte le flux sur un disque (πR²) mais le répartit sur toute la sphère (4πR²), jour et nuit compris : moyenne = S/4 = 1370/4 ≈ <b>342 W/m²</b>. Piège : 685 = S/2 (on aurait oublié que la surface éclairée est une demi-sphère et pas un disque).", 'a1'),
 ("24.", "L’albédo d’une surface est le rapport de :",
  ["L’énergie lumineuse incidente avec la constante solaire",
   "L’énergie lumineuse réfléchie par unité de surface avec l’énergie lumineuse incidente",
   "L’énergie lumineuse incidente avec l’énergie lumineuse réfléchie par unité de surface",
   "La constante solaire avec l’énergie solaire incidente"], "B",
  "Albédo = <b>réfléchi / incident</b>, un nombre entre 0 (tout absorbé) et 1 (tout réfléchi). C est l'inverse (il donnerait une valeur &gt; 1). Terre : ≈ 0,30 ; neige fraîche ≈ 0,8-0,9 ; océan ≈ 0,06.", 'a2'),
 ("25.", "La surface terrestre et l'atmosphère sont chauffées par le rayonnement solaire ; elles se refroidissent aussi en rayonnant de l'énergie vers l'espace. Pour le rayonnement solaire reçu (1) et pour le rayonnement émis vers l’espace (2), indiquez chaque fois le domaine correspondant à la majeure partie de l’énergie rayonnée :",
  ["L’infrarouge (1) et les UV (2)", "Les UV (1) et l’infrarouge (2)",
   "Les longueurs d'onde visibles (1) et l’infrarouge (2)", "Les longueurs d’onde visibles (1) et les UV (2)"], "C",
  "Loi de Wien : λ<sub>max</sub> = 2898 / T (µm). Soleil, T ≈ 5800 K → λ<sub>max</sub> ≈ 0,5 µm : le <b>visible</b>. Terre, T ≈ 255-288 K → λ<sub>max</sub> ≈ 10 µm : l'<b>infrarouge</b>. Les deux spectres ne se recouvrent presque pas, c'est la base de l'effet de serre.", 'a2'),
 ("26.", "Déterminer l’énergie libérée par la fusion d’un atome de carbone avec un atome d’hydrogène<br><span style='display:block;text-align:center;margin:6px 0'><sup>12</sup><sub>6</sub>C + <sup>1</sup><sub>1</sub>H → <sup>13</sup><sub>7</sub>N + rayonnement ionisant</span>Données : 1 uma = 1.660539*10<sup>-27</sup> kg, <sup>12</sup>C = 12.011 uma, <sup>1</sup>H=1.0079 uma, <sup>13</sup>N=13.005739 uma",
  ["1.20*10<sup>15</sup> J", "0.20*10<sup>-11</sup> J", "4.33*10<sup>-12</sup> J", "3.9*10<sup>-20</sup> J"], "B",
  "1) Perte de masse : Δm = (12,011 + 1,0079) − 13,005739 = 0,013161 uma.<br>2) En kg : 0,013161 × 1,660539×10<sup>-27</sup> = 2,185×10<sup>-29</sup> kg.<br>3) E = Δm·c² = 2,185×10<sup>-29</sup> × (3×10<sup>8</sup>)² = 1,96×10<sup>-12</sup> J ≈ <b>0,20×10<sup>-11</sup> J</b>. Piège : la réponse est écrite 0,20×10<sup>-11</sup> et non 2,0×10<sup>-12</sup> ; c'est la même valeur.", 'a1'),
 ("27.", "Trouver la phrase correcte :",
  ["La longueur d’onde à laquelle un corps noir émet le plus de flux de lumière énergétique est inversement proportionnelle à sa température",
   "La longueur d’onde à laquelle un corps noir émet le moins de flux de lumière énergétique est inversement proportionnelle à sa température",
   "La longueur d’onde à laquelle un corps noir émet le plus de flux de lumière énergétique est proportionnelle à sa température",
   "La longueur d’onde à laquelle un corps noir émet le moins de flux de lumière énergétique est proportionnelle à sa température"], "A",
  "C'est la <b>loi de Wien</b> : λ<sub>max</sub> = 2898 µm·K / T. λ<sub>max</sub> est la longueur d'onde du <b>maximum</b> d'émission, et elle est <b>inversement</b> proportionnelle à T : plus un corps est chaud, plus il émet vers le bleu.", 'a1'),
 ("28.", "L’albédo de Géosciences vaut",
  ["0,23", "0,30", "0,77", "0,90"], "C",
  "Flux solaire moyen reçu = S/4 = 2580/4 = 645 W/m². Albédo = réfléchi / reçu = 498/645 ≈ <b>0,77</b>. Piège : diviser par 2580 (donnerait 0,19, absent des réponses) ; 0,23 = 1 − 0,77 est la part <i>absorbée</i>.", 'a2'),
 ("29.", "Le flux solaire arrivant à la surface de Géosciences est de",
  ["148 W.m<sup>-2</sup>", "497 W.m<sup>-2</sup>", "645 W.m<sup>-2</sup>", "2580 W.m<sup>-2</sup>"], "C",
  "Comme pour la Terre, on répartit la constante solaire sur toute la sphère : S/4 = 2580/4 = <b>645 W/m²</b> (c'est la valeur utilisée en Q28). 148 W/m² est la partie <i>absorbée</i> (645 − 498 ≈ 147), qui sert à la Q30.", 'a2'),
 ("30.", "La température d’équilibre qu’on peut en déduire est égale à",
  ["-227 °C", "-47°C", "47°C", "227°C"], "B",
  "À l'équilibre, la planète émet autant qu'elle absorbe : σT⁴ = (1 − A)·S/4 = 645 − 498 ≈ 147 W/m².<br>T = (147 / 5,6703×10<sup>-8</sup>)<sup>1/4</sup> = (2,59×10<sup>9</sup>)<sup>1/4</sup> ≈ 226 K, soit 226 − 273 ≈ <b>−47 °C</b>. Astuce calculatrice : puissance 1/4 = deux racines carrées successives. Piège : oublier de passer de K en °C (on lirait 227 → D).", 'a2'),
]

CC2 = [
 ("1-", "Lorsqu’une onde sismique arrive à un interface plan séparant 2 milieux de vitesses V<sub>1</sub> et V<sub>2</sub> avec un angle d’incidence i<sub>1</sub>, elle est transmise dans le milieu de l’autre côté de l’interface et repart avec un angle i<sub>2</sub>. La loi de Snell-Descartes dit que :",
  ["V<sub>1</sub> sin i<sub>1</sub> = V<sub>2</sub> sin i<sub>2</sub>",
   f"{fr('sin i<sub>1</sub>','V<sub>2</sub>')} = {fr('sin i<sub>2</sub>','V<sub>1</sub>')}",
   f"{fr('sin i<sub>1</sub>','V<sub>1</sub>')} = {fr('sin i<sub>2</sub>','V<sub>2</sub>')}",
   "sin i<sub>1</sub> = sin i<sub>2</sub>"], "C",
  "Loi de Snell-Descartes en sismique : <b>sin i<sub>1</sub>/V<sub>1</sub> = sin i<sub>2</sub>/V<sub>2</sub></b> (= paramètre du rai p, constant le long du rai). Chaque sinus va avec la vitesse <b>de son propre milieu</b>. Conséquence : si V<sub>2</sub> &gt; V<sub>1</sub>, l'onde s'écarte de la normale (i<sub>2</sub> &gt; i<sub>1</sub>).", 'b3'),
 ("2-", "Qu’est-ce que l’angle d’incidence critique i<sub>c</sub> :",
  ["L’angle d’incidence maximale pour avoir une onde transmise et où apparait l’onde conique",
   "L’angle où il n’y a pas d’onde réfléchie", "L’angle où l’onde P est totalement convertie en onde S",
   "L’angle où l’onde P revient en surface en faisant une explosion"], "A",
  "À l'angle critique, l'onde transmise part à 90° (i<sub>2</sub> = 90°) et file le long de l'interface à la vitesse V<sub>2</sub> : c'est elle qui génère l'<b>onde conique</b> (réfractée). Au-delà de i<sub>c</sub>, il n'y a plus d'onde transmise : réflexion totale. B est faux : il y a toujours une onde réfléchie.", 'b3'),
 ("3-", "Quelle relation est juste :",
  ["i<sub>c</sub> = asinV<sub>1</sub>/V<sub>2</sub>", "i<sub>c</sub> = V<sub>1</sub>/V<sub>2</sub>", "i<sub>c</sub> = sinV<sub>1</sub>/sinV<sub>2</sub>", "sinV<sub>1</sub> = i<sub>c</sub>sinV<sub>2</sub>"], "A",
  "Snell-Descartes avec i<sub>2</sub> = 90° (sin 90° = 1) : sin i<sub>c</sub>/V<sub>1</sub> = 1/V<sub>2</sub>, donc sin i<sub>c</sub> = V<sub>1</sub>/V<sub>2</sub> et <b>i<sub>c</sub> = arcsin(V<sub>1</sub>/V<sub>2</sub>)</b> (« asin » = arcsin). B oublie l'arcsin ; C et D prennent le sinus d'une vitesse, ce qui n'a pas de sens.", 'b3'),
 ("4-", "Laquelle des formules ci-dessous donne le temps de parcours de l’onde conique dans un milieu constitué d’une couche horizontale d’épaisseur h et de vitesse V<sub>1</sub>, sur une ½ espace homogène de vitesse V<sub>2</sub> :",
  [f"t(x) = {fr('x','V<sub>1</sub>')} + {fr('2hcos i<sub>c</sub>','V<sub>2</sub>')}",
   f"t(x) = {fr('x','V<sub>2</sub>')} + {fr('2hcos i<sub>c</sub>','V<sub>1</sub>')}",
   f"t(x) = {fr('2x','V<sub>2</sub>')} + {fr('2hcos i<sub>c</sub>','V<sub>1</sub>')}",
   f"t(x) = {fr('x','V<sub>2</sub>')} + {fr('hcos i<sub>c</sub>','V<sub>1</sub>')}"], "B",
  "L'onde conique est une <b>droite</b> sur l'hodochrone : pente <b>1/V<sub>2</sub></b> (elle voyage à V<sub>2</sub> le long de l'interface) et ordonnée à l'origine t<sub>0</sub> = <b>2h cos i<sub>c</sub>/V<sub>1</sub></b> (descente + remontée dans la couche 1, d'où le « 2 » et le V<sub>1</sub>). D oublie le 2 ; C double x ; A inverse les vitesses.", 'b3'),
 ("5-", "Dans un milieu avec 2 couches, la première de vitesse V<sub>1</sub> = 4km/s et d’épaisseur h = 5km et la seconde de vitesse V<sub>2</sub> = 6km/s, à quelle distance l’onde directe et l’onde conique arrivent au même instant ?",
  ["22,3 km", "32,3 km", "42,3 km", "52,3 km"], "A",
  "C'est la <b>distance de croisement</b> x<sub>c</sub> : x/V<sub>1</sub> = x/V<sub>2</sub> + 2h cos i<sub>c</sub>/V<sub>1</sub>, ce qui donne x<sub>c</sub> = 2h √((V<sub>2</sub>+V<sub>1</sub>)/(V<sub>2</sub>−V<sub>1</sub>)).<br>x<sub>c</sub> = 2×5 × √(10/2) = 10 × √5 = 10 × 2,236 ≈ <b>22,3 km</b>.<br>Vérification : directe 22,36/4 = 5,59 s ; conique 22,36/6 + 1,86 = 5,59 s ✔.", 'b3'),
 ("6-", "Dans un milieu avec 2 couches, la première de vitesse V<sub>1</sub> = 4km/s et d’épaisseur h = 5km et la seconde de vitesse V<sub>2</sub> = 6km/s, pour une distance de 30 km, quel est le temps de parcours de l’onde directe ?",
  ["3,5 s", "5,5 s", "7,5 s", "9,5 s"], "C",
  "L'onde directe longe la surface dans la couche 1 : t = x/V<sub>1</sub> = 30/4 = <b>7,5 s</b>.", 'b3'),
 ("7-", "Dans un milieu avec 2 couches, la première de vitesse V<sub>1</sub> = 4km/s et d’épaisseur h = 5km et la seconde de vitesse V<sub>2</sub> = 6km/s, pour une distance de 30 km, quel est le temps de parcours de l’onde réfléchie ?",
  ["6,9 s", "7,9 s", "8,9 s", "9,9 s"], "B",
  "L'onde réfléchie descend jusqu'à l'interface et remonte, toujours à V<sub>1</sub>. Par Pythagore, le trajet vaut √(x² + 4h²) : t = √(30² + 10²)/4 = √1000/4 = 31,62/4 ≈ <b>7,9 s</b>. Elle arrive toujours après l'onde directe (7,5 s) : logique, son chemin est plus long à la même vitesse.", 'b3'),
 ("8-", "Dans un milieu avec 2 couches, la première de vitesse V<sub>1</sub> = 4km/s et d’épaisseur h = 5km et la seconde de vitesse V<sub>2</sub> = 6km/s, pour une distance de 30 km, quel est le temps de parcours de l’onde conique ?",
  ["4,9 s", "5,9 s", "6,9 s", "7,9 s"], "C",
  "sin i<sub>c</sub> = 4/6 = 0,667 → i<sub>c</sub> = 41,8° → cos i<sub>c</sub> = 0,745.<br>t = x/V<sub>2</sub> + 2h cos i<sub>c</sub>/V<sub>1</sub> = 30/6 + (2×5×0,745)/4 = 5 + 1,86 = <b>6,9 s</b>.<br>À 30 km (au-delà de x<sub>c</sub> = 22,3 km), la conique arrive <b>en premier</b> (6,9 s &lt; 7,5 s &lt; 7,9 s).", 'b3'),
 ("9-", "On réalise un profil sismique au-dessus d’un milieu à 2 couches (la première de vitesse V<sub>1</sub> et d’épaisseur h et la seconde de vitesse V<sub>2</sub>).<br>On observe les temps suivants pour l’onde directe : en x<sub>1</sub>=60km, t<sub>1</sub>=10,9s et en x<sub>2</sub>=120km, t<sub>2</sub> = 21,8s.<br>Pour l’onde conique on observe en x<sub>3</sub>=200km, t<sub>3</sub>=32,5s et en x<sub>4</sub>=300km, t<sub>4</sub>=44,7s.<br>Quelle est la valeur de V<sub>1</sub> ?",
  ["5,0 km/s", "5,5 km/s", "6,0 km/s", "6,5 km/s"], "B",
  "L'onde directe passe par l'origine : V<sub>1</sub> = x/t = 60/10,9 = <b>5,5 km/s</b> (et 120/21,8 = 5,5 aussi : la droite passe bien par 0).", 'b3'),
 ("10-", "On réalise un profil sismique au-dessus d’un milieu à 2 couches (la première de vitesse V<sub>1</sub> et d’épaisseur h et la seconde de vitesse V<sub>2</sub>).<br>On observe les temps suivants pour l’onde directe : en x<sub>1</sub>=60km, t<sub>1</sub>=10,9s et en x<sub>2</sub>=120km, t<sub>2</sub> = 21,8s.<br>Pour l’onde conique on observe en x<sub>3</sub>=200km, t<sub>3</sub>=32,5s et en x<sub>4</sub>=300km, t<sub>4</sub>=44,7s.<br>Quelle est la valeur de V<sub>2</sub> ?",
  ["8,0 km/s", "8,2 km/s", "8,4 km/s", "8,6 km/s"], "B",
  "La conique ne passe <b>pas</b> par l'origine : on prend la pente entre deux points. V<sub>2</sub> = Δx/Δt = (300 − 200)/(44,7 − 32,5) = 100/12,2 = <b>8,2 km/s</b>. Piège : faire 200/32,5 ou 300/44,7 (on obtiendrait 6,2 ou 6,7). Avec V<sub>2</sub> ≈ 8 km/s, la couche 2 est le <b>manteau</b> : l'interface est le Moho.", 'b3'),
 ("11-", "On réalise un profil sismique au-dessus d’un milieu à 2 couches (la première de vitesse V<sub>1</sub> et d’épaisseur h et la seconde de vitesse V<sub>2</sub>).<br>On observe les temps suivants pour l’onde directe : en x<sub>1</sub>=60km, t<sub>1</sub>=10,9s et en x<sub>2</sub>=120km, t<sub>2</sub> = 21,8s.<br>Pour l’onde conique on observe en x<sub>3</sub>=200km, t<sub>3</sub>=32,5s et en x<sub>4</sub>=300km, t<sub>4</sub>=44,7s.<br>Quelle est la valeur de h ?",
  ["30 km", "35 km/s", "40 km/s", "45 km/s"], "A",
  "1) Ordonnée à l'origine de la conique : t<sub>0</sub> = t<sub>3</sub> − x<sub>3</sub>/V<sub>2</sub> = 32,5 − 200/8,2 = 32,5 − 24,4 = 8,1 s.<br>2) sin i<sub>c</sub> = V<sub>1</sub>/V<sub>2</sub> = 5,5/8,2 = 0,671 → i<sub>c</sub> = 42,2° → cos i<sub>c</sub> = 0,741.<br>3) t<sub>0</sub> = 2h cos i<sub>c</sub>/V<sub>1</sub> donc h = t<sub>0</sub>·V<sub>1</sub>/(2 cos i<sub>c</sub>) = 8,1 × 5,5/(2 × 0,741) ≈ <b>30 km</b> : une croûte continentale classique. (Les « km/s » des réponses B à D sont une coquille du sujet : une épaisseur est en km.)", 'b3'),
 ("12-", "Quelle est l’épaisseur moyenne de la croûte continentale sous l’Altiplano, le plateau central des Andes ?",
  ["30 km", "34 km", "38 km", "70 km"], "D",
  "Sous les grandes chaînes de montagnes, la croûte est très épaissie : c'est la <b>racine crustale</b> (isostasie : la montagne « flotte » sur le manteau comme un iceberg). Sous l'Altiplano, elle atteint <b>≈ 70 km</b>, environ le double de la moyenne continentale (30-35 km).", 'b3'),
 ("13-", "Comment appelle -t-on une onde P qui traverse le manteau puis le noyau externe, se réfléchit sur l’interface de Lehmann et remonte à la surface ?",
  ["PKP", "PKKP", "PKiKP", "PKIKP"], "C",
  "Code des phases : P = onde P dans le manteau, K = onde P dans le noyau externe, I = onde P dans la graine, <b>i = réflexion sur la graine</b>. Trajet : P (manteau) → K (noyau externe) → réflexion sur la graine (i) → K → P : <b>PKiKP</b>. Attention à la casse : PKIKP (I majuscule) <i>traverse</i> la graine ; PKKP se réfléchit sous la limite noyau-manteau.", 'b4'),
 ("14-", "Qu’est-ce que PREM",
  ["Un modèle de Terre où les paramètres physiques varient en fonction de la profondeur",
   "Un modèle de Terre en 3 dimensions", "Le vrai nom de l’onde P", "Le nom de l’interface entre la croûte et le manteau"], "A",
  "PREM = <i>Preliminary Reference Earth Model</i> (Dziewonski & Anderson, 1981) : un modèle <b>à une dimension</b> (1D) qui donne vitesses sismiques, densité, pression… en fonction de la <b>seule profondeur</b>. Les modèles 3D sont ceux de la tomographie sismique.", 'b4'),
 ("15-", "La latitude est une coordonnée géographique représentée par une",
  ["Distance, expression de la position d’un point sur Terre, au nord ou au sud de l’équateur",
   "Distance, expression de la position d’un point sur Terre, à l’est ou à l’ouest d’une perpendiculaire à l’équateur",
   "Valeur angulaire, expression de la position d’un point sur Terre, au nord ou au sud de l’équateur",
   "Valeur angulaire, expression de la position d’un point sur Terre, à l’est ou à l’ouest d’une perpendiculaire à l’équateur"], "C",
  "La latitude est un <b>angle</b> (en degrés, de 0° à l'équateur à 90° aux pôles), mesuré <b>au nord ou au sud de l'équateur</b>. D décrit la <b>longitude</b> (est/ouest du méridien de Greenwich). A et B sont faux : ce ne sont pas des distances.", 'a5'),
 ("16-", "La déclinaison solaire est",
  ["L’angle que forme le rayonnement solaire avec le plan de l’horizon en un lieu donné",
   "L’angle que forme la direction Terre-Soleil par rapport au plan de l’équateur terrestre",
   "Le rayonnement solaire avec le plan de l’équateur terrestre",
   "L’angle que forme la direction Terre-Soleil avec l’horizon en un lieu donné"], "B",
  "Déclinaison δ = angle entre la direction <b>Terre-Soleil</b> et le <b>plan de l'équateur</b>. Elle varie de +23,44° (solstice de juin) à −23,44° (solstice de décembre) et vaut 0 aux équinoxes. Elle ne dépend pas du lieu : A et D décrivent la hauteur du Soleil, qui elle dépend du lieu.", 'a5'),
 ("17-", "Quand la déclinaison est minimale, la durée du jour est",
  ["Quasi nulle dans l’hémisphère sud", "Nulle au niveau de l’équateur",
   "Faible aux latitudes tempérées de l’hémisphère sud", "Maximale dans les régions polaires de l’hémisphère sud"], "D",
  "Déclinaison minimale (−23,44°) = <b>solstice de décembre</b> : le Soleil est au-dessus du tropique du Capricorne, c'est l'<b>été austral</b>. Les régions polaires sud sont éclairées 24 h/24 (jour polaire) : durée du jour <b>maximale</b>. A et C disent l'inverse ; à l'équateur le jour dure toujours ≈ 12 h (B faux).", 'a5'),
 ("18-", "La couche d’ozone absorbe essentiellement les rayonnements",
  ["Solaires incidents infra-rouges", "Solaires incidents ultra-violets", "Terrestres émis ultra-violets", "Terrestres émis infra-rouges"], "B",
  "L'ozone <b>stratosphérique</b> (la « couche d'ozone », 15-35 km) filtre les <b>UV venant du Soleil</b> (UV-B et UV-C). C'est ce qui chauffe la stratosphère et protège le vivant. La Terre, elle, n'émet pas d'UV (trop froide) : C est impossible.", 'a3'),
 ("19-", "L’ozone troposphérique absorbe essentiellement les rayonnements",
  ["Solaires incidents infra-rouges", "Solaires incidents ultra-violets", "Terrestres émis ultra-violets", "Terrestres émis infra-rouges"], "D",
  "L'ozone <b>troposphérique</b> (près du sol, polluant) agit comme un <b>gaz à effet de serre</b> : il absorbe l'<b>infrarouge émis par la Terre</b> (bande vers 9,6 µm). Même molécule que Q18, mais rôle différent selon l'altitude : c'est le piège de la paire de questions.", 'a3'),
 ("20-", "Les saisons sont dues à",
  ["La distance Terre-Soleil", "La sphéricité de la Terre", "Aux équinoxes de printemps", "L’obliquité de la Terre"], "D",
  "Les saisons viennent de l'<b>obliquité</b> (inclinaison de l'axe de 23,44°) : au fil de l'année, chaque hémisphère reçoit les rayons plus ou moins verticalement et pendant plus ou moins longtemps. Piège classique A : la Terre est au plus près du Soleil début janvier, en plein hiver boréal.", 'a5'),
 ("21-", "Le soleil est au zénith quand",
  ["L’incidence solaire forme un angle de 90° par rapport à l’horizon",
   "La déclinaison solaire forme un angle de 90° par rapport à l’équateur",
   "L’incidence solaire forme un angle de 90° par rapport à l’équateur",
   "La déclinaison solaire forme un angle de 90° par rapport à l’horizon"], "A",
  "Zénith = le point <b>juste au-dessus de la tête</b> : les rayons arrivent à la verticale, à <b>90° de l'horizon</b>. Cela n'arrive qu'entre les tropiques. La déclinaison ne dépasse jamais 23,44° : B et D sont impossibles.", 'a5'),
 ("22-", "Le solstice est le jour où",
  ["La déclinaison solaire est minimale et la durée du jour est égale à celle de la nuit",
   "La déclinaison solaire est maximale et l’écart entre la durée du jour et de la nuit est le plus important",
   "La déclinaison solaire est nulle et la durée du jour est égale à celle de la nuit",
   "La déclinaison solaire est nulle et l’écart entre la durée du jour et de la nuit est le plus important"], "B",
  "Au solstice, la déclinaison atteint son extrême (±23,44°, « maximale » en valeur absolue) et l'écart jour/nuit est le <b>plus grand</b> de l'année (jour le plus long ou le plus court). C décrit l'<b>équinoxe</b> (δ = 0, jour = nuit). A et D mélangent les deux.", 'a5'),
 ("23-", "Quand l’inclinaison est la plus forte",
  ["Les étés sont plus chauds et les hivers plus chauds", "Les étés sont plus froids et les hivers plus chauds",
   "Les étés sont plus chauds et les hivers sont plus froids", "Les étés sont plus froids et les hivers sont plus froids"], "C",
  "Plus l'axe est incliné (obliquité qui varie entre ≈ 22,1° et 24,5°), plus le <b>contraste saisonnier</b> est fort : en été l'hémisphère est encore plus tourné vers le Soleil, en hiver encore plus détourné. Donc <b>étés plus chauds et hivers plus froids</b>.", 'a4'),
 ("24-", "L’obliquité a une périodicité de",
  ["100 et 413 ka", "41 ka", "23 et 19 ka"], "B",
  "Les 3 cycles de Milankovic : <b>excentricité</b> ≈ 100 et 413 ka ; <b>obliquité</b> ≈ <b>41 ka</b> ; <b>précession</b> ≈ 23 et 19 ka (ka = milliers d'années). Moyen de retenir : du plus long au plus court, E-O-P (100 / 41 / 21).", 'a4'),
 ("25-", "La précession des équinoxes",
  ["Entraîne un déplacement des pôles", "Module le contraste des saisons",
   "Correspond au degré d’aplatissement de l’ellipse par rapport au cercle",
   "Est l’inclinaison de l’axe de rotation terrestre par rapport à une perpendiculaire au plan de l’écliptique"], "B",
  "La précession fait tourner l'axe de la Terre comme une toupie : la date de passage au plus près du Soleil (périhélie) se décale par rapport aux saisons. Selon que l'été d'un hémisphère tombe au périhélie ou à l'aphélie, ses saisons sont plus ou moins contrastées : elle <b>module le contraste des saisons</b>. C = définition de l'excentricité ; D = définition de l'obliquité.", 'a4'),
 ("26-", "L’insolation moyenne globale annuelle reçue sur Terre est",
  ["Inversement proportionnelle à √(1-e<sup>2</sup>) et diminue très légèrement quand l’excentricité augmente",
   "Proportionnelle à √(1-e<sup>2</sup>) et diminue très légèrement quand l’excentricité augmente",
   "Proportionnelle à √(1-e<sup>2</sup>) et augmente très légèrement quand l’excentricité augmente",
   "Inversement proportionnelle à √(1-e<sup>2</sup>) et augmente très légèrement quand l’excentricité augmente"], "D",
  "Insolation moyenne annuelle ∝ <b>1/√(1 − e²)</b>. Quand e augmente, (1 − e²) diminue, donc 1/√(1 − e²) <b>augmente</b>… très légèrement (e ≤ 0,06 → +0,2 % au maximum). C'est pourquoi l'excentricité agit peu sur le total annuel, mais beaucoup via la précession. A est contradictoire (inversement proportionnelle mais diminue).", 'a4'),
 ("27-", "La deuxième loi de Képler dit :",
  ["L’orbite de la Terre est une ellipse dont le Soleil occupe l’un des foyers",
   "Les planètes balayent des aires égales en des temps égaux",
   "Le carré de la période de révolution est proportionnel au cube de la distance au Soleil"], "B",
  "1<sup>re</sup> loi = orbite elliptique (A) ; <b>2<sup>e</sup> loi = loi des aires (B)</b> : la planète va plus vite près du Soleil ; 3<sup>e</sup> loi = T² ∝ a³ (C).", 'a4'),
 ("28-", "Les masses d’eau dans l’hémisphère sud sont déviées vers",
  ["La droite", "La gauche", "Le haut", "Le bas"], "B",
  "Force de Coriolis : déviation vers la <b>droite dans l'hémisphère nord</b>, vers la <b>gauche dans l'hémisphère sud</b>, nulle à l'équateur.", 'a6'),
 ("29-", "Au solstice d’été de l’hémisphère nord la déclinaison est",
  ["Maximale et la durée du jour est minimale dans l’hémisphère nord",
   "Minimale et la durée du jour est maximale dans l’hémisphère nord",
   "Maximale et la durée du jour est maximale dans l’hémisphère nord",
   "Minimale et la durée du jour est minimale dans l’hémisphère nord"], "C",
  "Solstice de juin (≈ 21 juin) : Soleil au-dessus du tropique du Cancer, déclinaison <b>maximale (+23,44°)</b> et jour le <b>plus long</b> de l'année dans l'hémisphère nord.", 'a5'),
 ("30-", "Transformer 43°18’ en valeur décimale",
  ["26,18’", "72,18’", "43,11’", "43,30’"], "D",
  "1° = 60′, donc 18′ = 18/60 = 0,30°. 43°18′ = <b>43,30°</b>. Piège : écrire 43,18 (on ne peut pas juxtaposer les minutes, c'est de la base 60). Le symbole ’ dans les réponses est une coquille du sujet : il faut lire 43,30°.", 'a5'),
]

SUJETS = [
 ('cc1', 'CC1 · Novembre 2022', CC1),
 ('cc2', 'CC2 · Décembre 2022', CC2),
]

def item(cc, label, q, ctx):
    num, txt, opts, ans, why, ch = q
    qid = f"{cc}-{num.strip('.-')}"
    lis = ''.join(f'<label><input type="radio" name="au-{ctx}-{qid}" value="{"ABCD"[i]}"> <b>{"ABCD"[i]}.</b> {o}</label>' for i, o in enumerate(opts))
    link = f'<a class="au-chap" href="#{ch}">→ revoir le chapitre {html.escape(CHAP[ch])}</a>' if ctx == 'all' else ''
    return (f'<div class="au-q" data-ans="{ans}" data-id="{qid}">'
            f'<div class="au-left"><div class="au-src">{label} · question {num.strip(".-")}</div>'
            f'<p class="au-txt"><b>{num}</b> {txt}</p><div class="au-opts">{lis}</div></div>'
            f'<div class="au-right"><button type="button" class="au-show">Voir la correction</button>'
            f'<div class="au-corr"><div class="au-good">Bonne réponse : {ans}</div><p>{why}</p>{link}</div></div></div>')

BANNER_TXT = 'ANNALES UNIVERSITÉ DE STRASBOURG'

def chapter_block(ch):
    qs = [(cc, lab, q) for cc, lab, L in SUJETS for q in L if q[5] == ch]
    if not qs:
        return ''
    n = len(qs)
    src = sorted({lab for _, lab, _ in qs})
    body = ''.join(item(cc, lab, q, ch) for cc, lab, q in qs)
    return (f'<details class="au-block">'
            f'<summary><span class="au-blink">🔴 {BANNER_TXT}</span>'
            f'<span class="au-sub">{n} question{"s" if n > 1 else ""} de vrai contrôle continu sur ce chapitre ({" et ".join(src)}) — clique pour ouvrir, essaie, puis regarde la correction</span></summary>'
            f'<div class="au-body">{body}'
            f'<p class="src">Énoncés recopiés tels quels (fautes et coquilles du sujet comprises). Sujet complet : <a href="#annales-unistra">page Annales Université de Strasbourg</a>.</p></div></details>')

def full_page():
    out = ['<section class="page" id="annales-unistra">',
           '<div class="kicker" style="color:#c62828">Réviser · Vrais sujets</div>',
           f'<h1><span class="au-blink" style="font-size:inherit">🔴 {BANNER_TXT}</span><br>Contrôles continus CC1 et CC2 (2022) corrigés</h1>',
           '<p class="lead">Les deux vrais contrôles continus de l\'UE « Structure et fonctionnement de la Terre » (F. Masson &amp; A.-D. Schmitt), Licences L1 &amp; L2, Université de Strasbourg. Les énoncés sont <b>recopiés tels quels</b>. Coche ta réponse, puis clique sur « Voir la correction », ou fais tout le sujet et clique sur « Corriger mon CC » pour avoir ta note.</p>',
           FORMAT,
           '<p style="margin:-6px 0 18px">Documents interdits, <b>calculatrice autorisée</b>. Les deux enseignants sont mélangés dans le même sujet (30 questions).</p>',
           '<div class="box keep"><b class="t">🗺️ Où sont tombées les questions</b><ul>'
           '<li><b>CC1 (nov. 2022)</b> : forme, couches et masse de la Terre (Q1-22, F. Masson) ; énergie solaire, albédo, Wien, fusion, température d\'équilibre (Q23-30, A.-D. Schmitt).</li>'
           '<li><b>CC2 (déc. 2022)</b> : sismique réfraction / réflexion et phases (Q1-14, F. Masson) ; latitude, saisons, ozone, Milankovic, Kepler, Coriolis (Q15-30, A.-D. Schmitt).</li>'
           '<li>Chaque question est aussi rangée dans son chapitre, dans l\'encadré rouge en haut de la page du chapitre.</li></ul></div>']
    for cc, lab, L in SUJETS:
        out.append(f'<h2 style="color:#c62828">{lab} — UE Structure et fonctionnement de la Terre</h2>')
        out.append(f'<div class="au-sujet" data-cc="{cc}" data-label="Annale Unistra {lab}">')
        out.append(''.join(item(cc, lab, q, 'all') for q in L))
        out.append(f'<div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:14px 0"><button type="button" class="btn au-grade" style="background:#c62828;border-color:#c62828">Corriger mon {lab.split(" ")[0]} (note /20)</button><button type="button" class="btn alt au-reset">Recommencer</button><span class="au-score"></span></div></div>')
    out.append('<p class="src">Corrections rédigées pour ce site de révision (non officielles) : en cas de doute, le cours des enseignants fait foi.</p></section>')
    return '\n'.join(out)

CSS = r"""
/* ===== Annales Université de Strasbourg ===== */
@keyframes auBlink{0%,100%{opacity:1}50%{opacity:.25}}
.au-blink{color:#d50000;font-weight:900;letter-spacing:.04em;animation:auBlink 1s steps(2,start) infinite}
@media (prefers-reduced-motion:reduce){.au-blink{animation:none}}
.au-top{display:block;background:#d50000;color:#fff!important;text-decoration:none;text-align:center;font-weight:900;font-size:clamp(1.05rem,2.4vw,1.45rem);letter-spacing:.05em;padding:14px 16px;border-radius:14px;margin:0 0 22px;box-shadow:0 4px 18px rgba(213,0,0,.35);animation:auBlink 1s steps(2,start) infinite}
.au-top small{display:block;font-size:.8rem;font-weight:600;letter-spacing:0;opacity:.95}
@media (prefers-reduced-motion:reduce){.au-top{animation:none}}
nav.side a.au-nav{background:#d50000;color:#fff;font-weight:850;margin:6px 0 10px;animation:auBlink 1s steps(2,start) infinite}
.au-block{border:3px solid #d50000;border-radius:14px;margin:10px 0 22px;background:#fff5f5}
.au-block>summary{cursor:pointer;padding:14px 18px;list-style:none}
.au-block>summary::-webkit-details-marker{display:none}
.au-block>summary .au-blink{display:block;font-size:clamp(1.15rem,2.6vw,1.6rem)}
.au-block .au-sub{display:block;color:#7a1f1f;font-weight:600;font-size:.92rem;margin-top:4px}
.au-body{padding:0 14px 10px}
.au-q{display:grid;grid-template-columns:1.35fr 1fr;gap:14px;background:#fff;border:1px solid #f0c4c4;border-left:5px solid #d50000;border-radius:12px;padding:12px 14px;margin:12px 0}
.au-src{font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#c62828}
.au-txt{margin:6px 0 8px;color:var(--deep)}
.au-opts label{display:block;padding:6px 10px;border:1px solid var(--line);border-radius:9px;margin:4px 0;cursor:pointer;font-size:.95rem}
.au-opts label:hover{background:var(--shade)}
.au-opts input{margin-right:4px}
.au-q.graded label.ok{background:var(--leaf-soft);border-color:#9fcfb6}
.au-q.graded label.ko{background:var(--warn-soft);border-color:#e3b2a6}
.au-right{border-left:1px dashed #f0c4c4;padding-left:14px}
.au-show{border:1px solid #c62828;background:#fff;color:#c62828;border-radius:9px;padding:7px 12px;font-weight:750;cursor:pointer}
.au-corr{display:none;font-size:.93rem}
.au-q.open .au-corr{display:block}
.au-q.open .au-show{display:none}
.au-good{font-weight:850;color:var(--good);font-size:1.05rem}
.au-chap{display:inline-block;margin-top:4px;font-size:.85rem;font-weight:650}
.au-format{background:#fff;border:4px solid #d50000;border-radius:16px;padding:18px 20px;margin:20px 0;box-shadow:0 4px 18px rgba(213,0,0,.18)}
.au-format-t{color:#d50000;font-weight:900;font-size:clamp(1.1rem,2.6vw,1.5rem);letter-spacing:.02em;line-height:1.25}
.au-format-g{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0}
.au-format-g div{background:#d50000;color:#fff;border-radius:12px;text-align:center;padding:10px 6px;font-weight:750;line-height:1.25}
.au-format-g b{display:block;font-size:clamp(2rem,6vw,3rem);line-height:1}
.au-format p{font-size:1.05rem;margin:6px 0 0}
.au-score{font-weight:850;font-size:1.1rem;color:var(--deep)}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.9em;margin:0 2px}
.fr>span:first-child{border-bottom:1px solid currentColor;padding:0 3px}
@media (max-width:900px){main{min-width:0}main table{display:block;overflow-x:auto;max-width:100%}main svg,main img{max-width:100%;height:auto}}
@media (max-width:760px){.au-q{grid-template-columns:1fr}.au-right{border-left:0;border-top:1px dashed #f0c4c4;padding:10px 0 0}}
"""

JS = r"""
// ===== Annales Université de Strasbourg : correction à côté + note =====
window.addEventListener('load',()=>setTimeout(()=>window.scrollTo(0,0),0));
document.addEventListener('click',e=>{const b=e.target.closest('.au-show');if(!b)return;const q=b.closest('.au-q');q.classList.add('open');
 const r=q.querySelector('input:checked');q.classList.add('graded');q.querySelectorAll('label').forEach(l=>{const v=l.querySelector('input').value;l.classList.toggle('ok',v===q.dataset.ans);l.classList.toggle('ko',!!r&&r.value===v&&v!==q.dataset.ans)})});
document.querySelectorAll('.au-sujet').forEach(s=>{const t0=Date.now();
 s.querySelector('.au-grade').onclick=()=>{const qs=[...s.querySelectorAll('.au-q')];let good=0,faux=[];
  qs.forEach(q=>{const r=q.querySelector('input:checked');q.classList.add('open','graded');
   q.querySelectorAll('label').forEach(l=>{const v=l.querySelector('input').value;l.classList.toggle('ok',v===q.dataset.ans);l.classList.toggle('ko',!!r&&r.value===v&&v!==q.dataset.ans)});
   if(r&&r.value===q.dataset.ans)good++;else faux.push(q.dataset.id)});
  const n=qs.length,note=Math.round(200*good/n)/10;s.querySelector('.au-score').textContent=good+' / '+n+' bonnes réponses → '+String(note).replace('.',',')+' / 20';
  if(window.ysraTrack)window.ysraTrack('note',{serie:s.dataset.label+' ('+note+'/20)',score:good,total:n,pourcentage:Math.round(100*good/n),a_revoir:faux.join(' ')||'rien',duree_min:Math.round((Date.now()-t0)/60000)})};
 s.querySelector('.au-reset').onclick=()=>{s.querySelectorAll('.au-q').forEach(q=>{q.classList.remove('open','graded');q.querySelectorAll('input').forEach(i=>i.checked=false);q.querySelectorAll('label').forEach(l=>l.classList.remove('ok','ko'))});s.querySelector('.au-score').textContent=''}});
"""

FORMAT = ('<div class="au-format"><div class="au-format-t">⚠️ ATTENTION : LE VRAI CC N\'EST PAS COMME LES QCM DE PRÉPARATION</div>'
 '<div class="au-format-g"><div><b>4</b>choix<br>(A, B, C, D)</div><div><b>1</b>seule bonne<br>réponse</div><div><b>0</b>point<br>négatif</div></div>'
 '<p>Dans les vrais CC de 2022, chaque question a <b>4 propositions</b> et <b>une seule bonne réponse</b>, et une erreur ne fait <b>pas perdre de points</b> : <b>réponds à toutes les questions, ne laisse jamais de case vide</b>. Les QCM de préparation de ce site (format A-E, plusieurs bonnes réponses possibles) sont <b>plus durs</b> que le vrai CC : c\'est voulu, ils servent à s\'entraîner.</p></div>')

TOP = ('<a class="au-top" href="#annales-unistra">🔴 ANNALES UNIVERSITÉ DE STRASBOURG 🔴'
       '<small>Les vrais contrôles continus CC1 (nov. 2022) et CC2 (déc. 2022), corrigés et expliqués — clique ici<br>Vrai CC : 4 choix · 1 seule bonne réponse · pas de point négatif</small></a>')
NAV = '<a href="#annales-unistra" class="au-nav">🔴 ANNALES UNISTRA · CC1 &amp; CC2</a>'

def put(path, start, end, content, anchor_re, where='after'):
    p = os.path.join(SRC, path)
    s = open(p, encoding='utf-8').read()
    block = f'{start}{content}{end}'
    if start in s:
        s = re.sub(re.escape(start) + '.*?' + re.escape(end), lambda m: block, s, flags=re.S)
    else:
        m = re.search(anchor_re, s)
        assert m, (path, anchor_re)
        i = m.end() if where == 'after' else m.start()
        s = s[:i] + block + s[i:]
    open(p, 'w', encoding='utf-8').write(s)

FILES = {}
for f in os.listdir(SRC):
    if f.endswith('.html'):
        for m in re.finditer(r'<section class="page" id="([a-z0-9-]+)">', open(os.path.join(SRC, f), encoding='utf-8').read()):
            FILES[m.group(1)] = f

if __name__ == '__main__':
    put('00_head.html', '/*AU-CSS*/', '/*/AU-CSS*/', CSS, r'</style>', 'before')
    put('00_head.html', '<!--AU-NAV-->', '<!--/AU-NAV-->', NAV, r'<div class="sub">.*?</div>\n')
    put('00_head.html', '<!--AU-TOP-->', '<!--/AU-TOP-->', TOP, r'<main>\n')
    for ch in CHAP:
        put(FILES[ch], f'<!--AU-{ch}-->', f'<!--/AU-{ch}-->', chapter_block(ch),
            r'<section class="page" id="' + ch + r'">\n(<div class="kicker[^\n]*\n)?<h1>[^\n]*\n')
    put('07_revision.html', '<!--AU-PAGE-->', '<!--/AU-PAGE-->', full_page() + '\n', r'<!-- =+ ANNALES|<section class="page" id="annales">', 'before')
    put('07_revision.html', '<!--AU-FMT-REEL-->', '<!--/AU-FMT-REEL-->', FORMAT, r'<section class="page" id="qcmreel">\n<div class="kicker[^\n]*\n<h1>[^\n]*\n')
    put('01_intro_A.html', '<!--AU-FMT-ORG-->', '<!--/AU-FMT-ORG-->', FORMAT, r'<section class="page" id="organisation">\n<div class="kicker[^\n]*\n<h1>[^\n]*\n')
    put('08_foot.html', '/*AU-JS*/', '/*/AU-JS*/', JS, r'// routage', 'before')
    print('ok', {cc: len(L) for cc, _, L in SUJETS})
