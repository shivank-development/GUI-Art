"""
Ultimate Poker: Animated GUI + smarter AI + table graphics + sounds
Requirements:
 - Pillow (PIL)  -> pip install pillow
 - pygame (for sound) -> pip install pygame
 - assets: cards/*.png (52 cards + back.png), table.png, deal.wav, win.wav
Place this script in the same folder as table.png, deal.wav, win.wav and a 'cards' folder.
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random, os, math, time
from collections import Counter
import pygame

# ----------------- Init Sound -----------------
pygame.mixer.init()
def play_sound(fname):
    try:
        pygame.mixer.Sound(fname).play()
    except Exception as e:
        print("Sound error:", e)

# ----------------- Config -----------------
ROOT_W, ROOT_H = 1200, 800
cards_folder = "cards"
table_image_file = "table.png"
deal_sound = "deal.wav"
win_sound = "win.wav"

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# players: human + 2 AIs (extendable)
players = [
    {"name":"You",  "chips":200, "hand":[], "bet":0, "folded":False},
    {"name":"AI_1", "chips":200, "hand":[], "bet":0, "folded":False},
    {"name":"AI_2", "chips":200, "hand":[], "bet":0, "folded":False}
]

# animation & gameplay globals
deck = []
hold_flags = [False]*5
max_rounds = 12
current_round = 1
pot = 0
card_size = (100,145)
deal_pos = (ROOT_W//2 - 50, 80)  # deck position (x,y)
player_positions = []  # will hold target coordinates for each player's card slots

# ----------------- Helper: card value & hand ranking -----------------
def card_value(card_name):
    # card_name like 'A_of_Spades.png' or '10_of_Hearts.png'
    rank = os.path.basename(card_name).split("_of_")[0]
    if rank.isdigit():
        return int(rank)
    return {'J':11,'Q':12,'K':13,'A':14}.get(rank, 0)

def hand_rank(hand):
    values = sorted([card_value(c) for c in hand], reverse=True)
    suits_list = [os.path.basename(c).split("_of_")[1].split(".")[0] for c in hand]
    counts = Counter(values)
    is_flush = len(set(suits_list)) == 1
    # handle wheel (A-2-3-4-5) as straight: treat A as 1 if needed
    vs = sorted(set(values))
    is_straight = False
    if len(vs)==5 and max(vs)-min(vs)==4:
        is_straight = True
    elif vs == [2,3,4,5,14]:  # A-2-3-4-5
        is_straight = True
        values = [5,4,3,2,1]
    # rank ordering: highest tuple wins lexicographically
    if is_straight and is_flush and max(values) == 14:
        return (10, values)  # Royal Flush
    if is_straight and is_flush:
        return (9, values)
    if 4 in counts.values():
        # four of a kind: primary key = value of four, then kicker
        four = [v for v,c in counts.items() if c==4][0]
        kicker = [v for v in values if v!=four]
        return (8, [four]+kicker)
    if 3 in counts.values() and 2 in counts.values():
        three = [v for v,c in counts.items() if c==3][0]
        pair = [v for v,c in counts.items() if c==2][0]
        return (7, [three, pair])
    if is_flush:
        return (6, values)
    if is_straight:
        return (5, values)
    if 3 in counts.values():
        three = [v for v,c in counts.items() if c==3][0]
        kickers = sorted([v for v in values if v!=three], reverse=True)
        return (4, [three]+kickers)
    if list(counts.values()).count(2) == 2:
        pairs = sorted([v for v,c in counts.items() if c==2], reverse=True)
        kicker = [v for v in values if v not in pairs]
        return (3, pairs + kicker)
    if 2 in counts.values():
        pair = [v for v,c in counts.items() if c==2][0]
        kickers = sorted([v for v in values if v!=pair], reverse=True)
        return (2, [pair]+kickers)
    return (1, values)

# ----------------- AI: improved strategy considering opponent bets -----------------
def evaluate_hand_strength(hand):
    """Return a float 0..1 estimating hand strength (simple heuristic)."""
    score, vals = hand_rank(hand)
    # base from rank
    base = score / 10.0
    # minor boost for high card values
    high = sum(vals[:2]) / 28.0  # max top2 = 14+13=27 ~ scale
    return min(1.0, base*0.8 + high*0.2)

def ai_place_bet(ai_index):
    ai = players[ai_index]
    # look at player's bet to decide reaction
    my_strength = evaluate_hand_strength(ai["hand"])
    # see max current player bet among others
    other_bets = [p["bet"] for i,p in enumerate(players) if i!=ai_index]
    max_other = max(other_bets) if other_bets else 0
    # base bet proportional to strength and chips
    base = int(max(5, min(ai["chips"],  int( (my_strength*30) + random.randint(-3,6) ))))
    # if opponents bet high and strength is low -> fold sometimes
    if max_other > 0 and my_strength < 0.35 and random.random() < 0.6:
        ai["folded"] = True
        ai["bet"] = 0
        return
    # if strong, raise above opponents
    if my_strength > 0.75:
        ai["bet"] = min(ai["chips"], max_other + base)
    else:
        ai["bet"] = min(ai["chips"], max(base, max_other))
    # small random bluff
    if my_strength < 0.4 and random.random() < 0.08 and ai["chips"]>10:
        ai["bet"] = min(ai["chips"], max_other + random.randint(5,15))  # bluff
    # ensure at least minimal bet if no prior bets
    if sum(other_bets)==0 and ai["bet"] < 5:
        ai["bet"] = 5

# ----------------- Deck helpers -----------------
def reset_deck():
    global deck
    deck = [f"{r}_of_{s}.png" for s in suits for r in ranks]
    random.shuffle(deck)

# ----------------- GUI init -----------------
root = tk.Tk()
root.title("Ultimate Animated Poker (Pro)")
root.geometry(f"{ROOT_W}x{ROOT_H}")
root.resizable(False, False)

# canvas for table + sliding animations
canvas = tk.Canvas(root, width=ROOT_W, height=ROOT_H)
canvas.pack()

# load table background if exists
if os.path.exists(table_image_file):
    tbl_img = Image.open(table_image_file).resize((ROOT_W, ROOT_H))
    tbl_photo = ImageTk.PhotoImage(tbl_img)
    canvas.create_image(0,0,anchor='nw',image=tbl_photo)
else:
    # simple green background
    canvas.create_rectangle(0,0,ROOT_W,ROOT_H, fill="#2d7a2d")

# compute player card slots (x,y) for 5 cards each around the table
def compute_player_positions():
    # positions for 3 players: bottom (human), left-top, right-top
    positions = []
    # Human (bottom center)
    base_x = ROOT_W//2 - (5*card_size[0] + 4*10)//2
    y = ROOT_H - 220
    human_slots = [(base_x + i*(card_size[0]+10), y) for i in range(5)]
    positions.append(human_slots)
    # AI_1 (left)
    x_left = 140
    y_top = 180
    ai1_slots = [(x_left, y_top + i*(card_size[1]//2)) for i in range(5)]
    positions.append(ai1_slots)
    # AI_2 (right)
    x_right = ROOT_W - 140 - card_size[0]
    ai2_slots = [(x_right, y_top + i*(card_size[1]//2)) for i in range(5)]
    positions.append(ai2_slots)
    return positions

player_positions = compute_player_positions()

# keep references to card images to avoid garbage collection
canvas_images = []  # list of canvas image ids

def load_card_image(name):
    path = os.path.join(cards_folder, name)
    if not os.path.exists(path):
        # fallback to back
        path = os.path.join(cards_folder, "red_joker.png")  # use a joker as back if exists
    img = Image.open(path).resize(card_size)
    return ImageTk.PhotoImage(img)

# card back image reference
back_img = load_card_image("red_joker.png")  # use a joker as back if exists

# UI frames (below canvas) for controls: bets, chips, buttons
ctrl_frame = tk.Frame(root, bg="#2b2b2b")
ctrl_frame.place(x=10, y=10)  # small control in top-left (transparent feel)
# Show chips & bet entry
player_labels = []
for i,p in enumerate(players):
    lbl = tk.Label(root, text=f"{p['name']}: {p['chips']} chips", bg="#2b2b2b", fg="white", font=("Arial",12))
    # place near their first card slot
    slot_x, slot_y = player_positions[i][0]
    lbl.place(x=slot_x, y=slot_y-30)
    player_labels.append(lbl)

bet_entry = tk.Entry(root, width=6, font=("Arial",14))
bet_entry.insert(0,"10")
bet_entry.place(x=ROOT_W//2 - 40, y=30)

pot_label = tk.Label(root, text=f"Pot: {pot}", bg="#2b2b2b", fg="white", font=("Arial",14))
pot_label.place(x=ROOT_W//2 - 30, y=5)

round_label = tk.Label(root, text=f"Round: {current_round}/{max_rounds}", bg="#2b2b2b", fg="white", font=("Arial",12))
round_label.place(x=ROOT_W-180, y=5)

# clickable overlays for human cards (store their canvas ids)
human_card_ids = [None]*5
human_hold_marks = [None]*5

# ----------------- Animation: slide from deck -> target -----------------
def slide_card(card_img, start, target, on_done=None, steps=18, delay=12):
    """Animate a canvas image from start(x,y) to target(x,y)."""
    x0,y0 = start
    x1,y1 = target
    dx = (x1 - x0) / steps
    dy = (y1 - y0) / steps
    img_id = canvas.create_image(x0, y0, image=card_img, anchor='nw')
    canvas_images.append((img_id, card_img))  # keep reference
    def step(i=0):
        nonlocal x0,y0
        if i >= steps:
            if on_done:
                on_done(img_id)
            return
        canvas.move(img_id, dx, dy)
        root.after(delay, lambda: step(i+1))
    step(0)
    return img_id

# ----------------- Deal logic -----------------
def clear_table_images():
    global canvas_images
    for cid, _ in list(canvas_images):
        try:
            canvas.delete(cid)
        except:
            pass
    canvas_images = []
    # clear human references
    for i in range(5):
        human_card_ids[i] = None
        if human_hold_marks[i]:
            canvas.delete(human_hold_marks[i])
            human_hold_marks[i] = None

def deal_initial_cards():
    global pot
    clear_table_images()
    play_sound(deal_sound)
    reset_deck()
    # reset player states
    for p in players:
        p["hand"] = []
        p["bet"] = 0
        p["folded"] = False
    # place player bets: read human entry, AI decide
    try:
        hb = int(bet_entry.get())
        if hb <=0 or hb > players[0]["chips"]:
            raise ValueError
        players[0]["bet"] = hb
    except:
        messagebox.showwarning("Invalid Bet","Enter valid bet (<= your chips)")
        return
    # AI bets
    for ai_idx in range(1, len(players)):
        ai_place_bet(ai_idx)
    # calculate pot initially
    pot = sum(p["bet"] for p in players)
    pot_label.config(text=f"Pot: {pot}")
    # animate dealing: deal 5 cards to each player in round-robin
    deal_order = []
    for r in range(5):
        for i in range(len(players)):
            deal_order.append((i,r))
    def deal_seq(idx=0):
        if idx >= len(deal_order):
            # after dealing, show human cards interactive and show back for AIs
            show_human_cards()
            show_ai_backs()
            update_labels()
            return
        i,rslot = deal_order[idx]
        card = deck.pop()
        players[i]["hand"].append(card)
        # compute target pos: add small offset so card centers correctly
        tx,ty = player_positions[i][rslot]
        # start from deck pos with slight offset
        start = deal_pos
        img = load_card_image(card)
        # for AI show back initially (but keep card in hand)
        if i!=0:
            show_img = back_img
        else:
            show_img = img
        # slide card
        slide_card(show_img, start, (tx,ty), on_done=None)
        # short delay between deals
        root.after(120, lambda idx=idx+1: deal_seq(idx))
        play_sound(deal_sound)
    deal_seq(0)

def show_human_cards():
    # place interactive images for human cards that can be clicked to hold
    base = player_positions[0]
    for i, card in enumerate(players[0]["hand"]):
        tx,ty = base[i]
        img = load_card_image(card)
        def on_done_factory(idx, card_img):
            # create a clickable overlay (we already have image created by slide)
            # create a fresh image to ensure we can bind events
            img_id = canvas.create_image(tx,ty, image=card_img, anchor='nw')
            canvas_images.append((img_id, card_img))
            human_card_ids[idx] = img_id
            # binding click
            canvas.tag_bind(img_id, "<Button-1>", lambda e, ix=idx: toggle_hold_visual(ix))
        # directly create (no slide) to ensure good responsiveness
        on_done_factory(i, img)

def show_ai_backs():
    # show backs for AI hands in their slots
    for pi in range(1, len(players)):
        base = player_positions[pi]
        for j in range(5):
            tx,ty = base[j]
            img_id = canvas.create_image(tx,ty, image=back_img, anchor='nw')
            canvas_images.append((img_id, back_img))

# ----------------- Hold visuals -----------------
def toggle_hold_visual(idx):
    hold_flags[idx] = not hold_flags[idx]
    # draw/erase small rectangle border on card
    cid = human_card_ids[idx]
    if cid is None:
        return
    x,y = canvas.coords(cid)
    if hold_flags[idx]:
        # yellow border rectangle
        rect = canvas.create_rectangle(x-4,y-4, x+card_size[0]+4, y+card_size[1]+4, outline="yellow", width=4)
        human_hold_marks[idx] = rect
    else:
        if human_hold_marks[idx]:
            canvas.delete(human_hold_marks[idx])
            human_hold_marks[idx] = None

# ----------------- Replace discarded (with small slide-in) -----------------
def replace_discarded():
    global pot
    # player's replacements
    for i in range(5):
        if not hold_flags[i]:
            # remove old image id if present
            if human_card_ids[i]:
                try: canvas.delete(human_card_ids[i])
                except: pass
            new_card = deck.pop()
            players[0]["hand"][i] = new_card
            tx,ty = player_positions[0][i]
            img = load_card_image(new_card)
            # slide from deck to slot
            slide_card(img, deal_pos, (tx,ty))
    # AI replacements: smarter choices using ai_decide_holds
    for ai_index in range(1, len(players)):
        ai_hold_idxs = ai_decide_holds_smarter(players[ai_index])
        for slot in range(5):
            if slot not in ai_hold_idxs:
                # replace
                players[ai_index]["hand"][slot] = deck.pop()
    # after replacements, show final ai cards (reveal) with slide from back to slot
    for pi in range(1, len(players)):
        base = player_positions[pi]
        for j,card in enumerate(players[pi]["hand"]):
            tx,ty = base[j]
            img = load_card_image(card)
            slide_card(img, deal_pos, (tx,ty))
    # update pot with any additional bets (for simplicity we assume bets fixed this stage)
    pot = sum(p["bet"] for p in players)
    pot_label.config(text=f"Pot: {pot}")
    play_sound(deal_sound)
    # small delay then determine winner
    root.after(900, determine_winner)

# Improved AI hold logic considering hand strength and visible opponent bet sizes
def ai_decide_holds_smarter(ai_player):
    hand = ai_player["hand"]
    score, vals = hand_rank(hand)
    hold_idxs = []
    counts = Counter([card_value(c) for c in hand])
    # Keep any pairs/trips/quads
    for i,c in enumerate(hand):
        v = card_value(c)
        if counts[v] > 1:
            hold_idxs.append(i)
    # If no pair but high cards present, keep top 1 maybe
    if not hold_idxs:
        top_idx = max(range(len(hand)), key=lambda i: card_value(hand[i]))
        if card_value(hand[top_idx]) >= 11 and random.random() < 0.7:
            hold_idxs.append(top_idx)
    # If ai betted high earlier and still has moderate strength, hold more
    if ai_player.get("bet",0) > 15 and evaluate_hand_strength(hand) > 0.4:
        # keep top 2
        sorted_idxs = sorted(range(5), key=lambda i: card_value(hand[i]), reverse=True)
        for idx in sorted_idxs[:2]:
            if idx not in hold_idxs:
                hold_idxs.append(idx)
    return sorted(set(hold_idxs))

# ----------------- Determine winner & payout -----------------
def determine_winner():
    global pot, current_round
    # compute ranks for players who didn't fold
    ranked = []
    for p in players:
        if p.get("folded"):
            ranked.append((p, (0,[])))  # folded become weakest
        else:
            ranked.append((p, hand_rank(p["hand"])))
    # compare by tuple (score, values) lexicographically
    # first find best numeric rank
    def score_key(item):
        p, (sc, vals) = item
        return (sc, vals)
    best = max(ranked, key=score_key)
    # find all equal winners (tie)
    winners = [p for p, hv in ranked if hv == best[1]]
    # payout: pot collected from bets
    pot = sum(p["bet"] for p in players)
    if len(winners)==1:
        winners[0]["chips"] += pot
    else:
        # split
        share = pot // len(winners)
        for w in winners:
            w["chips"] += share
    # deduct bets already placed (they were not removed from chips earlier)
    for p in players:
        p["chips"] -= p.get("bet",0)
    update_ui_after_round(winners)
    play_sound(win_sound)
    current_round += 1
    if current_round > max_rounds or any(p["chips"]<=0 for p in players):
        # tournament ends
        champion = max(players, key=lambda x: x["chips"])
        messagebox.showinfo("Tournament Over", f"Tournament Over! Winner: {champion['name']}")
        root.destroy()

def deal_card_animation(frame, card, col, callback=None):
    path = os.path.join(cards_folder, card)
    if not os.path.exists(path):  # agar back.png missing hai
        label = tk.Label(frame, text=card.split(".")[0], font=("Arial",12), width=10, height=5, relief="raised")
        label.grid(row=0, column=col, padx=5)
    else:
        img = Image.open(path).resize((100,145))
        img = ImageTk.PhotoImage(img)
        label = tk.Label(frame, image=img)
        label.image = img
        label.grid(row=0, column=col, padx=5)


def update_ui_after_round(winners):
    # reveal all hands on table already done; update label texts
    for i,p in enumerate(players):
        player_labels[i].config(text=f"{p['name']}: {p['chips']} chips")
    # mark winners
    names = ", ".join([w["name"] for w in winners])
    messagebox.showinfo("Round Result", f"Winner(s): {names}")
    pot_label.config(text=f"Pot: 0")
    # reset for next; small delay then clear table for next round
    root.after(1200, lambda: clear_table_images())

def update_labels():
    for i,p in enumerate(players):
        player_labels[i].config(text=f"{p['name']}: {p['chips']} chips")
    round_label.config(text=f"Round: {current_round}/{max_rounds}")
    pot_label.config(text=f"Pot: {sum(p['bet'] for p in players)}")

# ----------------- Buttons -----------------
btn_frame_y = ROOT_H - 60
start_btn = tk.Button(root, text="Start Round", font=("Arial",14), command=deal_initial_cards)
start_btn.place(x=ROOT_W//2 - 250, y=btn_frame_y)

replace_btn = tk.Button(root, text="Replace Discarded", font=("Arial",14), command=replace_discarded)
replace_btn.place(x=ROOT_W//2 - 80, y=btn_frame_y)

next_btn = tk.Button(root, text="Next Round (Force)", font=("Arial",12), command=lambda: (clear_table_images(),))
next_btn.place(x=ROOT_W//2 + 170, y=btn_frame_y)

# ----------------- On start -----------------
reset_deck()
update_labels()

# Start Tk mainloop
root.mainloop()
