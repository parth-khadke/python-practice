print("*** Grade Calculator ***")

total=0
score=0
counter=0

while True:
    score=int(input("Enter score (-1 to exit): "))

    if score==-1:
        break

    if score<0 and score>100:
        print("Inavlid marks. Enter marks between 0-100.")
        continue

    total+=score
    counter+=1

if counter==0:
    print("No score entered.")
else:
    average = total / counter
    print("Average:", average)
    
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
