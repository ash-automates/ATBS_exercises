import pyinputplus as pyip

prompt = "Want to know how to keep an idiot busy all day?\n"
while True:
    res = pyip.inputYesNo(prompt)
    if res == "no":
        print("Ok, have a nice day!")
        break
