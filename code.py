print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.oneshot import OneShot
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

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

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    # Base layer
    [
     KC.TAB,                KC.Q,         KC.W,           KC.E,                  KC.R,                   KC.T,                                              KC.Y,                           KC.U,             KC.I,                   KC.O,          KC.P,           KC.DEL,
     KC.OS(KC.LALT),        KC.A,         KC.S,           KC.D,                  KC.F,                   KC.G,                                              KC.H,                           KC.K,             KC.K,                   KC.L,          KC.QUOT,        KC.OS(KC.RALT),
     KC.OS(KC.LSFT),        KC.Z,         KC.X,           KC.C,                  KC.V,                   KC.B,                                              KC.N,                           KC.M,             KC.COMM,                KC.DOT,        KC.SLSH,        KC.OS(KC.MO(3)),
     XXXXXXX,               XXXXXXX,      XXXXXXX,        KC.OS(KC.LCTL),        KC.LCMD(KC.ENT),        KC.HT(KC.TAB, KC.FD(1)),                           KC.HT(KC.BSPC,KC.FD(2)),        KC.SPC,           KC.OS(KC.RSFT),         XXXXXXX,       XXXXXXX,        XXXXXXX
    ],
    # Lower layer
    [
     _______,      KC.EXLM,      KC.AT,        KC.HASH,      KC.DLR,       KC.PERC,                                                                         KC.CIRC,      KC.AMPR,      KC.ASTR,      KC.LPRN,       KC.RPRN,      _______,
     _______,      KC.P1,        KC.P2,        KC.P3,        KC.P4,        KC.P5,                                                                           KC.P6,        KC.P7,        KC.P8,        KC.P9,         KC.P0,        _______,
     _______,      XXXXXXX,      KC.TILD,      KC.GRV,       KC.LBRC,      KC.LCBR,                                                                         KC.RCBR,      KC.RBRC,      KC.COMM,      KC.DOT,        KC.SLSH,      _______,
     XXXXXXX,      XXXXXXX,      XXXXXXX,      _______,      _______,      KC.FD(0),                                                                        _______,      _______,      KC.COLN,      XXXXXXX,       XXXXXXX,      XXXXXXX
    ],
    # Raise layer
    [
     _______,      KC.DEL,       XXXXXXX,      KC.UNDS,            KC.PLUS,            KC.PGUP,                                                             XXXXXXX,      XXXXXXX,     XXXXXXX,      KC.BSLS,       KC.PIPE,      _______,
     _______,      KC.HOME,      KC.END,       KC.MINS,            KC.EQL,             KC.PGDN,                                                             KC.APP,       KC.LEFT,     KC.UP,        KC.RIGHT,      KC.DOWN,      _______,
     _______,      KC.LABK,      KC.RABK,      KC.LCMD(KC.C),      KC.LCMD(KC.V),      KC.SCLN,                                                             KC.MPLY,      KC.MPRV,     KC.MNXT,      KC.VOLD,       KC.VOLU,      _______,
     XXXXXXX,      XXXXXXX,      XXXXXXX,      KC.LCTL(KC.ESC),    _______,            XXXXXXX,                                                             KC.FD(0),     _______,     _______,      XXXXXXX,       XXXXXXX,      XXXXXXX
    ],
    # Func layer
    [
     _______,      KC.F1,         KC.F2,         KC.F3,        KC.F4,        KC.F5,                                                                          KC.F6,        KC.F7,         KC.F8,        KC.F9,         KC.F10,       _______,
     _______,      KC.F11,        KC.F12,        XXXXXXX,      XXXXXXX,      XXXXXXX,                                                                        XXXXXXX,      XXXXXXX,       XXXXXXX,      XXXXXXX,       XXXXXXX,      _______,
     _______,      XXXXXXX,       XXXXXXX,       XXXXXXX,      XXXXXXX,      XXXXXXX,                                                                        XXXXXXX,      XXXXXXX,       XXXXXXX,      XXXXXXX,       XXXXXXX,      XXXXXXX,
     _______,      XXXXXXX,       XXXXXXX,       XXXXXXX,      XXXXXXX,      XXXXXXX,                                                                        XXXXXXX,      KC.FD(0),      XXXXXXX,      XXXXXXX,       XXXXXXX,      XXXXXXX
    ]
]    

if __name__ == '__main__':
    keyboard.go()

