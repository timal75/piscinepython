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
	
if __name__ == '__main__':

	if len(sys.argv) != 2:
		quit()
	states = get_states()
	capital = get_capital ()
	inputstate = sys.argv[1]
	if (inputstate in states) and (states[inputstate] in capital):
	  print(capital[states[inputstate]])
	else:
	  print('Unknown state')