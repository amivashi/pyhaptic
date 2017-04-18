# -*- coding: utf-8 -*-
# mapping of chair to braille dots

braille = dict()
braille[1] = 0
braille[2] = 16
braille[3] = 32
braille[4] = 2
braille[5] = 18
braille[6] = 34
cells = dict()

# A - Z  a - z
cells["a"] = [braille[1]]
cells["b"] = [braille[1], braille[2]]
cells["c"] = [braille[1], braille[4]]
cells["d"] = [braille[1], braille[4], braille[5]]
cells["e"] = [braille[1], braille[5]]
cells["f"] = [braille[1], braille[2], braille[4]]
cells["g"] = [braille[1], braille[2], braille[4], braille[5]]
cells["h"] = [braille[1], braille[2], braille[5]]
cells["i"] = [braille[2], braille[4]]
cells["j"] = [braille[2], braille[4], braille[5]]
cells["k"] = [braille[1], braille[3]]
cells["l"] = [braille[1], braille[2], braille[3]]
cells["m"] = [braille[1], braille[3], braille[4]]
cells["n"] = [braille[1], braille[3], braille[4], braille[5]]
cells["o"] = [braille[1], braille[3], braille[5]]
cells["p"] = [braille[1], braille[2], braille[3], braille[4]]
cells["q"] = [braille[1], braille[2], braille[3], braille[4], braille[5]]
cells["r"] = [braille[1], braille[2], braille[3], braille[5]]
cells["s"] = [braille[2], braille[3], braille[4]]
cells["t"] = [braille[2], braille[3], braille[4], braille[5]]
cells["u"] = [braille[1], braille[3], braille[6]]
cells["v"] = [braille[1], braille[2], braille[3], braille[6]]
cells["w"] = [braille[2], braille[4], braille[5], braille[6]]
cells["x"] = [braille[1], braille[3], braille[4], braille[6]]
cells["y"] = [braille[1], braille[3], braille[4], braille[5], braille[6]]
cells["z"] = [braille[1], braille[3], braille[5], braille[6]]

# 0 - 9
cells["no"] = [braille[3], braille[4], braille[5], braille[6]]
cells[1] = [braille[1]]
cells[2] = [braille[1], braille[2]]
cells[3] = [braille[1], braille[4]]
cells[4] = [braille[1], braille[4], braille[5]]
cells[5] = [braille[1], braille[5]]
cells[6] = [braille[1], braille[2], braille[4]]
cells[7] = [braille[1], braille[2], braille[4], braille[5]]
cells[8] = [braille[1], braille[2], braille[5]]
cells[9] = [braille[2], braille[4]]
cells[0] = [braille[2], braille[4], braille[5]]

# punctuations
cells[" "] = []
cells[","] = [braille[2]]
cells[";"] = [braille[2], braille[3]]
cells[":"] = [braille[2], braille[5]]
cells["."] = [braille[2], braille[5], braille[6]]
cells["?"] = [braille[2], braille[3], braille[6]]
cells["!"] = [braille[2], braille[3], braille[5]]
cells["\""] = [braille[2], braille[3], braille[5], braille[6]]
cells["“"] = [braille[2], braille[3], braille[5], braille[6]]
cells["”"] = [braille[2], braille[3], braille[5], braille[6]]
cells["‘"] = [braille[3]]
cells["’"] = [braille[3]]
cells["'"] = [braille[3]]
cells["("] = [braille[2], braille[3], braille[6]]
cells[")"] = [braille[3], braille[5], braille[6]]
cells["/"] = [braille[3], braille[4]]
#cells["\\"] = 456 16
cells["–"] = [braille[3], braille[6]]
cells["–"] = [braille[3], braille[6]]
cells["—"] = [braille[3], braille[6]]
cells["-"] = [braille[3], braille[6]]
cells["@"] = [braille[3], braille[4], braille[5]]
cells["*"] = [braille[3], braille[5]]

"""
~
#
$
%
^
&
*
_
+
,
;
:
.
?
'
‘
’
\
/
"
“
”
(
)
[
]
{
}
-
!
@
*
"""