import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# --- Color Palette (Lively, Vibrant & Modern Business Proposal) ---
DEEP_GREEN    = RGBColor(30, 77, 54)     # #1E4D36 Deep Forest
VIBRANT_MINT  = RGBColor(42, 157, 143)   # #2A9D8F Fresh Mint
CORAL_WARM    = RGBColor(231, 111, 81)   # #E76F51 Energetic Coral
AMBER_GOLD    = RGBColor(244, 162, 97)   # #F4A261 Sun Amber
OCEAN_BLUE    = RGBColor(2, 132, 199)    # #0284C7 Ocean Blue
DARK_TEXT     = RGBColor(34, 34, 34)     # #222222 Crisp Charcoal
MUTED_TEXT    = RGBColor(74, 85, 78)     # #4A554E Slate Charcoal
WHITE         = RGBColor(255, 255, 255)
BORDER_LIGHT  = RGBColor(226, 232, 240)

# Card Background Tints
TINT_MINT     = RGBColor(242, 249, 246)
TINT_CORAL    = RGBColor(254, 244, 240)
TINT_AMBER    = RGBColor(255, 249, 238)
TINT_BLUE     = RGBColor(240, 248, 255)

FONT_HEADING = "Microsoft JhengHei"
FONT_BODY    = "Microsoft JhengHei"
FONT_EN      = "Arial"

# Image Paths from user's extracted media
IMG_ANNA = "/Users/annamei/notes/extracted_images/anna_photo.jpg"
IMG_DIFF = "/Users/annamei/notes/extracted_images/image3.png"
IMG_COST = "/Users/annamei/notes/extracted_images/image2.png"
IMG_EVOL = "/Users/annamei/notes/extracted_images/image4.png"

def add_dot_grid(slide, left, top, cols=5, rows=4, color=DEEP_GREEN):
    tb = slide.shapes.add_textbox(left, top, Inches(1.5), Inches(1.0))
    tf = tb.text_frame
    tf.word_wrap = False
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    dot_line = " ".join(["•"] * cols)
    for r in range(rows):
        p = tf.paragraphs[0] if r == 0 else tf.add_paragraph()
        p.text = dot_line
        p.font.name = FONT_EN
        p.font.size = Pt(11)
        p.font.color.rgb = color
        p.line_spacing = Pt(13)

def add_header(slide, en_tag, cn_title, subtitle=""):
    """Vibrant top banner matching Business Proposal.pdf with prominent typography"""
    # Top Tag Pill
    tag_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.35), Inches(2.6), Inches(0.42))
    tag_pill.fill.solid()
    tag_pill.fill.fore_color.rgb = DEEP_GREEN
    tag_pill.line.fill.background()
    p_tag = tag_pill.text_frame.paragraphs[0]
    p_tag.text = en_tag.upper()
    p_tag.font.name = FONT_EN
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = WHITE
    p_tag.alignment = PP_ALIGN.CENTER
    
    # Title Textbox
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(10.5), Inches(1.0))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_bottom = tf.margin_right = 0
    
    p = tf.paragraphs[0]
    p.text = cn_title
    p.font.name = FONT_HEADING
    p.font.size = Pt(23)
    p.font.bold = True
    p.font.color.rgb = DEEP_GREEN
    
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = FONT_BODY
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = MUTED_TEXT
        p2.space_before = Pt(3)

    # Decorative dots top right
    add_dot_grid(slide, Inches(11.6), Inches(0.35), cols=5, rows=3, color=VIBRANT_MINT)

def create_card(slide, left, top, width, height, bg_color=WHITE, border_color=BORDER_LIGHT, line_width=1.2):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(line_width)
    else:
        card.line.fill.background()
    return card

# ==============================================================================
# SLIDE 1: 標題 (Cover) - Exact user text, prominent, vibrant, left-to-right
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)

# Top green pill
pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.6), Inches(2.4), Inches(0.38))
pill1.fill.solid()
pill1.fill.fore_color.rgb = DEEP_GREEN
pill1.line.fill.background()
p_pill = pill1.text_frame.paragraphs[0]
p_pill.text = "★ 成果專題簡報"
p_pill.font.name = FONT_HEADING
p_pill.font.size = Pt(11)
p_pill.font.bold = True
p_pill.font.color.rgb = WHITE
p_pill.alignment = PP_ALIGN.CENTER

add_dot_grid(s1, Inches(0.4), Inches(0.5), cols=4, rows=5, color=VIBRANT_MINT)

# Main Title (Prominent, bold, colorful)
tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(6.0), Inches(2.6))
tf1 = tb1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = 0

p1 = tf1.paragraphs[0]
p1.text = "FocusLingua"
p1.font.name = FONT_EN
p1.font.size = Pt(40)
p1.font.bold = True
p1.font.color.rgb = DEEP_GREEN

p2 = tf1.add_paragraph()
p2.text = "微型多感官學習對話系統"
p2.font.name = FONT_HEADING
p2.font.size = Pt(26)
p2.font.bold = True
p2.font.color.rgb = CORAL_WARM
p2.space_before = Pt(4)

# Subtitle & Presenter Box (Lively card)
c_sub = create_card(s1, Inches(1.0), Inches(4.3), Inches(5.9), Inches(2.2), bg_color=TINT_MINT, border_color=VIBRANT_MINT, line_width=1.5)
tb_sub = s1.shapes.add_textbox(Inches(1.25), Inches(4.5), Inches(5.4), Inches(1.8))
tf_sub = tb_sub.text_frame
tf_sub.word_wrap = True
tf_sub.margin_left = tf_sub.margin_top = 0

ps1 = tf_sub.paragraphs[0]
ps1.text = "希伯崙 LiveABC 產學實習成果"
ps1.font.name = FONT_HEADING
ps1.font.size = Pt(14)
ps1.font.bold = True
ps1.font.color.rgb = DEEP_GREEN

ps2 = tf_sub.add_paragraph()
ps2.text = "專題發表人：陳詠芸 Anna Chen"
ps2.font.name = FONT_HEADING
ps2.font.size = Pt(15)
ps2.font.bold = True
ps2.font.color.rgb = DARK_TEXT
ps2.space_before = Pt(10)

# Right Side Photo with lively multi-layered border
frame_bg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.4), Inches(1.0), Inches(5.1), Inches(5.5))
frame_bg.fill.solid()
frame_bg.fill.fore_color.rgb = TINT_CORAL
frame_bg.line.color.rgb = CORAL_WARM
frame_bg.line.width = Pt(2.5)

if os.path.exists(IMG_ANNA):
    s1.shapes.add_picture(IMG_ANNA, Inches(7.55), Inches(1.15), Inches(4.8), Inches(5.2))

add_dot_grid(s1, Inches(11.6), Inches(6.1), cols=5, rows=4, color=AMBER_GOLD)


# ==============================================================================
# SLIDE 2: 目錄 (Content) - Exact user text, prominent, left-to-right flow
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)

# Left solid green decorative block
left_block = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.9), Inches(7.5))
left_block.fill.solid()
left_block.fill.fore_color.rgb = DEEP_GREEN
left_block.line.fill.background()

# Prominent Title
tb2 = s2.shapes.add_textbox(Inches(1.4), Inches(0.6), Inches(4.0), Inches(0.9))
tf2 = tb2.text_frame
tf2.margin_left = tf2.margin_top = 0
p = tf2.paragraphs[0]
p.text = "Content"
p.font.name = FONT_EN
p.font.size = Pt(38)
p.font.bold = True
p.font.color.rgb = DEEP_GREEN

p_sub = tf2.add_paragraph()
p_sub.text = "簡報目錄"
p_sub.font.name = FONT_HEADING
p_sub.font.size = Pt(14)
p_sub.font.bold = True
p_sub.font.color.rgb = VIBRANT_MINT
p_sub.space_before = Pt(2)

# 7 Items arranged in colorful horizontal cards (Left to Right flow)
user_agenda = [
    ("01", "自我介紹", VIBRANT_MINT, TINT_MINT),
    ("02", "專案動機", CORAL_WARM, TINT_CORAL),
    ("03", "企業實務痛點", AMBER_GOLD, TINT_AMBER),
    ("04", "專案架構與微型展示", OCEAN_BLUE, TINT_BLUE),
    ("05", "導入效益分析", VIBRANT_MINT, TINT_MINT),
    ("06", "未來擴散性與再精進", CORAL_WARM, TINT_CORAL),
    ("07", "個人學習成果與反思", DEEP_GREEN, TINT_MINT)
]

for idx, (num, text, color, tint) in enumerate(user_agenda):
    y = Inches(1.75 + idx * 0.76)
    
    # Card
    c = create_card(s2, Inches(1.4), y, Inches(9.8), Inches(0.64), bg_color=WHITE, border_color=color, line_width=1.2)
    
    # Left pill with number
    num_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), y + Inches(0.08), Inches(0.7), Inches(0.48))
    num_box.fill.solid()
    num_box.fill.fore_color.rgb = tint
    num_box.line.color.rgb = color
    num_box.line.width = Pt(1)
    np = num_box.text_frame.paragraphs[0]
    np.text = num
    np.font.name = FONT_EN
    np.font.size = Pt(14)
    np.font.bold = True
    np.font.color.rgb = color
    np.alignment = PP_ALIGN.CENTER
    
    # Title Text
    ttb = s2.shapes.add_textbox(Inches(2.35), y + Inches(0.12), Inches(8.5), Inches(0.45))
    ttf = ttb.text_frame
    ttf.margin_left = ttf.margin_top = 0
    tp = ttf.paragraphs[0]
    tp.text = text
    tp.font.name = FONT_HEADING
    tp.font.size = Pt(14)
    tp.font.bold = True
    tp.font.color.rgb = DARK_TEXT

add_dot_grid(s2, Inches(11.6), Inches(1.5), cols=4, rows=12, color=AMBER_GOLD)


# ==============================================================================
# SLIDE 3: 自我介紹 (About Presenter) - Exact user text, lively cards
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "About Presenter", "自我介紹")

# Left Column: Profile Card
pcard = create_card(s3, Inches(0.8), Inches(1.9), Inches(3.6), Inches(5.1), bg_color=TINT_MINT, border_color=VIBRANT_MINT, line_width=1.5)

if os.path.exists(IMG_ANNA):
    s3.shapes.add_picture(IMG_ANNA, Inches(1.05), Inches(2.1), Inches(3.1), Inches(2.4))

ptb = s3.shapes.add_textbox(Inches(1.0), Inches(4.65), Inches(3.2), Inches(2.2))
ptf = ptb.text_frame
ptf.word_wrap = True
ptf.margin_left = ptf.margin_top = 0

lp1 = ptf.paragraphs[0]
lp1.text = "陳詠芸 Anna Chen"
lp1.font.name = FONT_HEADING
lp1.font.size = Pt(17)
lp1.font.bold = True
lp1.font.color.rgb = DEEP_GREEN
lp1.alignment = PP_ALIGN.CENTER

lp2 = ptf.add_paragraph()
lp2.text = "中原大學四年級學生\n科系：應用外語＆財務金融學系"
lp2.font.name = FONT_BODY
lp2.font.size = Pt(11)
lp2.font.color.rgb = DARK_TEXT
lp2.alignment = PP_ALIGN.CENTER
lp2.space_before = Pt(6)

# Right Column: 4 Experiences (Exact User Text)
exp_list = [
    ("113中原國小晨間英語課輔老師", CORAL_WARM, TINT_CORAL, "🏫"),
    ("中原大學特資中心 英語課輔老師", VIBRANT_MINT, TINT_MINT, "🤝"),
    ("LiveABC 希伯崙 研發三處實習生 & 人事部工讀", OCEAN_BLUE, TINT_BLUE, "📚"),
    ("加拿大 Athabasca Univ. VIP Research 實習", AMBER_GOLD, TINT_AMBER, "🌐")
]

for idx, (exp_text, col, tint, icon) in enumerate(exp_list):
    y = Inches(1.9 + idx * 1.25)
    c = create_card(s3, Inches(4.7), y, Inches(7.8), Inches(1.1), bg_color=WHITE, border_color=col, line_width=1.5)
    
    # Left decorative badge
    badge = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.9), y + Inches(0.2), Inches(0.7), Inches(0.7))
    badge.fill.solid()
    badge.fill.fore_color.rgb = tint
    badge.line.color.rgb = col
    badge.line.width = Pt(1)
    bp = badge.text_frame.paragraphs[0]
    bp.text = icon
    bp.font.name = FONT_HEADING
    bp.font.size = Pt(18)
    bp.alignment = PP_ALIGN.CENTER
    
    tb = s3.shapes.add_textbox(Inches(5.8), y + Inches(0.3), Inches(6.5), Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    p = tf.paragraphs[0]
    p.text = exp_text
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT


# ==============================================================================
# SLIDE 4: 專案動機 (Motivation) - Exact user text, 2 horizontal cards with pictures
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "Motivation", "專案動機：「被忽視的認知極限」")

# Card 1 (Left): ADHD 孩子的學習阻力
c1 = create_card(s4, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.1), bg_color=WHITE, border_color=CORAL_WARM, line_width=1.5)
# Top accent
t1 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.7), Inches(0.1))
t1.fill.solid()
t1.fill.fore_color.rgb = CORAL_WARM
t1.line.fill.background()

# Image 3 inside Card 1
if os.path.exists(IMG_DIFF):
    s4.shapes.add_picture(IMG_DIFF, Inches(4.7), Inches(2.1), Inches(1.5), Inches(1.5))

tb4_1 = s4.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(3.5), Inches(1.5))
tf4_1 = tb4_1.text_frame
tf4_1.word_wrap = True
tf4_1.margin_left = tf4_1.margin_top = 0
p = tf4_1.paragraphs[0]
p.text = "ADHD 孩子的學習阻力，來自於學習教材的程度"
p.font.name = FONT_HEADING
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = CORAL_WARM

tb4_1_body = s4.shapes.add_textbox(Inches(1.05), Inches(3.7), Inches(5.2), Inches(3.1))
tf4_1_body = tb4_1_body.text_frame
tf4_1_body.word_wrap = True
tf4_1_body.margin_left = tf4_1_body.margin_top = 0

p = tf4_1_body.paragraphs[0]
p.text = "常態教材對於ADHD的孩子來說偏難："
p.font.name = FONT_HEADING
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = DARK_TEXT

p = tf4_1_body.add_paragraph()
p.text = "• 需花費比一般人多的時間消化知識"
p.font.name = FONT_BODY
p.font.size = Pt(10.5)
p.font.color.rgb = MUTED_TEXT
p.space_before = Pt(4)

p = tf4_1_body.add_paragraph()
p.text = "• 排斥複習與寫作業"
p.font.name = FONT_BODY
p.font.size = Pt(10.5)
p.font.color.rgb = MUTED_TEXT
p.space_before = Pt(2)

p = tf4_1_body.add_paragraph()
p.text = "市面教材嚴重缺乏階梯式鷹架：主流題庫預設學童具備 15 分鐘連續專注力，對低耐受度學童而言是持續性的挫折打擊。"
p.font.name = FONT_BODY
p.font.size = Pt(10.5)
p.font.color.rgb = DARK_TEXT
p.space_before = Pt(8)

# Card 2 (Right): 傳統輔助教學的人力成本
c2 = create_card(s4, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.1), bg_color=WHITE, border_color=VIBRANT_MINT, line_width=1.5)
t2 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.7), Inches(0.1))
t2.fill.solid()
t2.fill.fore_color.rgb = VIBRANT_MINT
t2.line.fill.background()

# Image 2 inside Card 2
if os.path.exists(IMG_COST):
    s4.shapes.add_picture(IMG_COST, Inches(10.7), Inches(2.1), Inches(1.5), Inches(1.5))

tb4_2 = s4.shapes.add_textbox(Inches(7.05), Inches(2.1), Inches(3.5), Inches(1.5))
tf4_2 = tb4_2.text_frame
tf4_2.word_wrap = True
tf4_2.margin_left = tf4_2.margin_top = 0
p = tf4_2.paragraphs[0]
p.text = "傳統輔助教學的人力成本高昂，邊際產出卻持續遞減"
p.font.name = FONT_HEADING
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DEEP_GREEN

tb4_2_body = s4.shapes.add_textbox(Inches(7.05), Inches(3.7), Inches(5.2), Inches(3.1))
tf4_2_body = tb4_2_body.text_frame
tf4_2_body.word_wrap = True
tf4_2_body.margin_left = tf4_2_body.margin_top = 0

p = tf4_2_body.paragraphs[0]
p.text = "• 課輔老師端缺乏合適的輔助工具，導致備課時間佔比過高，造成教育資源嚴重錯配。"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.color.rgb = DARK_TEXT

p = tf4_2_body.add_paragraph()
p.text = "• 學校與機構仰賴大量實習生與志工進行陪伴輔導，一旦人員流動教學質量便難以維繫"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.color.rgb = DARK_TEXT
p.space_before = Pt(8)


# ==============================================================================
# SLIDE 5: 企業實務痛點 (Pain Points) - Exact user text, clean 2-column horizontal
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Main Points", "目前困境 與 企業實務痛點")

# Left Column: 目前困境
c5_1 = create_card(s5, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.1), bg_color=TINT_CORAL, border_color=CORAL_WARM, line_width=1.5)
tb5_1 = s5.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(5.1), Inches(4.5))
tf5_1 = tb5_1.text_frame
tf5_1.word_wrap = True
tf5_1.margin_left = tf5_1.margin_top = 0

p = tf5_1.paragraphs[0]
p.text = "目前困境"
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = CORAL_WARM

p2 = tf5_1.add_paragraph()
p2.text = "特定族群分散，無法評估確切需求"
p2.font.name = FONT_HEADING
p2.font.size = Pt(14)
p2.font.bold = True
p2.font.color.rgb = DARK_TEXT
p2.space_before = Pt(16)

# Right Column: 企業實務痛點
c5_2 = create_card(s5, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.1), bg_color=WHITE, border_color=DEEP_GREEN, line_width=1.5)
tb5_2 = s5.shapes.add_textbox(Inches(7.1), Inches(2.2), Inches(5.1), Inches(4.5))
tf5_2 = tb5_2.text_frame
tf5_2.word_wrap = True
tf5_2.margin_left = tf5_2.margin_top = 0

p = tf5_2.paragraphs[0]
p.text = "企業實務痛點"
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = DEEP_GREEN

p2 = tf5_2.add_paragraph()
p2.text = "課輔老師資訊不對稱，客製化成本過高"
p2.font.name = FONT_HEADING
p2.font.size = Pt(13.5)
p2.font.bold = True
p2.font.color.rgb = DARK_TEXT
p2.space_before = Pt(12)

pts5 = [
    "課輔老師與原班導師缺乏出題標準同步機制，僅能手握紙本課本摸索。",
    "針對 1~6 年級不同年齡層手工降難度出題，單次需消耗 1~2 小時備課。",
    "傳統人工出題難以動態提供詞根、色彩音節等認知鷹架提示。"
]
for pt in pts5:
    p = tf5_2.add_paragraph()
    p.text = "• " + pt
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = MUTED_TEXT
    p.space_before = Pt(8)


# ==============================================================================
# SLIDE 6: 解決方案：FocusLingua - Exact user text, 2 horizontal cards
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Project & Demo", "解決方案：FocusLingua")

# Left Column: 教師端 Web 備課工作站
c6_1 = create_card(s6, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.1), bg_color=WHITE, border_color=VIBRANT_MINT, line_width=1.5)
tb6_1 = s6.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.2), Inches(4.7))
tf6_1 = tb6_1.text_frame
tf6_1.word_wrap = True
tf6_1.margin_left = tf6_1.margin_top = 0

p = tf6_1.paragraphs[0]
p.text = "💻 教師端 Web 備課工作站"
p.font.name = FONT_HEADING
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = DEEP_GREEN

t_blocks = [
    ("【教材自動出題】", "上傳課綱 PDF / 課文音檔，LLM Prompt 自動萃取關鍵單字，並按 1~6 年級認知階梯自動分流。"),
    ("【二次審核與把關】", "老師能直接微調句子長度、調整輔助提示詞，把關教學品質後一鍵派發。"),
    ("【特教數據看板】", "即時記錄全班學童答題延遲 、猶豫拐點與衝動性亂點，自動導出客觀之個別化輔導報表。")
]
for head, body in t_blocks:
    p = tf6_1.add_paragraph()
    p.text = head
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = VIBRANT_MINT
    p.space_before = Pt(8)
    
    p = tf6_1.add_paragraph()
    p.text = body
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(2)

# Right Column: 學生端手機 App 專注沙盒
c6_2 = create_card(s6, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.1), bg_color=WHITE, border_color=CORAL_WARM, line_width=1.5)
tb6_2 = s6.shapes.add_textbox(Inches(7.05), Inches(2.1), Inches(5.2), Inches(4.7))
tf6_2 = tb6_2.text_frame
tf6_2.word_wrap = True
tf6_2.margin_left = tf6_2.margin_top = 0

p = tf6_2.paragraphs[0]
p.text = "📱 學生端手機 App 專注沙盒"
p.font.name = FONT_HEADING
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = CORAL_WARM

s_blocks = [
    ("【90 秒沙漏倒數機制】", "強制限制單元於 90 秒內結束，以非侵入式漸進圓環替代跳動數字，消解 ADHD 學童之時間焦慮。"),
    ("【多感官無干擾伴讀卡】", "支援 Lexend 抗分心易讀字型切換、色彩音節高亮切片與原生真人單字語音播放，降低閱讀負荷。"),
    ("【觸覺拼裝與多巴胺回饋】", "捨棄傳統鍵盤手打阻力，改採點擊積木拼裝句子；答對即觸發觸覺微震動與 Canvas 微粒子慶賀。"),
    ("【課堂防沉迷護眼鎖定】", "微任務完成即刻啟動鎖定，引導學童閉眼休息 10 分鐘，保護專注神經，防止過度多巴胺刺激。")
]
for head, body in s_blocks:
    p = tf6_2.add_paragraph()
    p.text = head
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CORAL_WARM
    p.space_before = Pt(6)
    
    p = tf6_2.add_paragraph()
    p.text = body
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(1)


# ==============================================================================
# SLIDE 7: 產品演進脈絡 (Project & Demo) - Exact user text & image4.png
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Project & Demo", "產品演進脈絡：")

# Framed container for user's evolution picture
c7 = create_card(s7, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.3), bg_color=WHITE, border_color=BORDER_LIGHT)

if os.path.exists(IMG_EVOL):
    s7.shapes.add_picture(IMG_EVOL, Inches(1.1), Inches(1.95), Inches(11.133), Inches(5.0))


# ==============================================================================
# SLIDE 8: 預測效益分析 (Cost-Benefit & ROI) - Exact user text, 3 horizontal cards
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Cost-Benefit & ROI", "預測效益分析", "本產品未經過實測，僅以本人判斷。")

roi_list = [
    ("備課時間成本顯著縮減", "營運效率優化", 
     "課輔老師手工針對特殊生切片出題的時間由原本 90 分鐘降至 30 秒生成 ＋ 5 分鐘審核。單一師資可服務的學童人次提升 3 倍以上，有效緩解課輔機構師資不足之瓶頸。", VIBRANT_MINT, TINT_MINT),
    ("課堂即時掌握核心詞彙", "人因成效驗證 (Learning Effectiveness)",
     "將認知負荷嚴格限制在 90 秒黃金耐受期內。在微型拼裝與即時鷹架輔助下，學童衝動性亂點次數降低超過 60%，達成「課堂內直接消化、不將作業挫折帶回家」之目標。", CORAL_WARM, TINT_CORAL),
    ("打開新市場", "商業價值躍升 (Business Scalability)",
     "將傳統單向零售教材升級並打入學校特教組、資源班與兒福課輔機構，幫助更多學生受益。", OCEAN_BLUE, TINT_BLUE)
]

for idx, (title, sub, body, col, tint) in enumerate(roi_list):
    x = Inches(0.8 + idx * 4.0)
    c = create_card(s8, x, Inches(2.0), Inches(3.733), Inches(4.9), bg_color=WHITE, border_color=col, line_width=1.5)
    
    # Top Tag
    tag = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.2), Inches(2.2), Inches(3.333), Inches(0.42))
    tag.fill.solid()
    tag.fill.fore_color.rgb = tint
    tag.line.color.rgb = col
    tag.line.width = Pt(1)
    tp = tag.text_frame.paragraphs[0]
    tp.text = sub
    tp.font.name = FONT_HEADING
    tp.font.size = Pt(10.5)
    tp.font.bold = True
    tp.font.color.rgb = col
    tp.alignment = PP_ALIGN.CENTER
    
    tb = s8.shapes.add_textbox(x + Inches(0.2), Inches(2.8), Inches(3.333), Inches(3.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_HEADING
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT
    
    p = tf.add_paragraph()
    p.text = body
    p.font.name = FONT_BODY
    p.font.size = Pt(10.2)
    p.font.color.rgb = MUTED_TEXT
    p.space_before = Pt(10)


# ==============================================================================
# SLIDE 9: 未來擴散性 (Future Scalability) - Exact user text, 3 horizontal cards (Left to Right flow)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Future Scalability", "未來擴散性與再精進方案：構建跨學科特教生態圈", 
           "由單一英語教材，延伸至多元學科輔具、邊緣生理反饋與校園特教雲端聯網")

# 3 Horizontal Cards (Left to Right)
scale_list = [
    ("一、橫向學科擴展", "多領域「微單元切片」模組化延伸",
     "將 FocusLingua 架構，橫向擴展至國小國語文閱讀理解、數學應用題長句拆解，以及自然科記憶型知識點。實現單一核心引擎支援全年段、多學科之特教輔具標準化。", VIBRANT_MINT, TINT_MINT),
    ("二、邊緣人因感知", "結合生理反饋進行「動態疲勞預警」",
     "未來可進一步整合平板視訊鏡頭之輕量化視線追蹤 (Eye-tracking) 或穿戴裝置微心率變異度 (HRV)。當系統偵測到學童眼球頻繁飄移或專注力瀕臨崩潰拐點時，主動調降難度、切換放鬆白噪音，實現真正的自適應人因調節。", CORAL_WARM, TINT_CORAL),
    ("三、平台化商模", "打造「出版教材 ➔ 特資中心 ➔ 班級 ➔ 家長」之 雲端中樞",
     "LiveABC 可從內容提供商升級為「特教數據中樞」。讓課輔老師一鍵產出的行為分析報表直接同步至學校特教組與家長端 App，消解親師溝通鴻溝，形成高黏著度之特教智慧支持生態圈。", OCEAN_BLUE, TINT_BLUE)
]

for idx, (title, sub, body, col, tint) in enumerate(scale_list):
    x = Inches(0.8 + idx * 4.0)
    c = create_card(s9, x, Inches(2.0), Inches(3.733), Inches(4.9), bg_color=WHITE, border_color=col, line_width=1.5)
    
    # Top strip
    strip = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(2.0), Inches(3.733), Inches(0.1))
    strip.fill.solid()
    strip.fill.fore_color.rgb = col
    strip.line.fill.background()
    
    tb = s9.shapes.add_textbox(x + Inches(0.2), Inches(2.25), Inches(3.333), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_HEADING
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = col
    
    p = tf.add_paragraph()
    p.text = sub
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(4)
    
    p = tf.add_paragraph()
    p.text = body
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.color.rgb = MUTED_TEXT
    p.space_before = Pt(8)


# ==============================================================================
# SLIDE 10: 個人學習成果與反思 (Personal Reflections) - Exact user text, 2 horizontal cards
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "Personal Reflections", "個人學習成果與反思")

ref_list = [
    ("01", "產品思維之蛻變：理解 AI 的核心定位在於「克制減法」",
     "實作初期，我曾執著於使用 Claude 與 Stitch 拼湊的前台選單與 Chatbot 對話。但發現越是繁華的介面，學生反而更難專注。此外，一開始發餉解局方案的時候都是以學生為主，後來才發現其實老師及機構才是最主要買單者，因此轉換對象去設計整個產品", VIBRANT_MINT, TINT_MINT),
    ("02", "人機協同",
     "語言教學涉及細膩的同理心與課堂情緒管理，無法完全由演算法取代。FocusLingua 確立了「AI 負責有效率的製作教材，老師把關二次審核與情感陪伴」的分工架構。這使我體認到，優質的 EdTech 方案不是要取代教師，而是輔助並賦能教師成為更具專注力與溫度的引路人。", CORAL_WARM, TINT_CORAL)
]

for idx, (num, title, body, col, tint) in enumerate(ref_list):
    x = Inches(0.8 + idx * 5.95)
    c = create_card(s10, x, Inches(2.0), Inches(5.75), Inches(4.9), bg_color=WHITE, border_color=col, line_width=1.5)
    
    # Top Number Badge
    nb = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.3), Inches(2.3), Inches(0.7), Inches(0.5))
    nb.fill.solid()
    nb.fill.fore_color.rgb = tint
    nb.line.color.rgb = col
    nb.line.width = Pt(1)
    np = nb.text_frame.paragraphs[0]
    np.text = num
    np.font.name = FONT_EN
    np.font.size = Pt(14)
    np.font.bold = True
    np.font.color.rgb = col
    np.alignment = PP_ALIGN.CENTER
    
    tb = s10.shapes.add_textbox(x + Inches(0.3), Inches(3.0), Inches(5.15), Inches(3.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_HEADING
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = col
    
    p = tf.add_paragraph()
    p.text = body
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = DARK_TEXT
    p.space_before = Pt(10)


# ==============================================================================
# SLIDE 11: THANK YOU - Exact user text, lively & elegant ending
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)

add_dot_grid(s11, Inches(0.8), Inches(0.8), cols=5, rows=4, color=VIBRANT_MINT)
add_dot_grid(s11, Inches(11.5), Inches(5.8), cols=5, rows=4, color=AMBER_GOLD)

ty_box = s11.shapes.add_textbox(Inches(2.0), Inches(2.2), Inches(9.333), Inches(3.2))
tyf = ty_box.text_frame
tyf.word_wrap = True
tyf.margin_left = tyf.margin_top = 0

p_ty = tyf.paragraphs[0]
p_ty.text = "THANK YOU"
p_ty.font.name = FONT_EN
p_ty.font.size = Pt(56)
p_ty.font.bold = True
p_ty.font.color.rgb = DEEP_GREEN
p_ty.alignment = PP_ALIGN.CENTER

p_sub = tyf.add_paragraph()
p_sub.text = "FocusLingua 成果專題簡報 ｜ 敬請指教"
p_sub.font.name = FONT_HEADING
p_sub.font.size = Pt(20)
p_sub.font.bold = True
p_sub.font.color.rgb = CORAL_WARM
p_sub.alignment = PP_ALIGN.CENTER
p_sub.space_before = Pt(14)

p_pres = tyf.add_paragraph()
p_pres.text = "陳詠芸 Anna Chen"
p_pres.font.name = FONT_BODY
p_pres.font.size = Pt(14)
p_pres.font.bold = True
p_pres.font.color.rgb = DARK_TEXT
p_pres.alignment = PP_ALIGN.CENTER
p_pres.space_before = Pt(8)

# Save to both paths
desktop_path = "/Users/annamei/Desktop/FocusLingua_成果專題簡報.pptx"
notes_path   = "/Users/annamei/notes/FocusLingua_成果專題簡報.pptx"

prs.save(desktop_path)
prs.save(notes_path)
print("SUCCESSFULLY refined user PPTX with exact text, prominent titles, left-to-right flow, and vibrant colors!")
