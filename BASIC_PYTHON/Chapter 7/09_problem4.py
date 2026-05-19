# WAF to find in which line of the file does the word "learning"occur first.
# Print -1 if word not found.
def find_word():
    with open("practice.txt","r") as f:
        line1=f.readline()
        line2=f.readline()
        line3=f.readline()
        if(line1.find("learning") != -1):
            print("Word found in line 1")
        elif(line2.find("learning") != -1):
            print("Word found in line 2")
        elif(line3.find("learning") != -1):
            print("Word found in line 3")
        else:
            print("Not found !")
find_word()