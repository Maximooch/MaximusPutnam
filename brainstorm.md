# Personal Website Design Brainstorm

## Current: Retro Mac OS (System 7 / Classic Mac)
**Vibe:** Nostalgic, playful, distinctive
**Pros:** Memorable, shows personality, fun to interact with
**Cons:** Can feel gimmicky, mobile UX is awkward, accessibility challenges

---

## Alternative Design Directions

### 1. Terminal / CLI Aesthetic
**Inspiration:** Hacker News, old BBS systems, htop
- Monospace font (JetBrains Mono, Fira Code)
- Green/amber text on dark background
- Blinking cursor, command-line navigation
- `cat about.txt`, `ls projects/`
- **Fits your brand:** You're building dev tools (Penguin). This screams "I live in the terminal."
- **Risk:** Overdone in tech circles

### 2. Brutalist Web Design
**Inspiration:** Craigslist, Bloomberg terminal, early web
- Raw HTML look, minimal styling
- System fonts, harsh borders, no rounded corners
- Dense information, no whitespace worship
- **Fits your brand:** "I ship, I don't polish unnecessarily"
- **Risk:** Can look lazy if not intentional

### 3. Newspaper / Editorial
**Inspiration:** NYT, The Verge, old broadsheets
- Multi-column layouts
- Serif headlines (Playfair Display, Georgia)
- Datelines, bylines, pull quotes
- **Fits your brand:** You write/think about ideas (energy, theology, infra)
- **Risk:** Feels more "writer" than "builder"

### 4. Dashboard / Control Panel
**Inspiration:** Vercel dashboard, Linear, Raycast
- Cards, stats, status indicators
- Real-time elements (GitHub activity, current project status)
- Dark mode default, subtle gradients
- **Fits your brand:** You're building Link (workspace/dashboard product)
- **Risk:** Could look like a SaaS landing page

### 5. Minimalist Single Page
**Inspiration:** https://paco.me, https://leerob.io
- One scrolling page
- Big name, short bio, links
- Maybe 3-4 sections max
- **Fits your brand:** "I'm too busy shipping to build a complex site"
- **Risk:** Forgettable, everyone does this

### 6. 3D / WebGL Experience
**Inspiration:** Bruno Simon's portfolio, Awwwards winners
- Interactive 3D scene (Three.js)
- Navigate a virtual space
- **Fits your brand:** Shows technical chops
- **Risk:** Heavy, slow, accessibility nightmare, maintenance burden

### 7. Notion-Style / Wiki
**Inspiration:** Notion public pages, GitBook
- Clean, readable, toggles and nested content
- Sidebar navigation
- Easy to update (could literally be a Notion embed)
- **Fits your brand:** You're building productivity tools
- **Risk:** Looks like everyone else's "second brain"

### 8. Card-Based / Bento Grid
**Inspiration:** Apple's feature pages, Bento box layouts
- Grid of cards with different sizes
- Each card = one thing (bio, project, link, stat)
- Responsive, works on mobile
- **Fits your brand:** Modern, clean, organized
- **Risk:** Trendy, might age poorly

### 9. Split Screen / Diptych
**Inspiration:** Fashion portfolios, architecture sites
- Two panels: left = navigation/identity, right = content
- Fixed left, scrolling right
- **Fits your brand:** Clean separation of "who" and "what"
- **Risk:** Can feel static

### 10. Hybrid: Retro + Modern
Keep the Mac OS aesthetic but modernize:
- Better mobile experience (stack windows as cards)
- Smoother animations
- Accessibility fixes
- Real content management (headless CMS for posts)
- **Best of both:** Keeps personality, fixes UX issues

---

## Questions to Answer First

1. **Who's the audience?**
   - VCs/angels? → Clean, professional, show traction
   - Engineers you want to hire? → Show technical depth, personality
   - Potential users? → Focus on products, not you
   - General curiosity? → Personality-forward is fine

2. **What action do you want visitors to take?**
   - Email you? → Make contact prominent
   - Check out Penguin/Link? → Hero those projects
   - Read your writing? → Blog-forward design
   - Just know you exist? → Simple is fine

3. **How much maintenance are you willing to do?**
   - Low → Static HTML, minimal updates
   - Medium → Markdown blog with static site generator
   - High → CMS, dynamic content, real-time elements

4. **What impression do you want to leave?**
   - "This person is creative/fun" → Current retro style
   - "This person is serious/competent" → Minimalist/dashboard
   - "This person ships" → Brutalist/terminal
   - "This person thinks deeply" → Editorial/longform

---

## My Take

The **retro Mac OS** is genuinely distinctive—most personal sites are forgettable minimalist pages. It shows personality and technical ability.

**But** if I were advising you as a founder:

1. **Short term:** Keep the retro site, fix mobile UX (stack windows as cards on small screens)
2. **For fundraising:** Have a clean, separate `/invest` or pitch page that's professional
3. **Long term:** Consider the **Dashboard/Control Panel** style—it aligns with what you're building (Link) and signals "I build tools like this"

The current site says "I'm interesting." A dashboard site would say "I build interesting things."

Both are valid. Depends on what you're optimizing for.

---

## Quick Wins for Current Site

If you stick with retro Mac:
- [ ] Add touch support for window dragging (or disable on mobile)
- [ ] Stack windows vertically on mobile as a fallback
- [ ] Add favicon (pixelated Mac icon?)
- [ ] Add OG image for social sharing
- [ ] External posts to `/posts/index.json` for easier updates
- [ ] Add a "Download Resume" file in Finder
- [ ] Easter egg: Konami code opens a hidden window?
