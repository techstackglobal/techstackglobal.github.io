import re, os
html_block = """      <!-- Feature Review Animated Cards -->
      <div class="hero-visual" style="position: relative;">
        <!-- Swiper integration -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
        <style>
          .hero-swiper-shell {
            position: relative;
            max-width: 440px;
            margin: 0 auto;
            display: flex;
            align-items: center;
          }
          .swiper-card-effect {
            width: 100%;
            max-width: 340px;
            height: 480px;
            padding: 30px 0;
            overflow: visible;
          }
          .swiper-card-effect .swiper-slide {
            display: flex;
            flex-direction: column;
            border-radius: var(--border-radius, 12px);
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-glass, rgba(255,255,255,0.1));
            border-top: 4px solid var(--accent, #38bdf8);
            box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5);
            padding: 2rem;
            cursor: grab;
            box-sizing: border-box;
          }
          .swiper-card-effect .swiper-slide:active {
            cursor: grabbing;
          }
          .swiper-card-effect .swiper-slide img {
            width: 100%;
            height: 200px;
            object-fit: contain;
            border-radius: 8px;
            background: #ffffff;
            padding: 0.5rem;
            margin-bottom: 1rem;
            pointer-events: none;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
          }
          .swiper-card-effect .swiper-slide h3 {
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
            line-height: 1.3;
            color: #fff;
          }
          .swiper-card-effect .swiper-slide p {
            color: var(--text-secondary, #94a3b8);
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: auto;
          }
          
          /* Custom Navigation Styles floating outside the slides */
          .swiper-btn-next, .swiper-btn-prev {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 48px;
            height: 48px;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass, rgba(255,255,255,0.1));
            border-radius: 50%;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            transition: 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 10;
          }
          .swiper-btn-prev { left: -15px; }
          .swiper-btn-next { right: -15px; }

          .swiper-btn-next:hover, .swiper-btn-prev:hover {
            background: var(--accent, #38bdf8);
            color: #000;
            transform: translateY(-50%) scale(1.1);
          }
          .swiper-button-disabled {
            opacity: 0.35;
            cursor: auto;
            pointer-events: none;
          }
          
          /* Mobile Responsiveness */
          @media (max-width: 767px) {
            .swiper-card-effect {
              height: 380px; 
              max-width: 280px; 
              padding: 20px 0;
            }
            .swiper-card-effect .swiper-slide {
              padding: 1.25rem;
            }
            .swiper-card-effect .swiper-slide h3 {
              font-size: 1.2rem;
            }
            .swiper-card-effect .swiper-slide p {
              font-size: 0.85rem;
              margin-bottom: 0.5rem;
            }
            .swiper-card-effect .swiper-slide img {
              height: 130px;
              margin-bottom: 0.75rem;
            }
            /* Hide floating arrows on mobile for a swipe-only interface */
            .swiper-btn-next, .swiper-btn-prev {
                display: none;
            }
          }
        </style>

        <div class="hero-swiper-shell">
          <!-- External Prev Arrow -->
          <div class="swiper-btn-prev"><i class="fa-solid fa-arrow-left"></i></div>
          
          <div class="swiper swiper-card-effect">
            <div class="swiper-wrapper">
              <!-- Card 0: Sony -->
              <div class="swiper-slide">
                <div style="font-size: 0.75rem; color: var(--accent); font-weight: bold; text-transform: uppercase; margin-bottom: 0.5rem;">
                  <i class="fa-solid fa-headphones"></i> Audio
                </div>
                <img src="posts/images/sony-wh-1000xm5-front.jpg" alt="Sony WH-1000XM5" loading="lazy">
                <h3>Sony WH-1000XM5</h3>
                <p>Top-tier active noise cancellation and supreme all-day comfort for deep focus sessions.</p>
                <a class="read-more" href="posts/sony-wh-1000xm5-review.html" style="font-weight: 700; display:inline-block; margin-top: 1rem;">Read Review <i class="fa-solid fa-arrow-right" style="margin-left: 5px;"></i></a>
              </div>

              <!-- Card 1: Shure -->
              <div class="swiper-slide">
                <div style="font-size: 0.75rem; color: var(--accent); font-weight: bold; text-transform: uppercase; margin-bottom: 0.5rem;">
                  <i class="fa-solid fa-microphone"></i> Broadcasting
                </div>
                <img src="posts/images/shure-sm7db-primary.jpg" alt="Shure SM7dB Microphone" loading="lazy">
                <h3>Shure SM7dB</h3>
                <p>The industry standard podcast microphone, now powered with a built-in clean preamp.</p>
                <a class="read-more" href="posts/shure-sm7db-review.html" style="font-weight: 700; display:inline-block; margin-top: 1rem;">Read Review <i class="fa-solid fa-arrow-right" style="margin-left: 5px;"></i></a>
              </div>

              <!-- Card 2: Alienware -->
              <div class="swiper-slide">
                <div style="font-size: 0.75rem; color: var(--accent); font-weight: bold; text-transform: uppercase; margin-bottom: 0.5rem;">
                  <i class="fa-solid fa-desktop"></i> Displays
                </div>
                <img src="posts/images/alienware-aw3423dwf-front.jpg" alt="Alienware AW3423DWF" loading="lazy">
                <h3>Alienware AW3423DWF</h3>
                <p>Stunning QD-OLED ultrawide performance delivering flawless visual immersion.</p>
                <a class="read-more" href="posts/alienware-aw3423dwf-review.html" style="font-weight: 700; display:inline-block; margin-top: 1rem;">Read Review <i class="fa-solid fa-arrow-right" style="margin-left: 5px;"></i></a>
              </div>
            </div>
          </div>
          
          <!-- External Next Arrow -->
          <div class="swiper-btn-next"><i class="fa-solid fa-arrow-right"></i></div>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
        <script>
          document.addEventListener('DOMContentLoaded', () => {
             const heroSwiper = new Swiper('.swiper-card-effect', {
               effect: 'cards',
               grabCursor: true,
               resistanceRatio: 0.65, // Adds a premium physical "bounce" rubber banding
               cardsEffect: {
                 perSlideOffset: 12,    // How far stacked cards stick out
                 perSlideRotate: 4,     // Subtle tilt when cards are stacked
                 slideShadows: true,    // Realistic shadow casting internally
               },
               navigation: {
                 nextEl: '.swiper-btn-next',
                 prevEl: '.swiper-btn-prev',
               },
             });
          });
        </script>
      </div>"""

base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
idx = os.path.join(base, "index.html")

with open(idx, "r", encoding="utf-8") as f:
    text = f.read()

new_text = re.sub(
    r'<!-- Pull-Out Animated Deck -->.*?</div>\s*</section>',
    html_block + "\n    </section>",
    text,
    flags=re.DOTALL
)

with open(idx, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated index.html to professional Swiper.js cards!")
