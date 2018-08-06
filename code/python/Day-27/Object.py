class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')
ob = MyClass()
print(MyClass.func)
print(ob.func)
ob.func()
