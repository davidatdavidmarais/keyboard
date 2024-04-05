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

keyboard.keymap = [
    # Base layer
    [
     KC.TAB,                KC.Q,         KC.W,           KC.E,                  KC.R,                   KC.T,                                              KC.Y,           KC.U,          KC.I,           KC.O,          KC.P,           KC.LBRC,
     KC.OS(KC.LALT),        KC.A,         KC.S,           KC.D,                  KC.F,                   KC.G,                                              KC.H,           KC.K,          KC.K,           KC.L,          KC.SCLN,        KC.QUOT,
     KC.OS(KC.LSFT),        KC.Z,         KC.X,           KC.C,                  KC.V,                   KC.B,                                              KC.N,           KC.M,          KC.COMM,        KC.DOT,        KC.SLSH,        KC.RSFT,
     KC.NO,                 KC.NO,        KC.NO,          KC.OS(KC.LCTL),        KC.LGUI(KC.ENT),        KC.HT(KC.TAB, KC.FD(1)),                                  KC.BSPC,        KC.ENT,        KC.MEH,         KC.NO,         KC.NO,          KC.NO
    ],
    # Lower layer
    [
     KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,                                                                         KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,       KC.TRNS,      KC.TRNS,  
     KC.NO,        KC.P1,        KC.P2,        KC.P3,        KC.P4,        KC.P5,                                                                           KC.P6,        KC.P7,        KC.P8,        KC.P9,         KC.P0,        KC.NO,  
     KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,                                                                         KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.TRNS,       KC.TRNS,      KC.TRNS,  
     KC.NO,        KC.NO,        KC.NO,        KC.TRNS,      KC.TRNS,      KC.FD(0),                                                                        KC.TRNS,      KC.TRNS,      KC.TRNS,      KC.NO,         KC.NO,        KC.NO
    ],
]    

if __name__ == '__main__':
    keyboard.go()

