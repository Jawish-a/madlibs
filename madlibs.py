def main():
	# write your code here
	time = 1
	items = ''
	name = ''
	scream = ''
	action = ''

	print("Mad libs where libs get mad.")
	print("Start Below:")
	print("")
	time = input("Enter a number from 1 to 12: ")
	items = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	scream = input("Enter any sentence: ")
	action = input("Enter a verb: ")
	print("")
	print("The story goes...")
	print("")
	print("It was " + str(time) + " o'clock when I heard a knock at the door.")
	print("I opened the door and there was a box full of " + items + " with a note saying \"From Mr. " + name.capitalize() + ".\"")
	print("Just as I closed the door I heard a scream \"" + scream.upper() + ".\"")
	print("I froze in place and all I could do was " + action + ".")




if __name__ == '__main__':
	main()