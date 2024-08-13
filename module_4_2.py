def test_function ():
	def inner_function ():
		print ("Я в области видимости функции test_function")
	inner_function()
	
test_function()
#inner_function() - получаем ошибку, т.к. функция inner_function определена только внутри функции test_function и находится в ее области видимости