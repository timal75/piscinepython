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
	inputcapital = sys.argv[1]
	if inputcapital in capital.values():
		capital = [key for key, value in capital.items() if value == inputcapital]
		state = [key for key, value in states.items() if value == capital[0]][0]
		print(state)
	else:
		print('Unknown capital city')