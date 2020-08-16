def main():
	# write your code here
	number = 1
	plural_noun = ''
	name = ''
	sentence = ''
	verb = ''

	print("Mad libs where libs get mad.")
	print("Start Below:")
	print("")
	number = input("Enter a number from 1 to 12: ")
	plural_noun = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	sentence = input("Enter any sentence: ")
	verb = input("Enter a verb: ")
	print("")
	print("The story goes")
	print("")
	print("It was " + str(number) + " O'clock when I heard a knock on the door.")
	print("I opened the door and there was a box full of " + plural_noun + " with a note saying \"From Mr. " + name + ".\"")
	print("Just as I closed the door I heard a scream \"" + sentence.upper() + ".\"")
	print("I froze in place and all I could do was " + verb + ".")




if __name__ == '__main__':
	main()