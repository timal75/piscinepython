import sys

def get_states():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	return (states)

def get_capital():
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	return (capital_cities)

def traite_input(arg):

	states = get_states()
	capital = get_capital ()
	if (arg in states) and (states[arg] in capital):
	  print(capital[states[arg]], "is the capital of", arg)
	elif arg in capital.values():
		capital = [key for key, value in capital.items() if value == arg]
		state = [key for key, value in states.items() if value == capital[0]][0]
		print(arg, "is the capital of", state)
	else:
		print(arg, "is neither a capital city nor a state")

 
if __name__ == '__main__':

	if len(sys.argv) != 2:
		quit()
	input_str=sys.argv[1]
	for x in input_str.split(","):
		if len(x.strip()) > 0:
			traite_input(x.strip())
	