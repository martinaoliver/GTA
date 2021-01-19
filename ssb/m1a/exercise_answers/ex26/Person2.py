class Person: 
	#Represents a person
	population = 0 
	def __init__(self, name): 
		#Initializes the person's data
		self.name = name 
		print  ('Initializing %s' % self.name)
		# Add them to the population 
		Person.population += 1 
	
	def sayHi(self): 
		#Greeting by the person
		print ('Hi, my name is %s.' % self.name)

	def howMany(self): 
		# Prints the current population.
		print ('We have a population of %d here.' % Person.population)


stan  = Person("Stan")
stan.sayHi() 
stan.howMany() 

brian = Person("Brian")
brian.sayHi() 
brian.howMany() 

