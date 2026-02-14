class StringHandler:
    def getString(self):
        self.text = input()
    
    def printString(self):
        print(self.text.upper())

# Создаем объект класса
handler = StringHandler()

# Вызываем методы
handler.getString()
handler.printString()