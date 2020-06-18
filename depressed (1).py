
def checkPasswd():
  UserWrote = input("Enter the real password: ")
  if userinput == "":
      return True
  else:
      return False

def notcheckpass():
	UserWrote = input("Enter The Passwd: ")
	if UserWrote == "cbrh{1_c4n_n07_r34d_y0u}":
		return True
	else:
		return False

def weirdcheckpasswd():
	UserWrote = input("Enter The Passwd: ")
	if UserWrote == "cbrh{17_15_1n_7h3_c0d3_5p34k_d0wn}":
		return True
	else:
		return False

def checkingpassword():
	UserWrote = input("Enter The Passwd: ")
	if UserWrote == "cbrh{17_15_1n_7h3_c0d3}":
		return True
	else:
		return False

def bcheckpass():
  UserWrote = input("Enter the password: ")
  if UserWrote == "cbrh{0h_5h17_y0u_f0und_17}":
      return True
  else:
      return False

def Wrongcheckingpassword():
	auth = input("please enter your password...: ")
	if UserWrote == "cbrh{17_15_1n_7h3_c0d3}":
		return True
	else:
		return False

def main():
	auth = checkingpassword()
	if UserWrote == True:
		print("Bro/Sis, The flag is the password...")
		print("")
		exit()
	else:
		print("Wrong password... stupid nerd/geek")
		print("just stop thinking")
		WrongMain()

def WrongMain():
	auth = Wrongcheckingpassword()
	if auth == True:
		print("Wow You're a G.E.N.U.I.S")
		print("THE FLAG IS THE PASSWD BTW")
		exit()
	else:
		print("You didn't get it {again}")
		WrongMain()


auth == False
main()