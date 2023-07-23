""" 
기능 : 버튼, 스크롤, 체크박스, 슬라이더, 텍스트박스
테마 : dark, light, red, blue 모드

객체를 abstract_fac_pattern으로 생성한다.
"""

"""
abstract 구성 part
"""
class Button:
    def click(self):
        pass

class CheckBox:
    def check(self):
        pass

class ScrollBar:
    def scroll(self):
        pass

class Slider:
    def slide(self):
        pass

class TextBox:
    def write(self):
        pass


"""
abstract - 구체 Dark part
"""
class DarkButton(Button):
    def click(self):
        print("dark click")

class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")

class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("dark scroll")

class DarkSlider(Slider):
    def slide(self):
        print("dark slide")

class DarkTextBox(TextBox):
    def write(self):
        print("dark write")

"""
abstract - 구체 Light part
"""

class LightButton(Button):
    def click(self):
        print("light click")

class LightCheckBox(CheckBox):
    def check(self):
        print("light check")

class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light scroll")

class LightSlider(Slider):
    def slide(self):
        print("light slide")

class LightTextBox(TextBox):
    def write(self):
        print("light write")


"""
abstract - 구체 Red part
"""

class RedButton(Button):
    def click(self):
        print("red click")

class RedCheckBox(CheckBox):
    def check(self):
        print("red check")

class RedScrollBar(ScrollBar):
    def scroll(self):
        print("red scroll")

class RedSlider(Slider):
    def slide(self):
        print("red slide")

class RedTextBox(TextBox):
    def write(self):
        print("red write")


"""
abstract - 구체 Blue part
"""
class BlueButton(Button):
    def click(self):
        print("blue click")

class BlueCheckBox(CheckBox):
    def check(self):
        print("blue check")

class BlueScrollBar(ScrollBar):
    def scroll(self):
        print("blue scroll")

class BlueSlider(Slider):
    def slide(self):
        print("blue slide")

class BlueTextBox(TextBox):
    def write(self):
        print("blue write")



"""
abstract Factory class
"""
class UIFactory:
    def getButton(self):
        pass
    
    def getCheckBox(self):
        pass

    def getScrollBar(self):
        pass

    def getSlider(self):
        pass

    def getTextBox(self):
        pass


"""
Dark Factory class
"""

class DarkFactory(UIFactory):
    def getButton(self):
        return DarkButton()
    
    def getCheckBox(self):
        return DarkCheckBox()

    def getScrollBar(self):
        return DarkScrollBar()

    def getSlider(self):
        return DarkSlider()

    def getTextBox(self):
        return DarkTextBox()


"""
Light Factory class
"""

class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()
    
    def getCheckBox(self):
        return LightCheckBox()

    def getScrollBar(self):
        return LightScrollBar()

    def getSlider(self):
        return LightSlider()

    def getTextBox(self):
        return LightTextBox()


"""
Red Factory class
"""

class RedFactory(UIFactory):
    def getButton(self):
        return RedButton()
    
    def getCheckBox(self):
        return RedCheckBox()

    def getScrollBar(self):
        return RedScrollBar()

    def getSlider(self):
        return RedSlider()

    def getTextBox(self):
        return RedTextBox()
    


"""
Blue Factory class
"""

class BlueFactory(UIFactory):
    def getButton(self):
        return BlueButton()
    
    def getCheckBox(self):
        return BlueCheckBox()

    def getScrollBar(self):
        return BlueScrollBar()

    def getSlider(self):
        return BlueSlider()

    def getTextBox(self):
        return BlueTextBox()
    

df = DarkFactory()
bt = df.getButton()
cb = df.getCheckBox()
sb = df.getScrollBar()
s = df.getSlider()
t = df.getTextBox()

bt.click()
cb.check()
sb.scroll()
s.slide()
t.write()

print('')

df = RedFactory()
bt = df.getButton()
cb = df.getCheckBox()
sb = df.getScrollBar()
s = df.getSlider()
t = df.getTextBox()

bt.click()
cb.check()
sb.scroll()
s.slide()
t.write()

print('')

df = LightFactory()
bt = df.getButton()
cb = df.getCheckBox()
sb = df.getScrollBar()
s = df.getSlider()
t = df.getTextBox()

bt.click()
cb.check()
sb.scroll()
s.slide()
t.write()

print('')

df = BlueFactory()
bt = df.getButton()
cb = df.getCheckBox()
sb = df.getScrollBar()
s = df.getSlider()
t = df.getTextBox()

bt.click()
cb.check()
sb.scroll()
s.slide()
t.write()