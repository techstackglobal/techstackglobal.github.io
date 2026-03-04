import re

html_block = """      <!-- Pull-Out Animated Deck -->
      <div class="hero-visual">
        <style>
          .deck-container {
            position: relative;
            width: 100%;
            max-width: 400px;
            height: 520px;
            margin: 0 auto;
            perspective: 1200px;
            transform-style: preserve-3d;
          }
          .deck-card {
            position: absolute;
            top: 0; left: 0; right: 0;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-glass);
            border-top: 4px solid var(--accent);
            border-radius: var(--border-radius);
            padding: 2rem;
            height: 480px;
            display: flex;
            flex-direction: column;
            cursor: grab;
            user-select: none;
            will-change: transform, opacity;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            /* Smooth transitions when dropping or clicking next */
            transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.4s linear;
          }
          .deck-card:active {
            cursor: grabbing;
          }
          .deck-card img {
            width: 100%; height: auto; border-radius: 8px; margin-bottom: 1rem; aspect-ratio: 16/9; object-fit: cover; pointer-events: none;
          }
          .deck-card h3 { font-size: 1.4rem; margin-bottom: 0.5rem; line-height: 1.3; color: white; }
          .deck-card p { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.5; pointer-events: none; flex-grow: 1; }
          
          /* The pull indicator */
          .pull-indicator {
            position: absolute; top: -30px; right: 10px; font-size: 0.85rem; color: var(--accent); opacity: 0;
            font-weight: 600; text-transform: uppercase; letter-spacing: 1px; z-index: 10;
            animation: bounceX 2s infinite ease-in-out;
            pointer-events: none;
          }
          @keyframes bounceX {
            0%, 100% { transform: translateX(0); opacity: 0.8;}
            50% { transform: translateX(-10px); opacity: 0.4;}
          }
          
          /* Deck states based on data-depth attributes controlled by JS */
          .deck-card[data-depth="0"] { transform: translateZ(0) translateY(0) scale(1); z-index: 3; opacity: 1; }
          .deck-card[data-depth="1"] { transform: translateZ(-80px) translateY(25px) scale(0.95); z-index: 2; opacity: 0.8; }
          .deck-card[data-depth="2"] { transform: translateZ(-160px) translateY(50px) scale(0.9); z-index: 1; opacity: 0.4; }
          
          /* Thrown away states */
          .deck-card.throw-left { transform: translateZ(0) translateX(-150%) rotate(-15deg) !important; opacity: 0 !important; }
          .deck-card.throw-right { transform: translateZ(0) translateX(150%) rotate(15deg) !important; opacity: 0 !important; }

          /* Controls */
          .deck-controls {
            display: flex; justify-content: space-between; align-items: center; max-width: 400px; margin: 0 auto; position: relative; z-index: 10;
          }
          .deck-controls button {
            background: rgba(255,255,255,0.05); border: 1px solid var(--border-glass); color: white; width: 45px; height: 45px; border-radius: 50%; cursor: pointer; transition: 0.2s; display: flex; align-items: center; justify-content: center;
          }
          .deck-controls button:hover { background: var(--accent); color: #000; }
          .deck-controls button i { font-size: 1.1rem; }
        </style>

        <div class="deck-container" id="reviewDeck">
          <!-- The indicator shows up to hint users to swipe -->
          <div class="pull-indicator" id="pullHint">&larr; Pull to next</div>

          <!-- Card 0: Sony -->
          <div class="deck-card" data-index="0">
            <div style="font-size: 0.75rem; color: var(--accent); font-weight: bold; text-transform: uppercase; margin-bottom: 0.5rem;">
              <i class="fa-solid fa-headphones"></i> Audio
            </div>
            <img src="posts/images/sony-wh-1000xm5-front.jpg" alt="Sony WH-1000XM5" loading="lazy">
            <h3>Sony WH-1000XM5</h3>
            <p>Top-tier active noise cancellation and supreme all-day comfort for deep focus sessions.</p>
            <a class="read-more" href="posts/sony-wh-1000xm5-review.html" style="font-weight: 700; display:inline-block; margin-top: auto;">Read Review <i class="fa-solid fa-arrow-right" style="margin-left: 5px;"></i></a>
          </div>

          <!-- Card 1: Shure -->
          <div class="deck-card" data-index="1">
            <div style="font-size: 0.75rem; color: var(--accent); font-weight: bold; text-transform: uppercase; margin-bottom: 0.5rem;">
              <i class="fa-solid fa-microphone"></i> Broadcasting
            </div>
            <img src="posts/images/shure-sm7db-primary.jpg" alt="Shure SM7dB Microphone" loading="lazy">
            <h3>Shure SM7dB</h3>
            <p>The industry standard podcast microphone, now powered with a built-in clean preamp.</p>
            <a class="read-more" href="posts/shure-sm7db-review.html" style="font-weight: 700; display:inline-block; margin-top: auto;">Read Review <i class="fa-solid fa-arrow-right" style="margin-left: 5px;"></i></a>
          </div>

          <!-- Card 2: Alienware -->
          <div class="deck-card" data-index="2">
            <div style="font-size: 0.75rem; color: var(--accent); font-weight: bold; text-transform: uppercase; margin-bottom: 0.5rem;">
              <i class="fa-solid fa-desktop"></i> Displays
            </div>
            <img src="posts/images/alienware-aw3423dwf-front.jpg" alt="Alienware AW3423DWF" loading="lazy">
            <h3>Alienware AW3423DWF</h3>
            <p>Stunning QD-OLED ultrawide performance delivering flawless visual immersion.</p>
            <a class="read-more" href="posts/alienware-aw3423dwf-review.html" style="font-weight: 700; display:inline-block; margin-top: auto;">Read Review <i class="fa-solid fa-arrow-right" style="margin-left: 5px;"></i></a>
          </div>
        </div>
        
        <div class="deck-controls">
          <button id="deckPrev" aria-label="Previous Review"><i class="fa-solid fa-arrow-left"></i></button>
          <span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 600; letter-spacing: 1px;" id="deckCount">1 / 3</span>
          <button id="deckNext" aria-label="Next Review"><i class="fa-solid fa-arrow-right"></i></button>
        </div>

        <script>
          document.addEventListener('DOMContentLoaded', () => {
            const deck = document.getElementById('reviewDeck');
            if(!deck) return;
            
            const cards = Array.from(deck.querySelectorAll('.deck-card'));
            const prevBtn = document.getElementById('deckPrev');
            const nextBtn = document.getElementById('deckNext');
            const countEl = document.getElementById('deckCount');
            const hint = document.getElementById('pullHint');
            
            let topIndex = 0; 
            const total = cards.length;

            function updateDeck() {
              cards.forEach((card, i) => {
                 card.classList.remove('throw-left', 'throw-right');
                 card.style.transition = ''; // reset to CSS transition
                 card.style.transform = ''; // clears inline drag transforms
                 
                 // Distance from current top card
                 let depth = (i - topIndex + total) % total;
                 card.setAttribute('data-depth', depth.toString());
              });
              countEl.textContent = `${topIndex + 1} / ${total}`;
            }

            function throwCard(direction) {
              const currentTopCard = cards[topIndex];
              // Apply the throw animation class
              currentTopCard.classList.add(direction === 'left' ? 'throw-left' : 'throw-right');
              
              // Hide hint after first interaction
              if(hint) hint.style.display = 'none';

              // Wait enough time for the throw animation to clear visually before re-stacking
              setTimeout(() => {
                 if(direction === 'left' || direction === 'next') {
                    topIndex = (topIndex + 1) % total;
                 } else {
                    topIndex = (topIndex - 1 + total) % total;
                 }
                 updateDeck();
              }, 300); // 300ms matches CSS transition timing
            }

            nextBtn.addEventListener('click', () => throwCard('left'));
            prevBtn.addEventListener('click', () => throwCard('right'));

            // Mouse / Touch Drag Support
            let isDragging = false;
            let startX = 0;
            let currentX = 0;

            function onStart(x, y, target) {
              // Ignore clicks on links/buttons
              if(target.closest('a') || target.closest('button')) return;
              isDragging = true;
              startX = x;
              currentX = x;
              // Remove transition visually to make dragging instantaneous
              cards[topIndex].style.transition = 'none';
              
              if(hint) hint.style.display = 'none';
            }

            function onMove(x) {
              if(!isDragging) return;
              currentX = x;
              const diffX = currentX - startX;
              const rotate = diffX * 0.05; 
              // Instantly update transform
              cards[topIndex].style.transform = `translateZ(0) translateY(0) translateX(${diffX}px) rotate(${rotate}deg)`;
            }

            function onEnd() {
              if(!isDragging) return;
              isDragging = false;
              const diffX = currentX - startX;
              
              if(Math.abs(diffX) > 80) { // threshold passed
                 throwCard(diffX < 0 ? 'left' : 'right');
              } else {
                 // return to center smoothly
                 updateDeck(); 
              }
            }

            deck.addEventListener('mousedown', (e) => onStart(e.clientX, e.clientY, e.target));
            window.addEventListener('mousemove', (e) => onMove(e.clientX));
            window.addEventListener('mouseup', onEnd);
            
            deck.addEventListener('touchstart', (e) => onStart(e.touches[0].clientX, e.touches[0].clientY, e.target), {passive: false});
            deck.addEventListener('touchmove', (e) => {
                if(isDragging) { e.preventDefault(); onMove(e.touches[0].clientX); }
            }, {passive: false});
            deck.addEventListener('touchend', onEnd);

            // Init
            updateDeck();
            
            // Show hint briefly on load
            setTimeout(() => { if(hint) hint.style.opacity = '1'; }, 1500);
          });
        </script>
      </div>"""

import os
base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
idx = os.path.join(base, "index.html")

with open(idx, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the slider block
new_text = re.sub(
    r'<!-- Hero Featured Products Carousel -->.*?</div>\s*</div>\s*</section>',
    html_block + "\n    </section>",
    text,
    flags=re.DOTALL
)

with open(idx, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated index.html to animated deck!")
