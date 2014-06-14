class Parent(object):

# define function override
	def override(self):
		print "PARENT override()"
		
# define function implicit
	def implicit(self):
		print "PARENT implicit()"

# define function altered
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):

# This is an override, as Child redefines override
	def override(self):
		print "CHILD override()"
		
# The function is an override, but gets attributes from the Parent class through super.
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()