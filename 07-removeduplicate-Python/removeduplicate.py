# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	f=set(text)
	g=list(f)
	w=""
	for i in range(len(text)):
		if(text[i] in g):
			w+=text[i]
			g.pop(g.index(text[i]))
	return(w)
