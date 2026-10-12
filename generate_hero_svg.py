import os

def create_hero_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="100%" height="100%" class="laddu-hero-svg">
  <defs>
    <!-- Gradients -->
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFF0D0" />
      <stop offset="45%" stop-color="#FFE7BC" />
      <stop offset="85%" stop-color="#D7EFF8" />
      <stop offset="100%" stop-color="#A8D9E8" />
    </linearGradient>

    <linearGradient id="sunGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF8E7" stop-opacity="0.9" />
      <stop offset="60%" stop-color="#FFD166" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#FF9E00" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="hillsFar" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#93C6A2" />
      <stop offset="100%" stop-color="#5B9A72" />
    </linearGradient>

    <linearGradient id="hillsMid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3D8557" />
      <stop offset="100%" stop-color="#245A39" />
    </linearGradient>

    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#80C8DC" />
      <stop offset="50%" stop-color="#6BB9D0" />
      <stop offset="100%" stop-color="#51A3BD" />
    </linearGradient>

    <linearGradient id="pathGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D89D6C" />
      <stop offset="40%" stop-color="#E4B282" />
      <stop offset="80%" stop-color="#CF8A55" />
      <stop offset="100%" stop-color="#BA713D" />
    </linearGradient>

    <linearGradient id="groundGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#72A849" />
      <stop offset="40%" stop-color="#4E8732" />
      <stop offset="100%" stop-color="#2C5B1C" />
    </linearGradient>

    <radialGradient id="ladduGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFBEB" />
      <stop offset="35%" stop-color="#FFD152" />
      <stop offset="70%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </radialGradient>

    <linearGradient id="roofGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E27344" />
      <stop offset="100%" stop-color="#B3441B" />
    </linearGradient>

    <linearGradient id="woodGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#734222" />
      <stop offset="50%" stop-color="#583723" />
      <stop offset="100%" stop-color="#402312" />
    </linearGradient>

    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#17452D" flood-opacity="0.25" />
    </filter>

    <filter id="ladduMagicGlow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="10" result="blur1" />
      <feGaussianBlur stdDeviation="4" result="blur2" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="blur2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- SKY BACKGROUND -->
  <rect x="0" y="0" width="1000" height="680" fill="url(#skyGrad)" rx="24" />

  <!-- WARM SUN & LIGHT RAYS -->
  <circle cx="820" cy="140" r="130" fill="url(#sunGlow)" />
  <circle cx="820" cy="140" r="70" fill="#FFFBEB" opacity="0.6" />
  <g opacity="0.18">
    <polygon points="820,140 600,0 680,0" fill="#FFC857" />
    <polygon points="820,140 450,0 520,0" fill="#FFC857" />
    <polygon points="820,140 280,0 350,0" fill="#FFC857" />
    <polygon points="820,140 100,20 180,0" fill="#FFC857" />
  </g>

  <!-- DISTANT KERALA HILLS -->
  <path d="M 0 290 Q 180 230, 360 270 T 740 250 Q 880 230, 1000 280 L 1000 370 L 0 370 Z" fill="url(#hillsFar)" opacity="0.65" />
  <!-- Distant coconut silhouettes -->
  <g fill="#437D56" opacity="0.4">
    <path d="M 120 250 Q 125 220 130 190 M 130 190 Q 105 180 85 195 M 130 190 Q 140 170 160 180 M 130 190 Q 125 170 115 160 M 130 190 Q 145 190 155 205" stroke="#437D56" stroke-width="3" stroke-linecap="round" fill="none"/>
    <path d="M 280 260 Q 285 230 290 200 M 290 200 Q 265 190 245 205 M 290 200 Q 300 180 320 190 M 290 200 Q 285 180 275 170" stroke="#437D56" stroke-width="3" stroke-linecap="round" fill="none"/>
    <path d="M 780 245 Q 785 215 790 185 M 790 185 Q 765 175 745 190 M 790 185 Q 800 165 820 175 M 790 185 Q 805 185 815 200" stroke="#437D56" stroke-width="3" stroke-linecap="round" fill="none"/>
  </g>

  <!-- MIDDLE HILLS -->
  <path d="M 0 310 Q 220 270, 480 320 T 1000 300 L 1000 400 L 0 400 Z" fill="url(#hillsMid)" />

  <!-- KERALA BACKWATER RIVER -->
  <path d="M 0 335 Q 260 320, 520 345 T 1000 330 L 1000 420 Q 640 435, 320 415 T 0 420 Z" fill="url(#waterGrad)" />
  <!-- Water ripples -->
  <g stroke="#B3E5F2" stroke-width="2.5" stroke-linecap="round" opacity="0.6">
    <line x1="140" y1="360" x2="220" y2="360" />
    <line x1="380" y1="355" x2="490" y2="355" />
    <line x1="680" y1="365" x2="790" y2="365" />
    <line x1="840" y1="380" x2="930" y2="380" />
    <line x1="260" y1="385" x2="360" y2="385" />
  </g>

  <!-- TRADITIONAL KERALA HOUSE (NALUKETTU / TILE ROOF) IN BACKGROUND -->
  <g transform="translate(620, 240)">
    <!-- House base wall (warm cream with wood) -->
    <rect x="60" y="80" width="160" height="70" fill="#FFF3D9" stroke="#583723" stroke-width="2.5" rx="3" />
    <!-- Pillars -->
    <rect x="75" y="100" width="8" height="50" fill="url(#woodGrad)" />
    <rect x="110" y="100" width="8" height="50" fill="url(#woodGrad)" />
    <rect x="170" y="100" width="8" height="50" fill="url(#woodGrad)" />
    <rect x="200" y="100" width="8" height="50" fill="url(#woodGrad)" />
    <!-- Door -->
    <rect x="130" y="105" width="26" height="45" fill="#583723" rx="2" />
    <circle cx="150" cy="128" r="2.5" fill="#FFC857" />
    <!-- Wooden Charupadi / Veranda railing -->
    <rect x="60" y="130" width="160" height="6" fill="#734222" />
    <!-- Sloped Terracotta Tile Roof (Kerala Padippura / Gabled Roof) -->
    <polygon points="50,85 140,25 230,85" fill="url(#roofGrad)" stroke="#583723" stroke-width="3" />
    <polygon points="40,90 140,25 240,90" fill="none" stroke="#D96B3B" stroke-width="2" />
    <!-- Roof tiles texture ridges -->
    <line x1="140" y1="25" x2="75" y2="85" stroke="#9E3514" stroke-width="2" />
    <line x1="140" y1="25" x2="105" y2="85" stroke="#9E3514" stroke-width="2" />
    <line x1="140" y1="25" x2="140" y2="85" stroke="#9E3514" stroke-width="2" />
    <line x1="140" y1="25" x2="175" y2="85" stroke="#9E3514" stroke-width="2" />
    <line x1="140" y1="25" x2="205" y2="85" stroke="#9E3514" stroke-width="2" />
    <!-- Decorative Wooden Eaves finial -->
    <circle cx="140" cy="22" r="5" fill="#FFC857" stroke="#583723" stroke-width="1.5" />
  </g>

  <!-- LUSH COCONUT TREES (LEFT & RIGHT FRAMING) -->
  <!-- Left Coconut Tree 1 -->
  <g class="tree-sway">
    <!-- Curved Trunk -->
    <path d="M 60 520 C 75 420, 65 300, 115 180 C 122 165, 128 150, 135 140" stroke="#7A4E2B" stroke-width="18" stroke-linecap="round" fill="none" />
    <!-- Trunk rings -->
    <g stroke="#4F2E14" stroke-width="2.5" opacity="0.6">
      <line x1="58" y1="480" x2="74" y2="475" />
      <line x1="62" y1="430" x2="78" y2="425" />
      <line x1="68" y1="370" x2="84" y2="365" />
      <line x1="78" y1="300" x2="94" y2="295" />
      <line x1="95" y1="230" x2="110" y2="225" />
      <line x1="115" y1="170" x2="130" y2="165" />
    </g>
    <!-- Coconuts Cluster -->
    <circle cx="132" cy="142" r="9" fill="#583723" stroke="#2D1709" stroke-width="1.5" />
    <circle cx="142" cy="148" r="8" fill="#6B4423" stroke="#2D1709" stroke-width="1.5" />
    <circle cx="126" cy="149" r="8" fill="#7D512D" stroke="#2D1709" stroke-width="1.5" />
    <!-- Big Fronds (Stylized 2D Cartoon Style) -->
    <!-- Frond 1 (Top Left) -->
    <path d="M 135 140 C 90 90, 30 95, -10 130 C 25 125, 70 120, 135 140 Z" fill="#2E7D4E" stroke="#17452D" stroke-width="2.5" />
    <!-- Frond 2 (Top) -->
    <path d="M 135 140 C 130 60, 170 30, 200 40 C 185 70, 160 105, 135 140 Z" fill="#3D9B63" stroke="#17452D" stroke-width="2.5" />
    <!-- Frond 3 (Right) -->
    <path d="M 135 140 C 190 100, 260 115, 290 160 C 240 145, 185 145, 135 140 Z" fill="#22673F" stroke="#17452D" stroke-width="2.5" />
    <!-- Frond 4 (Lower Left) -->
    <path d="M 135 140 C 80 145, 20 180, 0 230 C 35 195, 90 170, 135 140 Z" fill="#1E5C37" stroke="#17452D" stroke-width="2.5" />
    <!-- Frond 5 (Lower Right) -->
    <path d="M 135 140 C 195 160, 240 210, 255 270 C 220 220, 175 180, 135 140 Z" fill="#358B58" stroke="#17452D" stroke-width="2.5" />
  </g>

  <!-- Right Coconut Tree (Framing the village scene) -->
  <g class="tree-sway-reverse" transform="translate(90, 0)">
    <path d="M 820 480 C 805 380, 810 260, 770 160 C 764 145, 758 132, 750 125" stroke="#7A4E2B" stroke-width="16" stroke-linecap="round" fill="none" />
    <!-- Coconuts -->
    <circle cx="745" cy="128" r="8" fill="#583723" />
    <circle cx="756" cy="132" r="7" fill="#6B4423" />
    <!-- Fronds -->
    <path d="M 750 125 C 790 70, 850 70, 890 100 C 850 100, 800 105, 750 125 Z" fill="#2E7D4E" stroke="#17452D" stroke-width="2" />
    <path d="M 750 125 C 740 50, 700 25, 665 40 C 685 70, 715 100, 750 125 Z" fill="#3D9B63" stroke="#17452D" stroke-width="2" />
    <path d="M 750 125 C 690 90, 625 110, 600 150 C 650 135, 700 130, 750 125 Z" fill="#1E5C37" stroke="#17452D" stroke-width="2" />
    <path d="M 750 125 C 800 140, 860 170, 885 220 C 845 185, 795 160, 750 125 Z" fill="#22673F" stroke="#17452D" stroke-width="2" />
  </g>

  <!-- FOREGROUND LUSH GRASS & VILLAGE GROUND -->
  <path d="M -20 430 Q 280 390, 540 430 T 1020 410 L 1020 700 L -20 700 Z" fill="url(#groundGrad)" />

  <!-- WINDING VILLAGE MUD PATH -->
  <path d="M 120 680 C 220 540, 360 480, 560 460 C 680 445, 800 440, 920 435 L 980 470 C 820 480, 660 510, 480 560 C 340 600, 240 660, 200 680 Z" fill="url(#pathGrad)" opacity="0.9" />

  <!-- Stepping stones on mud path -->
  <ellipse cx="260" cy="610" rx="28" ry="12" fill="#D3A072" stroke="#8C5C33" stroke-width="2" opacity="0.7"/>
  <ellipse cx="380" cy="555" rx="24" ry="10" fill="#D3A072" stroke="#8C5C33" stroke-width="2" opacity="0.7"/>
  <ellipse cx="500" cy="510" rx="20" ry="8" fill="#D3A072" stroke="#8C5C33" stroke-width="2" opacity="0.7"/>

  <!-- Wild Flowers & Grass Tufts -->
  <g fill="#FFC857" stroke="#583723" stroke-width="1.5">
    <circle cx="80" cy="560" r="5" />
    <circle cx="105" cy="580" r="6" />
    <circle cx="920" cy="530" r="6" />
    <circle cx="895" cy="550" r="5" />
    <circle cx="870" cy="620" r="7" fill="#D96B3B" />
    <circle cx="80" cy="630" r="6" fill="#D96B3B" />
  </g>
  <!-- Banana Leaf in Foreground Right -->
  <g transform="translate(850, 480)">
    <path d="M 20 180 C 40 100, 0 20, -70 -20 C -20 30, 0 100, -10 180 Z" fill="#3D9B63" stroke="#17452D" stroke-width="3" />
    <path d="M 0 120 C -30 90, -50 80, -65 75" stroke="#17452D" stroke-width="2" fill="none" />
    <path d="M 5 60 C -25 35, -45 25, -60 20" stroke="#17452D" stroke-width="2" fill="none" />
  </g>

  <!-- ============================================== -->
  <!-- THE ORIGINAL LADDU CARTOON TRIO (HERO CHARACTERS) -->
  <!-- ============================================== -->

  <!-- CHARACTER 1: APPU (Left - The Adventurous Explorer Boy) -->
  <g id="character-appu" transform="translate(240, 250)" filter="url(#dropShadow)">
    <!-- Shadow under feet -->
    <ellipse cx="60" cy="350" rx="45" ry="12" fill="#17452D" opacity="0.35" />

    <!-- Legs & Feet -->
    <g stroke="#17452D" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
      <!-- Left Leg (bent forward) -->
      <path d="M 45 250 L 38 295 L 32 335" fill="none" stroke="#E59866" stroke-width="12" />
      <!-- Left Shoe -->
      <ellipse cx="28" cy="340" rx="14" ry="8" fill="#17452D" />
      <ellipse cx="25" cy="342" rx="13" ry="5" fill="#FFC857" />

      <!-- Right Leg (stepping back) -->
      <path d="M 75 250 L 85 295 L 90 338" fill="none" stroke="#E59866" stroke-width="12" />
      <!-- Right Shoe -->
      <ellipse cx="94" cy="342" rx="14" ry="8" fill="#17452D" />
      <ellipse cx="96" cy="344" rx="13" ry="5" fill="#FFC857" />

      <!-- Little Bandage on right knee! -->
      <rect x="78" y="285" width="14" height="8" fill="#FFF3D9" stroke="#D96B3B" stroke-width="1.5" rx="2" transform="rotate(15 85 289)" />
    </g>

    <!-- Khaki Olive Shorts -->
    <path d="M 32 210 L 88 210 L 96 260 L 68 260 L 60 230 L 52 260 L 25 260 Z" fill="#4B6B48" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <line x1="60" y1="210" x2="60" y2="230" stroke="#17452D" stroke-width="2.5" />

    <!-- Mustard Yellow Polo Shirt -->
    <path d="M 28 140 Q 60 130 92 140 L 88 215 L 32 215 Z" fill="#FFC857" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <!-- Shirt Collar (Terracotta accent) -->
    <polygon points="46,140 60,162 74,140" fill="#D96B3B" stroke="#17452D" stroke-width="2.5" />
    <polygon points="35,138 48,142 42,156" fill="#D96B3B" stroke="#17452D" stroke-width="2" />
    <polygon points="85,138 72,142 78,156" fill="#D96B3B" stroke="#17452D" stroke-width="2" />

    <!-- Left Arm pointing forward excitedly -->
    <path d="M 30 148 L -5 180 L -30 165" stroke="#E59866" stroke-width="11" stroke-linecap="round" fill="none" />
    <!-- Pointing Hand -->
    <circle cx="-35" cy="162" r="8" fill="#E59866" stroke="#17452D" stroke-width="2.5" />
    <line x1="-38" y1="160" x2="-50" y2="152" stroke="#E59866" stroke-width="5" stroke-linecap="round" />
    <line x1="-38" y1="160" x2="-50" y2="152" stroke="#17452D" stroke-width="2" stroke-linecap="round" />

    <!-- Right Arm cheering up -->
    <path d="M 90 148 L 125 170 L 138 150" stroke="#E59866" stroke-width="11" stroke-linecap="round" fill="none" />
    <circle cx="142" cy="146" r="8" fill="#E59866" stroke="#17452D" stroke-width="2.5" />

    <!-- Neck -->
    <rect x="52" y="125" width="16" height="18" fill="#E59866" stroke="#17452D" stroke-width="3" />

    <!-- Head & Face (Expressive, cute 2D Indian cartoon boy) -->
    <ellipse cx="60" cy="95" rx="35" ry="38" fill="#F0A678" stroke="#17452D" stroke-width="3.5" />
    <!-- Cheerful rosy cheeks -->
    <ellipse cx="38" cy="108" rx="7" ry="5" fill="#FF7F66" opacity="0.6" />
    <ellipse cx="82" cy="108" rx="7" ry="5" fill="#FF7F66" opacity="0.6" />

    <!-- Big sparkling expressive cartoon eyes -->
    <!-- Left Eye -->
    <ellipse cx="46" cy="90" rx="9" ry="12" fill="#FFFFFF" stroke="#17452D" stroke-width="2.5" />
    <circle cx="48" cy="90" r="6" fill="#17452D" />
    <circle cx="46" cy="87" r="2.5" fill="#FFFFFF" />
    <!-- Right Eye -->
    <ellipse cx="74" cy="90" rx="9" ry="12" fill="#FFFFFF" stroke="#17452D" stroke-width="2.5" />
    <circle cx="72" cy="90" r="6" fill="#17452D" />
    <circle cx="70" cy="87" r="2.5" fill="#FFFFFF" />

    <!-- Playful Eyebrows -->
    <path d="M 38 74 Q 48 68 56 74" fill="none" stroke="#17452D" stroke-width="3.5" stroke-linecap="round" />
    <path d="M 64 74 Q 74 68 84 75" fill="none" stroke="#17452D" stroke-width="3.5" stroke-linecap="round" />

    <!-- Cute button nose -->
    <ellipse cx="60" cy="98" rx="3" ry="2" fill="#C46F43" />

    <!-- Joyful open mouth smile (showing upper teeth) -->
    <path d="M 46 112 Q 60 132 74 112 Z" fill="#800E13" stroke="#17452D" stroke-width="3" />
    <path d="M 48 112 Q 60 118 72 112" fill="#FFFFFF" />
    <path d="M 52 122 Q 60 128 68 122" fill="#FF758F" />

    <!-- Hair: Messy wavy curly dark brown hair with bounce -->
    <path d="M 24 95 C 20 65, 35 40, 60 38 C 85 36, 100 60, 96 95 C 92 82, 85 70, 78 72 C 70 65, 62 60, 50 66 C 40 64, 30 75, 24 95 Z" fill="#3D2214" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <!-- Fluffy tuft on top -->
    <path d="M 48 42 C 45 28, 62 25, 65 38 Z" fill="#3D2214" stroke="#17452D" stroke-width="3" />
    <path d="M 62 38 C 65 24, 78 26, 75 40 Z" fill="#3D2214" stroke="#17452D" stroke-width="3" />
  </g>

  <!-- CHARACTER 2: KANNAN (Center - The Hero Boy with the Golden LADDU!) -->
  <g id="character-kannan" transform="translate(450, 210)" filter="url(#dropShadow)">
    <!-- Shadow under feet -->
    <ellipse cx="65" cy="390" rx="52" ry="14" fill="#17452D" opacity="0.38" />

    <!-- Legs & Feet (Sturdy, happy bounce) -->
    <g stroke="#17452D" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M 46 295 L 42 340 L 40 375" fill="none" stroke="#E59866" stroke-width="14" />
      <!-- Left Shoe -->
      <ellipse cx="36" cy="380" rx="16" ry="9" fill="#17452D" />
      <ellipse cx="34" cy="382" rx="14" ry="6" fill="#D96B3B" />

      <path d="M 84 295 L 88 340 L 90 375" fill="none" stroke="#E59866" stroke-width="14" />
      <!-- Right Shoe -->
      <ellipse cx="94" cy="380" rx="16" ry="9" fill="#17452D" />
      <ellipse cx="96" cy="382" rx="14" ry="6" fill="#D96B3B" />
    </g>

    <!-- Deep Forest Green Shorts with Terracotta Drawstrings -->
    <path d="M 32 250 L 98 250 L 105 305 L 75 305 L 65 275 L 55 305 L 25 305 Z" fill="#17452D" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <line x1="62" y1="250" x2="58" y2="265" stroke="#FFC857" stroke-width="2.5" />
    <line x1="68" y1="250" x2="72" y2="265" stroke="#FFC857" stroke-width="2.5" />

    <!-- Sky Blue Round-neck T-shirt with Little Laddu Logo -->
    <path d="M 28 175 Q 65 165 102 175 L 98 255 L 32 255 Z" fill="#A8D9E8" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <!-- T-shirt Laddu Print! -->
    <circle cx="65" cy="210" r="12" fill="#FFC857" stroke="#D96B3B" stroke-width="2" />
    <circle cx="65" cy="210" r="3" fill="#D96B3B" />

    <!-- Chubby Arms lifted up high, presenting the Treasured Laddu -->
    <!-- Left Arm -->
    <path d="M 32 185 C 10 160, 5 110, 35 85" stroke="#E59866" stroke-width="14" stroke-linecap="round" fill="none" />
    <!-- Left Hand -->
    <circle cx="38" cy="80" r="10" fill="#E59866" stroke="#17452D" stroke-width="3" />

    <!-- Right Arm -->
    <path d="M 98 185 C 120 160, 125 110, 95 85" stroke="#E59866" stroke-width="14" stroke-linecap="round" fill="none" />
    <!-- Right Hand -->
    <circle cx="92" cy="80" r="10" fill="#E59866" stroke="#17452D" stroke-width="3" />

    <!-- Neck -->
    <rect x="56" y="160" width="18" height="20" fill="#E59866" stroke="#17452D" stroke-width="3" />

    <!-- Round Chubby Face (Lovable, joyful food-loving hero) -->
    <ellipse cx="65" cy="130" rx="38" ry="38" fill="#F0A678" stroke="#17452D" stroke-width="3.5" />
    <!-- Chubby Pink Cheeks with Dimples -->
    <ellipse cx="40" cy="140" rx="8" ry="6" fill="#FF7F66" opacity="0.65" />
    <ellipse cx="90" cy="140" rx="8" ry="6" fill="#FF7F66" opacity="0.65" />

    <!-- Happy Squinting Cartoon Eyes (Joy overload!) -->
    <path d="M 44 122 Q 52 112 60 122" fill="none" stroke="#17452D" stroke-width="4" stroke-linecap="round" />
    <path d="M 70 122 Q 78 112 86 122" fill="none" stroke="#17452D" stroke-width="4" stroke-linecap="round" />

    <!-- Cute button nose -->
    <ellipse cx="65" cy="130" rx="3.5" ry="2.5" fill="#C46F43" />

    <!-- Giant Delighted Open Laughing Smile -->
    <path d="M 48 142 Q 65 170 82 142 Z" fill="#800E13" stroke="#17452D" stroke-width="3.5" />
    <path d="M 50 142 Q 65 150 80 142" fill="#FFFFFF" />
    <path d="M 55 156 Q 65 165 75 156" fill="#FF758F" />

    <!-- Neat side-parted glossy black hair with sweet curl -->
    <path d="M 28 128 C 24 95, 38 75, 65 72 C 92 70, 106 95, 102 128 C 96 112, 90 95, 78 95 C 65 88, 50 92, 40 102 C 34 110, 30 118, 28 128 Z" fill="#2E1C11" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <path d="M 38 85 Q 48 75 60 82" fill="none" stroke="#66442E" stroke-width="2" stroke-linecap="round" />

    <!-- ============================================= -->
    <!-- THE HERO SWEET: GIANT GLORIOUS GOLDEN LADDU! -->
    <!-- ============================================= -->
    <g id="hero-sweet-laddu" transform="translate(65, 55)" filter="url(#ladduMagicGlow)">
      <!-- Golden Glow Halo -->
      <circle cx="0" cy="0" r="48" fill="#FFC857" opacity="0.35" />
      <circle cx="0" cy="0" r="38" fill="url(#ladduGlow)" stroke="#D97706" stroke-width="3" />

      <!-- Laddu Texture & Roasted Cashew/Pistachio Bits -->
      <!-- Roasted Cashew piece (ivory gold) -->
      <ellipse cx="-12" cy="-10" rx="8" ry="4.5" fill="#FFFBEB" stroke="#D97706" stroke-width="1.5" transform="rotate(-25 -12 -10)" />
      <!-- Roasted Almond speck -->
      <ellipse cx="14" cy="-8" rx="6" ry="3.5" fill="#78350F" stroke="#451A03" stroke-width="1.5" transform="rotate(35 14 -8)" />
      <!-- Pistachio green speck -->
      <ellipse cx="-4" cy="14" rx="5" ry="3" fill="#65A30D" stroke="#365314" stroke-width="1.5" transform="rotate(15 -4 14)" />
      <!-- Magizhampoo boondi texture dots -->
      <circle cx="-18" cy="8" r="3" fill="#F59E0B" />
      <circle cx="8" cy="12" r="3" fill="#D97706" />
      <circle cx="16" cy="5" r="2.5" fill="#FBBF24" />
      <circle cx="-6" cy="-18" r="3" fill="#FDE68A" />
      <circle cx="6" cy="-16" r="2.5" fill="#F59E0B" />
      <circle cx="0" cy="0" r="3.5" fill="#D97706" />

      <!-- Sparkles radiating from the delicious Laddu! -->
      <!-- Sparkle 1 (Top Left) -->
      <path d="M -35 -35 Q -35 -25 -25 -25 Q -35 -25 -35 -15 Q -35 -25 -45 -25 Q -35 -25 -35 -35 Z" fill="#FFFBEB" stroke="#FFC857" stroke-width="1.5" />
      <!-- Sparkle 2 (Top Right) -->
      <path d="M 38 -32 Q 38 -24 46 -24 Q 38 -24 38 -16 Q 38 -24 30 -24 Q 38 -24 38 -32 Z" fill="#FFFBEB" stroke="#FFC857" stroke-width="1.5" />
      <!-- Sparkle 3 (Bottom Right) -->
      <path d="M 40 25 Q 40 32 47 32 Q 40 32 40 39 Q 40 32 33 32 Q 40 32 40 25 Z" fill="#FFC857" />

      <!-- Comic motion lines around laddu -->
      <path d="M -22 -38 Q -28 -48 -38 -50" stroke="#FFC857" stroke-width="2.5" stroke-linecap="round" fill="none" />
      <path d="M 0 -44 L 0 -54" stroke="#FFC857" stroke-width="3" stroke-linecap="round" fill="none" />
      <path d="M 22 -38 Q 28 -48 38 -50" stroke="#FFC857" stroke-width="2.5" stroke-linecap="round" fill="none" />
    </g>
  </g>

  <!-- CHARACTER 3: MEENU (Right - The Clever & Playful Girl with Tiffin Box) -->
  <g id="character-meenu" transform="translate(670, 260)" filter="url(#dropShadow)">
    <!-- Shadow under feet -->
    <ellipse cx="65" cy="340" rx="42" ry="12" fill="#17452D" opacity="0.35" />

    <!-- Legs & Traditional Payal (Anklet) feet -->
    <g stroke="#17452D" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M 48 245 L 45 295 L 42 330" fill="none" stroke="#E59866" stroke-width="11" />
      <!-- Left sandal -->
      <ellipse cx="38" cy="334" rx="13" ry="7" fill="#D96B3B" />
      <ellipse cx="36" cy="336" rx="12" ry="4" fill="#FFC857" />

      <path d="M 80 245 L 85 295 L 88 330" fill="none" stroke="#E59866" stroke-width="11" />
      <!-- Right sandal -->
      <ellipse cx="92" cy="334" rx="13" ry="7" fill="#D96B3B" />
      <ellipse cx="94" cy="336" rx="12" ry="4" fill="#FFC857" />
    </g>

    <!-- Traditional Pavada Skirt (Warm Terracotta with Mango Yellow Border) -->
    <path d="M 40 180 Q 65 175 90 180 L 108 260 Q 65 268 22 260 Z" fill="#D96B3B" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <!-- Skirt Kasavu / Golden Zari Border -->
    <path d="M 23 245 Q 65 253 107 245 L 108 260 Q 65 268 22 260 Z" fill="#FFC857" stroke="#17452D" stroke-width="2" />
    <!-- Skirt pleat lines -->
    <line x1="48" y1="182" x2="44" y2="245" stroke="#B3441B" stroke-width="2" />
    <line x1="65" y1="180" x2="65" y2="246" stroke="#B3441B" stroke-width="2" />
    <line x1="82" y1="182" x2="86" y2="245" stroke="#B3441B" stroke-width="2" />

    <!-- Emerald Green Blouse / Top -->
    <path d="M 38 128 Q 65 120 92 128 L 88 180 L 42 180 Z" fill="#17452D" stroke="#17452D" stroke-width="3.5" stroke-linejoin="round" />
    <!-- Golden neckline trim -->
    <path d="M 52 128 Q 65 142 78 128" fill="none" stroke="#FFC857" stroke-width="2.5" />

    <!-- Left Arm holding the open Stainless-Steel Tiffin Box -->
    <path d="M 40 138 L 10 165 L 5 195" stroke="#E59866" stroke-width="10" stroke-linecap="round" fill="none" />
    <!-- Vintage 3-tier Stainless Steel Tiffin Box -->
    <g transform="translate(-15, 175)">
      <!-- Tier 1 -->
      <rect x="0" y="0" width="34" height="15" fill="#E2E8F0" stroke="#17452D" stroke-width="2.5" rx="3" />
      <!-- Tier 2 -->
      <rect x="0" y="14" width="34" height="15" fill="#CBD5E1" stroke="#17452D" stroke-width="2.5" rx="3" />
      <!-- Brass/Steel clip carrier latch -->
      <path d="M 17 -10 L 17 32" stroke="#64748B" stroke-width="2" />
      <path d="M 8 -10 Q 17 -18 26 -10" fill="none" stroke="#64748B" stroke-width="2.5" />
      <!-- Banana leaf liner peeking out with another laddu! -->
      <path d="M 6 0 Q 17 -6 28 0" fill="#3D9B63" stroke="#17452D" stroke-width="1.5" />
      <circle cx="17" cy="-2" r="5" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
    </g>

    <!-- Right Arm cheering/reaching towards Kannan's laddu -->
    <path d="M 90 138 L 120 160 L 135 150" stroke="#E59866" stroke-width="10" stroke-linecap="round" fill="none" />
    <circle cx="140" cy="148" r="7" fill="#E59866" stroke="#17452D" stroke-width="2.5" />

    <!-- Neck -->
    <rect x="58" y="115" width="14" height="16" fill="#E59866" stroke="#17452D" stroke-width="3" />

    <!-- Head & Face -->
    <ellipse cx="65" cy="85" rx="32" ry="34" fill="#F0A678" stroke="#17452D" stroke-width="3.5" />
    <!-- Cheeks -->
    <ellipse cx="44" cy="95" rx="6" ry="5" fill="#FF7F66" opacity="0.6" />
    <ellipse cx="86" cy="95" rx="6" ry="5" fill="#FF7F66" opacity="0.6" />

    <!-- Big sparkling eyes looking at Kannan's laddu -->
    <ellipse cx="50" cy="80" rx="8" ry="11" fill="#FFFFFF" stroke="#17452D" stroke-width="2.5" />
    <circle cx="48" cy="80" r="5.5" fill="#17452D" />
    <circle cx="46" cy="77" r="2.5" fill="#FFFFFF" />

    <ellipse cx="76" cy="80" rx="8" ry="11" fill="#FFFFFF" stroke="#17452D" stroke-width="2.5" />
    <circle cx="74" cy="80" r="5.5" fill="#17452D" />
    <circle cx="72" cy="77" r="2.5" fill="#FFFFFF" />

    <!-- Mischievous playful brows -->
    <path d="M 44 67 Q 52 62 60 68" fill="none" stroke="#17452D" stroke-width="3" stroke-linecap="round" />
    <path d="M 68 68 Q 76 62 84 67" fill="none" stroke="#17452D" stroke-width="3" stroke-linecap="round" />

    <!-- Nose & Smile -->
    <ellipse cx="64" cy="88" rx="2.5" ry="2" fill="#C46F43" />
    <path d="M 52 100 Q 65 118 78 100" fill="#800E13" stroke="#17452D" stroke-width="3" />
    <path d="M 54 100 Q 65 106 76 100" fill="#FFFFFF" />

    <!-- Traditional Pindi / Bindi -->
    <circle cx="65" cy="73" r="2.5" fill="#D96B3B" />

    <!-- Hair: Twin Braids with Jasmine Flowers (Mulla Poo) -->
    <!-- Front Hair Fringe -->
    <path d="M 34 82 C 32 55, 45 42, 65 40 C 85 40, 98 55, 96 82 C 88 72, 80 62, 65 62 C 50 62, 42 72, 34 82 Z" fill="#2E1C11" stroke="#17452D" stroke-width="3.5" />
    
    <!-- Left Braid with Jasmine clips -->
    <path d="M 36 68 C 20 75, 12 100, 16 125 C 18 140, 24 150, 20 165" stroke="#2E1C11" stroke-width="8" stroke-linecap="round" fill="none" />
    <!-- White Jasmine flowers (Mulla Poo) strung in hair -->
    <circle cx="28" cy="82" r="3.5" fill="#FFFFFF" stroke="#D97706" stroke-width="1" />
    <circle cx="22" cy="98" r="3.5" fill="#FFFFFF" stroke="#D97706" stroke-width="1" />
    <circle cx="16" cy="116" r="3.5" fill="#FFFFFF" stroke="#D97706" stroke-width="1" />
    <!-- Terracotta Ribbon at end of braid -->
    <ellipse cx="20" cy="165" rx="5" ry="3" fill="#D96B3B" />

    <!-- Right Braid with Jasmine clips -->
    <path d="M 94 68 C 110 75, 118 100, 114 125 C 112 140, 106 150, 110 165" stroke="#2E1C11" stroke-width="8" stroke-linecap="round" fill="none" />
    <circle cx="102" cy="82" r="3.5" fill="#FFFFFF" stroke="#D97706" stroke-width="1" />
    <circle cx="108" cy="98" r="3.5" fill="#FFFFFF" stroke="#D97706" stroke-width="1" />
    <circle cx="114" cy="116" r="3.5" fill="#FFFFFF" stroke="#D97706" stroke-width="1" />
    <ellipse cx="110" cy="165" rx="5" ry="3" fill="#D96B3B" />
  </g>

  <!-- ============================================== -->
  <!-- PLAYFUL CARTOON DOODLES, STARS & MOTION SWIRLS -->
  <!-- ============================================== -->
  <g class="storybook-doodles" stroke="#17452D" stroke-width="2" stroke-linecap="round" fill="none">
    <!-- Breeze swirl around Appu -->
    <path d="M 140 380 Q 180 360 210 390 Q 230 410 210 425 Q 190 435 180 415" stroke-dasharray="4,4" />
    
    <!-- Stars floating around the kids -->
    <g fill="#FFC857" stroke="#17452D" stroke-width="1.8">
      <!-- Star 1 -->
      <polygon points="210,210 214,222 226,222 216,229 220,241 210,233 200,241 204,229 194,222 206,222" />
      <!-- Star 2 -->
      <polygon points="790,220 793,230 803,230 795,236 798,246 790,239 782,246 785,236 777,230 787,230" />
      <!-- Star 3 -->
      <polygon points="630,160 633,168 641,168 635,173 637,181 630,176 623,181 625,173 619,168 627,168" />
    </g>

    <!-- Flying banana / mango leaf fragments -->
    <path d="M 370 180 Q 390 165 410 185 Q 390 195 370 180 Z" fill="#3D9B63" stroke="#17452D" stroke-width="2" />
    <path d="M 600 390 Q 620 375 640 395 Q 620 405 600 390 Z" fill="#FFC857" stroke="#17452D" stroke-width="2" />

    <!-- Cute little butterly near Appu -->
    <g transform="translate(160, 280) rotate(-15)">
      <ellipse cx="-8" cy="-5" rx="8" ry="6" fill="#FFC857" stroke="#17452D" stroke-width="1.5" />
      <ellipse cx="-6" cy="5" rx="6" ry="4" fill="#D96B3B" stroke="#17452D" stroke-width="1.5" />
      <ellipse cx="8" cy="-5" rx="8" ry="6" fill="#FFC857" stroke="#17452D" stroke-width="1.5" />
      <ellipse cx="6" cy="5" rx="6" ry="4" fill="#D96B3B" stroke="#17452D" stroke-width="1.5" />
      <line x1="0" y1="-8" x2="0" y2="8" stroke="#17452D" stroke-width="2" />
    </g>
  </g>
</svg>'''
    with open('assets/illustrations/hero_kerala_scene.svg', 'w') as f:
        f.write(svg)
    print('Hero illustration generated successfully!')

if __name__ == '__main__':
    create_hero_svg()
