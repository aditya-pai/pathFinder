import sys

def main():

	choice=input("Enter \n1 for Initial Algorithm on Initial Grid\n2 for Initial Algorithm on New Grid\n3 for New Algorithm on New Grid\n\n")
	choice=int(choice)
	if choice==1:
		import bfs
	elif choice==2:
		import algo1_failcase
	elif choice==3:
		import aStar
	else:
		print("Invalid Input")


if __name__ == "__main__": main()

