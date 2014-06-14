from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
x = "So %s," (user_name), raw_input(your first variable is:")
y = raw_input("Your second variable is: ")
z = raw_input("Your third variable is: ")

print """
Alrighty then, so your first variable is %r.
You said the second variable was %r,
then the last variable was %r. Cool beans."
""" % (x, y, z)