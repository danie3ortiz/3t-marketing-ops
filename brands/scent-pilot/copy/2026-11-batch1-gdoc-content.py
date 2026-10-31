import sys,json; sys.path.insert(0,'.')
import os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
from gdoc_brief_builder import *
SP='https://scentpilot.com/products/'
def tile(name,line,price,btn): return [P('[PRODUCT TILE: '+name+' bottle]','ph'),P(name,'b'),P(line),P(price,'small'),P(btn,'b')]
def review(label,quote,who,btn,rating=None):
    return [P(label,'b'),P('[STARS] 5/5'),P('"'+quote+'"','i'),P(who,'small'),P(btn,'b')]
E={}
# -------- Email 1
E[1]=[H2('Campaign | Product Roundup | Cold-Weather Scents Worth Sampling'),
 meta('Campaign | Product Roundup | Cold-Weather Scents Worth Sampling | Designed','Mon, Nov 9, 2026','Engaged list. Seasonal roundup of four warmer scents to test as decants now the weather is turning. No offer.'),
 subj('Retire The Summer Scent','Four warmer picks for cold air, and you can test every one before you buy the bottle.','Scent Pilot'),
 BL(),
 wire([
  [P('FREE SHIPPING ON ORDERS OVER $50','small')],
  [P('Logo'),P('[IMAGE: dark, moody shot of a bottle on a wool scarf or by a frosted window, spotlit like the Sep 22 hero]','ph'),P('COLD-WEATHER ROTATION','b'),P('THE COLD NEEDS SOMETHING HEAVIER','hero'),
   P("The fresh, citrusy bottle that got you through summer goes quiet once the air turns cold. This is the season for vanilla, tobacco, honey and spice. Below are four we'd reach for this month. Test any of them as a decant before you commit to a full bottle."),
   P('[FIND YOUR COLD-WEATHER SCENT]','b')],
  [P('Four for'),P('the cold months','h15'),BL(),
   cards(2,[tile('Tom Ford Tobacco Vanille','The deepest, warmest fall scent.','2ml $34.99','[SHOP TOBACCO VANILLE]'),
            tile('Jean Paul Gaultier Le Male Elixir','Your cold-weather closer. Honey and lavender over a smoky vanilla base.','2ml $19.99','[SHOP LE MALE ELIXIR]'),
            tile('Azzaro The Most Wanted Parfum','Spiced ginger up top, warm toffee, tonka and vanilla underneath.','2ml $16.99','[SHOP THE MOST WANTED]'),
            tile('Tom Ford Oud Wood','Rosewood and cardamom up top, oud and vanilla running through the base.','2ml $34.99','[SHOP OUD WOOD]')])],
  [P('Test It Before You Invest In It','h15'),BL(),
   cards(3,[[P('Pick a decant','b'),P('Any scent, small size.')],[P('Wear it a week','b'),P('Work, dinner, cold mornings.')],[P('Then decide','b'),P('Only buy the bottle if it earns it.')]]),
   P('Every decant is the actual luxury fragrance, poured from the actual bottle.'),P('[START SAMPLING]','b')],
  [P('Footer','small')]])]
# -------- Email 2
E[2]=[H2('Campaign | Sale Launch | Veterans Day Sale Is Live'),
 meta('Campaign | Sale Launch | Veterans Day Sale Is Live | Designed','Wed, Nov 11, 2026','Engaged list. Launch the Veterans Day sale: 15% off sitewide with code REMEMBER15 through Friday, Nov 13 at 11:59pm ET.'),
 subj('Veterans Day Sale: 15% Off Everything','Use code REMEMBER15 through Friday at 11:59pm ET, every brand, every size.','Scent Pilot'),
 BL(),
 wire([
  [P('FREE SHIPPING ON ORDERS OVER $50 | FREE 10ML TRAVEL SIZE ON ORDERS OVER $100','small')],
  [P('Logo'),P('[IMAGE: dark, spotlit hero of 3 to 4 decants lined up]','ph'),P('VETERANS DAY SALE','b'),P('15% OFF EVERYTHING','hero'),
   P('From today through Friday, every fragrance on the site is 15% off with code REMEMBER15. Every brand, every size, no exclusions. Orders over $100 also unlock a free 10ml travel size from brands like Montblanc and Versace. The sale ends Friday, November 13 at 11:59pm ET.'),
   P('[CODE: REMEMBER15]'),P('[SHOP THE SALE]','b')],
  [P('15% Off Is Just The Start','h15'),BL(),
   cards(3,[[P('15% OFF','b'),P('Sitewide with code REMEMBER15.')],[P('FREE SHIPPING','b'),P('On orders over $50.')],[P('FREE 10ML','b'),P('On orders over $100, from brands like Montblanc and Versace.')]])],
  [P('Start with'),P('a best seller','h15'),BL(),
   cards(2,[tile('Creed Aventus','Bergamot, black currant, smoky birch and musk. The one everyone wants.','2ml $34.99','[SHOP CREED AVENTUS]'),
            tile('Versace Eros Eau De Parfum','Mint and green apple up top, vanilla and cedarwood underneath.','2ml $13.99','[SHOP EROS EDP]'),
            tile('Acqua Di Gio Parfum 2024','Clean, aquatic, magnetic. The upgrade everyone keeps switching to.','2ml $19.99','[SHOP ACQUA DI GIO PARFUM]'),
            tile('Louis Vuitton Imagination','Bright citrus and grapefruit open into warm guaiac wood, then settle into clean, lingering musk.','2ml $39.99','[SHOP IMAGINATION]')])],
  [P("Don't forget to use your code before **Friday, 11:59pm ET**."),P('[CODE: REMEMBER15]'),P('[SHOP THE SALE]','b'),P('AUTHENTICITY GUARANTEED. OR YOUR MONEY BACK.','small')],
  [P('Footer','small')]])]
# -------- Email 3
E[3]=[H2('Campaign | Social Proof | What Buyers Say After Trying First'),
 meta('Campaign | Social Proof | What Buyers Say After Trying First | Designed','Fri, Nov 13, 2026 (morning, before the plain-text reminder)','Engaged list. Last day of the Veterans Day sale: three real buyer reviews, then the reviewed products, then the code.'),
 subj('Straight From The Testers','What buyers said after trying a decant first, and your 15% ends tonight at 11:59pm ET.','Scent Pilot'),
 BL(),
 wire([
  [P('LAST DAY: 15% OFF EVERYTHING WITH CODE REMEMBER15 | ENDS 11:59PM ET','small')],
  [P('Logo'),P('[IMAGE: close-up of a hand holding a 2ml decant, dark spotlit background]','ph'),P('LAST DAY OF THE VETERANS DAY SALE','b'),P('WHAT THEY SAID AFTER TRYING IT','hero'),
   P("Real reviews from verified buyers, pulled straight from our product pages. Today is the last day to try any of these for 15% less. Use code REMEMBER15 before 11:59pm ET tonight."),P('[SHOP THE SALE]','b')],
  [cards(1,[review('LOUIS VUITTON IMAGINATION','Legit, smells great, love scent pilot!','Richard N., verified buyer','[SHOP IMAGINATION]'),
            review('ACQUA DI GIO PARFUM 2024',"I wasn't too fond of the scent when I first tried it on my wrist. I wore it to work a few days later and got several compliments and the scent grew on me. I will definitely be buying a bottle.",'Kelvin T., verified buyer','[SHOP ACQUA DI GIO PARFUM]'),
            review('CREED AVENTUS','The samples arrived quickly, and I love the option of ordering smaller testers before investing in a whole bottle. Will definitely be ordering more to give other fragrances a try. Thank you!','Todd J., verified buyer','[SHOP CREED AVENTUS]')])],
  [P('Their picks.'),P('Your turn to test.','h15'),BL(),
   cards(3,[[P('[PRODUCT TILE: Louis Vuitton Imagination bottle]','ph'),P('Louis Vuitton Imagination','b'),P('[STARS] Rated 4.5 out of 5','small'),P('2ml $39.99','small'),P('[SHOP NOW]','b')],
            [P('[PRODUCT TILE: Acqua Di Gio Parfum 2024 bottle]','ph'),P('Acqua Di Gio Parfum 2024','b'),P('[STARS] Rated 4.2 out of 5','small'),P('2ml $19.99','small'),P('[SHOP NOW]','b')],
            [P('[PRODUCT TILE: Creed Aventus bottle]','ph'),P('Creed Aventus','b'),P('[STARS] Rated 4.6 out of 5','small'),P('2ml $34.99','small'),P('[SHOP NOW]','b')]])],
  [P('Your 15% off ends **tonight at 11:59pm ET**.'),P('[CODE: REMEMBER15]'),P('[SHOP THE SALE]','b'),P('Free shipping over $50. Free 10ml travel size on orders over $100.','small')],
  [P('Footer','small')]])]
# -------- Email 4 (plain text)
L=lambda t,st=None:P(t,st,'left')
E[4]=[H2('Campaign | Last Chance | Veterans Day Sale Ends Tonight'),
 meta('Campaign | Last Chance | Veterans Day Sale Ends Tonight | Plain text','Fri, Nov 13, 2026 (evening, after Email 3)','Engaged list. Plain-text last call from Hamza: the Veterans Day sale ends tonight at 11:59pm ET.'),
 subj('Your 15% Ends Tonight','A quick note from Hamza before the Veterans Day sale closes.','Hamza @ Scent Pilot'),
 BL(),
 wire([
  [P('[PLAIN TEXT: no logo, no images, no buttons. Sent from Hamza @ Scent Pilot. Links in navy #4D6488.]','ph')],
  [L("Hey {{ person.first_name|default:'there' }},"),BL(),L('Quick one.'),BL(),L('The Veterans Day sale ends **tonight at 11:59pm ET.**'),BL(),
   L('Code **REMEMBER15** takes 15% off everything on the site. Every brand, every size, no exclusions.'),BL(),
   L("If there's a scent you've been circling, grab a decant tonight and find out for 15% less."),BL(),
   L('Orders over **$100** also unlock a **free 10ml travel size** from brands like Montblanc and Versace.'),BL(),
   ('p',[('SHOP THE SALE >>>','link')],'left'),BL(),L('Smell good,'),L('Hamza'),L('Founder, Scent Pilot'),BL(),
   L('P.S. Every sample is Authenticity Guaranteed or your money back.')]])]
N=lambda t: ('p',runs(t),None)
E[5]=[H2('Notes'),
 H3('To confirm before build'),
 N('**Codes.** Veterans Day emails use **REMEMBER15** (Wed Nov 11 to Fri Nov 13, 11:59pm ET). Black Friday emails will use **BLACKFRIDAY15**. Check REMEMBER15 is live in Shopify for the sale window and expires on time.'),
 N('**Free 10ml.** Customer does not pick. Copy follows the client: unlock a 10ml travel size from a select variety of brands like Montblanc and Versace on orders over $100.'),
 N('**Email 3 reviews.** Quoted in full and word for word from the product pages (Loox, verified buyers). Kept the customers\' own punctuation, including two exclamation marks. Kelvin T. mentions compliments; that is his experience, not a brand claim. Confirm the client is happy to quote these three.'),
 N('**Product overlap.** Creed Aventus, Acqua Di Gio Parfum 2024 and Louis Vuitton Imagination appear in Email 2 (best sellers) and again in Email 3 (the reviewed products) two days later. Swap Email 2\'s grid if you want no repeats.'),
 N('**Email 2 subject** is 6 words (TTM aims for 2 to 5). Kept because it mirrors the approved Labor Day subject "Labor Day Sale: 15% Off Sitewide".'),
 N('**Send times and audience tiers** for all four emails are not set yet. Email 3 goes in the morning and Email 4 in the evening on Nov 13.'),
 N('**Prices** shown are the 2ml price from scentpilot.com on Oct 31, 2026, before any discount.'),
 H3('Designer notes'),
 N('**All designed emails.** Reuse the approved Sep 22 system ("The Curated Way To Try 170+ Fragrances", Figma node 8990:498): black top bar, dark navy body, typewriter-style uppercase headlines, square white buttons, moody spotlit bottle shots, white footer.'),
 N('**Email 1 | Cold-Weather Scents.** Product lines reuse approved copy from past emails (Labor Day, "Your Fragrance Wardrobe Is Missing Something", Sep 22). Each SHOP button links to its product page (links below).'),
 N('**Email 2 | Veterans Day Sale Is Live.** Sale layout like the approved Labor Day email, but this sale needs code REMEMBER15 (Labor Day applied automatically). The code box holds only the code. No Veterans Day imagery or tie-in language was supplied, so keep it to the event name.'),
 N('**Email 3 | What Buyers Say.** Review cards stack one per row, never a grid. No customer photos used. Product tiles show each product\'s Loox rating.'),
 N('**Email 4 | Sale Ends Tonight.** Plain text in Klaviyo\'s text-only editor. No logo, images or buttons. Link text in navy, all caps, ending ">>>" (Hamza\'s founder-email habit). Link: https://scentpilot.com/'),
 H3('Links'),
 N('Tom Ford Tobacco Vanille: https://scentpilot.com/products/tom-ford-tobacco-vanille'),
 N('Jean Paul Gaultier Le Male Elixir: https://scentpilot.com/products/jean-paul-gaultier-le-male-elixir'),
 N('Azzaro The Most Wanted Parfum: https://scentpilot.com/products/azzaro-the-most-wanted-parfum'),
 N('Tom Ford Oud Wood: https://scentpilot.com/products/tom-ford-oud-wood'),
 N('Creed Aventus: https://scentpilot.com/products/creed-aventus'),
 N('Versace Eros Eau De Parfum: https://scentpilot.com/products/versace-eros-eau-de-parfum'),
 N('Acqua Di Gio Parfum 2024: https://scentpilot.com/products/acqua-di-gio-parfum-2024'),
 N('Louis Vuitton Imagination: https://scentpilot.com/products/louis-vuitton-imagination'),
 N('Shop all / sale: https://scentpilot.com/'),
 H3('Sources'),
 N('Offer, codes, dates and threshold: Danie, Oct 31, 2026. Voice, sign-off and authenticity lines: Scent Pilot brand record (Claude Project export). Product lines: approved past emails in the Scent Pilot Figma file. Prices, stock and ratings: scentpilot.com, Oct 31, 2026. Reviews: Loox reviews on scentpilot.com product pages.'),
 N('**Used reviews:** Email 3: Richard N. (Louis Vuitton Imagination), Kelvin T. (Acqua Di Gio Parfum 2024), Todd J. (Creed Aventus). Do not reuse these in other November emails.')]
n=int(sys.argv[1]); tab=sys.argv[2]
req=build(tab,E[n])
print(json.dumps(req,separators=(',',':')))
