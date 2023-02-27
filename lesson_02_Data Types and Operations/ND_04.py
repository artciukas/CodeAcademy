"""
Create program that allows user to enter text
Convert that text to Leet speak 1337
print outcome

"""
text = input("Please write text: ")

print(f"Original text is: {text}")
code = text.upper().replace("A","4").replace("B","I3").replace("C", "[").replace("D", ")")
code = text.upper().replace("E","3").replace("F","|=").replace("G", "6").replace("H", "#")
code = text.upper().replace("I","1").replace("J",",_|").replace("K", ">|").replace("L", "£")
code = text.upper().replace("M","^^").replace("N","^/").replace("O", "0").replace("P", "|*")
code = text.upper().replace("Q","(_,)").replace("R","I2").replace("S", "5").replace("T", "7")
code = text.upper().replace("U","(_)").replace("V","\/").replace("W", "\/\/").replace("X", "><")
code = text.upper().replace("Y","j").replace("Z","2")
print(code)
print(f"Coded text is: {code}")



	 



