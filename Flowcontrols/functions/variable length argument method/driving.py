class Pycharm:
    def compile(self):
        print("compileusing pycharm")
    def execute(self):
        print("execute")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("compile using vscode")
    def execute(self):
        print("vscode execute")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p=Programmer()
pvc=Vscode()
p.coding(pvc)