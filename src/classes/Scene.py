from sys import exit
class Scene:
    "All the world's a stage."
    def __init__(self,screen,clock):
        self.modcheck = ["pygame.font"]
        for module in self.modcheck:
            try:
                self.attempt = eval(module)
            except:
                showerror("Module Error",f"\"{module}\" did not install correctly!")
                exit()
            else:
                if not self.attempt:
                    showerror("Module Error",f"\"{module}\" did not install correctly!")
                    exit()