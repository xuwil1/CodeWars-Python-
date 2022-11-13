#Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

#Examples
#replace("Hi!") === "H!!"
#replace("!Hi! Hi!") === "!H!! H!!"
#replace("aeiou") === "!!!!!"
#replace("ABCDE") === "!BCD!"

def replace_exclamation(s):
    for i in "aeuioAEUIO":  s = s.replace(i, "!")
    return s
