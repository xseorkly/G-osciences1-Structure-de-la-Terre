// Données par chapitre : coeur (à savoir par cœur), qcm [question, options, index bonne réponse, explication], exos [énoncé, corrigé]
const CH = {};
CH.organisation = {
 coeur:["CC1 : vendredi 13/11 à 18 h (QCM sur les 3 premiers cours de chaque enseignant)","CC2 : 14/01 à 14 h ; substitution : 22/01 à 18 h","Feuille QCM type 6 : stylo noir ou bleu, pas de feutre, pas de crayon à papier","Numéro d'étudiant : une seule case noircie par colonne","Pour changer une réponse : utiliser la 2ᵉ ligne ; 2ᵉ correction au correcteur en ruban","Case « Annul. » utile seulement s'il y a des points négatifs","Téléphone / montre connectée sur soi = fraude"],
 qcm:[
 ["Avec quoi faut-il remplir la feuille QCM ?",["Crayon à papier","Feutre noir","Stylo à encre noire ou bleue","Stylo rouge"],2,"Seules les encres noire et bleue sont garanties ; feutre et crayon à papier sont à éviter absolument."],
 ["Tu veux changer ta réponse à la question 12. Que fais-tu ?",["Tu gommes","Tu remplis la 2ᵉ ligne de la question","Tu coches « Annul. »","Tu écris la bonne réponse dans la marge"],1,"La 2ᵉ ligne remplace la 1ʳᵉ. Ne jamais écrire dans la marge."],
 ["Quand la case « Annul. » est-elle utile ?",["Toujours","Jamais","Quand les mauvaises réponses enlèvent des points","Quand on hésite entre deux réponses"],2,"Sans points négatifs, une réponse fausse vaut une abstention."],
 ["Ton téléphone éteint est dans ta poche pendant le CC. C'est…",["autorisé s'il est éteint","une fraude","autorisé en mode avion","toléré"],1,"Il doit être dans le sac posé devant : l'avoir sur soi est une fraude."]],
 exos:[]
};
CH.a1 = {
 coeur:["Flux interne ≈ 0,06 W/m² ; flux solaire moyen = 342 W/m² (~5 500 fois plus)","Masses : géosphère 5,98×10²⁴ kg ≫ hydrosphère 1,36×10²¹ ≫ atmosphère 5,25×10¹⁸ ≫ biosphère","Soleil : fusion H → He au centre (~15 millions °C) ; E = Δm·c²","Corps noir : absorbe tout ; spectre ne dépend que de T (loi de Planck)","Wien : λmax = 2,898×10⁻³ / T (m, K) → Soleil 500 nm (visible), corps humain 9,3 µm (IR)","Stefan-Boltzmann : E = σT⁴, σ = 5,67×10⁻⁸ W·m⁻²·K⁻⁴","T Soleil = 5 778 K ; R Soleil = 6,96×10⁵ km ; distance Terre-Soleil = 149,6×10⁶ km ; R Terre = 6 371 km","Puissance du Soleil ≈ 3,85×10²⁶ W","Constante solaire ≈ 1 368 W/m² (à 1 ua, perpendiculaire, sans atmosphère)","Moyenne sur la Terre : S/4 = 342 W/m² (disque πR² / sphère 4πR²)"],
 qcm:[
 ["Le flux d'énergie interne de la Terre vaut environ…",["342 W/m²","0,06 W/m²","1 368 W/m²","6 W/m²"],1,"≈ 0,06-0,08 W/m², négligeable devant le Soleil."],
 ["Laquelle de ces enveloppes est la plus massive ?",["Atmosphère","Hydrosphère","Biosphère","Géosphère"],3,"5,98×10²⁴ kg contre 1,36×10²¹ kg pour l'hydrosphère."],
 ["Dans le Soleil, l'énergie vient…",["de la combustion de l'hydrogène","de la fusion de l'hydrogène en hélium","de la fission de l'uranium","de réactions chimiques"],1,"Réactions thermonucléaires au centre (~15×10⁶ °C)."],
 ["Un corps noir est un corps qui…",["est de couleur noire","absorbe tout le rayonnement reçu","n'émet aucun rayonnement","réfléchit toute la lumière"],1,"Il absorbe tout et réémet un spectre qui ne dépend que de sa température."],
 ["Si la température d'un corps double, son émission (σT⁴) est multipliée par…",["2","4","8","16"],3,"2⁴ = 16."],
 ["Si la température d'un corps double, sa longueur d'onde λmax…",["double","est divisée par 2","ne change pas","est multipliée par 16"],1,"Loi de Wien : λmax inversement proportionnelle à T."],
 ["La constante solaire vaut environ…",["342 W/m²","240 W/m²","1 368 W/m²","6,3×10⁷ W/m²"],2,"Énergie reçue par m² à 1 ua, perpendiculairement, sans atmosphère."],
 ["L'unité de la constante σ de Stefan-Boltzmann est…",["m·K","W·m⁻²·K⁻⁴","J·kg⁻¹","W/m²"],1,"σ = 5,67×10⁻⁸ W·m⁻²·K⁻⁴ (ne pas confondre avec la constante de Wien en m·K)."],
 ["Le Soleil émet surtout dans…",["les UV","le visible","l'infrarouge","les ondes radio"],1,"λmax ≈ 500 nm."]],
 exos:[
 ["Une étoile a une température de surface de 3 000 K. Calcule sa longueur d'onde d'émission maximale. Dans quel domaine est-elle ?","λmax = 2,898×10⁻³ / 3 000 = 9,7×10⁻⁷ m ≈ 970 nm : <b>proche infrarouge</b> (l'étoile paraît rouge)."],
 ["Calcule le flux émis par m² par un corps noir à 300 K, puis à 600 K. Compare.","E(300) = 5,67×10⁻⁸ × 300⁴ ≈ <b>459 W/m²</b> ; E(600) = 5,67×10⁻⁸ × 600⁴ ≈ <b>7 348 W/m²</b>, soit 16 fois plus (2⁴)."],
 ["Mars est à 1,52 ua du Soleil. Calcule la constante solaire sur Mars (S Terre = 1 368 W/m²).","Le flux diminue comme 1/d² : S = 1 368 / 1,52² ≈ <b>592 W/m²</b>."],
 ["Retrouve le flux moyen de 342 W/m² à partir de la constante solaire. Explique le facteur.","La Terre intercepte S × πR² (un disque) mais répartit cette énergie sur sa sphère 4πR² : 1 368 / 4 = <b>342 W/m²</b>."],
 ["Calcule l'énergie libérée par la fusion de 4 noyaux d'hydrogène (1,0079 uma) en un noyau d'hélium (4,0026 uma). 1 uma = 1,66×10⁻²⁷ kg.","Δm = 4×1,0079 − 4,0026 = 0,029 uma = 4,8×10⁻²⁹ kg ; E = Δm c² = 4,8×10⁻²⁹ × 9×10¹⁶ ≈ <b>4,3×10⁻¹² J</b>."]]
};
CH.a2 = {
 coeur:["Albédo = énergie réfléchie / énergie reçue (sans unité) ; moyenne Terre = 0,3","Énergie absorbée = 0,7 × 342 ≈ 240 W/m²","Sans effet de serre : T = (240/σ)^¼ ≈ 255 K = −18 °C ; réel : +15 °C (écart 33 °C)","Rétroaction glace-albédo : fonte → albédo ↓ → absorption ↑ → réchauffement (positive)","Vénus 470 °C (effet de serre géant) ; Lune −18 °C (pas d'atmosphère)","Air sec : N₂ 78 %, O₂ 21 %, Ar 0,93 %, CO₂ ~0,04 %, H₂O 0-4 %","Troposphère : 80 % de la masse, toute la vapeur, T diminue ; stratosphère : T augmente (ozone)","3 modes de transfert : conduction, convection, rayonnement","GES = molécules à ≥ 3 atomes ou non symétriques (H₂O, CO₂, CH₄, N₂O, O₃, CFC) ; N₂, O₂ ne le sont pas","Domaine IR terrestre : 4-40 µm","Effet de serre naturel : H₂O 55 %, CO₂ 39 %, O₃/N₂O/CH₄ 2 % chacun","Saussure 1780 (caisses de verre) ; Arrhenius 1896 (×2 CO₂ → +5-6 °C)","Modèle à une vitre : sol reçoit 2F → T sol = 2^¼ × 255 ≈ 303 K","Énergie solaire : 30 % réfléchie, 20 % absorbée par l'atmosphère, 50 % par la surface"],
 qcm:[
 ["L'albédo moyen de la Terre est…",["0,03","0,3","0,5","0,7"],1,"30 % réfléchi."],
 ["Quelle surface a l'albédo le plus fort ?",["Océan","Forêt","Neige fraîche","Désert"],2,"0,8-0,9."],
 ["La température d'équilibre sans effet de serre est…",["−18 °C","0 °C","+15 °C","−273 °C"],0,"σT⁴ = 240 → T ≈ 255 K."],
 ["La rétroaction glace-albédo est…",["négative : elle stabilise","positive : elle amplifie le réchauffement","sans effet","propre à Vénus"],1,"Moins de glace → surface plus sombre → plus d'absorption → plus chaud."],
 ["Pourquoi Vénus est-elle à 470 °C ?",["Elle est très proche du Soleil","Son atmosphère de CO₂ crée un énorme effet de serre","Son noyau est très chaud","Elle n'a pas d'atmosphère"],1,"La théorie (sans atmosphère) prévoit bien moins : l'écart vient de l'effet de serre."],
 ["Dans quelle couche la température augmente-t-elle avec l'altitude grâce à l'ozone ?",["Troposphère","Stratosphère","Mésosphère","Asthénosphère"],1,"L'ozone absorbe les UV."],
 ["Quel gaz contribue le plus à l'effet de serre NATUREL ?",["CO₂","CH₄","H₂O","O₃"],2,"Vapeur d'eau ≈ 55 %, CO₂ ≈ 39 %."],
 ["Pourquoi O₂ et N₂ ne sont pas des GES ?",["Ils sont trop rares","Molécules diatomiques symétriques qui n'absorbent pas l'IR","Ils sont trop lourds","Ils restent au sol"],1,"Elles ne vibrent pas de façon à absorber l'IR."],
 ["Qui a calculé en 1896 qu'un doublement du CO₂ réchaufferait la Terre de 5-6 °C ?",["Fourier","Saussure","Arrhenius","Milankovic"],2,"Svante Arrhenius."],
 ["Dans le modèle à une vitre, le sol reçoit…",["F","2F","F/2","4F"],1,"F du Soleil + F réémis par la vitre."],
 ["L'analogie avec la serre du jardinier est limitée car…",["l'atmosphère est trop épaisse","la vraie serre bloque surtout la convection","la serre n'a pas de vitre","l'atmosphère réfléchit le visible"],1,"Effet mécanique (confinement) dans la serre ; effet radiatif dans l'atmosphère."]],
 exos:[
 ["Calcule la température d'équilibre d'une planète recevant en moyenne 342 W/m² avec un albédo de 0,6 (planète très nuageuse).","Absorbé : 0,4 × 342 = 137 W/m² ; T = (137 / 5,67×10⁻⁸)^¼ ≈ <b>222 K ≈ −51 °C</b>. Plus l'albédo est fort, plus la planète est froide."],
 ["Avec le modèle à une vitre, quelle serait la température du sol si F = 240 W/m² et s'il y avait DEUX vitres superposées ?","Avec n vitres parfaites, le sol émet (n+1)F. Pour n = 2 : σT⁴ = 720 W/m² → T ≈ <b>335 K</b>. Plus d'atmosphère absorbante = sol plus chaud."],
 ["La Lune et la Terre sont à la même distance du Soleil. Explique en 2 phrases pourquoi leurs températures diffèrent de ~33 °C.","La Lune n'a pas d'atmosphère : sa température est proche de la température d'équilibre (−18 °C). La Terre a des GES qui absorbent l'IR et le renvoient vers le sol : <b>effet de serre</b> → +15 °C."],
 ["Complète : le Soleil émet surtout dans le … (λ ≈ …) et la Terre dans l'… (λ ≈ …). L'atmosphère est … au premier et … au second.","Visible (≈ 0,5 µm) ; infrarouge (≈ 10 µm) ; <b>transparente</b> au premier, <b>en grande partie opaque</b> au second."]]
};
CH.a3 = {
 coeur:["Forçage radiatif (W/m²) = énergie reçue − énergie émise ; positif → réchauffement","Forçage 1750-2019 : +2,7 W/m² (+3,8 GES ; −1,1 aérosols) — GIEC 2021","CO₂ 2025 : 427,49 ppm ; jamais > 300 ppm en 450 000 ans ; 300 dépassé vers 1910 ; inédit depuis ~14 Ma","2025 : ≈ +1,5 °C par rapport au préindustriel","Soleil : variations négligeables ; volcans : refroidissement de 1-3 ans (aérosols soufrés)","Éruptions : Pelée 1902, Katmai 1912, Agung 1963, El Chichón 1982, Pinatubo 1991","Part du réchauffement 1750-2011 : CO₂ 56 %, CH₄ 32 %, N₂O 6 %, gaz fluorés + O₃ 6 %","PRG (100 ans) : CO₂ 1, CH₄ 25, N₂O 298, CFC-12 10 900, SF₆ 22 800","Durées de vie : CH₄ 12 ans, N₂O 120 ans, CO₂ 50-200 ans, SF₆ 3 200 ans","Changement climatique irréversible à court terme","Ozone stratosphérique (20-30 km) : O₂ + UV → 2 O ; O + O₂ → O₃ ; arrête UV-C et UV-B","Ozone troposphérique = polluant (NO₂ du trafic + soleil)","Trou d'ozone : > 50 % détruit ; Antarctique, à partir de septembre ; −80 °C, vortex, nuages stratosphériques polaires","CFC : durée de vie 60-200 ans, chlore libéré par photolyse dans la stratosphère","Montréal : 16/09/1987 ; Kigali (HFC) : 15/10/2016","Hunga Tonga 15/01/2022 : vapeur d'eau dans la stratosphère ; trou 2023 = 26 Mkm²","Pergélisol : gelé ≥ 2 ans ; continu 100 %, discontinu 50-90 %, sporadique 10-50 % ; 1/4 des terres de l'hémisphère Nord","Dégel → CO₂ + CH₄ → rétroaction positive ; thermokarst"],
 qcm:[
 ["Un forçage radiatif négatif tend à…",["réchauffer","refroidir","détruire l'ozone","augmenter l'albédo des océans"],1,"Plus d'énergie émise que reçue."],
 ["Le forçage anthropique 1750-2019 vaut environ…",["0,27 W/m²","2,7 W/m²","27 W/m²","342 W/m²"],1,"+3,8 (GES) − 1,1 (aérosols)."],
 ["Concentration de CO₂ en 2025 ?",["280 ppm","350 ppm","427 ppm","1 000 ppm"],2,"427,49 ppm."],
 ["Sur les 450 000 dernières années (avant l'industrie), le CO₂ est resté…",["sous 300 ppm","au-dessus de 400 ppm","constant à 280 ppm","au-dessus de 1 000 ppm"],0,"Entre ~180 et ~300 ppm."],
 ["Effet d'une grande éruption volcanique sur le climat global ?",["Réchauffement durable","Refroidissement de quelques années","Aucun","Trou d'ozone permanent"],1,"Les aérosols soufrés réfléchissent la lumière ~1-3 ans."],
 ["Quel gaz a le plus contribué au réchauffement 1750-2011 ?",["CH₄","N₂O","CO₂","CFC"],2,"CO₂ ≈ 56 %."],
 ["Le PRG du méthane (sur 100 ans) vaut environ…",["1","25","298","22 800"],1,"Tableau GIEC du cours : 25."],
 ["Où se trouve la couche d'ozone protectrice ?",["Troposphère","Stratosphère (20-30 km)","Mésosphère","Thermosphère"],1,"Elle absorbe les UV."],
 ["Le trou d'ozone antarctique se creuse surtout…",["en juin","en septembre-octobre","en janvier","toute l'année"],1,"Au retour du Soleil après l'hiver polaire."],
 ["Les CFC détruisent l'ozone car…",["ils absorbent les UV","leur photolyse libère du chlore dans la stratosphère","ils sont des GES","ils refroidissent la stratosphère"],1,"Un atome de chlore détruit des milliers d'O₃."],
 ["Le protocole de Montréal a été signé en…",["1979","1987","1997","2016"],1,"16 septembre 1987."],
 ["Le pergélisol est un sol gelé depuis au moins…",["1 hiver","2 années consécutives","10 ans","1 000 ans"],1,"Définition du cours."],
 ["Un pergélisol discontinu est gelé sur…",["100 %","50-90 %","10-50 %","moins de 10 %"],1,"Continu 100 %, discontinu 50-90 %, sporadique 10-50 %."],
 ["Pourquoi la fonte du pergélisol est-elle une rétroaction positive ?",["Elle augmente l'albédo","Elle libère CO₂ et CH₄ qui renforcent l'effet de serre","Elle refroidit l'Arctique","Elle absorbe du CO₂"],1,"Plus de GES → plus de réchauffement → plus de dégel."]],
 exos:[
 ["Un gaz X a un PRG de 300. Combien de tonnes de CO₂ faut-il émettre pour avoir le même effet que 2 tonnes de X sur 100 ans ?","2 × 300 = <b>600 tonnes</b> d'équivalent CO₂."],
 ["Explique, étape par étape, la formation du trou d'ozone antarctique (4 étapes).","1) Nuit polaire : −80 °C. 2) Vortex polaire qui isole l'air. 3) Nuages stratosphériques polaires : des molécules s'y fixent, libérant du chlore réactif. 4) Retour du Soleil (septembre) : les UV activent le chlore qui détruit l'O₃ en chaîne."],
 ["Donne deux arguments du cours montrant que le réchauffement actuel n'est pas naturel.","1) L'activité solaire n'a presque pas varié sur 150 ans. 2) Les volcans ne peuvent que refroidir, et brièvement. (3) Seules les simulations incluant les facteurs humains reproduisent la courbe observée."],
 ["Pourquoi le CO₂, avec un PRG de 1, est-il pourtant le premier responsable du réchauffement ?","Parce qu'il est émis en quantités <b>énormes</b> (combustion fossile, déforestation) et qu'il reste très longtemps dans l'atmosphère (50-200 ans et plus)."],
 ["Ozone « bon » et « mauvais » : localise chacun et donne son origine.","Bon : <b>stratosphère</b> (20-30 km), formé par les UV (O₂ → 2 O ; O + O₂ → O₃), protège des UV. Mauvais : <b>troposphère</b>, formé à partir du NO₂ des pots d'échappement sous fort ensoleillement ; polluant et GES."]]
};
CH.a4 = {
 coeur:["Kepler : 1) orbite elliptique, Soleil à un foyer ; 2) aires égales en temps égaux ; 3) T² ∝ a³","Excentricité : 0 à 0,06 ; aujourd'hui 0,017 ; cycles ~100 000 et 400 000 ans","Aphélie = a(1+e) = 152,1×10⁶ km (juillet) ; périhélie = a(1−e) = 147,1×10⁶ km (janvier)","Obliquité : 22° à 24,5° ; aujourd'hui 23,5° ; cycle 41 000 ans ; stabilisée par la Lune ; cause des saisons","Précession : ~19 000-23 000 ans ; change la date du périhélie, pas la quantité totale d'énergie","Analyse spectrale (Fourier) : décompose une courbe en cycles ; période = 1/fréquence","Pics dans les archives : 100, 41, 23, 19 ka ; exemple du cours : pic à 41,0 ka (obliquité)"],
 qcm:[
 ["La 2ᵉ loi de Kepler dit que…",["l'orbite est un cercle","la planète balaie des aires égales en des temps égaux","T² ∝ a³","la Terre est au centre"],1,"Loi des aires : la planète va plus vite près du Soleil."],
 ["L'excentricité actuelle de l'orbite terrestre vaut…",["0","0,017","0,06","0,5"],1,"Elle varie entre ~0 et 0,06."],
 ["Une excentricité e = 0 correspond à…",["une parabole","une ellipse très allongée","un cercle","une hyperbole"],2,"e = 0 cercle ; 0<e<1 ellipse ; e = 1 parabole ; e > 1 hyperbole."],
 ["La période de l'obliquité est d'environ…",["11 ans","23 000 ans","41 000 ans","100 000 ans"],2,"41 000 ans."],
 ["Quel astre stabilise l'obliquité de la Terre ?",["Le Soleil","Jupiter","La Lune","Mars"],2,"Sans la Lune, l'obliquité varierait beaucoup plus."],
 ["Quand l'obliquité augmente, les saisons sont…",["moins marquées","plus marquées","inversées","inchangées"],1,"Étés plus chauds, hivers plus froids."],
 ["La précession des équinoxes modifie…",["la quantité totale d'énergie reçue","la date du périhélie et la répartition de l'énergie","la distance moyenne Terre-Soleil","l'excentricité"],1,"Elle ne change pas l'énergie totale, seulement sa distribution."],
 ["Un pic spectral à la fréquence 0,024 cycle/ka correspond à une période de…",["24 ans","24 ka","41 ka","100 ka"],2,"Période = 1/0,024 ≈ 41 ka : obliquité."],
 ["La Terre est au périhélie…",["début janvier","début juillet","au printemps","en septembre"],0,"Au plus près du Soleil en janvier, en plein hiver boréal."]],
 exos:[
 ["Calcule les distances au périhélie et à l'aphélie si l'excentricité valait 0,06 (a = 149,6×10⁶ km). Compare avec aujourd'hui.","Périhélie : 149,6 × 0,94 = <b>140,6×10⁶ km</b> ; aphélie : 149,6 × 1,06 = <b>158,6×10⁶ km</b>. Écart 18×10⁶ km contre 5×10⁶ aujourd'hui : saisons beaucoup plus contrastées."],
 ["Le flux solaire varie comme 1/d². De combien le flux au périhélie dépasse-t-il celui de l'aphélie aujourd'hui ?","(152,1/147,1)² = 1,069 : environ <b>7 % de plus</b> au périhélie."],
 ["Un spectre montre des pics à 0,01 ; 0,0244 ; 0,043 et 0,053 cycle/ka. Donne les périodes et associe chaque pic à un paramètre.","0,01 → <b>100 ka</b> (excentricité) ; 0,0244 → <b>41 ka</b> (obliquité) ; 0,043 → <b>23 ka</b> et 0,053 → <b>19 ka</b> (précession)."],
 ["Range les trois paramètres de Milankovic de la période la plus courte à la plus longue.","Précession (19-23 ka) &lt; obliquité (41 ka) &lt; excentricité (100 ka, 400 ka)."]]
};
CH.a5 = {
 coeur:["Latitude 0° (équateur) à 90° (pôles) ; tropiques 23,4° (23°27') ; cercles polaires 66,6° (66°33')","Surface éclairée par 1 m² de faisceau = 1/sin(i) : équateur 1 m², Bordeaux 1,4 m², Oslo 2 m², pôle 57 m²","Déclinaison δ : angle direction Terre-Soleil / plan de l'équateur ; entre −23,45° et +23,45°","Cooper : δ = 23,45 sin[360(284+J)/365]","Solstice : δ maximale ; Soleil au zénith d'un tropique (21 juin Cancer, 21 décembre Capricorne)","Équinoxe : δ = 0 ; jour = nuit = 12 h partout ; Soleil au zénith de l'équateur (~20 mars, ~22 sept.)","Hauteur à midi : i = 90° − |δ − L| (même hémisphère) ; i = 90° − |δ + L| (hémisphères différents)","Équateur : toujours 12 h de jour ; Soleil au zénith 2 fois par an","Été plus chaud : Soleil plus haut + jours plus longs","La distance Terre-Soleil ne fait PAS les saisons","Rotation → jour/nuit ; inclinaison + révolution → saisons ; inclinaison + sphéricité → zones climatiques","L'hémisphère austral reçoit un peu plus en été (périhélie en janvier)"],
 qcm:[
 ["À quelle latitude se trouve le tropique du Capricorne ?",["0°","23°27' N","23°27' S","66°33' S"],2,"Hémisphère Sud."],
 ["Le jour de l'équinoxe, quelle est la durée du jour à 66°33' N ?",["0 h","12 h","24 h","18 h"],1,"Aux équinoxes : 12 h partout."],
 ["Le 21 juin, quelle est la durée du jour au pôle Sud ?",["0 h","12 h","24 h","6 h"],0,"Nuit polaire australe."],
 ["La déclinaison solaire vaut 0 le jour…",["du solstice d'été","du solstice d'hiver","d'un équinoxe","du périhélie"],2,"Soleil au-dessus de l'équateur."],
 ["Le 21 juin à midi, au-dessus de quel parallèle le Soleil est-il au zénith ?",["Équateur","Tropique du Cancer","Tropique du Capricorne","Cercle polaire"],1,"δ = +23°27'."],
 ["Le 22/12 (δ = 23,45° S), hauteur du Soleil à midi à 30° S ?",["53,45°","83,45°","36,55°","6,55°"],1,"Même hémisphère : 90 − (30 − 23,45)."],
 ["Le 22/12, hauteur du Soleil à midi à l'équateur ?",["90°","66°33'","23°27'","0°"],1,"90 − 23,45 = 66,55°."],
 ["À 60° N à l'équinoxe (i = 30°), 1 m² de faisceau s'étale sur…",["0,5 m²","1 m²","2 m²","57 m²"],2,"1/sin 30° = 2."],
 ["Ce qui cause les saisons, c'est…",["la distance au Soleil","l'inclinaison de l'axe de rotation","la rotation de la Terre sur elle-même","l'activité solaire"],1,"Les deux hémisphères ont des saisons opposées à la même distance."],
 ["Ce qui cause les zones climatiques (selon la latitude), c'est…",["la rotation seule","l'inclinaison + la forme sphérique","la précession","l'excentricité"],1,"Tableau de synthèse du cours (diapo 41)."]],
 exos:[
 ["Le 21 juin (δ = 23,45° N), calcule la hauteur du Soleil à midi à Strasbourg (48,6° N), à l'équateur et à 70° S.","Strasbourg, même hémisphère : 90 − (48,6 − 23,45) = <b>64,85°</b>. Équateur : 90 − 23,45 = <b>66,55°</b>. 70° S, hémisphères différents : 90 − (23,45 + 70) = −3,45° → <b>Soleil sous l'horizon</b> (nuit polaire)."],
 ["Avec la formule de Cooper, calcule la déclinaison le 1ᵉʳ mai (J = 121).","δ = 23,45 × sin[360 × (284 + 121)/365] = 23,45 × sin(399,5°) = 23,45 × sin(39,5°) ≈ <b>+14,9°</b> (le Soleil est au-dessus de l'hémisphère Nord)."],
 ["Calcule la surface éclairée par un faisceau d'1 m² quand le Soleil est à 20° au-dessus de l'horizon. Combien d'énergie par m² par rapport au zénith ?","Surface = 1/sin 20° = <b>2,92 m²</b> ; énergie par m² = sin 20° ≈ <b>34 %</b> de celle reçue au zénith."],
 ["Pourquoi fait-il plus chaud le 14 septembre que le 11 mars, alors que le Soleil a presque la même hauteur ?","Grâce à l'<b>inertie thermique</b> : en septembre, océans et sols ont stocké la chaleur de l'été ; en mars, ils sont encore refroidis par l'hiver."]]
};
CH.a6 = {
 coeur:["Intertropical : excès d'énergie ; pôles : déficit","Transport méridien : océan 40 % (basses latitudes), atmosphère 60 % (moyennes/hautes)","3 cellules par hémisphère : Hadley (0-30°), Ferrel (30-60°), polaire (60-90°)","Hadley : air chaud monte à l'équateur (pluies, ZCIT), redescend sec à 30° (déserts)","Vents au sol : alizés NE (H. Nord) et SE (H. Sud), vents d'ouest (30-60°), vents d'est polaires","Coriolis : à droite au Nord, à gauche au Sud, nulle à l'équateur, max aux pôles ; F = 2mΩv sin λ","Foucault 1851 : pendule de 65 m au Panthéon → rotation de la Terre","Ekman : spirale sur ~100 m ; transport net à 90° du vent","Circulation profonde = thermohaline (température + salinité)","Atmosphère : troposphère (≤ 8-16 km, jusqu'à −56 °C), stratosphère (≤ 50 km, ~0 °C), mésosphère (≤ 85 km, −90 °C), thermosphère","Zone polaire : aucun mois > 10 °C ; zone tropicale : aucun mois < 16 °C ; tempérée : alternance"],
 qcm:[
 ["Quelle région reçoit plus d'énergie qu'elle n'en émet ?",["Les pôles","La zone intertropicale","Les moyennes latitudes","Aucune"],1,"Excès d'énergie entre les tropiques."],
 ["Aux moyennes et hautes latitudes, la chaleur est surtout transportée par…",["l'océan","l'atmosphère","la conduction dans le sol","les glaciers"],1,"Atmosphère ≈ 60 %."],
 ["Combien de cellules de convection atmosphérique par hémisphère ?",["1","2","3","6"],2,"Hadley, Ferrel, polaire."],
 ["Vers 30° de latitude, l'air de la cellule de Hadley…",["monte et donne des pluies","redescend sec : déserts","reste immobile","forme la ZCIT"],1,"Hautes pressions subtropicales : Sahara, Sonora."],
 ["La force de Coriolis est nulle…",["aux pôles","à l'équateur","à 45°","partout"],1,"sin(0) = 0."],
 ["Dans l'hémisphère Sud, la force de Coriolis dévie vers…",["la droite","la gauche","le haut","le bas"],1,"Gauche au Sud, droite au Nord."],
 ["Le transport d'Ekman se fait…",["dans le sens du vent","à 90° du vent","contre le vent","vers le fond"],1,"Résultat de la spirale d'Ekman."],
 ["La circulation océanique profonde est due à…",["les vents","les différences de densité (température, salinité)","la Lune","Coriolis seule"],1,"Circulation thermohaline."],
 ["Une zone sans aucun mois au-dessus de 10 °C est une zone…",["tropicale","tempérée","polaire","désertique"],2,"Pas d'été thermique."],
 ["Où se trouve le point le plus froid de l'atmosphère (~−90 °C) ?",["Tropopause","Stratopause","Mésopause (~85 km)","Au sol en Antarctique"],2,"Sommet de la mésosphère."]],
 exos:[
 ["Un avion part de l'équateur vers le nord. Sans correction, de quel côté sera-t-il dévié par Coriolis ? Et un bateau qui part vers le sud depuis le Brésil ?","Avion (hémisphère Nord) : vers la <b>droite</b>, donc vers l'est. Bateau (hémisphère Sud) : vers la <b>gauche</b>, donc aussi vers l'est."],
 ["Décris le trajet de l'air dans une cellule de Hadley en 4 étapes.","1) Équateur : l'air chaud et humide monte (BP, nuages, pluies). 2) En altitude, il part vers les pôles. 3) Vers 30°, il redescend, se réchauffe et s'assèche (HP, déserts). 4) Au sol, il revient vers l'équateur : les alizés."],
 ["Calcule le rapport de la force de Coriolis à 45° et à 90° de latitude (même vitesse).","sin 45° / sin 90° = <b>0,71</b> : à 45°, Coriolis vaut 71 % de sa valeur au pôle."],
 ["Pourquoi le Sahara est-il un désert alors qu'il reçoit beaucoup de Soleil ?","Il est sous la branche <b>descendante</b> de la cellule de Hadley (~30° N) : l'air qui descend se réchauffe et s'assèche, il n'y a pas de nuages ni de pluie."]]
};
