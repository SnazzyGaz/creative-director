## Critique

On both screenshots the page looks like a test of how many fonts and colours one screen can hold. The one thing it has to say, "order by Thursday, collect on Saturday", is there, but it's purple text on a purple box in a cursive font, in the middle of a paragraph. On a phone outdoors nobody will find it.

### What's good (keep it)

- **All the required content is already on the page.** The name, the three loaves, the pre-order idea, the hours and the address are all there. Nothing has to be invented, only reorganised.
- **The name "Crumb & Co"** is short, friendly and easy to remember. It deserves to be the first thing people see.
- **The opening hours and address are specific** (Tue–Fri 7–3, Sat 8–1, 14 Mill Lane, Hebden Bridge). That's exactly what a neighbour needs.
- **The orange #E8743B** is a warm, bready colour that suits a bakery. It's only lost because everything else on the page is shouting too.
- **There is a pre-order idea.** The page knows what it's for. It just doesn't say so.

### What must change, most important first

1. **Make "Order by Thursday, collect Saturday" the headline.** Right now it's buried in sentence four of a purple box, written as "Pre orders are possible for weekend bread if you order before the deadline which is thursday…". It should be the biggest, first thing on the screen, as five words.
2. **Give the page one clear, working pre-order action.** There are six buttons ("click", "here", "Submit", "Go"…) and none of them does anything or says what it does. "Submit" is yellow on orange and hard to read. Replace them with one large orange button that says **"Pre-order for Saturday"** and takes people to a short form: loaves, name, phone.
3. **Make the text readable.** Several pieces of text are barely visible, or not at all: purple on purple (b2), light grey #c0c0c0 on white (hours box), yellow on bright green (nav), and the 9 px footer. Outdoors on a phone they disappear completely. Use dark text on light backgrounds, body text of at least 17 px, and only use orange where it passes contrast: dark text on an orange button, never orange text on white.
4. **Fix the phone layout.** The layout uses fixed widths (1250 px, 900 px) and absolutely positioned boxes, so at 390 px the pre-order box runs off the screen and the tagline gets cut off. Most of your audience is on phones, so build for phones first: one column, nothing positioned by hand, no sideways scrolling.
5. **Show the three loaves as things you can order.** "SOURDOUGH!!! RYE!!! SEEDED!!!" is rotated and printed in orange on yellow. Give each loaf a name, a one-line description, and a quantity control right in the order form.
6. **Make the hours and address easy to use.** Put the hours in a simple day-by-day list, make the address a map link and the phone number a tap-to-call link, and say clearly that Saturday collection is 8am–1pm.
7. **Cut everything that isn't part of the job.** Remove the marquee, "WELCOME TO THE WEBSITE", the nine-item nav (BLOG, CAREERS, LOGIN, CART(0), "MORE BREAD"), the jargon tagline ("Artisanal Synergy… Carb Journey"), "Allergens: may contain everything", "Follow us on 9 platforms", and the gradient background. Each of these competes with the one message.
8. **Use one or two typefaces, and make sure they load.** The page names nine fonts (Creepster, Pacifico, Bungee, Lobster…) and loads none of them, so what people actually see depends on their device. Use one bold, friendly display face for headings and one plain face for text.
9. **Tidy the basics.** Add `lang` and a viewport meta tag (without the viewport tag, phones render the page as a zoomed-out desktop page). Replace the `<marquee>` element and use real `<button>`, `<label>` and `<a>` elements so the page works with screen readers and keyboards.

### Things I couldn't decide for you

- **The Thursday cut-off time.** The brief says "by Thursday". I've written "by Thursday" and left a clearly marked spot to add a time (e.g. "by 3pm Thursday", when the shop closes).
- **Prices.** None were given, so I didn't invent any. There's a commented place to add them.
- **Where orders go.** There's no backend, so the form's `action` is a placeholder (`/preorder`). Point it at whatever you use (Formspree, Netlify Forms, your till system, an email service). The phone number also works as a fallback.
- **The phone number** 01422 000000 looks like a placeholder. Swap in the real one.

## Improved page

What I changed:

- The page now runs top to bottom on a phone: the headline and pre-order button, then the loaves with quantities, then a short form, then the hours and address.
- It's a light theme only, on purpose. It's easier to read in sunlight.
- The orange is used for the button and accents, always with dark text on it (about 5.7:1 contrast).
- It uses system fonts, so it loads instantly on mobile data.

```html
<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Crumb &amp; Co — Weekend bread pre-orders</title>
<meta name="description" content="Order your weekend loaf by Thursday, collect it Saturday 8am–1pm at Crumb & Co, 14 Mill Lane, Hebden Bridge.">
<style>
  :root{
    --orange:#E8743B;        /* brand */
    --orange-deep:#B5501F;   /* for orange text/lines on light bg (AA) */
    --ink:#1F1A17;           /* main text: ~16:1 on cream */
    --ink-soft:#4A413B;      /* secondary text: ~9:1 on cream */
    --cream:#FFF8F1;         /* page */
    --card:#FFFFFF;
    --line:#E9DDD2;
    --focus:#1F1A17;
    --radius:14px;
  }
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{
    margin:0;background:var(--cream);color:var(--ink);
    font:400 1.0625rem/1.55 system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  }
  a{color:var(--ink);text-underline-offset:3px}
  a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid var(--focus);outline-offset:3px}
  .wrap{max-width:1040px;margin:0 auto;padding:0 16px}

  /* Header */
  header{padding:18px 0 0}
  .brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.25rem;letter-spacing:-.01em;text-decoration:none}
  .brand-mark{width:28px;height:28px;border-radius:50%;background:var(--orange);flex:none}

  /* Hero */
  .hero{padding:32px 0 36px}
  .eyebrow{margin:0 0 10px;font-weight:700;font-size:.95rem;color:var(--orange-deep);text-transform:uppercase;letter-spacing:.06em}
  h1{
    margin:0 0 14px;font-weight:850;line-height:1.02;letter-spacing:-.025em;
    font-size:clamp(2.6rem,11vw,5rem);
  }
  h1 .then{display:block;color:var(--ink-soft)}
  .lede{margin:0 0 24px;font-size:1.15rem;max-width:34ch;color:var(--ink-soft)}
  .btn{
    display:inline-flex;align-items:center;justify-content:center;gap:8px;
    min-height:56px;padding:14px 26px;border:0;border-radius:999px;
    background:var(--orange);color:var(--ink);
    font:inherit;font-weight:800;font-size:1.125rem;text-decoration:none;cursor:pointer;
    box-shadow:0 2px 0 rgba(31,26,23,.25);
  }
  .btn:hover{background:#EF8550}
  .btn:active{transform:translateY(1px);box-shadow:none}
  .btn-block{width:100%}
  .hero .btn{width:100%;max-width:360px}
  .steps{
    list-style:none;margin:28px 0 0;padding:0;display:grid;gap:10px;
    grid-template-columns:repeat(3,minmax(0,1fr));max-width:560px;
  }
  .steps li{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:12px}
  .steps b{display:block;font-size:1rem}
  .steps span{font-size:.9rem;color:var(--ink-soft)}

  /* Sections */
  section{padding:36px 0;border-top:1px solid var(--line)}
  h2{margin:0 0 6px;font-size:clamp(1.6rem,6vw,2.1rem);line-height:1.1;letter-spacing:-.015em}
  .sub{margin:0 0 20px;color:var(--ink-soft)}

  /* Order form */
  .loaves{display:grid;gap:12px;margin:0 0 20px;padding:0;border:0}
  .loaves legend{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
  .loaf{
    display:grid;grid-template-columns:1fr auto;align-items:center;gap:12px;
    background:var(--card);border:1px solid var(--line);border-left:6px solid var(--orange);
    border-radius:var(--radius);padding:16px;
  }
  .loaf h3{margin:0;font-size:1.2rem}
  .loaf p{margin:2px 0 0;color:var(--ink-soft);font-size:.98rem}
  /* <!-- add price here, e.g. <p class="price">£4.50</p> --> */
  .qty{display:flex;align-items:center;gap:4px}
  .qty button{
    width:44px;height:44px;border-radius:50%;border:2px solid var(--ink);background:var(--card);
    font:inherit;font-size:1.4rem;font-weight:700;line-height:1;cursor:pointer;color:var(--ink);
  }
  .qty input{
    width:48px;height:44px;text-align:center;border:0;background:transparent;
    font:inherit;font-size:1.25rem;font-weight:800;color:var(--ink);
    -moz-appearance:textfield;
  }
  .qty input::-webkit-outer-spin-button,.qty input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}

  .fields{display:grid;gap:14px;margin:0 0 18px}
  .field label{display:block;font-weight:700;margin:0 0 6px}
  .field input{
    width:100%;min-height:52px;padding:12px 14px;border:2px solid #8C7F75;border-radius:10px;
    background:var(--card);font:inherit;font-size:1.0625rem;color:var(--ink);
  }
  .note{margin:12px 0 0;font-size:.95rem;color:var(--ink-soft)}
  .error{margin:0 0 12px;color:#9A2B0B;font-weight:700}
  .error[hidden]{display:none}

  /* Visit */
  .visit{display:grid;gap:16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px}
  .card h3{margin:0 0 10px;font-size:1.15rem}
  .hours{width:100%;border-collapse:collapse}
  .hours th,.hours td{padding:8px 0;border-bottom:1px solid var(--line);text-align:left;font-size:1.05rem}
  .hours th{font-weight:600}
  .hours td{text-align:right}
  .hours tr:last-child th,.hours tr:last-child td{border-bottom:0}
  .hours .closed{color:var(--ink-soft)}
  .hours .sat{font-weight:800}
  .hours .sat td::after{content:" · collection";color:var(--orange-deep);font-weight:700}
  address{font-style:normal;font-size:1.1rem;margin:0 0 12px}
  .links{display:flex;flex-wrap:wrap;gap:10px}
  .link-btn{
    display:inline-flex;align-items:center;min-height:48px;padding:10px 18px;border-radius:999px;
    border:2px solid var(--ink);text-decoration:none;font-weight:700;
  }

  footer{padding:28px 0 40px;border-top:1px solid var(--line);color:var(--ink-soft);font-size:.95rem}

  /* Wider screens */
  @media (min-width:760px){
    .hero{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:end;padding:56px 0}
    .steps{grid-template-columns:1fr;max-width:none;margin:0}
    .order-grid{display:grid;grid-template-columns:1.3fr 1fr;gap:32px;align-items:start}
    .visit{grid-template-columns:1fr 1fr}
  }
  @media (max-width:360px){
    .steps{grid-template-columns:1fr}
  }
  @media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
</head>
<body>

<header>
  <div class="wrap">
    <a class="brand" href="#top"><span class="brand-mark" aria-hidden="true"></span>Crumb &amp; Co</a>
  </div>
</header>

<main id="top">
  <div class="wrap hero">
    <div>
      <p class="eyebrow">Weekend bread · Hebden Bridge</p>
      <h1>Order by Thursday.<span class="then">Collect on Saturday.</span></h1>
      <p class="lede">Sourdough, rye and seeded loaves baked fresh for you and kept behind the counter.</p>
      <a class="btn" href="#order">Pre-order for Saturday</a>
    </div>
    <ol class="steps" aria-label="How it works">
      <li><b>1. Pick your loaves</b><span>Order by Thursday<!-- add cut-off time, e.g. "by 3pm" --></span></li>
      <li><b>2. We bake them</b><span>Fresh on Saturday morning</span></li>
      <li><b>3. Collect</b><span>Saturday 8am–1pm, 14 Mill Lane</span></li>
    </ol>
  </div>

  <section id="order" aria-labelledby="order-h">
    <div class="wrap">
      <h2 id="order-h">Pre-order your weekend bread</h2>
      <p class="sub">Choose how many of each, leave your name and number, and collect on Saturday.</p>

      <!-- Point action at your form handler (Formspree, Netlify Forms, etc.) -->
      <form class="order-grid" action="/preorder" method="post" novalidate>
        <fieldset class="loaves">
          <legend>Loaves</legend>

          <div class="loaf">
            <div>
              <h3 id="l-sour">Sourdough</h3>
              <p>Open crumb, crackly crust. Our everyday loaf.</p>
            </div>
            <div class="qty">
              <button type="button" data-step="-1" aria-label="One fewer sourdough">−</button>
              <input type="number" name="sourdough" value="0" min="0" max="10" inputmode="numeric" aria-labelledby="l-sour">
              <button type="button" data-step="1" aria-label="One more sourdough">+</button>
            </div>
          </div>

          <div class="loaf">
            <div>
              <h3 id="l-rye">Rye</h3>
              <p>Dark, dense and tangy. Keeps for days.</p>
            </div>
            <div class="qty">
              <button type="button" data-step="-1" aria-label="One fewer rye">−</button>
              <input type="number" name="rye" value="0" min="0" max="10" inputmode="numeric" aria-labelledby="l-rye">
              <button type="button" data-step="1" aria-label="One more rye">+</button>
            </div>
          </div>

          <div class="loaf">
            <div>
              <h3 id="l-seed">Seeded</h3>
              <p>Packed with sunflower, pumpkin and linseed.</p>
            </div>
            <div class="qty">
              <button type="button" data-step="-1" aria-label="One fewer seeded">−</button>
              <input type="number" name="seeded" value="0" min="0" max="10" inputmode="numeric" aria-labelledby="l-seed">
              <button type="button" data-step="1" aria-label="One more seeded">+</button>
            </div>
          </div>
        </fieldset>

        <div>
          <div class="fields">
            <div class="field">
              <label for="name">Your name</label>
              <input id="name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="phone">Phone number</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required>
            </div>
          </div>
          <p class="error" id="form-error" role="alert" hidden></p>
          <button class="btn btn-block" type="submit">Pre-order for Saturday</button>
          <p class="note">Order by Thursday. Pay when you collect, Saturday 8am–1pm.<br>
          Prefer to ring? <a href="tel:+441422000000">01422 000000</a></p>
        </div>
      </form>
    </div>
  </section>

  <section aria-labelledby="visit-h">
    <div class="wrap">
      <h2 id="visit-h">Find us</h2>
      <p class="sub">Collection is from the shop counter.</p>
      <div class="visit">
        <div class="card">
          <h3>Opening hours</h3>
          <table class="hours">
            <tbody>
              <tr><th scope="row">Monday</th><td class="closed">Closed</td></tr>
              <tr><th scope="row">Tuesday – Friday</th><td>7am – 3pm</td></tr>
              <tr class="sat"><th scope="row">Saturday</th><td>8am – 1pm</td></tr>
              <tr><th scope="row">Sunday</th><td class="closed">Closed</td></tr>
            </tbody>
          </table>
        </div>
        <div class="card">
          <h3>Address</h3>
          <address>Crumb &amp; Co<br>14 Mill Lane<br>Hebden Bridge</address>
          <div class="links">
            <a class="link-btn" href="https://maps.google.com/?q=14+Mill+Lane,+Hebden+Bridge">Open in Maps</a>
            <a class="link-btn" href="tel:+441422000000">Call 01422 000000</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <p>Crumb &amp; Co · 14 Mill Lane, Hebden Bridge · Baking since 2019</p>
    <p>Ask in the shop for allergen information.</p>
  </div>
</footer>

<script>
  // +/− steppers
  document.querySelectorAll('.qty').forEach(function (q) {
    var input = q.querySelector('input');
    q.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () {
        var v = (parseInt(input.value, 10) || 0) + parseInt(b.dataset.step, 10);
        input.value = Math.max(0, Math.min(10, v));
      });
    });
  });

  // Light validation: at least one loaf, plus name and phone
  document.querySelector('form').addEventListener('submit', function (e) {
    var total = 0;
    this.querySelectorAll('.qty input').forEach(function (i) { total += parseInt(i.value, 10) || 0; });
    var err = document.getElementById('form-error');
    var msg = '';
    if (total < 1) msg = 'Please choose at least one loaf.';
    else if (!this.name.value.trim()) msg = 'Please add your name so we can label your bread.';
    else if (!this.phone.value.trim()) msg = 'Please add a phone number in case we need to reach you.';
    if (msg) { e.preventDefault(); err.textContent = msg; err.hidden = false; }
    else { err.hidden = true; }
  });
</script>
</body>
</html>
```

Before you put it live:

- Check the three loaf descriptions. I wrote them, so make sure they match your actual bread.
- Add the Thursday cut-off time and prices where the comments say.
- Point the form at a real handler.
- Swap in the real phone number.
