def bottles_of_beer(num_of_bottles):
    while num_of_bottles > 1:
        print "There are " + str(num_of_bottles) + " bottles of beer on the wall"
        print str(num_of_bottles) + " bottles of beer"
        print "You take one down pass it around"
        num_of_bottles -= 1
        if num_of_bottles == 1:
            print "There is " + str(num_of_bottles) + " bottle of beer on the wall"
            print str(num_of_bottles) + " bottle of beer"
            print "You take one down, you pass it around"
            print "There are no bottles of beer on the wall"
print bottles_of_beer(100)
