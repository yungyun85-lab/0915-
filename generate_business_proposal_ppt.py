import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Initialize
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Brand Colors (Extracted directly from Business Proposal.pdf)
DEEP_GREEN = RGBColor(30, 77, 54)       # #1E4D36 (Main brand forest green)
LIGHT_GREEN_BG = RGBColor(241, 246, 242) # Soft sage tint
WHITE = RGBColor(255, 255, 255)
CARD_BG = RGBColor(255, 255, 255)
BORDER_GRAY = RGBColor(220, 226, 222)
TEXT_DARK = RGBColor(30, 41, 35)        # Deep forest charcoal
TEXT_MUTED = RGBColor(85, 100, 92)      # Elegant slate green-gray
DOT_COLOR = RGBColor(120, 155, 135)     # Decorative dots color

FONT_TITLE = "Arial"
FONT_BODY = "Microsoft JhengHei"

PHOTO_PATH = "/Users/annamei/notes/assets/截圖 2026-09-09 晚上10.01.52.png"

def add_dot_grid(slide, left, top, cols=5, rows=4):
    """Add aesthetic dot cluster matching Business Proposal.pdf"""
    tb = slide.shapes.add_textbox(left, top, Inches(1.5), Inches(1.0))
    tf = tb.text_frame
    tf.word_wrap = False
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    dot_line = " ".join(["•"] * cols)
    for r in range(rows):
        p = tf.paragraphs[0] if r == 0 else tf.add_paragraph()
        p.text = dot_line
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.color.rgb = DOT_COLOR
        p.line_spacing = Pt(13)

def add_header(slide, en_tag, cn_title, subtitle=""):
    """Header style inspired by Business Proposal.pdf"""
    # Top curved green banner or top pill
    top_bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.35), Inches(2.6), Inches(0.42))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = DEEP_GREEN
    top_bar.line.fill.background()
    p_bar = top_bar.text_frame.paragraphs[0]
    p_bar.text = en_tag.upper()
    p_bar.font.name = FONT_TITLE
    p_bar.font.size = Pt(11)
    p_bar.font.bold = True
    p_bar.font.color.rgb = WHITE
    p_bar.alignment = PP_ALIGN.CENTER
    
    # Title box
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(10.5), Inches(0.95))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_bottom = tf.margin_right = 0
    
    p = tf.paragraphs[0]
    p.text = cn_title
    p.font.name = FONT_BODY
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = DEEP_GREEN
    
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = FONT_BODY
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(3)

    # Top-right decorative dots
    add_dot_grid(slide, Inches(11.6), Inches(0.35), cols=5, rows=3)

def create_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_GRAY):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
    else:
        card.line.fill.background()
    return card


# ==============================================================================
# SLIDE 1: 標題 (Title / Cover)
# Exactly matching Page 1 layout of Business Proposal.pdf:
# Left: Green bar, dots, large bold title, credentials
# Right: Framed photo with green rounded border
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)

# Top green pill
pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.6), Inches(2.2), Inches(0.38))
pill1.fill.solid()
pill1.fill.fore_color.rgb = DEEP_GREEN
pill1.line.fill.background()

# Top left dots
add_dot_grid(s1, Inches(0.4), Inches(0.5), cols=4, rows=5)

# Big English/Chinese Title
tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.35), Inches(5.8), Inches(3.2))
tf1 = tb1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = 0

p1 = tf1.paragraphs[0]
p1.text = "FOCUSLINGUA"
p1.font.name = FONT_TITLE
p1.font.size = Pt(36)
p1.font.bold = True
p1.font.color.rgb = DEEP_GREEN

p2 = tf1.add_paragraph()
p2.text = "LESSON切片"
p2.font.name = FONT_TITLE
p2.font.size = Pt(36)
p2.font.bold = True
p2.font.color.rgb = DEEP_GREEN

p3 = tf1.add_paragraph()
p3.text = "SYSTEM"
p3.font.name = FONT_TITLE
p3.font.size = Pt(36)
p3.font.bold = True
p3.font.color.rgb = DEEP_GREEN

# Vertical divider line
div = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(4.7), Inches(0.08), Inches(1.8))
div.fill.solid()
div.fill.fore_color.rgb = DEEP_GREEN
div.line.fill.background()

# Subtitle & Credential
tb1_sub = s1.shapes.add_textbox(Inches(1.25), Inches(4.65), Inches(5.6), Inches(1.9))
tf1_sub = tb1_sub.text_frame
tf1_sub.word_wrap = True
tf1_sub.margin_left = tf1_sub.margin_top = 0

ps1 = tf1_sub.paragraphs[0]
ps1.text = "B2B2C 英語數位教材智慧切片與課堂輔助系統"
ps1.font.name = FONT_BODY
ps1.font.size = Pt(13)
ps1.font.bold = True
ps1.font.color.rgb = DEEP_GREEN

ps2 = tf1_sub.add_paragraph()
ps2.text = "希伯崙 LiveABC 產學實習成果 ｜ 專為國小低專注耐受度學童打造"
ps2.font.name = FONT_BODY
ps2.font.size = Pt(11)
ps2.font.color.rgb = TEXT_MUTED
ps2.space_before = Pt(3)

ps3 = tf1_sub.add_paragraph()
ps3.text = "專題發表人：陳詠芸 Anna Chen"
ps3.font.name = FONT_BODY
ps3.font.size = Pt(11.5)
ps3.font.bold = True
ps3.font.color.rgb = TEXT_DARK
ps3.space_before = Pt(8)

ps4 = tf1_sub.add_paragraph()
ps4.text = "中原大學 應用外語學系（主修）× 財務金融學系（雙主修）"
ps4.font.name = FONT_BODY
ps4.font.size = Pt(10)
ps4.font.color.rgb = TEXT_MUTED

# Right Framed Illustration / Image Container (matching Business Proposal.pdf page 1 frame)
frame_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.3), Inches(1.1), Inches(5.2), Inches(5.4))
frame_box.fill.solid()
frame_box.fill.fore_color.rgb = WHITE
frame_box.line.color.rgb = DEEP_GREEN
frame_box.line.width = Pt(3.5)

if os.path.exists(PHOTO_PATH):
    s1.shapes.add_picture(PHOTO_PATH, Inches(7.45), Inches(1.25), Inches(4.9), Inches(5.1))

# Bottom right dots
add_dot_grid(s1, Inches(11.8), Inches(6.1), cols=5, rows=4)


# ==============================================================================
# SLIDE 2: 目錄 (Content)
# Matching Page 2 of Business Proposal.pdf:
# Left deep green strip, bold Content title, numbered agenda with generous space
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)

# Left solid green decorative block
left_block = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(1.1), Inches(7.5))
left_block.fill.solid()
left_block.fill.fore_color.rgb = DEEP_GREEN
left_block.line.fill.background()

# Title "Content"
tb2 = s2.shapes.add_textbox(Inches(1.6), Inches(0.7), Inches(5.0), Inches(1.0))
tf2 = tb2.text_frame
tf2.margin_left = tf2.margin_top = 0
p = tf2.paragraphs[0]
p.text = "Content"
p.font.name = FONT_TITLE
p.font.size = Pt(36)
p.font.bold = True
p.font.color.rgb = TEXT_DARK

agenda_list = [
    ("01", "自我介紹 (About Presenter)", "外語人因實務 × 財金量化思維之跨域背景"),
    ("02", "專案動機 (Motivation)", "特教課輔講台到數位出版：被忽視的認知極限"),
    ("03", "企業實務痛點 (Pain Points)", "LiveABC 數位教材的三大現場轉型阻礙"),
    ("04", "專案架構與微型展示 (Project & Live Demo)", "AI 減法切片：教師 Web 工作站 ＋ 學生手機沙盒"),
    ("05", "導入效益分析 (Cost-Benefit & ROI)", "營運備課成本降 80% ＋ 專注耐受度顯著躍升"),
    ("06", "未來擴散性與再精進 (Future Expansion)", "跨學科微切片 ＋ 多模態特教生態圈聯網"),
    ("07", "個人學習成果與反思 (Personal Reflections)", "從「盲目炫技」到「克制落地」的思維蛻變")
]

for idx, (num, title, desc) in enumerate(agenda_list):
    y = Inches(1.75 + idx * 0.76)
    
    # Number
    ntb = s2.shapes.add_textbox(Inches(1.6), y, Inches(0.7), Inches(0.6))
    ntf = ntb.text_frame
    ntf.margin_left = ntf.margin_top = 0
    np = ntf.paragraphs[0]
    np.text = num
    np.font.name = FONT_TITLE
    np.font.size = Pt(16)
    np.font.bold = True
    np.font.color.rgb = DEEP_GREEN
    
    # Text
    ttb = s2.shapes.add_textbox(Inches(2.3), y, Inches(8.5), Inches(0.65))
    ttf = ttb.text_frame
    ttf.margin_left = ttf.margin_top = 0
    tp = ttf.paragraphs[0]
    tp.text = title + "  —  " + desc
    tp.font.name = FONT_BODY
    tp.font.size = Pt(12)
    tp.font.color.rgb = TEXT_DARK

# Right side decorative dots
add_dot_grid(s2, Inches(11.5), Inches(1.0), cols=4, rows=12)


# ==============================================================================
# SLIDE 3: 自我介紹 (About Presenter)
# Tone: Senior student double majoring in Applied Foreign Languages & Finance
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "About Presenter", "自我介紹：語言教學人因 × 財金量化分析的跨域視角", 
           "具備第一線特教學童陪伴實務、外語數位教材研發企劃，以及嚴謹的商業成本效益思維")

# Left Column: Profile Card
pcard = create_card(s3, Inches(0.8), Inches(2.0), Inches(3.5), Inches(5.0), bg_color=LIGHT_GREEN_BG, border_color=BORDER_GRAY)

# Frame for photo inside card
if os.path.exists(PHOTO_PATH):
    s3.shapes.add_picture(PHOTO_PATH, Inches(1.05), Inches(2.2), Inches(3.0), Inches(2.3))

ptb = s3.shapes.add_textbox(Inches(1.0), Inches(4.6), Inches(3.1), Inches(2.2))
ptf = ptb.text_frame
ptf.word_wrap = True
ptf.margin_left = ptf.margin_top = 0

p1 = ptf.paragraphs[0]
p1.text = "陳詠芸 Anna Chen"
p1.font.name = FONT_BODY
p1.font.size = Pt(15)
p1.font.bold = True
p1.font.color.rgb = DEEP_GREEN
p1.alignment = PP_ALIGN.CENTER

p2 = ptf.add_paragraph()
p2.text = "中原大學 雙主修大四\n應用外語學系 (主修) ｜ 財務金融學系 (雙主修)\nGPA: 3.7 ｜ 雅思：IELTS 6.5 (L 7.5 / R 6.5)"
p2.font.name = FONT_BODY
p2.font.size = Pt(10)
p2.font.color.rgb = TEXT_MUTED
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(4)

# Right Column: 4 Experiences (Framed clean cards)
experiences = [
    ("中原大學特資中心 英語課輔老師", "特教現場洞察",
     "第一線輔導注意力不集中 (ADHD) 及低專注耐受度學童。掌握其認知負荷拐點（超過5分鐘易疲乏逃避），促成本專案針對國小 1~6 年級微單元鷹架之核心命題。"),
    ("LiveABC 希伯崙 研發三處實習生 & 人事部工讀", "數位出版實戰",
     "參與英語數位教材企劃、教案研析與課文音檔切片勘誤。熟悉出版社既有數位題庫架構，並掌握跨部門行政協調與教材研發推進流程。"),
    ("加拿大 Athabasca Univ. VIP Research 實習", "前瞻海外科研",
     "獲選赴加運用 MEGA World 研發英語教育遊戲，深度融合 TPR (全身肢體反應法) 與 CLT (溝通教學法)，將沉浸互動理論轉化為數位載體。"),
    ("2025 全國前瞻科技英語教學創新競賽", "全國優等第二名",
     "以創新互動教學架構獲全國評審肯定，展現結合語言教學人因、數位技術整合與商業落地可行性之跨域統整能力。")
]

for idx, (title, tag, desc) in enumerate(experiences):
    y = Inches(2.0 + idx * 1.22)
    c = create_card(s3, Inches(4.6), y, Inches(7.9), Inches(1.12))
    
    # Left deep green border tag
    tag_box = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.6), y, Inches(0.12), Inches(1.12))
    tag_box.fill.solid()
    tag_box.fill.fore_color.rgb = DEEP_GREEN
    tag_box.line.fill.background()
    
    tb = s3.shapes.add_textbox(Inches(4.85), y + Inches(0.08), Inches(7.5), Inches(0.95))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    tp1 = tf.paragraphs[0]
    tp1.text = f"{title}  ｜  [{tag}]"
    tp1.font.name = FONT_BODY
    tp1.font.size = Pt(11.5)
    tp1.font.bold = True
    tp1.font.color.rgb = DEEP_GREEN
    
    tp2 = tf.add_paragraph()
    tp2.text = desc
    tp2.font.name = FONT_BODY
    tp2.font.size = Pt(9.5)
    tp2.font.color.rgb = TEXT_DARK
    tp2.space_before = Pt(3)


# ==============================================================================
# SLIDE 4: 動機 (Motivation)
# Format matching Business Proposal.pdf Page 3/5/6: Top Activity/Goal layout
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "Motivation", "專案動機：從課輔講台到數位出版，看見「被忽視的認知極限」",
           "結合應外人因教學觀察與財金資源配置邏輯，直擊特殊教育與輔導體系的核心痛點")

# Two wide cards (Activity & Goal / Dual perspectives)
m_cards = [
    ("一、應外人因視角：ADHD 孩子的學習阻力，來自於「錯誤的任務顆粒度」", 
     [
         "單字背誦效率失衡：在特資中心輔導時，我發現注意力缺失孩子並非缺乏理解力，而是背誦單字常需消耗常人 2 倍以上的認知能量，極易在長篇課文中迷航。",
         "課後複習結構崩潰：學童回家後極度排斥厚重作業，且家庭端缺乏一對一專注引導環境。學童最強烈的訴求是「在學校課堂內直接無痛吸收」，而非把挫折帶回家。",
         "市面教材嚴重缺乏階梯式鷹架：主流題庫預設學童具備 15 分鐘連續專注力，對低耐受度學童而言是持續性的挫折打擊。"
     ], Inches(2.0), DEEP_GREEN),
     
    ("二、財金配置視角：傳統補救教學的人力成本高昂，邊際產出卻持續遞減",
     [
         "高投入、低產出的備課困局：課輔老師手邊缺乏專門輔助工具，單堂課需耗時 1~2 小時手工出題與切片，備課時間佔比過高，造成教育資源嚴重錯配。",
         "缺乏標準化輔助工具：學校與機構仰賴大量實習生與志工進行「陪伴式肉搏」，一旦人員流動教學質量便難以維繫，亟需一套兼具低成本與高複製性的輔助系統。"
     ], Inches(4.5), TEXT_MUTED)
]

for title, pts, y_pos, border_col in m_cards:
    c = create_card(s4, Inches(0.8), y_pos, Inches(11.733), Inches(2.3))
    
    # Top accent line
    top_bar = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_pos, Inches(11.733), Inches(0.08))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = border_col
    top_bar.line.fill.background()
    
    tb = s4.shapes.add_textbox(Inches(1.1), y_pos + Inches(0.18), Inches(11.1), Inches(2.0))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DEEP_GREEN
    
    for pt in pts:
        p_pt = tf.add_paragraph()
        p_pt.text = "• " + pt
        p_pt.font.name = FONT_BODY
        p_pt.font.size = Pt(10)
        p_pt.font.color.rgb = TEXT_DARK
        p_pt.space_before = Pt(4)


# ==============================================================================
# SLIDE 5: 企業痛點 (Enterprise Pain Points)
# Focus: LiveABC's operational and business challenges
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Pain Points", "企業實務痛點：LiveABC 數位教材出版的三大轉型瓶頸",
           "想用 AI 解決的關鍵命題：傳統題庫一體適用、特教出題繁重、商業端缺乏客觀量化數據")

pain_cards = [
    ("01", "教材端痛點", "題庫關卡過長，無法適配特殊學習受眾", 
     [
         "現行題庫以 15~20 分鐘為最小單位，主要服務常態自學者。",
         "面對國小 1~6 年級 ADHD 與注意力不集中學生，長題庫導致學童在第 3 分鐘便出現專注崩潰與亂點。",
         "缺乏將長篇課綱自動拆解為「90 秒微型單元」的自動化切片機制。"
     ]),
    ("02", "現場端痛點", "課輔老師資訊不對稱，客製化成本過高",
     [
         "課輔老師與原班導師缺乏出題標準同步機制，僅能手握紙本課本摸索。",
         "針對 1~6 年級不同年齡層手工降難度出題，單次需消耗 1~2 小時備課。",
         "傳統人工出題難以動態提供詞根、色彩音節等認知鷹架提示。"
     ]),
    ("03", "商業端痛點", "數據僅限正誤率，缺乏特教 IEP 評估價值",
     [
         "傳統題庫僅回傳單一「答對/答錯率」，無法反映學童做題延遲 (Latency) 與猶豫拐點。",
         "無法產出符合學校特教組與輔導室所需的「個別化教育計畫 (IEP) 報表」。",
         "難以形成高黏著度的 B2B 機構採購模式，錯失特教藍海市場。"
     ])
]

for idx, (num, subtitle, title, points) in enumerate(pain_cards):
    x = Inches(0.8 + idx * 4.0)
    c = create_card(s5, x, Inches(2.0), Inches(3.733), Inches(4.8), bg_color=CARD_BG)
    
    # Top card banner with number
    num_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.2), Inches(2.2), Inches(0.7), Inches(0.45))
    num_box.fill.solid()
    num_box.fill.fore_color.rgb = LIGHT_GREEN_BG
    num_box.line.color.rgb = DEEP_GREEN
    num_box.line.width = Pt(1)
    np = num_box.text_frame.paragraphs[0]
    np.text = num
    np.font.name = FONT_TITLE
    np.font.size = Pt(14)
    np.font.bold = True
    np.font.color.rgb = DEEP_GREEN
    np.alignment = PP_ALIGN.CENTER
    
    tb = s5.shapes.add_textbox(x + Inches(0.2), Inches(2.8), Inches(3.333), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p1 = tf.paragraphs[0]
    p1.text = subtitle
    p1.font.name = FONT_BODY
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED
    
    p2 = tf.add_paragraph()
    p2.text = title
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12.5)
    p2.font.bold = True
    p2.font.color.rgb = DEEP_GREEN
    p2.space_before = Pt(3)
    
    for pt in points:
        p_pt = tf.add_paragraph()
        p_pt.text = "• " + pt
        p_pt.font.name = FONT_BODY
        p_pt.font.size = Pt(9.5)
        p_pt.font.color.rgb = TEXT_DARK
        p_pt.space_before = Pt(8)


# ==============================================================================
# SLIDE 6: 專案（微型demo） (Project & Micro Demo)
# Tone: Analytical & structural presentation of FocusLingua decoupled architecture
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Project & Demo", "專案方向：FocusLingua 雙端解耦架構與 AI 減法實作",
           "經歷「自選過多」與「Chatbot離題」兩代失敗原型，淬鍊出以課輔老師為軸心的極簡雙端模式")

# Left Box: Teacher Web Workspace
tw = create_card(s6, Inches(0.8), Inches(2.0), Inches(5.7), Inches(4.9), bg_color=WHITE)
# Top header line
th = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.0), Inches(5.7), Inches(0.08))
th.fill.solid()
th.fill.fore_color.rgb = DEEP_GREEN
th.line.fill.background()

ttb = s6.shapes.add_textbox(Inches(1.05), Inches(2.2), Inches(5.2), Inches(4.5))
ttf = ttb.text_frame
ttf.word_wrap = True
ttf.margin_left = ttf.margin_top = 0

tp1 = ttf.paragraphs[0]
tp1.text = "💻 教師端 Web 備課工作站 (Desktop Workspace)"
tp1.font.name = FONT_BODY
tp1.font.size = Pt(13.5)
tp1.font.bold = True
tp1.font.color.rgb = DEEP_GREEN

t_pts = [
    ("教材 30 秒自動切片", "上傳課綱 PDF / 課文音檔，LLM Prompt 於 30 秒內自動萃取關鍵單字，並按 1~6 年級認知階梯自動分流。"),
    ("二次審核與鷹架把關", "落實 Human-in-the-Loop，老師能直接微調句子長度、調整輔助提示詞，把關教學品質後一鍵派發。"),
    ("特教 IEP 數據看板", "即時記錄全班學童答題延遲 (Latency)、猶豫拐點與衝動性亂點，自動導出客觀之個別化輔導報表。")
]
for sub, desc in t_pts:
    p = ttf.add_paragraph()
    p.text = "【" + sub + "】"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)
    
    p2 = ttf.add_paragraph()
    p2.text = desc
    p2.font.name = FONT_BODY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(2)

# Right Box: Student Mobile App Sandbox
sw = create_card(s6, Inches(6.8), Inches(2.0), Inches(5.7), Inches(4.9), bg_color=WHITE)
sh = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(2.0), Inches(5.7), Inches(0.08))
sh.fill.solid()
sh.fill.fore_color.rgb = DEEP_GREEN
sh.line.fill.background()

stb = s6.shapes.add_textbox(Inches(7.05), Inches(2.2), Inches(5.2), Inches(4.5))
stf = stb.text_frame
stf.word_wrap = True
stf.margin_left = stf.margin_top = 0

sp1 = stf.paragraphs[0]
sp1.text = "📱 學生端手機 App 專注沙盒 (Mobile Sandbox)"
sp1.font.name = FONT_BODY
sp1.font.size = Pt(13.5)
sp1.font.bold = True
sp1.font.color.rgb = DEEP_GREEN

s_pts = [
    ("90 秒沙漏倒數機制", "強制限制單元於 90 秒內結束，以非侵入式漸進圓環替代跳動數字，消解 ADHD 學童之時間焦慮。"),
    ("多感官無干擾伴讀卡", "支援 Lexend 抗分心易讀字型切換、色彩音節高亮切片與原生真人單字語音播放，降低閱讀負荷。"),
    ("觸覺拼裝與多巴胺回饋", "捨棄傳統鍵盤手打阻力，改採點擊積木拼裝句子；答對即觸發觸覺微震動與 Canvas 微粒子慶賀。"),
    ("課堂防沉迷護眼鎖定", "微任務完成即刻啟動鎖定，引導學童閉眼休息 10 分鐘，保護專注神經，防止過度多巴胺刺激。")
]
for sub, desc in s_pts:
    p = stf.add_paragraph()
    p.text = "【" + sub + "】"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(6)
    
    p2 = stf.add_paragraph()
    p2.text = desc
    p2.font.name = FONT_BODY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(1)


# ==============================================================================
# SLIDE 7: 導入效益 (Cost-Benefit & ROI)
# Tone: Finance major's analytical perspective (Cost, Efficiency, LTV, Scaling)
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Cost-Benefit & ROI", "導入效益分析：財金量化視角之營運優化與商業回報",
           "以資本預算與資源配置邏輯評估：大幅降低邊際備課成本，開拓出版業高黏著度之 B2B 藍海")

roi_cards = [
    ("80%", "備課時間成本顯著縮減", "營運效率優化 (Operational Efficiency)",
     "課輔老師手工針對特殊生切片出題的時間由原本 90 分鐘降至 30 秒生成 ＋ 5 分鐘審核。單一師資可服務的學童人次提升 3 倍以上，有效緩解課輔機構師資不足之瓶頸。"),
    ("90s", "課堂即時掌握核心詞彙", "人因成效驗證 (Learning Effectiveness)",
     "將認知負荷嚴格限制在 90 秒黃金耐受期內。在微型拼裝與即時鷹架輔助下，學童衝動性亂點次數降低超過 60%，達成「課堂內直接消化、不將作業挫折帶回家」之目標。"),
    ("B2B", "開拓特教機構採購藍海", "商業價值躍升 (Business Scalability)",
     "將傳統單向零售教材升級為具備 IEP 評估報告之智慧型解決方案。打入學校特教組、資源班與兒福課輔機構，大幅提升客戶終身價值 (LTV) 與年約續訂率。")
]

for idx, (stat, title, subtitle, desc) in enumerate(roi_cards):
    x = Inches(0.8 + idx * 4.0)
    c = create_card(s7, x, Inches(2.0), Inches(3.733), Inches(4.8), bg_color=CARD_BG)
    
    # Big stat block
    sb = s7.shapes.add_textbox(x + Inches(0.2), Inches(2.2), Inches(3.333), Inches(0.9))
    sf = sb.text_frame
    sf.margin_left = sf.margin_top = 0
    sp = sf.paragraphs[0]
    sp.text = stat
    sp.font.name = FONT_TITLE
    sp.font.size = Pt(36)
    sp.font.bold = True
    sp.font.color.rgb = DEEP_GREEN
    
    tb = s7.shapes.add_textbox(x + Inches(0.2), Inches(3.1), Inches(3.333), Inches(3.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p1 = tf.paragraphs[0]
    p1.text = title
    p1.font.name = FONT_BODY
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_DARK
    
    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(2)
    
    p3 = tf.add_paragraph()
    p3.text = desc
    p3.font.name = FONT_BODY
    p3.font.size = Pt(9.8)
    p3.font.color.rgb = TEXT_DARK
    p3.space_before = Pt(10)


# ==============================================================================
# SLIDE 8: 未來擴散性 (Future Scalability)
# Strategic expansion & creative propositions
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Future Scalability", "未來擴散性與再精進方案：構建跨學科特教生態圈",
           "由單一英語教材切片，延伸至多元學科輔具、邊緣生理反饋與校園特教雲端聯網")

expansion_items = [
    ("一、橫向學科擴展：多領域「微單元切片」模組化延伸",
     "將 FocusLingua 驗證成功的「30秒 AI 切片 ＋ 90秒動態鷹架」架構，橫向擴展至國小國語文閱讀理解、數學應用題長句拆解，以及自然科記憶型知識點。實現單一核心引擎支援全年段、多學科之特教輔具標準化。"),
    ("二、邊緣人因感知：結合生理反饋進行「動態疲勞預警」",
     "未來可進一步整合平板視訊鏡頭之輕量化視線追蹤 (Eye-tracking) 或穿戴裝置微心率變異度 (HRV)。當系統偵測到學童眼球頻繁飄移或專注力瀕臨崩潰拐點時，主動調降難度、切換放鬆白噪音，實現真正的自適應人因調節。"),
    ("三、平台化商模：打造「出版教材 ➔ 特資中心 ➔ 班級 ➔ 家長」之 IEP 雲端中樞",
     "LiveABC 可從內容提供商升級為「特教數據中樞」。讓課輔老師一鍵產出的行為分析報表直接同步至學校特教組與家長端 App，消解親師溝通鴻溝，形成高黏著度之特教智慧支持生態圈。")
]

for idx, (title, desc) in enumerate(expansion_items):
    y = Inches(2.0 + idx * 1.65)
    c = create_card(s8, Inches(0.8), y, Inches(11.733), Inches(1.48))
    
    # Left deep green bar
    lb = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y, Inches(0.12), Inches(1.48))
    lb.fill.solid()
    lb.fill.fore_color.rgb = DEEP_GREEN
    lb.line.fill.background()
    
    tb = s8.shapes.add_textbox(Inches(1.15), y + Inches(0.12), Inches(11.1), Inches(1.25))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DEEP_GREEN
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10.2)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(4)


# ==============================================================================
# SLIDE 9: 個人學習成果 (Personal Reflections)
# Senior double major reflection: From fancy tech to disciplined value creation
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Personal Reflections", "個人學習成果與反思：雙主修思維碰撞下的產品成長",
           "回顧參與實作前、後心態轉變：從追求「技術盲目加法」到體會「教育克制減法」的成熟蛻變")

reflections = [
    ("01", "產品思維之蛻變：理解 AI 的核心定位在於「克制減法」",
     "實作初期，我曾執著於使用 Claude 與 Stitch 拼湊華麗的前台選單與 Chatbot 對話。但在特教現場試錯後深刻體會到：注意力不集中的孩子需要的不是眼花繚亂的 AI 炫技，而是「過濾雜訊、降低負載的減法切片」。產品的最高境界不在於能加多少功能，而在於能為使用者減去多少不必要的認知干擾。"),
    ("02", "人機協同之真諦：Human-in-the-Loop 的教育落地嚴謹度",
     "語言教學涉及細膩的同理心與課堂情緒管理，無法完全委由演算法取代。FocusLingua 確立了「AI 負責 30 秒高強度繁重切片，老師把關二次審核與情感陪伴」的分工架構。這使我體認到，優質的 EdTech 方案不是要取代教師，而是賦能教師成為更具專注力與溫度的引路人。"),
    ("03", "跨域視野之整合：應外教學人因 × 財金商管邏輯的實踐檢驗",
     "身為應外與財金雙主修的大四生，這次專案是我大學四年所學最深刻的融合驗證。我將特教實務觀察、TPR/CLT 教學法，與財務分析的成本效益、B2B2C 商業模式深度接軌。學會不僅從「學習者痛點」出發設計體驗，更能以「企業永續營運」視角規劃落地可行性，完成了一次完整的專題實戰淬鍊。")
]

for idx, (num, title, desc) in enumerate(reflections):
    y = Inches(2.0 + idx * 1.65)
    c = create_card(s9, Inches(0.8), y, Inches(11.733), Inches(1.48))
    
    # Left circle with number
    cir = s9.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.1), y + Inches(0.18), Inches(0.42), Inches(0.42))
    cir.fill.solid()
    cir.fill.fore_color.rgb = DEEP_GREEN
    cir.line.fill.background()
    cp = cir.text_frame.paragraphs[0]
    cp.text = num
    cp.font.name = FONT_TITLE
    cp.font.size = Pt(10.5)
    cp.font.bold = True
    cp.font.color.rgb = WHITE
    cp.alignment = PP_ALIGN.CENTER
    
    tb = s9.shapes.add_textbox(Inches(1.7), y + Inches(0.12), Inches(10.5), Inches(1.25))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DEEP_GREEN
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(4)


# ==============================================================================
# SLIDE 10: 結尾 (Thank You / Q&A)
# Matching Page 12 of Business Proposal.pdf
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)

# Decorative dots top-left and bottom-right
add_dot_grid(s10, Inches(0.8), Inches(0.8), cols=5, rows=4)
add_dot_grid(s10, Inches(11.5), Inches(5.8), cols=5, rows=4)

# Center Big "THANK YOU"
ty_box = s10.shapes.add_textbox(Inches(2.0), Inches(2.3), Inches(9.333), Inches(2.8))
tyf = ty_box.text_frame
tyf.word_wrap = True
tyf.margin_left = tyf.margin_top = 0

p_ty = tyf.paragraphs[0]
p_ty.text = "THANK YOU"
p_ty.font.name = FONT_TITLE
p_ty.font.size = Pt(54)
p_ty.font.bold = True
p_ty.font.color.rgb = DEEP_GREEN
p_ty.alignment = PP_ALIGN.CENTER

p_sub = tyf.add_paragraph()
p_sub.text = "FocusLingua 成果專題簡報 ｜ 敬請指教"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(18)
p_sub.font.bold = True
p_sub.font.color.rgb = TEXT_DARK
p_sub.alignment = PP_ALIGN.CENTER
p_sub.space_before = Pt(14)

p_pres = tyf.add_paragraph()
p_pres.text = "陳詠芸 Anna Chen ｜ 中原大學 應外系 × 財金系雙主修"
p_pres.font.name = FONT_BODY
p_pres.font.size = Pt(12)
p_pres.font.color.rgb = TEXT_MUTED
p_pres.alignment = PP_ALIGN.CENTER
p_pres.space_before = Pt(6)

# Output Paths
desktop_path = "/Users/annamei/Desktop/FocusLingua_成果專題簡報.pptx"
notes_path = "/Users/annamei/notes/FocusLingua_成果專題簡報.pptx"

prs.save(desktop_path)
prs.save(notes_path)
print("Business Proposal styled PPTX successfully saved to:")
print(f"1. {desktop_path}")
print(f"2. {notes_path}")
