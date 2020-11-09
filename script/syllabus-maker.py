import os

# Apologies for my probably not great python scripting
print("Welcome to the PRAXIS Syllabus Maker.")
print("Here are the available modules.")

default_name = "generated-syllabus.md"
print("\nDefault output syllabus: " + default_name)

with open("../"+default_name, "w") as out:
	basepath = "../modules"
	for module_filename in os.listdir(basepath):
		path = basepath + "/" + module_filename
		with open(path) as module:
			# could be one list comprehension, I guess
			lines = module.readlines()
			for line in lines:
				out.write(line)