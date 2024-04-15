print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.oneshot import OneShot
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

split = Split(split_type=SplitType.UART, split_flip=True, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

keyboard.col_pins = (board.GP22, board.GP10, board.GP18, board.GP19, board.GP21, board.GP20)
keyboard.row_pins = (board.GP8, board.GP7, board.GP6, board.GP5)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

oneshot = OneShot()
oneshot.tap_time = 2000
keyboard.modules.append(oneshot)

holdtap = HoldTap()
holdtap.tap_time = 200
keyboard.modules.append(holdtap)

___ = KC.TRNS
N_A = KC.NO

# MULTI
CA = KC.LCTRL(KC.LALT)
CC = KC.LCMD(KC.C)
CV = KC.LCMD(KC.V)
# OS
OS_ALT = KC.OS(KC.LALT)
OS_SFT = KC.OS(KC.LSFT)
OS_MEH = KC.OS(KC.MEH)
# HT
HT_ENT_GUI = KC.HT(KC.ENT, KC.LGUI)
# LEVELS
L0 = KC.FD(0)
L1 = KC.FD(1)
L2 = KC.FD(2)
L3 = KC.FD(3)


keyboard.keymap = [
    # Base layer
    [
     KC.HT(KC.TAB, CA),    KC.Q,         KC.W,        KC.E,               KC.R,               KC.T,                                       KC.Y,           KC.U,         KC.I,               KC.O,          KC.P,           KC.ESC,
     OS_SFT,               KC.HT(KC.A, KC.LALT, prefer_hold=False),      KC.HT(KC.S, KC.LCMD, prefer_hold=False),        KC.HT(KC.D, KC.LGUI, prefer_hold=False),               KC.HT(KC.F, KC.SFT, prefer_hold=False),               KC.G, KC.H, KC.HT(KC.J, KC.SFT, prefer_hold=False),              KC.HT(KC.K, KC.LGUI, prefer_hold=False),          KC.HT(KC.L, KC.LCMD, prefer_hold=False),         KC.HT(KC.SCLN, KC.LALT, prefer_hold=False),        KC.QUOT,
     OS_ALT,               KC.Z,         KC.X,        KC.C,               KC.V,               KC.B,                                       KC.N,           KC.M,         KC.COMM,            KC.DOT,        KC.SLSH,        KC.QUES,
     N_A,                  N_A,          N_A,         OS_MEH,             HT_ENT_GUI,         KC.HT(L1, KC.MO(2)),                        KC.HT(KC.BSPC, KC.MO(1)),        KC.SPC,       KC.LCTL,            N_A,           N_A,            N_A
    ],
    # Lower layer
    [
     KC.EXLM,             KC.AT,        KC.HASH,      KC.DLR,             KC.PERC,            KC.CIRC,                                    KC.AMPR,        KC.ASTR,      KC.LPRN,            KC.RPRN,       KC.UNDS,        KC.PPLS,  
     KC.P1,               KC.P2,        KC.P3,        KC.P4,              KC.P5,              KC.P6,                                      KC.P7,          KC.P8,        KC.P9,              KC.P0,         KC.MINUS,       KC.EQL,
     KC.OS(KC.LSFT),      N_A,          KC.TILD,      KC.GRV,             KC.LBRC,            KC.LCBR,                                    KC.RCBR,        KC.RBRC,      KC.LABK,            KC.RABK,       KC.QUES,        KC.QUES,
     N_A,                 N_A,          N_A,          OS_MEH,             HT_ENT_GUI,         L2,                                         L0,             KC.SPC,       KC.COLN,            N_A,           N_A,            N_A
    ],
    # Raise layer
    [
     KC.HT(KC.TAB, CA),   KC.DEL,       N_A,          KC.UNDS,            KC.PLUS,            KC.PGUP,                                    N_A,            N_A,          KC.UP,              KC.BSLS,       KC.PIPE,        ___,
     KC.LSFT,             KC.HOME,      KC.END,       KC.MINS,            KC.EQL,             KC.PGDN,                                    KC.APP,         KC.LEFT,      KC.DOWN,            KC.RIGHT,      KC.DOWN,        ___,
     KC.LALT,             KC.LABK,      KC.RABK,      CC,                 CV,                 KC.SCLN,                                    KC.MPLY,        KC.MPRV,      KC.MNXT,            KC.VOLD,       KC.VOLU,        ___,
     N_A,                 N_A,          N_A,          ___,                ___,                L3,                                         L0,             ___,          ___,                N_A,           N_A,            N_A
    ],
    # Func layer
    [
     KC.F1,               KC.F2,        KC.F3,        KC.F4,              KC.F5,              KC.F6,                                      KC.F7,          KC.F8,        KC.F9,              KC.F10,        KC.F11,         KC.F12,
     KC.P0,               KC.P1,        KC.P2,        KC.P3,              KC.P4,              KC.P5,                                      KC.P6,          KC.P7,        KC.P8,              KC.P9,         ___,            ___,
     ___,                 N_A,          N_A,          N_A,                N_A,                N_A,                                        N_A,            N_A,          N_A,                N_A,           N_A,            N_A,
     ___,                 N_A,          N_A,          N_A,                N_A,                N_A,                                        L0,             N_A,          N_A,                N_A,           N_A,            N_A
    ]
]    

if __name__ == '__main__':
    keyboard.go()





