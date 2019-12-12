def min_max():
  
  the_array = [15, 22, 84, 14, 88, 23]  

  the_array.sort() 
  
  the_highest_value = the_array[-1] 
  the_smallest_number = the_array[0]
  difference = (the_highest_value) - (the_smallest_number)
  
  print ("The highest value is " + str(the_highest_value))    
  print ("The smallest value is " + str(the_smallest_number)) 
  print ("The difference is " + str(difference)) 
  
min_max()
