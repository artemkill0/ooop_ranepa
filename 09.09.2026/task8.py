class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(mem_slots)[:4]

    def get_config(self):
        mem_info = ", ".join(f"{m.name} {m.volume}GB" for m in self.mem_slots) or "нет"
        return [
            f"Материнская плата: {self.name}",
            f"Процессор: {self.cpu.name} {self.cpu.fr}GHz",
            f"Слотов памяти: {len(self.mem_slots)}",
            f"Память: {mem_info}"
        ]

cpu = CPU("Intel i7", 3.6)
m1 = Memory("DDR4-1", 8)
m2 = Memory("DDR4-2", 16)

mb = MotherBoard("ASUS Z690", cpu, m1, m2)
for line in mb.get_config():
    print(line)