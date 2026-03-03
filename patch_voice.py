import os

# gen_head edits
with open('gen_head.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '"tldr": "The Sony WH-1000XM5 remains our top recommendation for most professionals, offering the best blend of precise noise cancellation, comfort, and unmatched call quality, making it indispensable for remote work. If you prioritize maximum comfort during long flights, the Bose QuietComfort Ultra is your immediate runner-up.",',
    '"tldr": "If you commute, work in an open office, or regularly take Zoom calls, the Sony WH-1000XM5 is the absolute best noise-cancelling headphone available. If your primary use case is 12-hour flights and clamping force triggers headaches, choose the Bose QuietComfortUltra instead.",'
)

text = text.replace(
    '"why_matters": "Active Noise Cancellation has moved from a luxury travel feature to a strict necessity for remote and hybrid workers. The ability to instantly fabricate a quiet environment in a coffee shop, an open-plan office, or a noisy living room is invaluable for maintaining deep focus. Beyond just drowning out distractions, a quality pair of ANC headphones protects your hearing by allowing you to listen to audio at lower volumes. The modern iterations employ computational audio and multi-microphone arrays to map soundscapes in real-time. In this pillar guide, we will break down exactly which flagship model fits your specific workflow." * 2,',
    '"why_matters": "Active Noise Cancellation (ANC) separates productive deep work from cognitive overload. Modern multi-microphone arrays don\'t just dampen sound—computational audio maps and inverts your environment in real-time. Whether you need aggressive low-frequency rejection for trans-atlantic travel or precise voice isolation for remote meetings, the hardware differences between leading chipsets dictate your workflow. We evaluate these models based on ANC attenuation curves, long-term clamping force, and dual-device multipoint execution." * 2,'
)

text = text.replace(
    '"final_verdict": "For 2026, the market is highly competitive, but the Sony WH-1000XM5 holds the crown for the best all-around feature set. The Bose QuietComfort Ultra remains the champion of pure physical comfort." * 2',
    '"final_verdict": "The Sony WH-1000XM5 is the definitive choice for remote workers and multipoint desktop users. Buy the Bose QuietComfort Ultra only if physical clamping force is your primary bottleneck or you exclusively use the Apple ecosystem." * 2'
)

with open('gen_head.py', 'w', encoding='utf-8') as f:
    f.write(text)

# gen_mic edits
with open('gen_mic.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '"tldr": "The Shure SM7dB is the ultimate choice for high-end podcasting and voice-over work, offering the legendary warm tone of the original with a built-in preamp to ensure you get professional, low-noise gain without needing extra external hardware. If you already own high-quality outboard gear, the classic Shure SM7B remains the king of the purist setup.",',
    '"tldr": "If you are building a new podcast studio from scratch, the Shure SM7dB is the exact microphone you should buy. The integrated preamp eliminates the complex gain staging required by vintage gear. If you already own a high-end audio interface and Cloudlifter, stick with the classic Shure SM7B.",'
)

text = text.replace(
    '"why_matters": "In the world of content creation and professional communication, extreme audio parity is expected. Listeners will forgive subpar video quality, but bad audio will cause immediate drop-offs. A high-quality podcast microphone not only makes your voice sound rich, warm, and authoritative, but a dynamic microphone actively fights against the harsh realities of untreated rooms. Whether a dog is barking outside or your computer fan spins up, a proper dynamic mic rejects that interference. This category pillar breaks down exactly how to achieve industry-standard audio." * 2,',
    '"why_matters": "Broadcast audio isn\'t just about sounding warm—it is about signal chain control and off-axis noise rejection. Using a highly sensitive condenser microphone in an untreated bedroom guarantees you will capture echo, keyboard clicks, and traffic. Dynamic microphones solve this. By mastering gain staging and selecting the right preamp integration, you can immediately achieve the rigid audio parity expected in professional podcasting." * 2,'
)

text = text.replace(
    '"how_choose": "<p>Choosing between XLR, USB, Dynamic, and Condenser microphones can be daunting. The cardinal rule for home podcasters is to favor Dynamic microphones over Condensers. Condensers are too sensitive for untreated, echoey bedrooms. The next step is deciding your ecosystem: XLR requires an audio interface (like a Focusrite Scarlett) giving you hardware control and upgrade paths. USB is plug-and-play simplicity. The Shure SM7dB combines the best of dynamic sound rejection with easier drive requirements.</p>" * 3,',
    '"how_choose": "<p>Choosing between XLR, USB, Dynamic, and Condenser microphones can be daunting. The cardinal rule for home podcasters is to favor Dynamic microphones over Condensers. Condensers are too sensitive for untreated, echoey bedrooms. The next step is deciding your ecosystem: XLR requires an audio interface (like a Focusrite Scarlett) giving you hardware control and upgrade paths. USB is plug-and-play simplicity. The Shure SM7dB combines the best of dynamic sound rejection with easier drive requirements.</p>" * 3 + "<div style=\'padding: 1.5rem; border-left: 4px solid #ff4b2b; background: rgba(255,75,43,0.05); margin: 2rem 0; border-radius: 4px;\'><h3 style=\'color: #ff4b2b; margin-top:0;\'>Common Mistakes</h3><p><strong>Buying a Condenser Mic for a Bedroom:</strong> Condensers pick up everything. Stick to Dynamic.<br><br><strong>Ignoring the Boom Arm:</strong> Desk stands transmit keyboard vibrations straight into the capsule. You need an isolated arm.</p></div>",'
)

text = text.replace(
    '"final_verdict": "The microphone you choose sets the foundation of your show\'s brand. The Shure SM7dB removes the traditional hurdles of the SM7B ecosystem by integrating the preamp, making it our definitive recommendation for 2026." * 2',
    '"final_verdict": "The Shure SM7dB fundamentally solves the gain shortage that plagued home studio builders for the last decade. It is the only broadcast dynamic mic you will ever need." * 2'
)

with open('gen_mic.py', 'w', encoding='utf-8') as f:
    f.write(text)

# gen_mon edits
with open('gen_mon.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '"tldr": "The Alienware AW3423DWF offers an unmatched combination of QD-OLED vibrancy, a reasonable price tag, and an incredible three-year burn-in warranty. It remains our definitive premium pick for anyone looking to overhaul their display setup. The sleek Samsung Odyssey G8 is a stunning alternative for those prioritizing minimalist aesthetics.",',
    '"tldr": "For creative professionals and gamers, the Alienware AW3423DWF is the superior QD-OLED display thanks to its glossy panel coating and best-in-class burn-in warranty. If you are exclusively coding or managing spreadsheets for 10 hours a day, buy the LG 34GP83A-B to eliminate OLED degradation risks entirely.",'
)

text = text.replace(
    '"why_matters": "Ditching dual-monitor bezels for a singular cinematic ultrawide canvas fundamentally changes how you interact with an operating system. By removing the physical gap between screens, window management becomes fluid. You can snap three vertical windows side-by-side or dedicate the entire 34-inch span to a massive video editing timeline. As we step deeper into peak remote work culture, upgrading your visual real estate provides an immediate, tangible boost to output speed and ergonomic comfort." * 2,',
    '"why_matters": "Upgrading to an ultrawide monitor fundamentally shifts OS taxonomy. Eliminating the center bezel transforms how you manage IDEs, dense spreadsheets, and video timelines. But panel technology dictates longevity. OLED delivers infinite contrast at the risk of static burn-in, while IPS panels offer text clarity and durability for heavy coding. We evaluate these displays strictly based on HDR window performance, text fringing, and true workspace throughput." * 2,'
)

text = text.replace(
    '"final_verdict": "The Alienware AW3423DWF is a masterclass in modern display technology, merging the best of gaming performance with stunning color accuracy for productivity." * 2',
    '"final_verdict": "The Alienware AW3423DWF represents the peak of modern QD-OLED performance. Choose it for contrast-heavy work, but pivot immediately to the LG Nano-IPS if static UI longevity is your critical bottleneck." * 2'
)

with open('gen_mon.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch applied")
