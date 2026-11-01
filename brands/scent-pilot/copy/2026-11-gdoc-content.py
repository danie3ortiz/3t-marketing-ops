"""Scent Pilot | November 2026 briefs. Run: python3 <this file> <email 1-13 | 14=Notes> <tabId> [clearEnd]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
from gdoc_brief_builder import *

def tile(name, line, price, btn): return [P('[PRODUCT TILE: ' + name + ' bottle]', 'ph'), P(name, 'b'), P(line), P(price, 'small'), P(btn, 'b')]
def gtile(who, name, line, price, btn): return [P(who, 'small'), P('[PRODUCT TILE: ' + name + ' bottle]', 'ph'), P(name, 'b'), P(line), P(price, 'small'), P(btn, 'b')]
def review(label, quote, who, btn, stars='[STARS] 5/5'): return [P(label, 'b'), P(stars), P('"' + quote + '"', 'i'), P(who, 'small'), P(btn, 'b')]
def step(n, title, line): return [P(n, 'h15'), P(title, 'b'), P(line)]
def faq(q, a): return [P(q, 'b'), P(a)]
def note(label, line): return [P(label, 'b'), P(line)]
L = lambda t, st=None: P(t, st, 'left')
FOOT = [P('Footer', 'small')]
AUTH = [P('AUTHENTICITY GUARANTEED. OR YOUR MONEY BACK.', 'small')]
HOW = [P('How It Works', 'h15'), P('Test it first. Invest only when you love it.'), BL(),
       cards(2, [step('1', 'Pick a fragrance', 'Designer and niche houses, sorted by brand.'),
                 step('2', 'Choose your size', '2ml, 5ml, or 10ml.'),
                 step('3', 'We decant it fresh', 'We freshly decant your order using sterile equipment.'),
                 step('4', 'Wear it, then decide', 'Wear it. Love it. Then decide on the full bottle.')])]
TRUST = [P('Testing Before Investing', 'h15'), BL(),
         cards(2, [note('2ML, 5ML OR 10ML', 'Try a fragrance small before you commit to a full bottle.'),
                   note('AUTHENTIC ORIGINALS', '100% authentic originals. Never dupes, never diluted.'),
                   note('FRESHLY DECANTED', 'Freshly decanted per order. Sterile equipment.'),
                   note('GUARANTEED', 'Authenticity Guaranteed. Or Your Money Back.')])]
def plain(sender): return [P('[PLAIN TEXT: no logo, no images, no buttons. Sent from ' + sender + '. Links in navy #4D6488.]', 'ph')]
LINK = lambda t: ('p', [(t, 'link')], 'left')
SIGN = lambda off: [L(off), L('Hamza'), L('Founder, Scent Pilot')]
VD = 'REMEMBER15'; BF = 'BLACKFRIDAY15'
E = {}
# 1 ---------------------------------------------------------------------------
E[1] = [H2('Campaign | Product Roundup | Cold-Weather Scents Worth Sampling'),
 meta('Campaign | Product Roundup | Cold-Weather Scents Worth Sampling | Designed', 'Mon, Nov 9, 2026', 'Engaged list. Seasonal roundup of four warmer scents to test as decants now the weather is turning. No offer.'),
 subj('Retire The Summer Scent', 'Four warmer picks for cold air, and you can test every one before you buy the bottle.', 'Scent Pilot'), BL(),
 wire([[P('FREE SHIPPING ON ORDERS OVER $50', 'small')],
  [P('Logo'), P('[IMAGE: dark, moody shot of a bottle on a wool scarf or by a frosted window, spotlit like the Sep 22 hero]', 'ph'), P('COLD-WEATHER ROTATION', 'b'), P('THE COLD NEEDS SOMETHING HEAVIER', 'hero'),
   P("The fresh, citrusy bottle that got you through summer goes quiet once the air turns cold. This is the season for vanilla, tobacco, honey and spice. Below are four we'd reach for this month. Test any of them as a decant before you commit to a full bottle."),
   P('[FIND YOUR COLD-WEATHER SCENT]', 'b')],
  [P('Four for'), P('the cold months', 'h15'), BL(),
   cards(2, [tile('Tom Ford Tobacco Vanille', 'The deepest, warmest fall scent.', '2ml $34.99', '[SHOP TOBACCO VANILLE]'),
             tile('Jean Paul Gaultier Le Male Elixir', 'Your cold-weather closer. Honey and lavender over a smoky vanilla base.', '2ml $19.99', '[SHOP LE MALE ELIXIR]'),
             tile('Azzaro The Most Wanted Parfum', 'Spiced ginger up top, warm toffee, tonka and vanilla underneath.', '2ml $16.99', '[SHOP THE MOST WANTED]'),
             tile('Tom Ford Oud Wood', 'Rosewood and cardamom up top, oud and vanilla running through the base.', '2ml $34.99', '[SHOP OUD WOOD]')])],
  [P('A Closer Look:'), P('Tom Ford Tobacco Vanille', 'h15'), P('[IMAGE: Tobacco Vanille bottle, spotlit, with callout lines to each note, like the Sep 22 notes diagram]', 'ph'), BL(),
   cards(3, [note('TOP', 'Tobacco leaf and aromatic spices.'), note('HEART', 'Vanilla, cacao and tonka bean.'), note('BASE', 'Dried fruits and warm woods.')]),
   P('Test it in 2ml before you commit to the full bottle.'), P('[SHOP TOBACCO VANILLE]', 'b')],
  [cards(1, [review('AZZARO THE MOST WANTED PARFUM', "I absolutely love this! It's sweet, but the spicy cuts the tone, so it balances out nicely. I give this a 10 out 10. I will buy a full size for sure.", 'Norman G., verified buyer', '[SHOP THE MOST WANTED]')])],
  HOW + [P('[START SAMPLING]', 'b')],
  AUTH, FOOT])]
# 2 ---------------------------------------------------------------------------
E[2] = [H2('Campaign | Sale Launch | Veterans Day Sale Is Live'),
 meta('Campaign | Sale Launch | Veterans Day Sale Is Live | Designed', 'Wed, Nov 11, 2026', 'Engaged list. Launch the Veterans Day sale: 15% off sitewide with code REMEMBER15 through Friday, Nov 13 at 11:59pm ET.'),
 subj('Veterans Day Sale: 15% Off Everything', 'Use code REMEMBER15 through Friday at 11:59pm ET, every brand, every size.', 'Scent Pilot'), BL(),
 wire([[P('FREE SHIPPING ON ORDERS OVER $50 | FREE 10ML TRAVEL SIZE ON ORDERS OVER $100', 'small')],
  [P('Logo'), P('[IMAGE: dark, spotlit hero of 3 to 4 decants lined up]', 'ph'), P('VETERANS DAY SALE', 'b'), P('15% OFF EVERYTHING', 'hero'),
   P('From today through Friday, every fragrance on the site is 15% off with code REMEMBER15. Every brand, every size, no exclusions. Orders over $100 also unlock a free 10ml travel size from brands like Montblanc and Versace. The sale ends Friday, November 13 at 11:59pm ET.'),
   P('[CODE: REMEMBER15]'), P('[SHOP THE SALE]', 'b')],
  [P('15% Off Is Just The Start', 'h15'), BL(),
   cards(3, [note('15% OFF', 'Sitewide with code REMEMBER15.'), note('FREE SHIPPING', 'On orders over $50.'), note('FREE 10ML', 'On orders over $100, from brands like Montblanc and Versace.')])],
  [P('Start with'), P('a best seller', 'h15'), BL(),
   cards(2, [tile('Versace Dylan Blue', 'Bergamot, grapefruit and fig up top, incense, tonka and musk underneath.', '2ml $13.99', '[SHOP DYLAN BLUE]'),
             tile('Versace Eros Eau De Parfum', 'Lemon, mint and green apple up top, vanilla and cedarwood underneath.', '2ml $13.99', '[SHOP EROS EDP]'),
             tile('Dolce & Gabbana Light Blue Intense', 'Grapefruit, mandarin and sea water, warmed up by musk and amberwood.', '2ml $17.99', '[SHOP LIGHT BLUE INTENSE]'),
             tile('Boss Bottled Absolu', 'Incense and leather up top, patchouli and myrrh, then cedarwood.', '2ml $19.99', '[SHOP BOTTLED ABSOLU]')])],
  [P('Pick Your Size', 'h15'), P('Most fragrances come in three sizes, and all of them are 15% off this week.'), BL(),
   cards(3, [note('2ML', 'Enough to wear it for a week.'), note('5ML', 'For the scents you already know you like.'), note('10ML', 'A travel size that fits in any bag.')]),
   P('[FIND YOUR SIZE]', 'b')],
  TRUST,
  [P("Don't forget to use your code before **Friday, 11:59pm ET**."), P('[CODE: REMEMBER15]'), P('[SHOP THE SALE]', 'b')],
  FOOT])]
# 3 ---------------------------------------------------------------------------
E[3] = [H2('Campaign | Social Proof | What Buyers Say After Trying First'),
 meta('Campaign | Social Proof | What Buyers Say After Trying First | Designed', 'Fri, Nov 13, 2026 (morning, before the plain-text reminder)', 'Engaged list. Last day of the Veterans Day sale: three real buyer reviews, then the reviewed products, then why testing first works, then the code.'),
 subj('Straight From The Testers', 'What buyers said after trying a decant first, and your 15% ends tonight at 11:59pm ET.', 'Scent Pilot'), BL(),
 wire([[P('LAST DAY: 15% OFF EVERYTHING WITH CODE REMEMBER15 | ENDS 11:59PM ET', 'small')],
  [P('Logo'), P('[IMAGE: close-up of a hand holding a 2ml decant, dark spotlit background]', 'ph'), P('LAST DAY OF THE VETERANS DAY SALE', 'b'), P('WHAT THEY SAID AFTER TRYING IT', 'hero'),
   P('Real reviews from verified buyers, pulled straight from our product pages. Today is the last day to try any of these for 15% less. Use code REMEMBER15 before 11:59pm ET tonight.'), P('[SHOP THE SALE]', 'b')],
  [cards(1, [review('LOUIS VUITTON IMAGINATION', 'Legit, smells great, love scent pilot!', 'Richard N., verified buyer', '[SHOP IMAGINATION]'),
             review('ACQUA DI GIO PARFUM 2024', "I wasn't too fond of the scent when I first tried it on my wrist. I wore it to work a few days later and got several compliments and the scent grew on me. I will definitely be buying a bottle.", 'Kelvin T., verified buyer', '[SHOP ACQUA DI GIO PARFUM]'),
             review('CREED AVENTUS', 'The samples arrived quickly, and I love the option of ordering smaller testers before investing in a whole bottle. Will definitely be ordering more to give other fragrances a try. Thank you!', 'Todd J., verified buyer', '[SHOP CREED AVENTUS]')])],
  [P('Their picks.'), P('Your turn to test.', 'h15'), BL(),
   cards(3, [[P('[PRODUCT TILE: Louis Vuitton Imagination bottle]', 'ph'), P('Louis Vuitton Imagination', 'b'), P('[STARS] Rated 4.5 out of 5', 'small'), P('2ml $39.99', 'small'), P('[SHOP NOW]', 'b')],
             [P('[PRODUCT TILE: Acqua Di Gio Parfum 2024 bottle]', 'ph'), P('Acqua Di Gio Parfum 2024', 'b'), P('[STARS] Rated 4.2 out of 5', 'small'), P('2ml $19.99', 'small'), P('[SHOP NOW]', 'b')],
             [P('[PRODUCT TILE: Creed Aventus bottle]', 'ph'), P('Creed Aventus', 'b'), P('[STARS] Rated 4.6 out of 5', 'small'), P('2ml $34.99', 'small'), P('[SHOP NOW]', 'b')]])],
  [P('Why They Tested First', 'h15'), BL(),
   cards(2, [note('EVERYWHERE ELSE', 'Scroll for an hour, guess, hope you picked right.'), note('SCENT PILOT', 'Sorted by house, ready to test in 2ml.')]),
   P('[GRAPHIC: two-column comparison like the Sep 22 email, with a 2ml vial image in the Scent Pilot column]', 'ph')],
  [P('Your 15% off ends **tonight at 11:59pm ET**.'), P('[CODE: REMEMBER15]'), P('[SHOP THE SALE]', 'b'), P('Free shipping over $50. Free 10ml travel size on orders over $100.', 'small')],
  AUTH, FOOT])]
# 4 ---------------------------------------------------------------------------
E[4] = [H2('Campaign | Last Chance | Veterans Day Sale Ends Tonight'),
 meta('Campaign | Last Chance | Veterans Day Sale Ends Tonight | Plain text', 'Fri, Nov 13, 2026 (evening, after Email 3)', 'Engaged list. Plain-text last call from Hamza: the Veterans Day sale ends tonight at 11:59pm ET.'),
 subj('Your 15% Ends Tonight', 'A quick note from Hamza before the Veterans Day sale closes.', 'Hamza @ Scent Pilot'), BL(),
 wire([plain('Hamza @ Scent Pilot'),
  [L("Hey {{ person.first_name|default:'there' }},"), BL(), L('Quick one.'), BL(), L('The Veterans Day sale ends **tonight at 11:59pm ET.**'), BL(),
   L('Code **REMEMBER15** takes 15% off everything on the site. Every brand, every size, no exclusions.'), BL(),
   L("If there's a scent you've been circling, grab a decant tonight and find out for 15% less."), BL(),
   L('Orders over **$100** also unlock a **free 10ml travel size** from brands like Montblanc and Versace.'), BL(),
   LINK('SHOP THE SALE >>>'), BL()] + SIGN('Smell good,') + [BL(), L('P.S. Every sample is Authenticity Guaranteed or your money back.')]])]
# 5 ---------------------------------------------------------------------------
E[5] = [H2("Campaign | Founder Video | Hamza's YouTube Video"),
 meta("Campaign | Founder Video | Hamza's YouTube Video | Designed", 'Mon, Nov 16, 2026', "Engaged list. Drive views to Hamza's I Will by Giorgio Armani comparison video, then to the I Will page. No offer."),
 subj('I Will, Tested On Camera', "Hamza put Armani's I Will side by side on YouTube, so you can see it before you smell it.", 'Scent Pilot'), BL(),
 wire([AUTH,
  [P('Logo'), P('[IMAGE: video thumbnail from the YouTube video with a play button, linked to the video]', 'ph'), P('NEW FROM HAMZA', 'b'), P('I WILL, PUT TO THE TEST', 'hero'),
   P("Hamza's latest video puts I Will by Giorgio Armani side by side with missing info: the fragrance(s) it's compared to. Watch the comparison, then try I Will in 2ml and settle it on your own skin."),
   P('[WATCH THE VIDEO]', 'b')],
  [P('What I Will', 'h15'), P('Actually Smells Like', 'h15'), P('[IMAGE: I Will bottle, spotlit, with callout lines to each note]', 'ph'), BL(),
   cards(3, [note('OPENS WITH', 'Bergamot, lavender and violet leaf.'), note('WARMS INTO', 'Vanilla and smoky leather.'), note('FINISHES ON', 'Patchouli, bold and magnetic.')]),
   P('[TRY I WILL IN 2ML]', 'b')],
  [P('Pick Your Size', 'h15'), BL(),
   cards(3, [note('2ML | $19.99', 'Enough to wear it for a week.'), note('5ML | $26.99', 'For when the video already sold you.'), note('10ML | $36.99', 'A travel size for your bag.')]),
   P('[SHOP I WILL]', 'b')],
  [P('Also In The Video', 'h15'), BL(), P('[PRODUCT TILE x2 to x3: missing info: the other fragrance(s) in the comparison, each with its own [SHOP NOW] button]', 'ph')],
  [P('Watch first. Test second. Buy the bottle only if it earns it.', 'b'), P('[WATCH THE VIDEO]', 'b')],
  FOOT])]
# 6 ---------------------------------------------------------------------------
E[6] = [H2('Campaign | Myth vs Fact | Does A Decant Smell Like The Full Bottle'),
 meta('Campaign | Myth vs Fact | Does A Decant Smell Like The Full Bottle | Plain text', 'Wed, Nov 18, 2026', 'Engaged list. Plain-text note from Hamza answering the most common worry: a decant is the same fragrance, poured from the real bottle. No offer.'),
 subj('Is A Decant The Real Thing?', "Short answer from Hamza: yes, and here's exactly where it comes from.", 'Hamza @ Scent Pilot'), BL(),
 wire([plain('Hamza @ Scent Pilot'),
  [L("Hey {{ person.first_name|default:'there' }},"), BL(),
   L("Here's a question I hear all the time: does a decant actually smell like the full bottle?"), BL(),
   L('Short answer: **yes. It is the full bottle.**'), BL(),
   L('Every decant is poured from the original bottle after you order, using sterile equipment, into the size you pick. Same liquid. Smaller bottle.'), BL(),
   L("The only thing that changes is the packaging. Your decant ships in our own labeled bottle, not the designer's. The fragrance inside is the original."), BL(),
   L("And we will never sell fakes, copies or diluted products. That's the whole point."), BL(),
   L("So when you test a 2ml for a week, you're not testing a stand-in. You're wearing the real thing before you spend on the bottle."), BL(),
   LINK('FIND YOUR NEXT SCENT >>>'), BL()] + SIGN('Talk soon,') + [BL(), L('P.S. Every sample is Authenticity Guaranteed or your money back.')]])]
# 7 ---------------------------------------------------------------------------
E[7] = [H2("Campaign | Founder Video | Hamza's Latest Comparison Video"),
 meta("Campaign | Founder Video | Hamza's Latest Comparison Video | Designed", 'Fri, Nov 20, 2026', 'Engaged list. Drive views to Hamza\'s "10 Signature Scents That Actually Get Compliments" video, then to the scents in it. No offer.'),
 subj('10 Signature Scents, Ranked', "Hamza's new video walks through ten of them, and every one is testable in 2ml.", 'Scent Pilot'), BL(),
 wire([AUTH,
  [P('Logo'), P('[IMAGE: video thumbnail from the YouTube video with a play button, linked to the video]', 'ph'), P('NEW FROM HAMZA', 'b'), P('10 SIGNATURE SCENTS', 'hero'),
   P('Finding a signature scent off a YouTube video is how most blind buys start. So test it instead. Watch Hamza walk through all ten, pick the two or three that sound like you, and wear each one for a week in 2ml.'),
   P('[WATCH THE VIDEO]', 'b')],
  [P('From The Video', 'h15'), BL(), P('[PRODUCT TILE x4 in a 2-up grid: missing info: which of the ten scents to feature (name, one line, 2ml price, [SHOP NOW])]', 'ph'), P('[SHOP THE FULL LIST]', 'b')],
  [P('What You Smell First', 'h15'), P("Isn't What Lingers", 'h15'), P('That is why a week in 2ml beats a paper strip.'), BL(),
   cards(3, [note('TOP | 0-15 MIN', 'The first impression. Bright, and gone fast.'), note('HEART | 15 MIN-2 HRS', 'The character of the scent.'), note('BASE | 2+ HRS', 'What is still there at the end of the day.')])],
  [cards(1, [review('VERSACE DYLAN BLUE', "This is a first time order from me and didn't know what to expect but I gotta say honestly, I'm more than impressed and pleased with my purchase. I love the idea of try before you buy and found all his recommendations on YouTube to be accurate. The Dylan Blue by Versace and YSL Myself have been my favorite and the others really smell great to that I got just haven't really had a chance to use them in public. It came very well packaged and even included a little gift. Definitely try all his recommendations because this they are incredible and you will be satisfied. Excellent prices as well! I will be making a new order for some other ones soon! Thank you.", 'Joseph L., verified buyer', '[SHOP DYLAN BLUE]')])],
  [P('Watch it. Test it. Then decide.', 'b'), P('[WATCH THE VIDEO]', 'b')],
  FOOT])]
# 8 ---------------------------------------------------------------------------
E[8] = [H2('Campaign | How It Is Made | How Your Decant Gets Made'),
 meta('Campaign | How It Is Made | How Your Decant Gets Made | Designed', 'Sun, Nov 22, 2026', 'Engaged list. Walk through what happens after an order: poured from the original bottle with sterile equipment into a Scent Pilot labeled bottle. Answer the top questions. No offer.'),
 subj('From Their Bottle To Yours', "What happens between you clicking order and a decant landing on your doorstep.", 'Scent Pilot'), BL(),
 wire([AUTH,
  [P('Logo'), P('[IMAGE: close-up of a fragrance being decanted into a small labeled vial, dark spotlit background]', 'ph'), P('BEHIND THE DECANT', 'b'), P('FROM THEIR BOTTLE TO YOURS', 'hero'),
   P("Every decant starts after you order. We pour it from the original bottle with sterile equipment, into the size you chose, and send it out in our own labeled bottle. Here's exactly what happens."),
   P('[FIND YOUR SCENT]', 'b')],
  [P('Four Steps', 'h15'), P('From order to your shelf'), BL(),
   cards(2, [step('1', 'You pick', 'A fragrance and a size: 2ml, 5ml, or 10ml.'),
             step('2', 'We pour', 'Decanted after you order, using sterile equipment.'),
             step('3', 'We label', 'Into our own Scent Pilot bottle. Only the liquid comes from the original.'),
             step('4', 'You test', 'Wear it for a week. Buy the full bottle only if it earns it.')])],
  [P('Your Questions,'), P('Answered Straight', 'h15'), BL(),
   cards(1, [faq('Is it the real fragrance?', 'Yes. Every decant is poured from the original bottle. We never sell fakes, copies or diluted products.'),
             faq("Why isn't it in the designer's bottle?", "Because we pour it ourselves. Your decant ships in Scent Pilot's own labeled bottle. We're not affiliated with the brands we carry."),
             faq('What size should I start with?', '2ml. It is enough to wear a scent for a week and see how it plays on your skin.'),
             faq('Can I return it?', 'All sales are final. Every decant is covered by our authenticity guarantee.')])],
  [P('Start with a 2ml.', 'b'), P('[START SAMPLING]', 'b')],
  FOOT])]
# 9 ---------------------------------------------------------------------------
E[9] = [H2('Campaign | Sale Launch | Black Friday Sale Is Live'),
 meta('Campaign | Sale Launch | Black Friday Sale Is Live | Designed', 'Mon, Nov 23, 2026', 'Engaged list. Launch the Black Friday sale: 15% off sitewide with code BLACKFRIDAY15 through Friday, Dec 4 at midnight ET.'),
 subj('Black Friday Starts Now', 'Code BLACKFRIDAY15 takes 15% off every fragrance, every size, through December 4.', 'Scent Pilot'), BL(),
 wire([[P('FREE SHIPPING ON ORDERS OVER $50 | FREE 10ML TRAVEL SIZE ON ORDERS OVER $100', 'small')],
  [P('Logo'), P('[IMAGE: dark, spotlit hero of a row of decants and full bottles, Black Friday energy without discount clip-art]', 'ph'), P('BLACK FRIDAY SALE', 'b'), P('15% OFF EVERYTHING', 'hero'),
   P("Black Friday is here, and it runs for almost two weeks. Every fragrance on the site is 15% off with code BLACKFRIDAY15. Every brand, every size, no exclusions. Orders over $100 also unlock a free 10ml travel size from brands like Montblanc and Versace. The sale ends Friday, December 4 at midnight ET."),
   P('[CODE: BLACKFRIDAY15]'), P('[SHOP BLACK FRIDAY]', 'b')],
  [P('Three Ways', 'h15'), P('This Sale Pays Off', 'h15'), BL(),
   cards(3, [note('15% OFF', 'Sitewide with code BLACKFRIDAY15.'), note('FREE SHIPPING', 'On orders over $50.'), note('FREE 10ML', 'On orders over $100, from brands like Montblanc and Versace.')])],
  [P('The Ones Everyone', 'h15'), P('Starts With', 'h15'), BL(),
   cards(2, [tile('Prada Paradigme Eau De Parfum', 'Ambery woods, green bourbon geranium and Calabrian bergamot.', '2ml $19.99', '[SHOP PARADIGME]'),
             tile('Montblanc Legend Elixir', 'Lavender and cardamom over rich woods, leather and vanilla.', '2ml $13.99', '[SHOP LEGEND ELIXIR]'),
             tile('Louis Vuitton Imagination', 'Bright bergamot, black tea and ambroxan. Refined and fresh.', '2ml $39.99', '[SHOP IMAGINATION]'),
             tile('Acqua Di Gio Parfum 2024', 'Marine notes, bergamot and rosemary over incense and patchouli.', '2ml $19.99', '[SHOP ACQUA DI GIO PARFUM]')]),
   P('[SHOP ALL BEST SELLERS]', 'b')],
  TRUST,
  [P('Sale ends **Friday, December 4 at midnight**.'), P('[CODE: BLACKFRIDAY15]'), P('[SHOP BLACK FRIDAY]', 'b')],
  FOOT])]
# 10 --------------------------------------------------------------------------
E[10] = [H2('Campaign | Product Spotlight | Creed Aventus Spotlight'),
 meta('Campaign | Product Spotlight | Creed Aventus Spotlight | Designed', 'Wed, Nov 25, 2026', 'Engaged list. One-product spotlight on Creed Aventus: the notes, every size and price, one review, with the Black Friday code as the reason to order.'),
 subj('$510 Bottle Or A $35 Test?', 'Creed Aventus starts at $34.99 in 2ml, and BLACKFRIDAY15 takes 15% off that.', 'Scent Pilot'), BL(),
 wire([[P('BLACK FRIDAY: 15% OFF EVERYTHING WITH CODE BLACKFRIDAY15', 'small')],
  [P('Logo'), P('[IMAGE: Creed Aventus bottle, dramatic spotlight on dark background]', 'ph'), P('BLACK FRIDAY SPOTLIGHT', 'b'), P('CREED AVENTUS', 'hero'),
   P('The full bottle of Creed Aventus is $510. A 2ml is $34.99, and code BLACKFRIDAY15 takes 15% off either one. Wear it for a week first. If it earns the bottle, you will know.'),
   P('[CODE: BLACKFRIDAY15]'), P('[SHOP CREED AVENTUS]', 'b')],
  [P('What Aventus', 'h15'), P('Actually Smells Like', 'h15'), P('[IMAGE: Aventus bottle with callout lines to each note, like the Sep 22 notes diagram]', 'ph'), BL(),
   cards(3, [note('TOP', 'Bergamot, black currant, apple and lemon.'), note('HEART', 'Pineapple, patchouli and jasmine.'), note('BASE', 'Smoky birch, musk and cedarwood.')])],
  [P('$510 Is A Lot', 'h15'), P('To Gamble On A Guess', 'h15'), BL(),
   cards(2, [note('2ML | $34.99', 'Enough to wear it for a week.'), note('5ML | $54.99', 'For when you already know.'), note('10ML | $89.99', 'Your travel bottle.'), note('100ML | $510.00', 'The full bottle, once it earns it.')]),
   P('[FIND YOUR SIZE]', 'b')],
  [cards(1, [review('CREED AVENTUS', "Great classic scent. It's one of the GOATs for a reason.", 'Juan G., verified buyer', '[SHOP CREED AVENTUS]')])],
  [P('Use code **BLACKFRIDAY15** before the sale ends Friday, December 4 at midnight ET.'), P('[CODE: BLACKFRIDAY15]'), P('[SHOP CREED AVENTUS]', 'b')],
  AUTH, FOOT])]
# 11 --------------------------------------------------------------------------
E[11] = [H2('Campaign | Founder Note | Thanksgiving Thank You From Hamza'),
 meta('Campaign | Founder Note | Thanksgiving Thank You From Hamza | Plain text', 'Thu, Nov 26, 2026 (Thanksgiving)', 'Engaged list. Short plain-text thank you from Hamza, with one line that the Black Friday sale is still running.'),
 subj('Thank You, From Hamza', 'A short note for Thanksgiving, and a reminder that the sale runs through December 4.', 'Hamza @ Scent Pilot'), BL(),
 wire([plain('Hamza @ Scent Pilot'),
  [L("Hey {{ person.first_name|default:'there' }},"), BL(), L('Happy Thanksgiving.'), BL(),
   L("I started Scent Pilot after I watched the reviews, bought a fragrance without ever trying it, and was disappointed. I wanted a place where you could test first and only buy the bottle once it earned it."), BL(),
   L("Every order since then has come from someone who wanted to try before they invest. So thank you for testing with us."), BL(),
   L('If you are shopping this weekend, the Black Friday sale is still on: **15% off everything with code BLACKFRIDAY15** through Friday, December 4.'), BL(),
   LINK('SHOP THE SALE >>>'), BL()] + SIGN('Cheers,') + [BL(), L('P.S. Every sample is Authenticity Guaranteed or your money back.')]])]
# 12 --------------------------------------------------------------------------
E[12] = [H2('Campaign | Gift Guide | The Black Friday Gift Guide'),
 meta('Campaign | Gift Guide | The Black Friday Gift Guide | Designed', 'Fri, Nov 27, 2026 (Black Friday)', 'Engaged list. Gift guide pairing scent profiles with decant sizes and price points, with the Black Friday code on top.'),
 subj('Gift The Test, Not The Guess', 'Fragrance gifts by the person you are shopping for, all 15% off with code BLACKFRIDAY15.', 'Scent Pilot'), BL(),
 wire([[P('BLACK FRIDAY: 15% OFF EVERYTHING WITH CODE BLACKFRIDAY15', 'small')],
  [P('Logo'), P('[IMAGE: a few decants arranged like a gift, dark spotlit background]', 'ph'), P('THE BLACK FRIDAY GIFT GUIDE', 'b'), P('GIFT THE TEST, NOT THE GUESS', 'hero'),
   P("Buying fragrance for someone else is a blind buy twice over. So give them a few decants instead and let them find the one they love. Every pick below is 15% off with code BLACKFRIDAY15 through December 4."),
   P('[CODE: BLACKFRIDAY15]'), P('[SHOP GIFTS]', 'b')],
  [P('Pick By'), P('The Person', 'h15'), BL(),
   cards(2, [gtile('FOR THE FRESH-AND-CLEAN ONE', 'Dolce & Gabbana Light Blue Intense', 'Grapefruit, mandarin and sea water, warmed up by musk and amberwood.', '2ml $17.99 | 5ml $24.99 | 10ml $34.99', '[SHOP LIGHT BLUE INTENSE]'),
             gtile('FOR THE WARM-AND-SMOOTH ONE', 'Montblanc Legend Elixir', 'Lavender and cardamom over rich woods, leather and vanilla.', '2ml $13.99 | 5ml $17.99 | 10ml $21.99', '[SHOP LEGEND ELIXIR]'),
             gtile('FOR THE BOLD ONE', 'Giorgio Armani I Will', 'Bergamot, lavender and violet leaf over vanilla, smoky leather and patchouli.', '2ml $19.99 | 5ml $26.99 | 10ml $36.99', '[SHOP I WILL]'),
             gtile('FOR THE ONE WHO HAS EVERYTHING', 'Tom Ford Oud Wood', 'Cardamom, rosewood and oud, finished with tonka, amber and vanilla.', '2ml $34.99 | 5ml $54.99 | 10ml $74.99', '[SHOP OUD WOOD]')])],
  [P('Pick By'), P('Budget', 'h15'), BL(),
   cards(3, [note('UNDER $20', 'A 2ml of Legend Elixir, Light Blue Intense or I Will.'), note('UNDER $40', 'A 10ml travel size of Legend Elixir, Light Blue Intense or I Will.'), note('THE BIG ONE', 'A 10ml of Oud Wood. Or build an order over $100 and get a free 10ml too.')])],
  TRUST,
  [P('15% off everything with code **BLACKFRIDAY15** through Friday, December 4.'), P('[CODE: BLACKFRIDAY15]'), P('[SHOP GIFTS]', 'b')],
  FOOT])]
# 13 --------------------------------------------------------------------------
E[13] = [H2('Campaign | Offer Push | Cyber Monday: Your Free 10ml Is Waiting'),
 meta('Campaign | Offer Push | Cyber Monday: Your Free 10ml Is Waiting | Designed', 'Mon, Nov 30, 2026 (Cyber Monday)', 'Engaged list. Push the free 10ml travel size on orders over $100, with the Black Friday sale (BLACKFRIDAY15) still running through Dec 4.'),
 subj('Your Free 10ml Is Waiting', 'Spend over $100 and a free 10ml travel size comes with your order, plus 15% off with BLACKFRIDAY15.', 'Scent Pilot'), BL(),
 wire([[P('CYBER MONDAY: 15% OFF EVERYTHING WITH CODE BLACKFRIDAY15', 'small')],
  [P('Logo'), P('[IMAGE: a 10ml travel size with a gift tag, dark spotlit background]', 'ph'), P('CYBER MONDAY', 'b'), P('YOUR FREE 10ML IS WAITING', 'hero'),
   P('The Black Friday sale is still on: 15% off everything with code BLACKFRIDAY15. Spend over $100 and you also unlock a free 10ml travel size from brands like Montblanc and Versace. The sale ends Friday, December 4 at midnight ET.'),
   P('[CODE: BLACKFRIDAY15]'), P('[SHOP CYBER MONDAY]', 'b')],
  [P('How To Unlock It', 'h15'), BL(),
   cards(3, [step('1', 'Fill your cart', 'Any fragrances, any sizes.'), step('2', 'Use your code', 'BLACKFRIDAY15 takes 15% off.'), step('3', 'Pass $100', 'A free 10ml travel size comes with your order.')])],
  [P('Here Is What $100', 'h15'), P('Can Look Like', 'h15'), BL(),
   cards(1, [[P('Louis Vuitton Imagination 10ml: $99.99'), P('Versace Eros Eau De Parfum 10ml: $24.99'), P('Subtotal: $124.98'), P('With 15% off: **$106.23**'), P('Free 10ml travel size unlocked.', 'b')]]),
   P('[GRAPHIC: receipt-style card with the lines above]', 'ph')],
  [P('Fill It With'), P('A 10ml You Will Use', 'h15'), BL(),
   cards(2, [tile('Louis Vuitton Imagination', 'Bright bergamot, black tea and ambroxan. Refined and fresh.', '10ml $99.99', '[SHOP IMAGINATION]'),
             tile('Creed Aventus', 'Bergamot, black currant and pineapple over smoky birch and musk.', '10ml $89.99', '[SHOP CREED AVENTUS]'),
             tile('Versace Eros Eau De Parfum', 'Lemon, mint and green apple up top, vanilla and cedarwood underneath.', '10ml $24.99', '[SHOP EROS EDP]'),
             tile('Montblanc Legend Elixir', 'Lavender and cardamom over rich woods, leather and vanilla.', '10ml $21.99', '[SHOP LEGEND ELIXIR]')])],
  [P('Code **BLACKFRIDAY15** works through Friday, December 4.'), P('[CODE: BLACKFRIDAY15]'), P('[SHOP CYBER MONDAY]', 'b')],
  AUTH, FOOT])]
# Notes -----------------------------------------------------------------------
N = lambda t: ('p', runs(t), None)
E[14] = [H2('Notes'), H3('To confirm before build'),
 N('**Codes.** Veterans Day emails (1 to 4) use **REMEMBER15**, Nov 11 to Fri Nov 13, 11:59pm ET. Black Friday emails (9 to 13) use **BLACKFRIDAY15**, Nov 23 to Fri Dec 4 at midnight ET. Check both codes are live in Shopify for their windows.'),
 N('**Black Friday time zone.** Confirmed by Danie (Nov 1, 2026): the sale ends Friday, December 4 at midnight ET.'),
 N('**Free 10ml.** Customer does not pick. Copy follows the client: unlock a 10ml travel size from a select variety of brands like Montblanc and Versace on orders over $100.'),
 N("**Hamza's videos (Emails 5 and 7).** YouTube is blocked from Claude's session, so the fragrances compared in the I Will video and the ten scents in the signature-scents video are missing info. Send the list (or allow youtube.com) and the product tiles get filled in. The Email 7 subject says \"Ranked\": confirm the video actually ranks them, or change it to \"10 Signature Scents Worth Testing\"."),
 N('**Reviews.** All quoted in full and word for word from Loox reviews on scentpilot.com product pages (verified buyers), keeping the customers\' own punctuation. Approved to quote (Danie, Nov 1, 2026). Kelvin T. (Email 3) and the Joseph L. review (Email 7) mention compliments and YouTube recommendations; those are their experiences, not brand claims.'),
 N('**Email 2 subject** is 6 words (TTM aims for 2 to 5). Kept because it mirrors the approved Labor Day subject "Labor Day Sale: 15% Off Sitewide".'),
 N('**Email 13 math.** LV Imagination 10ml $99.99 + Versace Eros EDP 10ml $24.99 = $124.98; 15% off = $106.23 (over $100). Re-check prices before the send.'),
 N('**Prices** are from scentpilot.com on Oct 31, 2026, before any discount. The cheapest 2ml on the site is now $5.99, so the old "2ml starts at $7" line is not used.'),
 N('**Send times and audience tiers** are not set yet. On Nov 13, Email 3 goes in the morning and Email 4 in the evening.'),
 H3('Designer notes'),
 N('**All designed emails.** Reuse the approved Sep 22 system ("The Curated Way To Try 170+ Fragrances", Figma node 8990:498): black top bar, dark navy body, typewriter-style uppercase headlines, square white buttons, moody spotlit bottle shots, white footer. Section types are taken from approved past emails: notes diagram (Sep 22), How It Works steps ("Why Guys Are Done Blind-Buying"), Testing Before Investing block ("The Cologne You\'ve Been Sleeping On"), Everywhere else vs Scent Pilot (Sep 22), note timeline ("Here\'s Exactly What Lingers").'),
 N('**Review and FAQ cards** stack one per row, never a grid. No customer photos are quoted.'),
 N('**Videos (Emails 5 and 7).** Use a video thumbnail with a play button linked to YouTube; the main button goes to the video, the product buttons to the product pages.'),
 N("**Plain-text emails (4, 6, 11).** Build in Klaviyo's text-only editor. No logo, images or buttons. Link text in navy, all caps, ending \">>>\" (Hamza's founder-email habit)."),
 H3('Links'),
 N('Videos: I Will comparison https://www.youtube.com/watch?v=Ttis-DvuM9Y | 10 Signature Scents https://www.youtube.com/watch?v=i8c66yepilc'),
 N('Shop all / sale: https://scentpilot.com/'),
 N('Products: https://scentpilot.com/products/ + tom-ford-tobacco-vanille, jean-paul-gaultier-le-male-elixir, azzaro-the-most-wanted-parfum, tom-ford-oud-wood, versace-dylan-blue, versace-eros-eau-de-parfum, dolce-gabbana-light-blue-intense, boss-bottled-absolu-by-hugo-boss, louis-vuitton-imagination, acqua-di-gio-parfum-2024, creed-aventus, i-will-by-giorgio-armani, prada-paradigme-edp, montblanc-legend-elixir'),
 H3('Sources'),
 N('Offer, codes, dates and threshold: Danie, Oct 31, 2026. Voice, sign-offs and authenticity lines: Scent Pilot brand record (Claude Project export). Product notes and prices: scentpilot.com product pages, Oct 31, 2026. Product lines in Email 1: approved past emails in the Scent Pilot Figma file. Decanting facts: scentpilot.com/pages/discalimers. Return policy: scentpilot.com/pages/return-policy.'),
 N('**Used reviews (do not reuse in November):** Email 1 Norman G. (Most Wanted Parfum); Email 3 Richard N. (LV Imagination), Kelvin T. (ADG Parfum 2024), Todd J. (Creed Aventus); Email 7 Joseph L. (Dylan Blue); Email 10 Juan G. (Creed Aventus).')]

if __name__ == '__main__':
    n = int(sys.argv[1]); tab = sys.argv[2]
    req = build(tab, E[n])
    if len(sys.argv) > 3:
        end = int(sys.argv[3])
        req = [{"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1, "tabId": tab}}},
               {"updateParagraphStyle": {"range": {"startIndex": 1, "endIndex": 2, "tabId": tab}, "paragraphStyle": {"namedStyleType": "NORMAL_TEXT", "alignment": "START"}, "fields": "namedStyleType,alignment"}}] + req
    print(json.dumps(req, separators=(',', ':')))
