import os

def create_story_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="storyBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFF3D9" />
      <stop offset="60%" stop-color="#FFE0B2" />
      <stop offset="100%" stop-color="#F5C48E" />
    </linearGradient>
    <linearGradient id="verandaWood" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#6F4426" />
      <stop offset="100%" stop-color="#462711" />
    </linearGradient>
    <linearGradient id="tileGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D96B3B" />
      <stop offset="100%" stop-color="#A53D14" />
    </linearGradient>
    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#17452D" flood-opacity="0.25" />
    </filter>
  </defs>

  <!-- Background Warm Evening Sky -->
  <rect width="800" height="600" rx="20" fill="url(#storyBg)" />

  <!-- Window into Courtyard with Coconut Palm & Rain Tree -->
  <g opacity="0.65">
    <ellipse cx="680" cy="200" rx="140" ry="140" fill="#FFEDB3" />
    <!-- Distant Greenery -->
    <path d="M 450 340 Q 580 260 720 300 T 800 290 L 800 480 L 450 480 Z" fill="#7CB58C" />
    <path d="M 520 360 Q 640 310 760 340 L 800 480 L 520 480 Z" fill="#3D8557" />
    <!-- Coconut frond framing window -->
    <path d="M 780 140 C 720 180 640 180 580 230 C 640 210 700 210 780 180 Z" fill="#2E7D4E" />
  </g>

  <!-- Traditional Kerala Veranda (Charupadi) Structure -->
  <!-- Red Terracotta Tiled Roof Eaves above -->
  <polygon points="0,0 800,0 800,90 0,90" fill="url(#tileGrad)" stroke="#583723" stroke-width="3" />
  <g stroke="#7D2B0E" stroke-width="2">
    <line x1="80" y1="0" x2="80" y2="90" />
    <line x1="160" y1="0" x2="160" y2="90" />
    <line x1="240" y1="0" x2="240" y2="90" />
    <line x1="320" y1="0" x2="320" y2="90" />
    <line x1="400" y1="0" x2="400" y2="90" />
    <line x1="480" y1="0" x2="480" y2="90" />
    <line x1="560" y1="0" x2="560" y2="90" />
    <line x1="640" y1="0" x2="640" y2="90" />
    <line x1="720" y1="0" x2="720" y2="90" />
  </g>
  <!-- Carved Wooden Eaves Pattern (Mukhappu border) -->
  <path d="M 0 90 Q 20 105 40 90 Q 60 105 80 90 Q 100 105 120 90 Q 140 105 160 90 Q 180 105 200 90 Q 220 105 240 90 Q 260 105 280 90 Q 300 105 320 90 Q 340 105 360 90 Q 380 105 400 90 Q 420 105 440 90 Q 460 105 480 90 Q 500 105 520 90 Q 540 105 560 90 Q 580 105 600 90 Q 620 105 640 90 Q 660 105 680 90 Q 700 105 720 90 Q 740 105 760 90 Q 780 105 800 90" fill="#583723" stroke="#3D2214" stroke-width="2" />

  <!-- Carved Wooden Pillars -->
  <!-- Left Pillar -->
  <rect x="70" y="90" width="36" height="380" fill="url(#verandaWood)" stroke="#381D0B" stroke-width="2" />
  <rect x="62" y="100" width="52" height="15" fill="#8D552B" stroke="#381D0B" stroke-width="1.5" rx="3" />
  <rect x="62" y="440" width="52" height="20" fill="#8D552B" stroke="#381D0B" stroke-width="1.5" rx="3" />

  <!-- Right Pillar -->
  <rect x="680" y="90" width="36" height="380" fill="url(#verandaWood)" stroke="#381D0B" stroke-width="2" />
  <rect x="672" y="100" width="52" height="15" fill="#8D552B" stroke="#381D0B" stroke-width="1.5" rx="3" />
  <rect x="672" y="440" width="52" height="20" fill="#8D552B" stroke="#381D0B" stroke-width="1.5" rx="3" />

  <!-- Wooden Charupadi / Curved Veranda Bench Railing -->
  <path d="M 106 310 C 240 330 540 330 680 310 L 680 370 C 540 390 240 390 106 370 Z" fill="#5A351D" stroke="#381D0B" stroke-width="2" />
  <g stroke="#381D0B" stroke-width="2">
    <line x1="200" y1="320" x2="200" y2="380" />
    <line x1="300" y1="325" x2="300" y2="385" />
    <line x1="400" y1="326" x2="400" y2="386" />
    <line x1="500" y1="325" x2="500" y2="385" />
    <line x1="600" y1="320" x2="600" y2="380" />
  </g>

  <!-- Wooden Floor Steps (Red oxide polished Kerala veranda floor) -->
  <polygon points="0,460 800,460 800,600 0,600" fill="#B24424" stroke="#7A2810" stroke-width="3" />
  <polygon points="0,460 800,460 800,480 0,480" fill="#D96B3B" />
  <polygon points="0,530 800,530 800,545 0,545" fill="#993214" />

  <!-- Vintage School Bags Leaning against the Left Pillar -->
  <g transform="translate(100, 390)" filter="url(#softShadow)">
    <!-- Canvas Satchel School Bag -->
    <rect x="0" y="15" width="60" height="55" rx="8" fill="#4B6B48" stroke="#17452D" stroke-width="2.5" />
    <polygon points="0,15 60,15 50,45 10,45" fill="#3D5A3B" stroke="#17452D" stroke-width="2" />
    <rect x="25" y="40" width="10" height="12" fill="#FFC857" stroke="#17452D" stroke-width="1.5" rx="2" />
    <!-- Strap -->
    <path d="M 10 15 Q -10 50 15 70" fill="none" stroke="#2C3E2A" stroke-width="4" />
    <!-- Notebook ruler peeking out -->
    <rect x="15" y="-5" width="8" height="25" fill="#FFC857" stroke="#17452D" stroke-width="1.5" />
  </g>

  <!-- CHARACTERS SITTING TOGETHER ON VERANDA -->

  <!-- KANNAN & APPU SHARING LADDU ON STEPS -->
  <!-- Appu (Sitting Left) -->
  <g transform="translate(240, 290)" filter="url(#softShadow)">
    <!-- Body Sitting -->
    <path d="M 20 130 Q 50 120 75 130 L 70 190 L 15 190 Z" fill="#FFC857" stroke="#17452D" stroke-width="3" />
    <polygon points="35,130 45,150 58,130" fill="#D96B3B" />
    <!-- Shorts & Legs folded on step -->
    <path d="M 15 190 L 75 190 L 85 235 L -10 235 Z" fill="#4B6B48" stroke="#17452D" stroke-width="3" />
    <!-- Head turned right smiling -->
    <ellipse cx="50" cy="85" rx="30" ry="32" fill="#F0A678" stroke="#17452D" stroke-width="3" />
    <ellipse cx="32" cy="95" rx="6" ry="4" fill="#FF7F66" opacity="0.6" />
    <ellipse cx="68" cy="95" rx="6" ry="4" fill="#FF7F66" opacity="0.6" />
    <!-- Eyes -->
    <circle cx="42" cy="80" r="5" fill="#17452D" />
    <circle cx="62" cy="80" r="5" fill="#17452D" />
    <circle cx="44" cy="78" r="1.5" fill="#FFFFFF" />
    <circle cx="64" cy="78" r="1.5" fill="#FFFFFF" />
    <path d="M 40 98 Q 52 110 64 98" fill="none" stroke="#800E13" stroke-width="3" stroke-linecap="round" />
    <!-- Curly Hair -->
    <path d="M 20 85 C 16 55, 30 35, 52 35 C 74 35, 84 55, 80 85 C 75 70, 68 62, 52 62 C 38 62, 28 72, 20 85 Z" fill="#3D2214" stroke="#17452D" stroke-width="3" />
    <!-- Arm reaching to take the shared piece -->
    <path d="M 70 140 L 105 155" stroke="#E59866" stroke-width="9" stroke-linecap="round" fill="none" />
  </g>

  <!-- Open Steel Tiffin Box on Banana Leaf on Step -->
  <g transform="translate(370, 440)" filter="url(#softShadow)">
    <!-- Banana Leaf Base -->
    <ellipse cx="50" cy="25" rx="65" ry="22" fill="#3D9B63" stroke="#17452D" stroke-width="2.5" />
    <line x1="-5" y1="25" x2="105" y2="25" stroke="#1E5C37" stroke-width="2" />
    <!-- Fresh Golden Laddus on Leaf -->
    <circle cx="35" cy="18" r="14" fill="#FFC857" stroke="#D97706" stroke-width="2" />
    <circle cx="65" cy="18" r="14" fill="#FFC857" stroke="#D97706" stroke-width="2" />
    <circle cx="50" cy="8" r="13" fill="#F59E0B" stroke="#D97706" stroke-width="2" />
    <circle cx="50" cy="8" r="3" fill="#FFFBEB" />
    <!-- Sparkles -->
    <polygon points="50,-10 52,-4 58,-4 53,0 55,6 50,2 45,6 47,0 42,-4 48,-4" fill="#FFF3D9" stroke="#FFC857" stroke-width="1" />
  </g>

  <!-- Kannan (Sitting Right, happily breaking a laddu into two) -->
  <g transform="translate(460, 270)" filter="url(#softShadow)">
    <!-- Body Sitting -->
    <path d="M 20 150 Q 55 140 90 150 L 85 210 L 25 210 Z" fill="#A8D9E8" stroke="#17452D" stroke-width="3" />
    <circle cx="55" cy="175" r="8" fill="#FFC857" />
    <!-- Shorts & Legs -->
    <path d="M 22 210 L 88 210 L 98 255 L 10 255 Z" fill="#17452D" stroke="#17452D" stroke-width="3" />
    <!-- Head smiling joyfully at Appu -->
    <ellipse cx="55" cy="100" rx="34" ry="34" fill="#F0A678" stroke="#17452D" stroke-width="3" />
    <ellipse cx="32" cy="110" rx="7" ry="5" fill="#FF7F66" opacity="0.65" />
    <ellipse cx="78" cy="110" rx="7" ry="5" fill="#FF7F66" opacity="0.65" />
    <!-- Squinting happy eyes -->
    <path d="M 36 94 Q 44 86 52 94" fill="none" stroke="#17452D" stroke-width="3.5" stroke-linecap="round" />
    <path d="M 60 94 Q 68 86 76 94" fill="none" stroke="#17452D" stroke-width="3.5" stroke-linecap="round" />
    <path d="M 42 112 Q 56 128 70 112 Z" fill="#800E13" stroke="#17452D" stroke-width="2.5" />
    <!-- Hair -->
    <path d="M 24 95 C 20 70, 32 50, 56 48 C 80 46, 92 68, 88 95 C 82 82, 75 72, 60 72 C 48 68, 35 78, 24 95 Z" fill="#2E1C11" stroke="#17452D" stroke-width="3" />
    <!-- Hands holding the two split halves of sweet laddu! -->
    <!-- Left Hand with half laddu -->
    <circle cx="5" cy="165" r="9" fill="#E59866" stroke="#17452D" stroke-width="2" />
    <path d="M -5 165 A 10 10 0 0 1 12 165 Z" fill="#FFC857" stroke="#D97706" stroke-width="2" />
    <!-- Right Hand with other half -->
    <circle cx="45" cy="160" r="9" fill="#E59866" stroke="#17452D" stroke-width="2" />
    <path d="M 38 160 A 10 10 0 0 1 54 160 Z" fill="#FFC857" stroke="#D97706" stroke-width="2" />
  </g>

  <!-- Nostalgic Flying Paper Plane Doodle in Air -->
  <g transform="translate(620, 160) rotate(-15)">
    <polygon points="0,0 50,20 15,30" fill="#FFFFFF" stroke="#17452D" stroke-width="2" />
    <polygon points="50,20 15,30 20,40" fill="#E2E8F0" stroke="#17452D" stroke-width="1.5" />
    <!-- Dashed flight line -->
    <path d="M -80 60 Q -30 40 0 0" fill="none" stroke="#D96B3B" stroke-width="2" stroke-dasharray="4,4" />
  </g>
</svg>'''
    with open('assets/illustrations/story_school_memories.svg', 'w') as f:
        f.write(svg)
    print('Story illustration generated!')

def create_ingredients_svg():
    # 6 Individual Ingredient Badges
    ingredients = [
        ('ingredient_besan.svg', 'Roasted Besan', '''
          <ellipse cx="60" cy="80" rx="42" ry="16" fill="#8C5C33" stroke="#583723" stroke-width="2.5" />
          <ellipse cx="60" cy="74" rx="42" ry="16" fill="#FFC857" stroke="#D97706" stroke-width="2" />
          <path d="M 20 74 C 30 50, 90 50, 100 74 Z" fill="#F59E0B" />
          <!-- Steam trails -->
          <path d="M 50 45 Q 40 30 50 15" fill="none" stroke="#FFC857" stroke-width="2.5" stroke-linecap="round" />
          <path d="M 70 48 Q 80 32 70 18" fill="none" stroke="#FFC857" stroke-width="2.5" stroke-linecap="round" />
          <polygon points="80,10 82,16 88,16 83,20 85,26 80,22 75,26 77,20 72,16 78,16" fill="#FFC857" />
        '''),
        ('ingredient_ghee.svg', 'Pure Desi Ghee', '''
          <!-- Brass Kindi / Ghee pot -->
          <path d="M 35 40 Q 60 30 85 40 L 78 85 Q 60 92 42 85 Z" fill="#FFC857" stroke="#D97706" stroke-width="2.5" />
          <ellipse cx="60" cy="40" rx="25" ry="8" fill="#FDE68A" stroke="#D97706" stroke-width="2" />
          <ellipse cx="60" cy="40" rx="18" ry="5" fill="#F59E0B" />
          <!-- Golden Ghee Ribbon Flowing down -->
          <path d="M 60 42 C 55 60, 50 80, 58 100 C 62 108, 62 115, 60 118" fill="none" stroke="#FFD166" stroke-width="5" stroke-linecap="round" />
          <circle cx="60" cy="118" r="6" fill="#FFD166" stroke="#D97706" stroke-width="1.5" />
          <!-- Sparkles -->
          <circle cx="30" cy="55" r="3" fill="#FFFBEB" />
          <circle cx="90" cy="65" r="3" fill="#FFFBEB" />
        '''),
        ('ingredient_cardamom.svg', 'Green Cardamom (Elaichi)', '''
          <!-- Two green cardamom pods -->
          <ellipse cx="50" cy="65" rx="24" ry="14" fill="#65A30D" stroke="#365314" stroke-width="2.5" transform="rotate(-30 50 65)" />
          <path d="M 30 50 Q 50 65 70 80" stroke="#4D7C0F" stroke-width="2" fill="none" />
          <!-- Open pod showing black aromatic seeds -->
          <ellipse cx="72" cy="55" rx="22" ry="13" fill="#84CC16" stroke="#365314" stroke-width="2.5" transform="rotate(25 72 55)" />
          <ellipse cx="74" cy="54" rx="14" ry="7" fill="#3D2214" transform="rotate(25 74 54)" />
          <circle cx="70" cy="52" r="2.5" fill="#17452D" />
          <circle cx="76" cy="56" r="2" fill="#17452D" />
          <circle cx="80" cy="52" r="2" fill="#17452D" />
          <!-- Scent aroma waves -->
          <path d="M 60 25 Q 70 12 85 20" fill="none" stroke="#65A30D" stroke-width="2" stroke-linecap="round" />
        '''),
        ('ingredient_nuts.svg', 'Cashews & Almonds', '''
          <!-- Golden Cashew Nut -->
          <path d="M 35 45 C 20 55, 22 80, 42 85 C 55 88, 65 78, 55 65 C 50 58, 48 55, 52 48 C 55 42, 45 38, 35 45 Z" fill="#FEF3C7" stroke="#D97706" stroke-width="2.5" />
          <!-- Almond slice -->
          <ellipse cx="75" cy="65" rx="20" ry="11" fill="#92400E" stroke="#451A03" stroke-width="2.5" transform="rotate(-40 75 65)" />
          <ellipse cx="75" cy="65" rx="15" ry="7" fill="#FEF3C7" transform="rotate(-40 75 65)" />
          <!-- Crunch stars -->
          <polygon points="58,30 60,34 65,34 61,37 63,42 58,39 54,42 56,37 52,34 57,34" fill="#FFC857" />
          <polygon points="90,45 92,48 96,48 93,51 94,55 90,52 87,55 88,51 85,48 89,48" fill="#FFC857" />
        '''),
        ('ingredient_jaggery.svg', 'Natural Cane Jaggery', '''
          <!-- Jaggery block cube -->
          <polygon points="35,55 65,40 95,55 65,70" fill="#B45309" stroke="#78350F" stroke-width="2" />
          <polygon points="35,55 65,70 65,100 35,85" fill="#92400E" stroke="#78350F" stroke-width="2" />
          <polygon points="65,70 95,55 95,85 65,100" fill="#78350F" stroke="#451A03" stroke-width="2" />
          <!-- Raw Sugar Cane shoot -->
          <rect x="20" y="25" width="8" height="60" rx="3" fill="#84CC16" stroke="#365314" stroke-width="2" transform="rotate(-25 20 25)" />
          <line x1="20" y1="45" x2="32" y2="40" stroke="#365314" stroke-width="2" />
          <!-- Golden sweetness sparkle -->
          <circle cx="85" cy="35" r="4" fill="#FDE68A" />
        '''),
        ('ingredient_saffron.svg', 'Saffron & Nutmeg', '''
          <!-- Nutmeg seed -->
          <ellipse cx="48" cy="65" rx="18" ry="14" fill="#78350F" stroke="#451A03" stroke-width="2.5" />
          <path d="M 40 55 Q 48 65 42 75" stroke="#B45309" stroke-width="2" fill="none" />
          <!-- Crimson Saffron Strands -->
          <path d="M 65 75 C 75 55, 70 35, 85 20" stroke="#DC2626" stroke-width="3" stroke-linecap="round" fill="none" />
          <path d="M 68 78 C 82 60, 85 45, 95 32" stroke="#EA580C" stroke-width="2.5" stroke-linecap="round" fill="none" />
          <path d="M 60 76 C 65 62, 75 50, 78 40" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round" fill="none" />
          <!-- Golden aura -->
          <circle cx="85" cy="22" r="5" fill="#FEF08A" opacity="0.8" />
        ''')
    ]

    for filename, title, inner in ingredients:
        content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
          <circle cx="60" cy="60" r="54" fill="#FFF3D9" stroke="#17452D" stroke-width="2.5" />
          {inner}
        </svg>'''
        with open(f'assets/illustrations/{filename}', 'w') as f:
            f.write(content)
    print('Ingredients SVGs generated!')

def create_moments_svg():
    # 4 Mini-scenes for Section 6
    moments = [
        ('moment_busy_break.svg', '''
          <!-- 4 PM Busy Day Break -->
          <rect width="400" height="280" rx="16" fill="#FFF3D9" />
          <!-- Table Surface -->
          <rect y="190" width="400" height="90" fill="#D96B3B" />
          <rect y="190" width="400" height="12" fill="#BA552A" />
          <!-- Kerala Tea Glass -->
          <polygon points="120,130 160,130 152,190 128,190" fill="#F8FAFC" stroke="#17452D" stroke-width="2.5" opacity="0.9" />
          <polygon points="123,145 157,145 151,185 129,185" fill="#B45309" />
          <!-- Frothy milk layer on top of tea -->
          <ellipse cx="140" cy="145" rx="16" ry="4" fill="#FEF3C7" />
          <!-- Tea Steam swirls -->
          <path d="M 135 120 Q 130 105 140 95" stroke="#D96B3B" stroke-width="2.5" stroke-linecap="round" fill="none" />
          <path d="M 148 122 Q 155 108 145 92" stroke="#D96B3B" stroke-width="2" stroke-linecap="round" fill="none" />
          <!-- Banana leaf coaster with golden laddu -->
          <ellipse cx="260" cy="190" rx="55" ry="18" fill="#3D9B63" stroke="#17452D" stroke-width="2" />
          <!-- Golden Laddu with Cashew -->
          <circle cx="260" cy="165" r="26" fill="#FFC857" stroke="#D97706" stroke-width="3" />
          <ellipse cx="255" cy="158" rx="6" ry="3" fill="#FFFBEB" />
          <circle cx="270" cy="170" r="3" fill="#65A30D" />
          <!-- Laptop / notebook in background -->
          <rect x="290" y="110" width="90" height="75" rx="6" fill="#17452D" stroke="#0D2E1D" stroke-width="2" />
          <rect x="296" y="116" width="78" height="55" rx="3" fill="#A8D9E8" />
          <!-- Sparkles -->
          <polygon points="220,135 222,140 227,140 223,143 225,148 220,145 216,148 217,143 214,140 219,140" fill="#FFC857" stroke="#17452D" stroke-width="1" />
        '''),
        ('moment_friends_share.svg', '''
          <!-- Friends Sharing a Snack -->
          <rect width="400" height="280" rx="16" fill="#FFF3D9" />
          <!-- Shady Green Background -->
          <path d="M 0 140 Q 200 90 400 140 L 400 280 L 0 280 Z" fill="#2E7D4E" />
          <!-- Wooden Bench -->
          <rect x="40" y="190" width="320" height="18" rx="4" fill="#7A4E2B" stroke="#3D2214" stroke-width="2.5" />
          <line x1="80" y1="208" x2="80" y2="250" stroke="#3D2214" stroke-width="6" />
          <line x1="320" y1="208" x2="320" y2="250" stroke="#3D2214" stroke-width="6" />
          <!-- Appu & Kannan heads together laughing -->
          <!-- Boy 1 -->
          <ellipse cx="150" cy="130" rx="28" ry="30" fill="#F0A678" stroke="#17452D" stroke-width="3" />
          <circle cx="140" cy="125" r="4.5" fill="#17452D" />
          <path d="M 136 142 Q 148 152 160 142" fill="none" stroke="#800E13" stroke-width="2.5" stroke-linecap="round" />
          <path d="M 125 125 C 122 100, 135 85, 155 85 C 175 85, 180 100, 178 125 Z" fill="#3D2214" stroke="#17452D" stroke-width="2.5" />
          <!-- Boy 2 -->
          <ellipse cx="250" cy="125" rx="30" ry="30" fill="#F0A678" stroke="#17452D" stroke-width="3" />
          <path d="M 238 120 Q 244 112 250 120" stroke="#17452D" stroke-width="3" fill="none" />
          <path d="M 256 120 Q 262 112 268 120" stroke="#17452D" stroke-width="3" fill="none" />
          <path d="M 242 135 Q 254 150 266 135 Z" fill="#800E13" />
          <path d="M 226 122 C 222 98, 238 82, 258 82 C 278 82, 285 98, 282 122 Z" fill="#2E1C11" stroke="#17452D" stroke-width="2.5" />
          <!-- Both holding the Laddu between them -->
          <circle cx="200" cy="175" r="18" fill="#FFC857" stroke="#D97706" stroke-width="2.5" />
          <circle cx="200" cy="175" r="3" fill="#FFFBEB" />
          <!-- Sparkles -->
          <polygon points="200,145 202,150 207,150 203,153 205,158 200,155 196,158 197,153 194,150 199,150" fill="#FFC857" stroke="#17452D" stroke-width="1" />
        '''),
        ('moment_family_home.svg', '''
          <!-- Family Moment at Home -->
          <rect width="400" height="280" rx="16" fill="#FFF3D9" />
          <!-- Red Oxide Veranda floor -->
          <rect y="170" width="400" height="110" fill="#B24424" />
          <!-- Traditional Brass Nilavilakku (Oil Lamp) -->
          <polygon points="70,140 90,140 85,210 75,210" fill="#FFC857" stroke="#D97706" stroke-width="2" />
          <ellipse cx="80" cy="140" rx="15" ry="5" fill="#FFD166" />
          <path d="M 80 135 Q 82 125 80 120 Q 78 125 80 135" fill="#D96B3B" stroke="#9A3412" stroke-width="1.5" />
          <!-- Muthassi (Grandmother) Hand giving laddu to little child hand -->
          <!-- Grandmother's arm (traditional gold bangles / kangan) -->
          <path d="M 360 120 C 300 130 250 150 215 155" stroke="#E59866" stroke-width="14" stroke-linecap="round" fill="none" />
          <circle cx="280" cy="140" r="5" fill="#FFC857" stroke="#D97706" stroke-width="2" />
          <!-- Fresh Laddu in hand -->
          <circle cx="200" cy="155" r="20" fill="#FFC857" stroke="#D97706" stroke-width="2.5" />
          <circle cx="196" cy="150" r="3" fill="#FFFBEB" />
          <circle cx="206" cy="160" r="2.5" fill="#65A30D" />
          <!-- Child's little eager hand reaching up -->
          <path d="M 110 210 C 140 200 170 180 185 170" stroke="#F0A678" stroke-width="11" stroke-linecap="round" fill="none" />
          <!-- Floating heart / warmth doodle -->
          <path d="M 200 115 C 200 105, 185 100, 185 110 C 185 120, 200 130, 200 130 C 200 130, 215 120, 215 110 C 215 100, 200 105, 200 115 Z" fill="#D96B3B" />
        '''),
        ('moment_school_days.svg', '''
          <!-- Nostalgic School-Day Moment -->
          <rect width="400" height="280" rx="16" fill="#FFF3D9" />
          <!-- Vintage School Wall & Window -->
          <rect y="170" width="400" height="110" fill="#17452D" />
          <!-- Brass School Bell on wooden post -->
          <g transform="translate(80, 70)">
            <rect x="0" y="0" width="16" height="110" fill="#7A4E2B" stroke="#3D2214" stroke-width="2" />
            <path d="M -15 40 Q 8 20 31 40 L 26 70 Q 8 75 -10 70 Z" fill="#FFC857" stroke="#D97706" stroke-width="2.5" />
            <circle cx="8" cy="78" r="5" fill="#92400E" />
            <!-- Sound Waves "TRRRING!" -->
            <path d="M 38 45 Q 46 55 38 65" stroke="#D96B3B" stroke-width="2.5" fill="none" stroke-linecap="round" />
            <path d="M 45 40 Q 55 55 45 70" stroke="#D96B3B" stroke-width="2.5" fill="none" stroke-linecap="round" />
          </g>
          <!-- Steel Tiffin Box Open on desk with laddus inside -->
          <g transform="translate(230, 130)">
            <rect x="0" y="20" width="90" height="40" rx="8" fill="#CBD5E1" stroke="#17452D" stroke-width="2.5" />
            <rect x="0" y="0" width="90" height="20" rx="6" fill="#E2E8F0" stroke="#17452D" stroke-width="2" />
            <!-- Laddus inside lined with banana leaf -->
            <ellipse cx="45" cy="16" rx="38" ry="10" fill="#3D9B63" />
            <circle cx="28" cy="14" r="11" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
            <circle cx="48" cy="13" r="11" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
            <circle cx="68" cy="14" r="11" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
          </g>
          <!-- Sparkles -->
          <polygon points="340,90 342,95 347,95 343,98 345,103 340,100 336,103 337,98 334,95 339,95" fill="#FFC857" stroke="#17452D" stroke-width="1" />
        ''')
    ]

    for filename, inner in moments:
        content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 280" width="100%" height="100%">
          {inner}
        </svg>'''
        with open(f'assets/illustrations/{filename}', 'w') as f:
            f.write(content)
    print('Moments SVGs generated!')

def create_cta_sunset_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="100%" height="100%">
  <defs>
    <linearGradient id="sunsetSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7B2D26" />
      <stop offset="35%" stop-color="#D96B3B" />
      <stop offset="70%" stop-color="#FFC857" />
      <stop offset="100%" stop-color="#FFEAA7" />
    </linearGradient>
    <linearGradient id="sunsetWater" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E17055" />
      <stop offset="50%" stop-color="#D63031" />
      <stop offset="100%" stop-color="#2D3436" />
    </linearGradient>
  </defs>

  <!-- Sunset Sky -->
  <rect width="1000" height="450" rx="20" fill="url(#sunsetSky)" />

  <!-- Giant Golden Setting Sun -->
  <circle cx="500" cy="220" r="110" fill="#FFF3D9" opacity="0.9" />
  <circle cx="500" cy="220" r="150" fill="#FFC857" opacity="0.3" />

  <!-- Distant Coconut Palms & Hills Silhouettes -->
  <path d="M 0 250 Q 250 210 500 240 T 1000 230 L 1000 320 L 0 320 Z" fill="#583723" opacity="0.5" />

  <!-- Backwaters Glowing River -->
  <path d="M 0 270 Q 300 260 500 275 T 1000 265 L 1000 360 L 0 360 Z" fill="url(#sunsetWater)" opacity="0.85" />
  <!-- Water Reflection Lines -->
  <g stroke="#FFF3D9" stroke-width="2.5" opacity="0.6" stroke-linecap="round">
    <line x1="420" y1="285" x2="580" y2="285" />
    <line x1="440" y1="300" x2="560" y2="300" />
    <line x1="460" y1="315" x2="540" y2="315" />
    <line x1="480" y1="330" x2="520" y2="330" />
  </g>

  <!-- Foreground Shore with Coconut Trees Silhouettes -->
  <path d="M 0 330 Q 300 310 600 330 T 1000 320 L 1000 450 L 0 450 Z" fill="#17452D" />

  <!-- Left Coconut Tree Silhouette -->
  <path d="M 90 450 C 95 350 110 250 150 160" stroke="#0D2E1D" stroke-width="16" stroke-linecap="round" fill="none" />
  <g fill="#0D2E1D">
    <path d="M 150 160 C 100 120 40 130 0 160 C 40 145 90 145 150 160 Z" />
    <path d="M 150 160 C 145 90 180 60 215 70 C 195 100 175 130 150 160 Z" />
    <path d="M 150 160 C 205 125 260 140 290 180 C 240 165 190 165 150 160 Z" />
  </g>

  <!-- Right Coconut Tree Silhouette -->
  <path d="M 910 450 C 900 350 885 260 850 170" stroke="#0D2E1D" stroke-width="16" stroke-linecap="round" fill="none" />
  <g fill="#0D2E1D">
    <path d="M 850 170 C 890 120 950 125 990 160 C 950 145 900 145 850 170 Z" />
    <path d="M 850 170 C 840 95 805 65 770 75 C 790 105 815 135 850 170 Z" />
    <path d="M 850 170 C 795 130 735 145 710 185 C 760 170 810 170 850 170 Z" />
  </g>

  <!-- The LADDU Brand Box in the Center Foreground with the Kids Cheering! -->
  <g transform="translate(420, 270)">
    <!-- Cheerful Trio Silhouettes / Stylized Figures Cheering -->
    <!-- Appu waving -->
    <circle cx="-40" cy="20" r="18" fill="#FFC857" stroke="#17452D" stroke-width="2" />
    <path d="M -55 38 L -25 38 L -25 80 L -55 80 Z" fill="#D96B3B" stroke="#17452D" stroke-width="2" />
    <path d="M -55 45 L -75 25" stroke="#F0A678" stroke-width="6" stroke-linecap="round" />

    <!-- Kannan in center holding the golden box -->
    <circle cx="80" cy="10" r="20" fill="#FFC857" stroke="#17452D" stroke-width="2" />
    <path d="M 60 30 L 100 30 L 100 80 L 60 80 Z" fill="#A8D9E8" stroke="#17452D" stroke-width="2" />

    <!-- Meenu cheering -->
    <circle cx="195" cy="22" r="17" fill="#FFC857" stroke="#17452D" stroke-width="2" />
    <path d="M 180 39 L 210 39 L 215 80 L 175 80 Z" fill="#17452D" stroke="#FFC857" stroke-width="2" />
    <path d="M 210 45 L 230 25" stroke="#F0A678" stroke-width="6" stroke-linecap="round" />

    <!-- Premium LADDU Box in front -->
    <g transform="translate(15, 60)">
      <rect x="0" y="0" width="130" height="85" rx="10" fill="#17452D" stroke="#FFC857" stroke-width="3.5" />
      <rect x="6" y="6" width="118" height="73" rx="7" fill="#1F5A3B" />
      <rect x="12" y="12" width="106" height="61" rx="5" fill="#FFF3D9" />
      <text x="65" y="42" font-family="'Outfit', 'Inter', sans-serif" font-weight="900" font-size="20" fill="#17452D" text-anchor="middle" letter-spacing="2">LADDU</text>
      <circle cx="65" cy="56" r="8" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
      <!-- Golden ribbon bow -->
      <polygon points="65,-5 55,-18 75,-18" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
      <circle cx="65" cy="-5" r="4" fill="#D96B3B" />
    </g>
  </g>

  <!-- Stars and sparkles in twilight sky -->
  <g fill="#FFF3D9" stroke="#FFC857" stroke-width="1">
    <circle cx="280" cy="80" r="3" />
    <circle cx="360" cy="110" r="2.5" />
    <circle cx="680" cy="70" r="3.5" />
    <circle cx="750" cy="120" r="2" />
    <circle cx="180" cy="130" r="2" />
  </g>
</svg>'''
    with open('assets/illustrations/cta_sunset_kerala.svg', 'w') as f:
        f.write(svg)
    print('CTA sunset SVG generated!')

def create_brand_box_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <filter id="boxShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#17452D" flood-opacity="0.3" />
    </filter>
    <linearGradient id="boxGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF5D6" />
      <stop offset="50%" stop-color="#FFC857" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <linearGradient id="boxGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1F5A3B" />
      <stop offset="100%" stop-color="#113622" />
    </linearGradient>
  </defs>

  <!-- Isometric 3D Premium Box Presentation -->
  <g transform="translate(50, 40)" filter="url(#boxShadow)">
    <!-- Box Shadow Floor -->
    <ellipse cx="200" cy="380" rx="180" ry="40" fill="#17452D" opacity="0.35" />

    <!-- Top Lid (Isometric Diamond) -->
    <polygon points="200,60 370,140 200,220 30,140" fill="#FFF3D9" stroke="#17452D" stroke-width="4" stroke-linejoin="round" />
    
    <!-- Top Lid Artwork & Gold Trim -->
    <polygon points="200,75 350,140 200,205 50,140" fill="url(#boxGreen)" stroke="url(#boxGold)" stroke-width="3" />
    
    <!-- Gold Foil Brand Emblem on Top -->
    <g transform="translate(200, 140)">
      <ellipse cx="0" cy="0" rx="75" ry="32" fill="#FFF3D9" stroke="#FFC857" stroke-width="2.5" />
      <!-- Golden Mascot Laddu inside emblem -->
      <circle cx="0" cy="-6" r="14" fill="#FFC857" stroke="#D97706" stroke-width="2" />
      <circle cx="-4" cy="-8" r="2.5" fill="#FFFBEB" />
      <circle cx="4" cy="-4" r="2" fill="#65A30D" />
      <text x="0" y="16" font-family="'Outfit', sans-serif" font-weight="900" font-size="16" fill="#17452D" text-anchor="middle" letter-spacing="3">LADDU</text>
    </g>

    <!-- Left Box Side (in shade) -->
    <polygon points="30,140 200,220 200,360 30,280" fill="#113622" stroke="#17452D" stroke-width="4" stroke-linejoin="round" />
    <!-- Left side subtle pattern -->
    <g stroke="#1F5A3B" stroke-width="2" opacity="0.6">
      <line x1="50" y1="160" x2="50" y2="280" />
      <line x1="90" y1="180" x2="90" y2="300" />
      <line x1="130" y1="200" x2="130" y2="320" />
      <line x1="170" y1="215" x2="170" y2="340" />
    </g>
    <!-- Left text -->
    <text x="110" y="270" font-family="'Outfit', sans-serif" font-size="11" fill="#FFC857" letter-spacing="2" transform="rotate(25 110 270)">TRADITION IN EVERY BITE</text>

    <!-- Right Box Side (in warm light) -->
    <polygon points="200,220 370,140 370,280 200,360" fill="url(#boxGreen)" stroke="#17452D" stroke-width="4" stroke-linejoin="round" />
    <!-- Right side Gold Seal -->
    <ellipse cx="285" cy="250" rx="36" ry="30" fill="none" stroke="#FFC857" stroke-width="2" stroke-dasharray="4,3" />
    <text x="285" y="246" font-family="'Outfit', sans-serif" font-weight="800" font-size="11" fill="#FFF3D9" text-anchor="middle">100% PURE GHEE</text>
    <text x="285" y="260" font-family="'Outfit', sans-serif" font-weight="600" font-size="9" fill="#FFC857" text-anchor="middle">KERALA RECIPE</text>

    <!-- Golden Ribbon Wrapped Diagonally -->
    <polygon points="120,100 135,107 100,290 85,283" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
    <polygon points="275,98 290,105 320,295 305,288" fill="#FFC857" stroke="#D97706" stroke-width="1.5" />
  </g>
</svg>'''
    with open('assets/illustrations/laddu_box.svg', 'w') as f:
        f.write(svg)
    print('Brand box SVG generated!')

if __name__ == '__main__':
    create_story_svg()
    create_ingredients_svg()
    create_moments_svg()
    create_cta_sunset_svg()
    create_brand_box_svg()
