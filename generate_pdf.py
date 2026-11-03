from fpdf import FPDF

class AfridiPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "The Afridi Tribe - A Comprehensive Guide", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 16)
        self.set_fill_color(44, 62, 80)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def sub_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(41, 128, 185)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def body_text(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 7, text)
        self.ln(3)

pdf = AfridiPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# ============================================
# PAGE 1-2: INTRODUCTION
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 1: Introduction to the Afridi Tribe")

pdf.body_text(
    "The Afridi (Pashto: Apridi) is one of the largest and most prominent Pashtun tribes "
    "residing primarily in the Khyber Pass region and surrounding areas of Pakistan and Afghanistan. "
    "The Afridi tribe is part of the Karlani confederation of Pashtun tribes and has played a "
    "significant role in the history of the Indian subcontinent and Central Asia. They are known "
    "for their fierce independence, warrior traditions, and strategic control of the Khyber Pass, "
    "one of the most important mountain passes in the world."
)

pdf.body_text(
    "The Afridis are considered one of the oldest Pashtun tribes, with a history dating back "
    "thousands of years. They trace their lineage to Afridi, son of Ibrahim, who was a descendant "
    "of Karlan, one of the legendary ancestors of the Pashtun people. The tribe has been mentioned "
    "in numerous historical texts, including those of Greek, Mughal, and British historians. "
    "Their strategic location along the Khyber Pass made them central to trade, invasion routes, "
    "and geopolitical struggles throughout history."
)

pdf.body_text(
    "The total population of the Afridi tribe is estimated to be around 3 to 5 million people. "
    "The majority reside in the Khyber district of Pakistan's Khyber Pakhtunkhwa province, "
    "while significant populations also exist in Peshawar, Kohat, Darra Adam Khel, and various "
    "parts of Afghanistan. Diaspora communities can be found in Karachi, Lahore, and other major "
    "cities of Pakistan, as well as in the Gulf countries and Europe."
)

pdf.sub_title("Geographic Location")
pdf.body_text(
    "The Afridi homeland is centered around the Khyber Pass and the Tirah Valley. The Khyber Pass "
    "connects Peshawar in Pakistan to Jalalabad in Afghanistan and has been one of the most "
    "important trade and invasion routes in Asian history. The Tirah Valley, located south of "
    "the Khyber Pass, is a mountainous region that served as the traditional stronghold of the "
    "Afridi tribe. The terrain is rugged, with high mountains, narrow valleys, and dense forests, "
    "making it naturally defensible."
)

pdf.body_text(
    "The Khyber district, formerly part of the Federally Administered Tribal Areas (FATA), "
    "was merged with Khyber Pakhtunkhwa province in 2018. The district headquarters is at "
    "Landi Kotal, and other important towns include Jamrud, Bara, and Ali Masjid. The Tirah "
    "Valley includes areas such as Rajgal, Maidan, and Bagh, which are home to various "
    "Afridi sub-tribes."
)

# ============================================
# PAGE 3-5: SUB-TRIBES
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 2: Sub-Tribes (Khels) of the Afridi")

pdf.body_text(
    "The Afridi tribe is divided into eight major sub-tribes, known as Khels. Each Khel has "
    "its own territory, leadership structure, and distinct identity within the larger Afridi "
    "tribal framework. The eight major Khels are:"
)

khels = [
    ("1. Adam Khel",
     "The Adam Khel is one of the most well-known Afridi sub-tribes. They are primarily "
     "located in the Darra Adam Khel area, between Peshawar and Kohat. The Adam Khel are "
     "famous worldwide for their gunsmithing skills. Darra Adam Khel is known as the 'Gun "
     "Village' where artisans have been manufacturing firearms for over a century. They produce "
     "replicas of various international weapons, from pistols to assault rifles. The population "
     "of Adam Khel is approximately 400,000-500,000. They are known for their business acumen "
     "and have significant commercial interests beyond gunsmithing, including transport, trade, "
     "and real estate in Peshawar and Kohat."),

    ("2. Aka Khel",
     "The Aka Khel reside primarily in the Bara area of Khyber district. They are one of the "
     "larger sub-tribes with a population estimated at 300,000-400,000. The Aka Khel have been "
     "historically involved in trade through the Khyber Pass and have strong commercial ties "
     "with Afghanistan. They are known for their involvement in the transport business and "
     "cross-border trade. The Bara market, located in their territory, was one of the largest "
     "smuggling markets in the tribal areas before government regulation."),

    ("3. Kuki Khel",
     "The Kuki Khel inhabit the area around Jamrud and parts of the Khyber Pass. They are "
     "considered one of the most strategically located sub-tribes as they control the entrance "
     "to the Khyber Pass from the Peshawar side. Historically, they were responsible for "
     "collecting tolls from caravans passing through the pass. The Kuki Khel have a population "
     "of approximately 200,000-300,000 and are known for their strong warrior tradition."),

    ("4. Malik Din Khel",
     "The Malik Din Khel are located in the central Khyber area. They have a population of "
     "approximately 150,000-200,000. The Malik Din Khel are known for their role in tribal "
     "jirgas (councils) and have produced several prominent tribal leaders and politicians. "
     "They have traditionally been involved in agriculture and livestock in the Tirah Valley."),

    ("5. Kambar Khel",
     "The Kambar Khel reside in the Tirah Valley and surrounding areas. They are one of the "
     "sub-tribes with strong presence in the mountainous Tirah region. With a population of "
     "approximately 150,000-200,000, they are known for their agricultural practices in the "
     "fertile valleys of Tirah. The Kambar Khel have historically been guardians of the "
     "western approaches to the Tirah Valley."),

    ("6. Kamar Khel",
     "The Kamar Khel are another significant sub-tribe residing in various parts of the Khyber "
     "district. They have a population of approximately 100,000-150,000. The Kamar Khel have "
     "been historically involved in trade and commerce, particularly in the transport sector. "
     "They have strong ties with other Afridi sub-tribes and often play mediating roles in "
     "inter-tribal disputes."),

    ("7. Zakha Khel",
     "The Zakha Khel inhabit the western parts of the Khyber district, closer to the Afghan "
     "border. They have a population of approximately 200,000-250,000. The Zakha Khel are known "
     "for their involvement in cross-border trade and have strong connections with Pashtun "
     "communities in Afghanistan. They control several important routes connecting Pakistan "
     "and Afghanistan through the tribal areas."),

    ("8. Sepah / Sipah",
     "The Sepah are the smallest of the eight major Afridi sub-tribes, with a population of "
     "approximately 50,000-100,000. Despite their smaller size, they hold strategic territory "
     "in the Khyber area. The Sepah have been historically known for their role as mediators "
     "and peacekeepers within the larger Afridi tribal structure.")
]

for title, desc in khels:
    pdf.sub_title(title)
    pdf.body_text(desc)

# ============================================
# PAGE 6-8: HISTORY
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 3: History of the Afridi Tribe")

pdf.sub_title("Ancient History")
pdf.body_text(
    "The history of the Afridi tribe stretches back to ancient times. Some historians believe "
    "that the Afridis are mentioned in the accounts of Alexander the Great's invasion of the "
    "Indian subcontinent in 326 BC. The Greek historians referred to the fierce mountain tribes "
    "that resisted Alexander's army as it passed through the region. The Afridis controlled "
    "the Khyber Pass, which was the main route for armies entering the Indian subcontinent "
    "from Central Asia."
)

pdf.body_text(
    "During the early Islamic period, the Afridi tribe came into contact with Muslim armies "
    "and gradually converted to Islam. By the 10th century, the majority of Afridis had "
    "embraced Islam. The tribe played a role in the spread of Islam in the region and produced "
    "several notable religious scholars. The Tirah Valley became an important center of "
    "Islamic learning and Pashtun culture."
)

pdf.sub_title("Mughal Era")
pdf.body_text(
    "During the Mughal Empire (1526-1857), the Afridi tribe had a complex relationship with "
    "the Mughal rulers. The Mughals recognized the strategic importance of the Khyber Pass "
    "and tried to maintain control over it through a combination of military force and diplomacy. "
    "Emperor Akbar established forts along the Khyber Pass and stationed troops to protect "
    "the trade routes. However, the Afridis frequently rebelled against Mughal authority and "
    "disrupted trade caravans when their demands were not met."
)

pdf.body_text(
    "The Mughal Emperor Aurangzeb faced one of the most significant Afridi uprisings in 1672, "
    "known as the Afridi-Mughal War. The Afridis, under the leadership of Aimal Khan Mohmand "
    "and in alliance with other Pashtun tribes, inflicted a devastating defeat on a Mughal "
    "army of 40,000 soldiers in the Khyber Pass. This battle is considered one of the most "
    "significant military events in Pashtun tribal history and demonstrated the fighting "
    "capabilities of the Afridi warriors."
)

pdf.sub_title("British Colonial Period")
pdf.body_text(
    "The British colonial period (1839-1947) was a defining era for the Afridi tribe. The "
    "British recognized the strategic importance of the Khyber Pass for their control of India "
    "and the defense against Russian expansion from Central Asia (the Great Game). The Afridis "
    "became central to British frontier policy and were involved in numerous conflicts with "
    "the colonial forces."
)

pdf.body_text(
    "The most significant conflict was the Tirah Campaign of 1897-1898. The Afridis, along "
    "with the Orakzai tribe, rose in revolt against British authority, capturing several "
    "British outposts including the forts at Landi Kotal and Ali Masjid. The British responded "
    "with a massive military expedition of over 35,000 troops, the largest frontier campaign "
    "they had ever undertaken. The campaign lasted several months and resulted in significant "
    "casualties on both sides. Although the British eventually occupied the Tirah Valley, they "
    "were unable to permanently subjugate the Afridis and had to negotiate terms."
)

pdf.body_text(
    "The British established the Khyber Rifles, a paramilitary force recruited primarily from "
    "the Afridi tribe, to maintain order in the Khyber Pass region. The Khyber Rifles became "
    "one of the most famous frontier forces and many Afridis served with distinction. The "
    "British also paid regular subsidies to Afridi maliks (chiefs) to ensure safe passage "
    "through the Khyber Pass."
)

pdf.sub_title("Post-Independence Period")
pdf.body_text(
    "After the creation of Pakistan in 1947, the Afridi tribal areas became part of the "
    "Federally Administered Tribal Areas (FATA). The Pakistani government largely continued "
    "the British system of governing the tribal areas through political agents and tribal "
    "maliks. The Afridi tribe maintained its traditional autonomy and governance structures "
    "under the Frontier Crimes Regulation (FCR), a colonial-era law."
)

pdf.body_text(
    "In 2018, the 25th Constitutional Amendment merged FATA with Khyber Pakhtunkhwa province, "
    "ending the special administrative status of the tribal areas. This was a historic change "
    "that brought the Afridi areas under the regular legal and administrative framework of "
    "Pakistan for the first time. The merger included provisions for economic development, "
    "establishment of regular courts, and extension of political rights to tribal citizens."
)

# ============================================
# PAGE 9-11: CULTURE
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 4: Culture and Traditions")

pdf.sub_title("Pashtunwali - The Code of Honor")
pdf.body_text(
    "The Afridi tribe, like all Pashtun tribes, follows Pashtunwali, the traditional code of "
    "conduct that governs Pashtun society. Pashtunwali is an unwritten ethical code that has "
    "been followed for centuries and forms the basis of Afridi social life. The key principles "
    "of Pashtunwali include:"
)

pdf.body_text(
    "Melmastia (Hospitality): The Afridis are known for their exceptional hospitality. Every "
    "Afridi household is expected to provide food, shelter, and protection to any guest, "
    "regardless of their background. Guests are treated with the utmost respect and refusing "
    "hospitality is considered a great dishonor. The hujra (guest house) is a central "
    "institution in every Afridi village where guests are entertained and community matters "
    "are discussed."
)

pdf.body_text(
    "Nanawatai (Asylum/Forgiveness): This is the principle of providing asylum to anyone who "
    "seeks protection, even if they are an enemy. When someone enters an Afridi home seeking "
    "refuge, the host is obligated to protect them at all costs, even at the risk of their "
    "own life. This principle also extends to seeking forgiveness - if an offender comes to "
    "the house of the offended party seeking forgiveness, it is considered dishonorable to "
    "refuse."
)

pdf.body_text(
    "Badal (Revenge/Justice): The principle of reciprocity and justice is deeply ingrained in "
    "Afridi culture. If someone is wronged, they or their family have the right and obligation "
    "to seek revenge or justice. This can lead to blood feuds that sometimes last for "
    "generations. However, badal also applies to positive actions - a good deed must be "
    "reciprocated with an equal or greater good deed."
)

pdf.body_text(
    "Ghairat (Honor): Personal and family honor is of paramount importance in Afridi society. "
    "The Afridis will go to great lengths to protect their honor and the honor of their family "
    "and tribe. Any insult or slight to one's honor must be addressed, and the concept of "
    "ghairat extends to the protection of women, property, and tribal land."
)

pdf.body_text(
    "Namus (Protection of Women): The protection of women's honor and dignity is a fundamental "
    "aspect of Afridi culture. Women are considered the honor of the family and tribe, and "
    "any disrespect toward women is considered a grave offense that demands immediate action."
)

pdf.sub_title("Jirga System")
pdf.body_text(
    "The Jirga is the traditional decision-making assembly of the Afridi tribe. It is a "
    "council of elders and respected members of the community who gather to resolve disputes, "
    "make important decisions, and maintain social order. The Jirga system operates at multiple "
    "levels - from the village level to the sub-tribal level to the overall tribal level. "
    "Decisions in the Jirga are made through consensus, and the rulings are binding on all "
    "parties. The Jirga system has been the primary mechanism of governance and justice in "
    "Afridi society for centuries, predating any formal legal system."
)

pdf.sub_title("Language and Literature")
pdf.body_text(
    "The Afridis speak Pashto, which belongs to the Eastern Iranian branch of the Indo-European "
    "language family. The dialect spoken by the Afridis is the Pakhto (hard Pashto) variant, "
    "which is the northern dialect of the language. Pashto has a rich literary tradition, and "
    "the Afridis have contributed to Pashto literature through poetry, folk tales, and songs. "
    "The oral tradition of storytelling is particularly strong among the Afridis, with tales "
    "of heroism, love, and tribal history being passed down through generations."
)

pdf.sub_title("Music and Dance")
pdf.body_text(
    "The Attan is the traditional Pashtun dance performed by the Afridis on occasions such as "
    "weddings, celebrations, and tribal gatherings. It is a circular group dance performed to "
    "the beat of drums (dhol) and other traditional instruments. The dance starts slowly and "
    "gradually increases in speed, with dancers moving in a circle with synchronized steps. "
    "Traditional Afridi music features instruments such as the rabab (a stringed instrument), "
    "the harmonium, the tabla, and the dhol. Folk songs often celebrate bravery, love, and "
    "the beauty of the tribal homeland."
)

pdf.sub_title("Traditional Dress")
pdf.body_text(
    "The traditional Afridi dress for men consists of the shalwar kameez (loose trousers and "
    "long shirt), typically in white or light colors. A waistcoat (waskat) is often worn over "
    "the kameez, and a turban (lungi or pagri) or Chitrali cap is worn on the head. Many "
    "Afridi men traditionally carry a rifle or a knife as a symbol of their warrior identity. "
    "Women wear colorful embroidered dresses with elaborate patterns, along with traditional "
    "jewelry including nose rings, earrings, necklaces, and bangles."
)

pdf.sub_title("Food and Cuisine")
pdf.body_text(
    "Afridi cuisine is hearty and meat-based, reflecting the tribal lifestyle. The most famous "
    "dish is Chapli Kebab, a spiced meat patty that originated in the Pashtun tribal areas. "
    "Other popular dishes include Namkeen Gosht (salted meat), Kabuli Pulao (rice with meat "
    "and carrots), Mantu (meat dumplings), Sajji (whole roasted lamb), and Tikka (grilled "
    "meat). Green tea (kahwa) is the traditional beverage and is served with every meal and "
    "to every guest. Bread (naan or roti) is a staple of every meal and is baked fresh in "
    "traditional tandoor ovens."
)

# ============================================
# PAGE 12-13: ECONOMY
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 5: Economy and Livelihood")

pdf.sub_title("Traditional Economy")
pdf.body_text(
    "The traditional economy of the Afridi tribe was based on a combination of agriculture, "
    "livestock herding, and trade. The fertile valleys of Tirah and the areas around the Khyber "
    "Pass supported agriculture, with crops including wheat, maize, barley, and various fruits. "
    "Livestock, including sheep, goats, cattle, and horses, played an important role in the "
    "tribal economy. The Afridis also earned income by controlling the Khyber Pass and charging "
    "tolls on trade caravans passing through their territory."
)

pdf.sub_title("Arms Manufacturing")
pdf.body_text(
    "The Adam Khel sub-tribe is world-famous for its arms manufacturing industry, centered "
    "in Darra Adam Khel. This cottage industry has been operating for over 100 years and "
    "produces replicas of various international weapons, from handguns to assault rifles. "
    "The craftsmen of Darra Adam Khel are known for their remarkable skill in replicating "
    "weapons using basic tools and without modern machinery. While the legal status of this "
    "industry has been debated, it has been a significant source of income and employment "
    "for the local population. The Pakistani government has attempted to regulate the industry "
    "and encourage the artisans to shift to legitimate manufacturing."
)

pdf.sub_title("Trade and Commerce")
pdf.body_text(
    "The Afridi tribe has historically been involved in trade and commerce, particularly "
    "cross-border trade between Pakistan and Afghanistan. The Bara market in Khyber district "
    "was one of the largest commercial centers in the tribal areas, dealing in a wide range "
    "of goods including electronics, textiles, spices, and other consumer products. Many "
    "Afridi businessmen have established successful trading companies in Peshawar, Karachi, "
    "and other major cities. The transport sector is another major area of Afridi economic "
    "activity, with many tribesmen owning and operating trucks and buses."
)

pdf.sub_title("Modern Economy")
pdf.body_text(
    "In recent decades, the Afridi economy has diversified significantly. Many tribesmen have "
    "moved to urban areas for education and employment. Afridi professionals can be found in "
    "various fields including medicine, engineering, law, business, military, and civil service. "
    "The merger of FATA with Khyber Pakhtunkhwa has opened new economic opportunities, with "
    "government investments in infrastructure, education, and health facilities. The marble "
    "and minerals industry has also grown in the Afridi areas, with significant deposits of "
    "marble, chromite, and other minerals being commercially exploited."
)

# ============================================
# PAGE 14-15: NOTABLE PERSONALITIES
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 6: Notable Afridi Personalities")

pdf.sub_title("Historical Figures")
pdf.body_text(
    "Sultan Khel Afridi: A legendary warrior chief who led the Afridi resistance against the "
    "Mughal Empire in the 17th century. He organized a coalition of Afridi sub-tribes that "
    "successfully defended the Tirah Valley against Mughal incursions."
)

pdf.body_text(
    "Ajab Khan Afridi (1901-2002): A legendary figure who became famous for his daring "
    "abduction of a British girl named Molly Ellis in 1923 from Kohat. The incident became "
    "an international sensation and highlighted the Afridi resistance to British rule. Ajab "
    "Khan later became a respected tribal elder and lived to be over 100 years old."
)

pdf.body_text(
    "Shahid Afridi: Born Sahibzada Mohammad Shahid Khan Afridi in 1980, he is one of the most "
    "famous cricketers in the world. Known as 'Boom Boom Afridi' for his aggressive batting "
    "style, he represented Pakistan in international cricket for over 20 years. He holds "
    "several records including the fastest ODI century (37 balls, later broken). He served as "
    "captain of the Pakistan cricket team and is now involved in philanthropy through the "
    "Shahid Afridi Foundation, which provides education and healthcare services."
)

pdf.sub_title("Political Figures")
pdf.body_text(
    "The Afridi tribe has produced numerous political leaders at both the provincial and national "
    "levels. Several Afridis have served as members of the National Assembly and Senate of "
    "Pakistan. The tribe has also had representation in the Khyber Pakhtunkhwa provincial "
    "assembly. Afridi political leaders have been at the forefront of advocating for the "
    "development of the tribal areas and the rights of tribal people."
)

pdf.sub_title("Military Figures")
pdf.body_text(
    "The Afridis have a long tradition of military service and have produced several high-ranking "
    "officers in the Pakistan Armed Forces. Many Afridis serve in the Pakistan Army, particularly "
    "in the Frontier Force Regiment and the Khyber Rifles (now part of the Frontier Corps). "
    "Afridi soldiers have served with distinction in various conflicts and peacekeeping missions. "
    "The martial traditions of the tribe make military service a highly respected profession "
    "among the Afridis."
)

pdf.sub_title("Religious Scholars")
pdf.body_text(
    "The Afridi tribe has produced many notable religious scholars and spiritual leaders. "
    "The Tirah Valley has been home to several madrassas (religious seminaries) and Islamic "
    "learning centers. Afridi religious scholars have contributed to Islamic education and "
    "jurisprudence, and many have authored important religious texts in Pashto and Arabic. "
    "The Sufi tradition has also had a significant influence in the Afridi areas, with several "
    "Sufi shrines being important spiritual centers."
)

# ============================================
# PAGE 16-17: KHYBER PASS
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 7: The Khyber Pass - Gateway of History")

pdf.body_text(
    "The Khyber Pass is perhaps the most famous mountain pass in the world, and its history "
    "is inseparable from the history of the Afridi tribe. The pass stretches approximately "
    "53 kilometers (33 miles) from the Afghan border to the outskirts of Peshawar. At its "
    "narrowest point, the pass is only about 3 meters (10 feet) wide, making it a natural "
    "chokepoint that could be defended by a small number of fighters."
)

pdf.body_text(
    "Throughout history, every major invasion of the Indian subcontinent from Central Asia "
    "passed through the Khyber Pass, including those of Alexander the Great, the Mongols, "
    "Mahmud of Ghazni, Babur (founder of the Mughal Empire), Nadir Shah, and Ahmad Shah "
    "Durrani. The Afridis, as the guardians of the pass, were involved in or affected by "
    "all these historical events."
)

pdf.body_text(
    "The strategic importance of the Khyber Pass continued into the modern era. During the "
    "British colonial period, it was a crucial route for military campaigns and trade. During "
    "the Soviet-Afghan War (1979-1989), the pass was used to supply the Afghan mujahideen "
    "with weapons and supplies. Even today, the Khyber Pass remains an important trade route "
    "between Pakistan and Afghanistan, with thousands of trucks passing through daily."
)

pdf.sub_title("Key Landmarks")
pdf.body_text(
    "Bab-e-Khyber (Gateway of the Khyber): A large arch at the entrance of the pass near "
    "Jamrud, built as a monument to mark the beginning of the historic route. It is one of "
    "the most iconic landmarks of the tribal areas."
)

pdf.body_text(
    "Jamrud Fort: Built by Sikh General Hari Singh Nalwa in 1823 at the eastern entrance "
    "of the Khyber Pass. The fort has been the site of several battles and remains a "
    "significant historical monument."
)

pdf.body_text(
    "Ali Masjid Fort: Located at a strategic narrow point in the pass, this fort has been "
    "fought over by numerous armies throughout history. It overlooks the pass from a "
    "commanding height and was a key British military outpost."
)

pdf.body_text(
    "Landi Kotal: The town at the western end of the Khyber Pass, near the Afghan border. "
    "It serves as the headquarters of the Khyber district and is the last major town before "
    "entering Afghanistan. Landi Kotal has been an important trading post for centuries."
)

# ============================================
# PAGE 18-19: TIRAH VALLEY
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 8: Tirah Valley - The Afridi Heartland")

pdf.body_text(
    "The Tirah Valley is the traditional heartland of the Afridi tribe and one of the most "
    "inaccessible and mysterious regions in all of Pakistan. Located south of the Khyber Pass "
    "in the mountains between Pakistan and Afghanistan, the valley has remained largely "
    "isolated from the outside world for centuries. The name 'Tirah' is believed to come from "
    "the Pashto word meaning 'darkness' or 'shade', referring to the dense forest cover of "
    "the valley."
)

pdf.body_text(
    "The Tirah Valley is divided into two main areas: Maidan (the upper valley) and Rajgal "
    "(the lower valley). Maidan is a relatively flat, fertile area at an altitude of about "
    "1,800-2,100 meters (6,000-7,000 feet) above sea level. It is known for its pleasant "
    "climate, lush green meadows, and pine forests. Rajgal is a narrower, more rugged valley "
    "that extends toward the Afghan border."
)

pdf.sub_title("Natural Beauty")
pdf.body_text(
    "The Tirah Valley is known for its exceptional natural beauty. The valley is covered with "
    "dense forests of pine, deodar, and oak trees. Crystal-clear streams flow through the "
    "valleys, and the higher elevations are covered with snow during winter. The area is home "
    "to diverse wildlife, including leopards, bears, wolves, foxes, and various species of "
    "birds. The wildflowers that bloom in spring and summer cover the meadows in a carpet "
    "of colors, making the valley one of the most scenic places in Pakistan."
)

pdf.sub_title("Agriculture in Tirah")
pdf.body_text(
    "The fertile soil of the Tirah Valley supports a variety of crops. Wheat and maize are "
    "the main staple crops, along with barley, rice, and various vegetables. The valley is "
    "also known for its fruit orchards, producing apples, apricots, peaches, plums, walnuts, "
    "and almonds. Honey production is another important agricultural activity, with the "
    "wildflower honey of Tirah being considered among the finest in the region. "
    "Livestock farming, particularly sheep and goat herding, is also a major economic activity."
)

# ============================================
# PAGE 20-21: EDUCATION
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 9: Education and Development")

pdf.body_text(
    "Education has been a growing priority for the Afridi tribe in recent decades. While "
    "literacy rates in the tribal areas have historically been among the lowest in Pakistan, "
    "there has been significant progress in recent years. The merger of FATA with Khyber "
    "Pakhtunkhwa has brought increased government investment in education infrastructure."
)

pdf.sub_title("Educational Institutions")
pdf.body_text(
    "Several schools, colleges, and vocational training centers have been established in the "
    "Afridi areas. Government schools exist in most major towns, and private educational "
    "institutions have also been established. The Afridi community has also set up educational "
    "trusts and foundations to support education. Many Afridi students pursue higher education "
    "in Peshawar, Islamabad, and other cities, with some going abroad for advanced studies."
)

pdf.sub_title("Healthcare")
pdf.body_text(
    "Healthcare infrastructure in the Afridi areas has improved significantly in recent years. "
    "Government hospitals and health centers have been established in major towns such as "
    "Landi Kotal, Jamrud, and Bara. However, healthcare facilities in remote areas like the "
    "Tirah Valley remain limited. Non-governmental organizations and philanthropic "
    "organizations, including the Shahid Afridi Foundation, have played an important role in "
    "providing healthcare services to underserved areas."
)

pdf.sub_title("Infrastructure Development")
pdf.body_text(
    "The merger of FATA with Khyber Pakhtunkhwa has accelerated infrastructure development "
    "in the Afridi areas. Road construction projects have improved connectivity between "
    "remote areas and urban centers. Electricity supply has been extended to many previously "
    "unserved areas. Mobile phone and internet connectivity have also expanded, connecting "
    "the tribal areas with the rest of the world. The government has allocated special "
    "development funds for the former FATA areas, and international development organizations "
    "have also invested in various projects."
)

# ============================================
# PAGE 22-23: CHALLENGES
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 10: Contemporary Challenges")

pdf.sub_title("Security Issues")
pdf.body_text(
    "The Afridi areas have faced significant security challenges, particularly during the "
    "War on Terror period from 2001 onwards. Militant groups established presence in some "
    "parts of the Khyber district and the Tirah Valley, leading to military operations and "
    "displacement of civilians. The Pakistan military conducted several operations, including "
    "Operation Khyber I, II, III, and IV, to clear the area of militants. These operations "
    "resulted in significant displacement of the civilian population, with thousands of "
    "families having to leave their homes and take refuge in Peshawar and other cities."
)

pdf.sub_title("Displacement and Return")
pdf.body_text(
    "The military operations caused massive displacement of the Afridi population. At the "
    "peak of the displacement, hundreds of thousands of people were living in camps or with "
    "relatives in settled areas. The return process has been gradual, with many families still "
    "unable to return to their homes due to damaged infrastructure and ongoing security "
    "concerns. The government has provided compensation and assistance for returning families, "
    "but the process of rehabilitation and reconstruction remains incomplete."
)

pdf.sub_title("Economic Challenges")
pdf.body_text(
    "The Afridi areas face significant economic challenges, including high unemployment, "
    "limited industrialization, and dependence on traditional economic activities. The "
    "disruption caused by military operations and displacement has further exacerbated "
    "economic difficulties. Young people, in particular, face limited employment opportunities "
    "in their home areas, leading to migration to urban centers and overseas. The regulation "
    "of the arms industry in Darra Adam Khel has affected the livelihood of thousands of "
    "artisans who depend on this trade."
)

pdf.sub_title("Cultural Preservation")
pdf.body_text(
    "Like many indigenous communities worldwide, the Afridi tribe faces the challenge of "
    "preserving its cultural heritage in the face of modernization and globalization. "
    "Traditional practices, customs, and the Pashto language are under pressure from "
    "urbanization and exposure to mainstream media. Younger generations, particularly those "
    "living in urban areas, may be losing touch with their tribal heritage. Efforts are "
    "being made by cultural organizations and tribal elders to document and preserve Afridi "
    "traditions, including oral histories, folk songs, and traditional crafts."
)

# ============================================
# PAGE 24-25: FUTURE
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 11: The Future of the Afridi Tribe")

pdf.body_text(
    "The Afridi tribe stands at a crossroads between tradition and modernity. The merger "
    "of FATA with Khyber Pakhtunkhwa represents a new chapter in the history of the tribe, "
    "bringing both opportunities and challenges. The integration into the regular "
    "administrative and legal framework of Pakistan opens up new avenues for development, "
    "political participation, and economic growth."
)

pdf.sub_title("Political Integration")
pdf.body_text(
    "The merger has given the Afridi people full political rights, including the right to "
    "vote in provincial and national elections on an equal footing with other citizens. "
    "This political integration is expected to bring greater representation and voice to "
    "the Afridi community in the corridors of power. Several Afridi politicians have already "
    "emerged as significant figures in provincial and national politics."
)

pdf.sub_title("Economic Development Plans")
pdf.body_text(
    "The government has announced several economic development plans for the former FATA "
    "areas, including special economic zones, industrial estates, and tourism development "
    "projects. The Tirah Valley, with its exceptional natural beauty, has the potential to "
    "become a major tourist destination. The arms manufacturing skills of the Adam Khel "
    "craftsmen could be channeled into legitimate manufacturing industries. Cross-border "
    "trade through the Khyber Pass continues to be a significant economic opportunity."
)

pdf.sub_title("Education and Youth")
pdf.body_text(
    "The younger generation of Afridis is increasingly focused on education and professional "
    "development. Many young Afridis are pursuing higher education and establishing careers "
    "in various fields. This educated young generation is expected to play a crucial role in "
    "the development and modernization of the Afridi areas while maintaining the positive "
    "aspects of their tribal heritage."
)

pdf.body_text(
    "The future of the Afridi tribe will depend on the ability of its people to balance "
    "tradition with modernity, preserve their cultural identity while embracing change, and "
    "leverage their strategic location and human resources for sustainable development. With "
    "their history of resilience, adaptability, and determination, the Afridis are well "
    "positioned to meet the challenges and opportunities of the 21st century."
)

# ============================================
# PAGE 26: SUMMARY
# ============================================
pdf.add_page()
pdf.chapter_title("Chapter 12: Quick Reference Summary")

pdf.sub_title("Key Facts about the Afridi Tribe")

facts = [
    "Tribe Name: Afridi (Pashto: Apridi)",
    "Confederation: Karlani Pashtun",
    "Population: Estimated 3-5 million",
    "Location: Khyber District, Khyber Pakhtunkhwa, Pakistan",
    "Major Areas: Khyber Pass, Tirah Valley, Darra Adam Khel",
    "Language: Pashto (Pakhto/Northern dialect)",
    "Religion: Islam (predominantly Sunni, Hanafi school)",
    "Major Sub-tribes: 8 Khels - Adam Khel, Aka Khel, Kuki Khel, Malik Din Khel, Kambar Khel, Kamar Khel, Zakha Khel, Sepah",
    "Famous For: Control of Khyber Pass, warrior tradition, Pashtunwali code",
    "Economy: Trade, arms manufacturing (Darra Adam Khel), agriculture, livestock, transport",
    "Key Historical Events: Mughal-Afridi War (1672), Tirah Campaign (1897-98), FATA merger (2018)",
    "Notable Personality: Shahid Afridi (cricketer), Ajab Khan Afridi (freedom fighter)",
    "Traditional Governance: Jirga system (council of elders)",
    "Cultural Practices: Attan (dance), Pashtunwali (code of honor), Hujra (guest house)",
    "Cuisine: Chapli Kebab, Namkeen Gosht, Kabuli Pulao, Sajji, Kahwa (green tea)",
]

for fact in facts:
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(5, 7, "-")
    pdf.multi_cell(0, 7, fact)
    pdf.ln(1)

# Save PDF
output_path = "./data/your_document.pdf"
pdf.output(output_path)
print(f"PDF saved to {output_path}")
print(f"Total pages: {pdf.page_no()}")
