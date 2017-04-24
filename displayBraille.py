# -*- coding: utf-8 -*-
# mapping of chair to braille dots

braille = dict()
braille[4] = 0
braille[5] = 8
braille[6] = 16
braille[1] = 7
braille[2] = 15
braille[3] = 23

vibration = dict()
vibration["letter"] = 1
vibration["capital"] = 2
vibration["number"] = 3
vibration["special"] = 1

sleep = dict()
sleep["letter"] = 1.8
sleep["capital"] = 2.5
sleep["number"] = 3.5
sleep["special"] = 1.8


# cells representation of characters
cells = dict()
# a - z
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

# A - Z
cells["A"] = [braille[1]]
cells["B"] = [braille[1], braille[2]]
cells["C"] = [braille[1], braille[4]]
cells["D"] = [braille[1], braille[4], braille[5]]
cells["E"] = [braille[1], braille[5]]
cells["F"] = [braille[1], braille[2], braille[4]]
cells["G"] = [braille[1], braille[2], braille[4], braille[5]]
cells["H"] = [braille[1], braille[2], braille[5]]
cells["I"] = [braille[2], braille[4]]
cells["J"] = [braille[2], braille[4], braille[5]]
cells["K"] = [braille[1], braille[3]]
cells["L"] = [braille[1], braille[2], braille[3]]
cells["M"] = [braille[1], braille[3], braille[4]]
cells["N"] = [braille[1], braille[3], braille[4], braille[5]]
cells["O"] = [braille[1], braille[3], braille[5]]
cells["P"] = [braille[1], braille[2], braille[3], braille[4]]
cells["Q"] = [braille[1], braille[2], braille[3], braille[4], braille[5]]
cells["R"] = [braille[1], braille[2], braille[3], braille[5]]
cells["S"] = [braille[2], braille[3], braille[4]]
cells["T"] = [braille[2], braille[3], braille[4], braille[5]]
cells["U"] = [braille[1], braille[3], braille[6]]
cells["V"] = [braille[1], braille[2], braille[3], braille[6]]
cells["W"] = [braille[2], braille[4], braille[5], braille[6]]
cells["X"] = [braille[1], braille[3], braille[4], braille[6]]
cells["Y"] = [braille[1], braille[3], braille[4], braille[5], braille[6]]
cells["Z"] = [braille[1], braille[3], braille[5], braille[6]]

# 0 - 9
cells["no"] = [braille[3], braille[4], braille[5], braille[6]]
cells["1"] = [braille[1]]
cells["2"] = [braille[1], braille[2]]
cells["3"] = [braille[1], braille[4]]
cells["4"] = [braille[1], braille[4], braille[5]]
cells["5"] = [braille[1], braille[5]]
cells["6"] = [braille[1], braille[2], braille[4]]
cells["7"] = [braille[1], braille[2], braille[4], braille[5]]
cells["8"] = [braille[1], braille[2], braille[5]]
cells["9"] = [braille[2], braille[4]]
cells["0"] = [braille[2], braille[4], braille[5]]
cells["="] = [braille[1],braille[2], braille[3], braille[4], braille[5], braille[6]]
# punctuations
cells[" "] = []
cells[","] = [braille[2]]
cells[";"] = [braille[2], braille[3]]
cells[":"] = [braille[2], braille[5]]
cells["."] = [braille[2], braille[5], braille[6]]
cells["."] = [braille[2], braille[5], braille[6]]
cells["?"] = [braille[2], braille[3], braille[6]]
cells["!"] = [braille[2], braille[3], braille[5]]
cells["\""] = [braille[2], braille[3], braille[5], braille[6]]
cells["("] = [braille[2], braille[3], braille[5], braille[6]]
cells[")"] = [braille[2], braille[3], braille[5], braille[6]]
cells["["] = [braille[2], braille[3], braille[5], braille[6]]
cells["]"] = [braille[2], braille[3], braille[5], braille[6]]
cells["‘"] = [braille[3]]
cells["’"] = [braille[3]]
cells["'"] = [braille[3]]
cells["“"] = [braille[2], braille[3], braille[6]]
cells["”"] = [braille[3], braille[5], braille[6]]
cells["/"] = [braille[3], braille[4]]
#cells["\\"] = 456 16
cells["–"] = [braille[3], braille[6]]
cells["–"] = [braille[3], braille[6]]
cells["—"] = [braille[3], braille[6]]
cells["-"] = [braille[3], braille[6]]
cells["@"] = [braille[3], braille[4], braille[5]]
cells["*"] = [braille[3], braille[5]]
cells["#"] = [braille[3], braille[4], braille[5], braille[6]]

#Frequency Vibration of characters
freq = dict()
# a - z
freq["a"] = vibration["letter"]
freq["b"] = vibration["letter"]
freq["c"] = vibration["letter"]
freq["d"] = vibration["letter"]
freq["e"] = vibration["letter"]
freq["f"] = vibration["letter"]
freq["g"] = vibration["letter"]
freq["h"] = vibration["letter"]
freq["i"] = vibration["letter"]
freq["j"] = vibration["letter"]
freq["k"] = vibration["letter"]
freq["l"] = vibration["letter"]
freq["m"] = vibration["letter"]
freq["n"] = vibration["letter"]
freq["o"] = vibration["letter"]
freq["p"] = vibration["letter"]
freq["q"] = vibration["letter"]
freq["r"] = vibration["letter"]
freq["s"] = vibration["letter"]
freq["t"] = vibration["letter"]
freq["u"] = vibration["letter"]
freq["v"] = vibration["letter"]
freq["w"] = vibration["letter"]
freq["x"] = vibration["letter"]
freq["y"] = vibration["letter"]
freq["z"] = vibration["letter"]
freq["="] = vibration["letter"]
# A - Z
freq["A"] = vibration["capital"]
freq["B"] = vibration["capital"]
freq["C"] = vibration["capital"]
freq["D"] = vibration["capital"]
freq["E"] = vibration["capital"]
freq["F"] = vibration["capital"]
freq["G"] = vibration["capital"]
freq["H"] = vibration["capital"]
freq["I"] = vibration["capital"]
freq["J"] = vibration["capital"]
freq["K"] = vibration["capital"]
freq["L"] = vibration["capital"]
freq["M"] = vibration["capital"]
freq["N"] = vibration["capital"]
freq["O"] = vibration["capital"]
freq["P"] = vibration["capital"]
freq["Q"] = vibration["capital"]
freq["R"] = vibration["capital"]
freq["S"] = vibration["capital"]
freq["T"] = vibration["capital"]
freq["U"] = vibration["capital"]
freq["V"] = vibration["capital"]
freq["W"] = vibration["capital"]
freq["X"] = vibration["capital"]
freq["Y"] = vibration["capital"]
freq["Z"] = vibration["capital"]

# 0 - 9
freq["1"] = vibration["number"]
freq["2"] = vibration["number"]
freq["3"] = vibration["number"]
freq["4"] = vibration["number"]
freq["5"] = vibration["number"]
freq["6"] = vibration["number"]
freq["7"] = vibration["number"]
freq["8"] = vibration["number"]
freq["9"] = vibration["number"]
freq["0"] = vibration["number"]

# punctuations
freq[" "] = vibration["letter"]
freq[","] = vibration["special"]
freq[";"] = vibration["special"]
freq[":"] = vibration["special"]
freq["."] = vibration["special"]
freq["?"] = vibration["special"]
freq["!"] = vibration["special"]
freq["\""] =vibration["special"]
freq["“"] = vibration["special"]
freq["”"] = vibration["special"]
freq["‘"] = vibration["special"]
freq["’"] = vibration["special"]
freq["'"] = vibration["special"]
freq["("] = vibration["special"]
freq[")"] = vibration["special"]
freq["/"] = vibration["special"]
#freq["\\"] = 456 16vibration["special"]
freq["–"] = vibration["special"]
freq["–"] = vibration["special"]
freq["—"] = vibration["special"]
freq["-"] = vibration["special"]
freq["@"] = vibration["special"]
freq["*"] = vibration["special"]
freq["#"] = vibration["special"]
freq["["] = vibration["special"]
freq["]"] = vibration["special"]

#sleep time of characters
slp = dict()
# a - z
slp["a"] = sleep["letter"]
slp["b"] = sleep["letter"]
slp["c"] = sleep["letter"]
slp["d"] = sleep["letter"]
slp["e"] = sleep["letter"]
slp["f"] = sleep["letter"]
slp["g"] = sleep["letter"]
slp["h"] = sleep["letter"]
slp["i"] = sleep["letter"]
slp["j"] = sleep["letter"]
slp["k"] = sleep["letter"]
slp["l"] = sleep["letter"]
slp["m"] = sleep["letter"]
slp["n"] = sleep["letter"]
slp["o"] = sleep["letter"]
slp["p"] = sleep["letter"]
slp["q"] = sleep["letter"]
slp["r"] = sleep["letter"]
slp["s"] = sleep["letter"]
slp["t"] = sleep["letter"]
slp["u"] = sleep["letter"]
slp["v"] = sleep["letter"]
slp["w"] = sleep["letter"]
slp["x"] = sleep["letter"]
slp["y"] = sleep["letter"]
slp["z"] = sleep["letter"]
slp["="] = sleep["letter"]
# A - Z
slp["A"] = sleep["capital"]
slp["B"] = sleep["capital"]
slp["C"] = sleep["capital"]
slp["D"] = sleep["capital"]
slp["E"] = sleep["capital"]
slp["F"] = sleep["capital"]
slp["G"] = sleep["capital"]
slp["H"] = sleep["capital"]
slp["I"] = sleep["capital"]
slp["J"] = sleep["capital"]
slp["K"] = sleep["capital"]
slp["L"] = sleep["capital"]
slp["M"] = sleep["capital"]
slp["N"] = sleep["capital"]
slp["O"] = sleep["capital"]
slp["P"] = sleep["capital"]
slp["Q"] = sleep["capital"]
slp["R"] = sleep["capital"]
slp["S"] = sleep["capital"]
slp["T"] = sleep["capital"]
slp["U"] = sleep["capital"]
slp["V"] = sleep["capital"]
slp["W"] = sleep["capital"]
slp["X"] = sleep["capital"]
slp["Y"] = sleep["capital"]
slp["Z"] = sleep["capital"]

# 0 - 9
slp["1"] = sleep["number"]
slp["2"] = sleep["number"]
slp["3"] = sleep["number"]
slp["4"] = sleep["number"]
slp["5"] = sleep["number"]
slp["6"] = sleep["number"]
slp["7"] = sleep["number"]
slp["8"] = sleep["number"]
slp["9"] = sleep["number"]
slp["0"] = sleep["number"]

# punctuations
slp[" "] = sleep["letter"]
slp[","] = sleep["special"]
slp[";"] = sleep["special"]
slp[":"] = sleep["special"]
slp["."] = sleep["special"]
slp["?"] = sleep["special"]
slp["!"] = sleep["special"]
slp["\""] =sleep["special"]
slp["“"] = sleep["special"]
slp["”"] = sleep["special"]
slp["‘"] = sleep["special"]
slp["’"] = sleep["special"]
slp["'"] = sleep["special"]
slp["("] = sleep["special"]
slp[")"] = sleep["special"]
slp["/"] = sleep["special"]
#slp["\\"] = 456 16sleep["special"]
slp["–"] = sleep["special"]
slp["–"] = sleep["special"]
slp["—"] = sleep["special"]
slp["-"] = sleep["special"]
slp["@"] = sleep["special"]
slp["*"] = sleep["special"]
slp["#"] = sleep["special"]
slp["["] = sleep["special"]
slp["]"] = sleep["special"]

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