I'm taking this one over completely rather than fixing it in three steps (the skill's "Take over" rule). The page has more than three blockers, and on a phone it fails both the blur test and the thumbnail test: at 390 px the hours and address are off the screen, and nothing on it says "order by Thursday, collect on Saturday". I kept the brief's idea and every must-keep item and rebuilt everything else. You said "direct mode", so I went straight to the fix without waiting for you to approve the critique first.

## Brief
- **Purpose:** get neighbours to pre-order weekend bread [brief]. The page should do one job [brief]: "Order by Thursday, collect on Saturday."
- **Audience and where it's seen:** local people, mostly on phones, often outdoors [brief]. So it needs high contrast in sunlight, large text and big tap targets [inferred].
- **Must keep:** the name Crumb & Co, the pre-order action, opening hours, the address, the brand orange #E8743B, and the three loaves (sourdough, rye, seeded) [brief].
- **Mood:** an early morning at a neighbourhood bakery: warm, floury, unhurried [inferred]. Clean, friendly and finished, not loud [inferred].
- **Done means:** on a phone, someone sees the idea and the pre-order button in the first screen, can order without zooming, and can find the hours and address [inferred].

## Look (original, from the screenshots)
- **Blur:** the purple box and the "Crumb & Co" heading compete. The pre-order action doesn't stand out.
- **Thumbnail:** a rainbow gradient with boxes on it. The Thursday/Saturday idea doesn't come through.
- **Flip:** heavy at the top right on desktop, then a large empty gradient area below the boxes. On the phone the boxes run off the right edge.
- **Greyscale:** the body text in the purple and white boxes almost disappears.
- **Edges:** the boxes are rotated and overlap. The page scrolls sideways at 390 px, and the hours box isn't visible at all.

## Critique of the original (ranked; blockers first)
I measured contrast with WCAG ratios and checked sizes in the source CSS.

1. **UX-1 / UI-15: the main task can't be completed.** *Measured.* "Submit", "Go", "click" and "here" are `<span>`s with no link or form, so nothing happens when you tap them. At 390 px the layout is fixed at `.wrap{width:1250px}` with absolutely positioned boxes, so the page scrolls sideways, the pre-order box is cut off, and the hours/address box (`left:700px`) is entirely off screen. **Fix:** build a real one-column flow with a working pre-order form that sits near the top on a phone.
2. **UI-6: contrast fails almost everywhere.** *Measured.* Pre-order text #5b00c9 on #7a00ff is **1.43:1**. Hours/address #c0c0c0 on white is **1.82:1**. The top nav #ff0 on #0f0 is **1.28:1**. "Submit" #ffcc00 on the brand orange is **1.99:1**. "Go" (white on cyan) is **1.25:1**. The footer text on the gradient is about 1.1–1.3:1. All of these need 4.5:1. **Fix:** use dark ink on a light ground, and dark text on the orange (6.0:1, which is better than white at 3.0:1).
3. **TYPE-3: text is too small.** *Measured.* Footer 9 px, nav 11 px, buttons 12 px, hours/address 13 px, all below the 14 px minimum for reading text, and 9 px is under 12 px. That's worse outdoors. **Fix:** 18 px body text and nothing under 14 px.
4. **UI-10 / LAY-10: the layout breaks at zoom and leaves empty space.** *Measured.* `.wrap{height:520px}` with absolutely positioned boxes can't grow at 200% zoom. At 1280 there's an empty gradient area about 600 px tall under the boxes, far more than any intended gap. **Fix:** let the layout flow and use spacing from one scale (CORE-4).
5. **CORE-1 / UI-4 / CD (the one idea): there's no hierarchy and no single main action.** *Interpreted.* The page uses eight typefaces (Creepster, Pacifico, Bungee, Lobster, Special Elite, Comic Neue, Courier Prime and the serif fallback), five button colours and a scrolling marquee. The Thursday/Saturday idea is buried mid-sentence in the purple box. Also under CORE-8 / UX-6: the vague tagline ("Artisanal Synergy… Carb Journey"), 9 nav links, "Allergens: may contain everything" and "Follow us on 9 platforms" all add noise. **Fix:** make the idea the headline, have one main action, use one type pair, and remove the rest. The trade-off is that the page loses its loud personality, which doesn't fit "neighbours, outdoors, one job" anyway.

**What already works:** the name set large is the right instinct (I kept it, along with the brand orange, now used as a full colour field). The facts are all there: the loaves, hours, address and the Thursday/Saturday deadline.

## What I changed (rule IDs)
- **UX-1, UI-4:** One main action. The hero button goes to a real pre-order form, and "Pre-order for Saturday" submits it. Both use the same dark button style (CORE-9).
- **UI-12 / energy pass:** The one bold design move is the brief's own idea set large: "Order by Thursday. Collect on Saturday." in dark display type on a brand-orange field. It's the lead at thumbnail size, and the button is second.
- **UI-6:** Contrast pairs, all measured: ink on cream 16.8:1, ink on orange 6.0:1, secondary text 7.8:1 (6.7:1 on the hours panel), error red 7.1:1, control borders 7.8:1. Orange is never used as text on cream (2.79:1). Errors show a "!" and a written message, not just a red colour.
- **TYPE-3, CORE-7, TYPE-2:** One type pair: Fraunces for display and Atkinson Hyperlegible for text, chosen for legibility outdoors. Body text is 18 px, the smallest text is 14 px, and there are five sizes.
- **UI-7:** The loaves are a list with − / + steppers, not three identical cards. Controls and panels share one small 6 px radius, and there are no gradients, no emoji and no marquee.
- **UI-5, UX-3, UX-7:** Every field has a visible label. Tap targets are at least 48 px with visible focus. The form shows errors in place and keeps what the person typed: "Choose at least one loaf", plus the name and contact messages. Focus moves to the first problem.
- **UI-15, UI-10, LAY-10:** One column at 390 px, two columns (order and visit) from about 960 px. No horizontal scroll. Checked at 640 px for 200% zoom: nothing is clipped. No empty bands.
- **CORE-8:** Removed the marquee, the nav, the tagline, the gradient, the dashed boxes, the rotation, the joke allergen line and the long legal footer.
- **Kept, with a small addition:** Saturday is marked as "Collection" in the hours. "8am–1pm" comes from your own Saturday hours. "Open in maps" is a plain search for the address you gave.

**Check against the blockers (new version):** contrast passes; nothing meaningful is under 14 px; 200% zoom and 390 px pass; the task completes up to submit; I re-read the copy letter for letter (Crumb & Co; 14 Mill Lane, Hebden Bridge; Mon closed, Tue–Fri 7–3, Sat 8–1, Sun closed; Sourdough, Rye, Seeded); no logo was invented (the name is set in plain text, BRAND-4). I rendered it at 390, 1280 and 640 px (200% zoom), plus the error state. That render used fallback fonts (a Georgia-like serif and a system sans) because my sandbox couldn't load web fonts. The layout holds with either.

## What I left out, and questions for you
1. **Where should orders go?** The form posts to `/pre-order` as a placeholder (marked with a comment). Send me your real endpoint, email or order service. Until it's connected, orders won't be received.
2. **Thursday cut-off time:** is there one (for example "Thursday 5pm")? I didn't invent one.
3. **Hours format:** I wrote "7–3" and "8–1" as 7am–3pm and 8am–1pm. Please confirm.
4. **Phone number:** "01422 000000" looks like a placeholder, so I left it out. Send the real number and I'll add it as a tap-to-call link.
5. **Prices, allergens, privacy:** none were given, so none are shown. The form collects names and contact details, so you'll probably need a privacy link. Send the URL. A real allergen note would help too.
6. **Removed pages** (Blog, Careers, FAQ, Login, Cart, Est. 2019): "Est. 2019" is now in the footer. Tell me if any of the others need to stay on this landing page.

## Improved HTML

```html
<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Crumb &amp; Co · Weekend bread pre-orders</title>
<meta name="description" content="Pre-order sourdough, rye or seeded bread by Thursday and collect it on Saturday from Crumb &amp; Co, 14 Mill Lane, Hebden Bridge.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">
<style>
  /* Mood: early morning at a neighbourhood bakery - warm, floury, unhurried.
     Tokens: one accent (brand orange) used as a field, never as text on cream (2.79:1). */
  :root{
    --orange:#E8743B;      /* brand: hero field + small markers */
    --ink:#1F140C;         /* text; 16.8:1 on cream, 6.0:1 on orange */
    --ink-soft:#5C4A3D;    /* secondary text; 7.8:1 on cream */
    --cream:#FBF6EF;       /* page ground */
    --flour:#F6E3D3;       /* raised panels; ink 14.5:1 */
    --line:#5C4A3D;        /* input/control borders, 7.8:1 */
    --error:#A3200F;
    --radius:6px;
    --s1:4px; --s2:8px; --s3:16px; --s4:24px; --s5:32px; --s6:48px; --s7:64px;
    --display:"Fraunces", Georgia, "Times New Roman", serif;
    --text:"Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  *,*::before,*::after{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--text);font-size:1.125rem;line-height:1.45}
  a{color:inherit}
  :focus-visible{outline:3px solid var(--ink);outline-offset:3px}
  .hero :focus-visible{outline-color:var(--ink)}
  .wrap{max-width:72rem;margin:0 auto;padding:0 var(--s3)}
  @media (min-width:48rem){.wrap{padding:0 var(--s5)}}

  /* Header: the name in plain text (no logo file supplied) */
  .site-head{background:var(--orange)}
  .site-head .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--s2) var(--s4);padding-top:var(--s3);padding-bottom:var(--s3)}
  .name{font-family:var(--display);font-weight:800;font-size:1.75rem;line-height:1.1;margin:0;letter-spacing:-0.01em}
  .head-link{font-weight:700;font-size:1rem;text-underline-offset:3px;padding:var(--s2) 0}

  /* Hero: the one idea, set large on the brand orange */
  .hero{background:var(--orange);padding:var(--s4) 0 var(--s6)}
  @media (min-width:48rem){.hero{padding:var(--s6) 0 var(--s7)}}
  .eyebrow{font-weight:700;font-size:1rem;letter-spacing:.08em;text-transform:uppercase;margin:0 0 var(--s3)}
  .idea{font-family:var(--display);font-weight:800;font-size:clamp(2.75rem,7.5vw,5.75rem);line-height:1;letter-spacing:-0.02em;margin:0 0 var(--s4)}
  .idea span{display:block}
  .lede{font-size:1.25rem;max-width:34ch;margin:0 0 var(--s5)}

  .btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--s2);min-height:3.25rem;padding:var(--s3) var(--s5);
       background:var(--ink);color:var(--cream);border:2px solid var(--ink);border-radius:var(--radius);
       font:700 1.125rem/1.2 var(--text);text-decoration:none;cursor:pointer}
  .btn:hover{background:#3a2a1e;border-color:#3a2a1e}
  .btn:active{transform:translateY(1px)}
  .btn[aria-disabled="true"]{opacity:.6;cursor:not-allowed}

  /* Main: order (left) + visit (right) */
  main .wrap{display:grid;gap:var(--s6);padding-top:var(--s6);padding-bottom:var(--s6)}
  @media (min-width:60rem){main .wrap{grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:var(--s6)}}
  h2{font-family:var(--display);font-weight:800;font-size:2rem;line-height:1.1;margin:0 0 var(--s2)}
  .sub{color:var(--ink-soft);margin:0 0 var(--s4)}

  /* Loaves as a list with steppers, not three cards */
  fieldset{border:0;margin:0 0 var(--s4);padding:0;min-width:0}
  legend{font-weight:700;font-size:1.125rem;margin-bottom:var(--s2);padding:0}
  .loaves{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
  .loaf{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--s2) var(--s3);padding:var(--s3) 0;border-bottom:1px solid var(--line)}
  .loaf-name{font-family:var(--display);font-weight:600;font-size:1.5rem;line-height:1.2}
  .loaf-name::before{content:"";display:inline-block;width:.6em;height:.6em;border-radius:50%;background:var(--orange);margin-right:.4em;vertical-align:.08em}
  .stepper{display:flex;align-items:center;gap:var(--s2)}
  .step{width:3rem;height:3rem;border:2px solid var(--line);background:var(--cream);color:var(--ink);border-radius:var(--radius);font:700 1.5rem/1 var(--text);cursor:pointer}
  .step:hover{background:var(--flour)}
  .qty{width:3.5rem;height:3rem;text-align:center;border:2px solid var(--line);border-radius:var(--radius);background:#fff;color:var(--ink);font:700 1.25rem var(--text);-moz-appearance:textfield}
  .qty::-webkit-inner-spin-button,.qty::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}

  .field{margin:0 0 var(--s3)}
  .field label{display:block;font-weight:700;margin-bottom:var(--s1)}
  .field input{width:100%;min-height:3rem;padding:var(--s2) var(--s3);border:2px solid var(--line);border-radius:var(--radius);background:#fff;color:var(--ink);font:1.125rem var(--text)}
  .field input[aria-invalid="true"]{border-color:var(--error)}
  .msg{color:var(--error);font-weight:700;margin:var(--s1) 0 0;min-height:0}
  .msg:empty{display:none}
  .msg::before{content:"! ";}
  .form-msg{margin:0 0 var(--s3)}
  .note{color:var(--ink-soft);font-size:1rem;margin:var(--s3) 0 0}

  /* Visit panel */
  .visit{background:var(--flour);border-radius:var(--radius);padding:var(--s4);align-self:start}
  @media (min-width:48rem){.visit{padding:var(--s5)}}
  .addr{font-style:normal;font-size:1.25rem;font-weight:700;margin:0 0 var(--s2)}
  .map{display:inline-block;font-weight:700;text-underline-offset:3px;padding:var(--s2) 0;margin-bottom:var(--s4)}
  h3{font-weight:700;font-size:1.125rem;margin:0 0 var(--s2)}
  .hours{width:100%;border-collapse:collapse}
  .hours th,.hours td{text-align:left;padding:var(--s2) 0;border-bottom:1px solid rgba(31,20,12,.25);font-weight:400}
  .hours td{text-align:right}
  .hours .closed{color:var(--ink-soft)}
  .hours tr.collect th,.hours tr.collect td{font-weight:700}
  .tag{display:inline-block;margin-left:var(--s2);padding:0 var(--s2);background:var(--orange);color:var(--ink);border-radius:999px;font-size:.875rem;font-weight:700;vertical-align:.1em}

  footer{border-top:1px solid rgba(31,20,12,.25)}
  footer .wrap{padding-top:var(--s4);padding-bottom:var(--s5);color:var(--ink-soft);font-size:1rem}

  @media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
  html{scroll-behavior:smooth}
</style>
</head>
<body>

<header class="site-head">
  <div class="wrap">
    <p class="name">Crumb &amp; Co</p>
    <a class="head-link" href="#visit">Hours &amp; address</a>
  </div>
</header>

<section class="hero" aria-labelledby="idea">
  <div class="wrap">
    <p class="eyebrow">Weekend bread</p>
    <h1 class="idea" id="idea"><span>Order by Thursday.</span> <span>Collect on Saturday.</span></h1>
    <p class="lede">Sourdough, rye and seeded loaves, put aside for you at the shop on Saturday morning.</p>
    <a class="btn" href="#order">Pre-order your bread</a>
  </div>
</section>

<main>
  <div class="wrap">

    <section id="order" aria-labelledby="order-h">
      <h2 id="order-h">Pre-order</h2>
      <p class="sub">Order by Thursday, collect on Saturday, 8am–1pm.</p>

      <!-- REPLACE action with your real pre-order endpoint -->
      <form id="preorder" action="/pre-order" method="post" novalidate>
        <p class="msg form-msg" id="form-msg" role="alert" aria-live="assertive"></p>

        <fieldset aria-describedby="loaf-msg">
          <legend>How many loaves?</legend>
          <ul class="loaves">
            <li class="loaf">
              <label class="loaf-name" for="q-sourdough">Sourdough</label>
              <div class="stepper">
                <button type="button" class="step" data-step="-1" aria-label="One fewer sourdough" aria-controls="q-sourdough">−</button>
                <input class="qty" id="q-sourdough" name="sourdough" type="number" inputmode="numeric" min="0" max="20" value="0">
                <button type="button" class="step" data-step="1" aria-label="One more sourdough" aria-controls="q-sourdough">+</button>
              </div>
            </li>
            <li class="loaf">
              <label class="loaf-name" for="q-rye">Rye</label>
              <div class="stepper">
                <button type="button" class="step" data-step="-1" aria-label="One fewer rye" aria-controls="q-rye">−</button>
                <input class="qty" id="q-rye" name="rye" type="number" inputmode="numeric" min="0" max="20" value="0">
                <button type="button" class="step" data-step="1" aria-label="One more rye" aria-controls="q-rye">+</button>
              </div>
            </li>
            <li class="loaf">
              <label class="loaf-name" for="q-seeded">Seeded</label>
              <div class="stepper">
                <button type="button" class="step" data-step="-1" aria-label="One fewer seeded" aria-controls="q-seeded">−</button>
                <input class="qty" id="q-seeded" name="seeded" type="number" inputmode="numeric" min="0" max="20" value="0">
                <button type="button" class="step" data-step="1" aria-label="One more seeded" aria-controls="q-seeded">+</button>
              </div>
            </li>
          </ul>
          <p class="msg" id="loaf-msg"></p>
        </fieldset>

        <div class="field">
          <label for="name">Your name</label>
          <input id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-msg">
          <p class="msg" id="name-msg"></p>
        </div>
        <div class="field">
          <label for="contact">Phone or email</label>
          <input id="contact" name="contact" type="text" autocomplete="email" required aria-describedby="contact-msg">
          <p class="msg" id="contact-msg"></p>
        </div>

        <button class="btn" type="submit">Pre-order for Saturday</button>
      </form>
    </section>

    <aside id="visit" class="visit" aria-labelledby="visit-h">
      <h2 id="visit-h">Collect from the shop</h2>
      <address class="addr">14 Mill Lane, Hebden Bridge</address>
      <a class="map" href="https://www.google.com/maps/search/?api=1&amp;query=14+Mill+Lane+Hebden+Bridge">Open in maps</a>

      <h3>Opening hours</h3>
      <table class="hours">
        <tbody>
          <tr class="closed"><th scope="row">Monday</th><td>Closed</td></tr>
          <tr><th scope="row">Tuesday – Friday</th><td>7am – 3pm</td></tr>
          <tr class="collect"><th scope="row">Saturday <span class="tag">Collection</span></th><td>8am – 1pm</td></tr>
          <tr class="closed"><th scope="row">Sunday</th><td>Closed</td></tr>
        </tbody>
      </table>
    </aside>

  </div>
</main>

<footer>
  <div class="wrap">© Crumb &amp; Co · Est. 2019</div>
</footer>

<script>
(function(){
  var form=document.getElementById('preorder');
  var qtys=[].slice.call(form.querySelectorAll('.qty'));

  form.addEventListener('click',function(e){
    var b=e.target.closest('.step'); if(!b) return;
    var input=document.getElementById(b.getAttribute('aria-controls'));
    var v=(parseInt(input.value,10)||0)+parseInt(b.dataset.step,10);
    input.value=Math.max(0,Math.min(20,v));
    setMsg('loaf-msg','');
  });

  function setMsg(id,text,input){
    document.getElementById(id).textContent=text;
    if(input) input.setAttribute('aria-invalid',text?'true':'false');
  }

  form.addEventListener('submit',function(e){
    var ok=true, first=null;
    var total=qtys.reduce(function(s,i){return s+(parseInt(i.value,10)||0)},0);
    if(total<1){ok=false;first=first||qtys[0];setMsg('loaf-msg','Choose at least one loaf.');} else setMsg('loaf-msg','');

    var name=document.getElementById('name');
    if(!name.value.trim()){ok=false;first=first||name;setMsg('name-msg','Add your name so we can label your bread.',name);} else setMsg('name-msg','',name);

    var c=document.getElementById('contact');
    if(!c.value.trim()){ok=false;first=first||c;setMsg('contact-msg','Add a phone number or email.',c);} else setMsg('contact-msg','',c);

    if(!ok){
      e.preventDefault();
      setMsg('form-msg','Please check the items marked below.');
      first.focus();
    } else setMsg('form-msg','');
  });
})();
</script>
</body>
</html>
```
