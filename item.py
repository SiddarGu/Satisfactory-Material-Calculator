from typing import Callable

class Iron_ore:
    def __init__(self, count):
        self.count = count
        self.name = 'iron ore'
        self.isRaw = True

class Bauxite:
    def __init__(self, count):
        self.count = count
        self.name = 'bauxite'
        self.isRaw = True

class Caterium_ore:
    def __init__(self, count):
        self.count = count
        self.name = 'caterium ore'
        self.isRaw = True

class Coal:
    def __init__(self, count):
        self.count = count
        self.name = 'coal'
        self.isRaw = True

class Copper_ore:
    def __init__(self, count):
        self.count = count
        self.name = 'copper ore'
        self.isRaw = True

class Crude_oil:
    def __init__(self, count):
        self.count = count
        self.name = 'crude oil'
        self.isRaw = True

class Packaged_oil:
    def __init__(self, count) -> None:
        self.name = 'packaged oil'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Crude_oil(self.count), Empty_canister(self.count)]]
    def getByproduct(self):
        return [None]

class Limestone:
    def __init__(self, count):
        self.count = count
        self.name = 'limestone'
        self.isRaw = True

class Raw_quartz:
    def __init__(self, count):
        self.count = count
        self.name = 'raw quartz'
        self.isRaw = True

class SAM_ore:
    def __init__(self, count):
        self.count = count
        self.name = 'S.A.M. ore'
        self.isRaw = True

class Sulfur:
    def __init__(self, count):
        self.count = count
        self.name = 'sulfur'
        self.isRaw = True

class Uranium:
    def __init__(self, count):
        self.count = count
        self.name = 'uranium'
        self.isRaw = True

class Water:
    def __init__(self, count):
        self.count = count
        self.name = 'water'
        self.isRaw = True

class Packaged_water:
    def __init__(self, count) -> None:
        self.name = 'packaged water'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Water(self.count), Empty_canister(self.count)]]
    def getByproduct(self):
        return [None]

class Allen_carapace:
    def __init__(self, count):
        self.count = count
        self.name = 'allen carapace'
        self.isRaw = True

class Allen_organs:
    def __init__(self, count):
        self.count = count
        self.name = 'allen organs'
        self.isRaw = True

class Flower_petals:
    def __init__(self, count):
        self.count = count
        self.name = 'flower petals'
        self.isRaw = True

class Leaves:
    def __init__(self, count):
        self.count = count
        self.name = 'leaves'
        self.isRaw = True

class Mycelia:
    def __init__(self, count):
        self.count = count
        self.name = 'mycelia'
        self.isRaw = True

class Green_power_slug:
    def __init__(self, count):
        self.count = count
        self.name = 'green power slug'
        self.isRaw = True

class Yellow_power_slug:
    def __init__(self, count):
        self.count = count
        self.name = 'yellow power slug'
        self.isRaw = True

class Purple_power_slug:
    def __init__(self, count):
        self.count = count
        self.name = 'purple power slug'
        self.isRaw = True

class Wood:
    def __init__(self, count):
        self.count = count
        self.name = 'wood'
        self.isRaw = True

class Bacon_agaric:
    def __init__(self, count):
        self.count = count
        self.name = 'bacon agaric'
        self.isRaw = True

class Beryl_nut:
    def __init__(self, count):
        self.count = count
        self.name = 'beryl nut'
        self.isRaw = True

class Paleberry:
    def __init__(self, count):
        self.count = count
        self.name = 'paleberry'
        self.isRaw = True

class Medical_inhaler:
    def __init__(self, count):
        self.count = count
        self.name = 'medical inhaler'
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Bacon_agaric(self.count),
         Paleberry(self.count * 3), Beryl_nut(self.count * 7)]
        recipe2 = [Allen_organs(self.count * 3), Mycelia(self.count * 5)]
        recipe3 = [Bacon_agaric(self.count), Paleberry(self.count * 2),
         Beryl_nut(self.count * 3), Mycelia(self.count * 5)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Biomass:
    def __init__(self, count):
        self.name = 'biomass'
        self.count = count        
        self.isRaw = False
    def getIngredient(self):
        leaves = [Leaves(self.count * 2)]
        woods = [Wood(self.count / 5)]
        mycelias = [Mycelia(self.count)]
        carapaces = [Allen_carapace(self.count / 100)]
        organs = [Allen_organs(self.count / 200)]
        return [leaves, woods, mycelias, carapaces, organs]
    def getByproduct(self):
        return [None, None, None, None, None]
      
class Cable:
    def __init__(self, count):
        self.name = 'cable'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Wire(self.count * 2)]
        recipe2 = [Wire(self.count / 9 * 5), Heavy_oil_residue(self.count / 9 * 2)]
        recipe3 = [Wire(self.count / 20 * 9), Rubber(self.count / 20 * 6)]
        recipe4 = [Quickwire(self.count / 11 * 3), Rubber(self.count / 11 * 2)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [None, None, None, None]

class Concrete:
    def __init__(self, count):
        self.name = 'concrete'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Limestone(self.count * 3)]
        recipe2 = [Limestone(self.count / 9 * 10), Rubber(self.count / 9 * 2)]
        recipe3 = [Limestone(self.count / 4 * 6), Water(self.count / 4 * 5)]
        recipe4 = [Limestone(self.count / 10 * 12), Silica(self.count / 10 * 3)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [None, None, None, None]

class Copper_ingot:
    def __init__(self, count):
        self.name = 'copper ingot'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Copper_ore(self.count)]
        recipe2 = [Copper_ore(self.count / 2), Iron_ore(self.count / 4)]
        recipe3 = [Copper_ore(self.count / 5 * 2), Water(self.count / 15 * 4)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Iron_ingot:
    def __init__(self, count) -> None:
        self.name = 'iron ingot'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_ore(self.count)]
        recipe2 = [Iron_ore(self.count / 13 * 7), Water(self.count / 13 * 4)]
        recipe3 = [Iron_ore(self.count / 5 * 2), Copper_ore(self.count / 5 * 2)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Iron_plate:
    def __init__(self, count) -> None:
        self.name = 'iron plate'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_ingot(self.count * 1.5)]
        recipe2 = [Iron_ingot(self.count / 3 * 2), Plastic(self.count / 15 * 2)]
        recipe3 = [Steel_ingot(self.count / 6), Plastic(self.count / 9)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Iron_rod:
    def __init__(self, count) -> None:
        self.name = 'iron rod'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_ingot(self.count)]
        recipe2 = [Steel_ingot(self.count / 4)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Reinforced_iron_plate:
    def __init__(self, count) -> None:
        self.name = 'reinforced iron plate'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_plate(self.count * 6), Screw(self.count * 12)]
        recipe2 = [Iron_plate(self.count * 3), Rubber(self.count)]
        recipe3 = [Iron_plate(self.count * 6), Screw(self.count / 3 * 50)]
        recipe4 = [Iron_plate(self.count / 3 * 10), Wire(self.count / 3 * 20)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [None, None, None, None]

class Screw:
    def __init__(self, count) -> None:
        self.name = 'screw'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_rod(self.count / 4)]
        recipe2 = [Iron_ingot(self.count / 4)]
        recipe3 = [Steel_beam(self.count / 52)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Wire:
    def __init__(self, count) -> None:
        self.name = 'wire'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Copper_ingot(self.count / 2)]
        recipe2 = [Copper_ingot(self.count / 30 * 4), Caterium_ingot(self.count / 30)]
        recipe3 = [Iron_ingot(self.count / 9 * 5)]
        recipe4 = [Caterium_ingot(self.count / 8)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [None, None, None, None]

class Copper_sheet:
    def __init__(self, count) -> None:
        self.name = 'copper sheet'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Copper_ingot(self.count * 2)]
        recipe2 = [Copper_ingot(self.count), Water(self.count)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Solid_biofuel:
    def __init__(self, count) -> None:
        self.name = 'solid biofuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Biomass(self.count * 2)]]
    def getByproduct(self):
        return [None]

class Modular_frame:
    def __init__(self, count) -> None:
        self.name = 'modular frame'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Reinforced_iron_plate(self.count / 5 * 8), Iron_rod(self.count * 6)]
        recipe2 = [Reinforced_iron_plate(self.count * 1.5), Screw(self.count * 28)]
        recipe3 = [Reinforced_iron_plate(self.count / 3 * 2), Steel_pipe(self.count / 3 * 10)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Rotor:
    def __init__(self, count) -> None:
        self.name = 'rotor'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_rod(self.count * 5), Screw(self.count * 25)]
        recipe2 = [Copper_sheet(self.count * 2), Screw(self.count / 3 * 52)]
        recipe3 = [Steel_pipe(self.count * 2), Wire(self.count * 6)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Smart_plating:
    def __init__(self, count) -> None:
        self.name = 'smart plating'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Reinforced_iron_plate(self.count), Rotor(self.count)]
        recipe2 = [Reinforced_iron_plate(self.count / 2), 
         Rotor(self.count / 2), Plastic(self.count / 2 * 3)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Steel_beam:
    def __init__(self, count) -> None:
        self.name = 'steel beam'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Steel_ingot(self.count * 4)]]
    def getByproduct(self):
        return [None]

class Steel_ingot:
    def __init__(self, count) -> None:
        self.name = 'steel ingot'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_ore(self.count), Coal(self.count)]
        recipe2 = [Iron_ore(self.count / 4 * 3), Petroleum_coke(self.count / 4 * 3)]
        recipe3 = [Iron_ore(self.count * 0.6), Compacted_coal(self.count * 0.3)]
        recipe4 = [Iron_ingot(self.count / 3 * 2), Coal(self.count / 3 * 2)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [None, None, None, None]

class Steel_pipe:
    def __init__(self, count) -> None:
        self.name = 'steel pipe'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Steel_ingot(self.count * 1.5)]]
    def getByproduct(self):
        return [None]

class Versatile_framework:
    def __init__(self, count) -> None:
        self.name = 'versatile framework'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Modular_frame(self.count / 2), Steel_beam(self.count * 6)]
        recipe2 = [Modular_frame(self.count / 2),
         Steel_beam(self.count * 3), Rubber(self.count * 4)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Automated_wiring:
    def __init__(self, count) -> None:
        self.name = 'automated wiring'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Stator(self.count), Cable(self.count * 20)]
        recipe2 = [Stator(self.count / 2),
         Wire(self.count * 10), Highspeed_connector(self.count / 4)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Encased_industrial_beam:
    def __init__(self, count) -> None:
        self.name = 'encased industrial beam'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Steel_beam(self.count * 4), Concrete(self.count * 5)]
        recipe2 = [Steel_pipe(self.count * 7), Concrete(self.count * 5)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Heavy_modular_frame:
    def __init__(self, count) -> None:
        self.name = 'heavy modular frame'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Modular_frame(self.count * 5), Steel_pipe(self.count * 15),
         Encased_industrial_beam(self.count * 5), Screw(self.count * 100)]
        recipe2 = [Modular_frame(self.count * 5), Encased_industrial_beam(self.count * 3),
         Rubber(self.count * 20), Screw(self.count * 104)]
        recipe3 = [Modular_frame(self.count / 3 * 8), Encased_industrial_beam(self.count / 3 * 10),
         Steel_pipe(self.count * 12), Concrete(self.count / 3 * 22)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Motor:
    def __init__(self, count) -> None:
        self.name = 'motor'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Rotor(self.count * 2), Stator(self.count * 2)]
        recipe2 = [Rotor(self.count / 2), Stator(self.count / 2),
         Crystal_oscillator(self.count / 6)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Stator:
    def __init__(self, count) -> None:
        self.name = 'stator'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Steel_pipe(self.count * 3), Wire(self.count * 8)]
        recipe2 = [Steel_pipe(self.count * 2), Quickwire(self.count / 2 * 15)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Adaptive_control_unit:
    def __init__(self, count) -> None:
        self.name = 'adaptive control unit'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Automated_wiring(self.count * 7.5), Circuit_board(self.count * 5),
         Heavy_modular_frame(self.count), Computer(self.count)]]
    def getByproduct(self):
        return [None]

class Circuit_board:
    def __init__(self, count) -> None:
        self.name = 'circuit board'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Plastic(self.count * 4), Copper_sheet(self.count * 2)]
        recipe2 = [Rubber(self.count * 6), Petroleum_coke(self.count * 9)]
        recipe3 = [Copper_sheet(self.count / 5 * 11), Silica(self.count / 5 * 11)]
        recipe4 = [Plastic(self.count / 7 * 10), Quickwire(self.count / 7 * 30)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [None, None, None, None]

class Computer:
    def __init__(self, count) -> None:
        self.name = 'computer'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Circuit_board(self.count * 10), Cable(self.count * 9),
         Plastic(self.count * 18), Screw(self.count * 52)]
        recipe2 = [Circuit_board(self.count / 3 * 8), Crystal_oscillator(self.count)]
        recipe3 = [Circuit_board(self.count * 7),
         Quickwire(self.count * 28), Rubber(self.count * 12)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Empty_canister:
    def __init__(self, count) -> None:
        self.name = 'empty canister'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Plastic(self.count / 2)]
        recipe2 = [Steel_ingot(self.count / 2 * 3)]
        recipe3 = [Iron_plate(self.count / 2), Copper_sheet(self.count / 4)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [None, None, None]

class Fuel:
    def __init__(self, count) -> None:
        self.name = 'fuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Crude_oil(self.count * 1.5)]
        recipe2 = [Heavy_oil_residue(self.count * 1.5)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [[Polymer_resin(self.count / 4 * 3)], None]

class Packaged_fuel:
    def __init__(self, count) -> None:
        self.name = 'packaged fuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Fuel(self.count), Empty_canister(self.count)]
        recipe2 = [Heavy_oil_residue(self.count / 2), Packaged_water(self.count)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Heavy_oil_residue:
    def __init__(self, count) -> None:
        self.name = 'heavy oil residue'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Crude_oil(self.count * 1.5)]
        recipe2 = [Crude_oil(self.count * 3)]
        recipe3 = [Crude_oil(self.count / 4 * 3)]
        recipe4 = [Crude_oil(self.count * 3)]
        return [recipe1, recipe2, recipe3, recipe4]
    def getByproduct(self):
        return [[Rubber(self.count)], [Plastic(self.count * 2)],
         [Polymer_resin(self.count / 2)], [Polymer_resin(self.count / 2 * 13)]]

class Packaged_heavy_oil_residue:
    def __init__(self, count) -> None:
        self.name = 'packaged oil residue'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Heavy_oil_residue(self.count), Empty_canister(self.count)]]
    def getByproduct(self):
        return [None]

class Liquid_biofuel:
    def __init__(self, count) -> None:
        self.name = 'liquid biofuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Solid_biofuel(self.count * 1.5), Water(self.count * 0.75)]]
    def getByproduct(self):
        return [None]

class Packaged_liquid_biofuel:
    def __init__(self, count) -> None:
        self.name = 'packaged liquid biofuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Liquid_biofuel(self.count), Empty_canister(self.count)]]
    def getByproduct(self):
        return [None]

class Modular_engine:
    def __init__(self, count) -> None:
        self.name = 'modular engine'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Motor(self.count * 2),
         Rubber(self.count * 15), Smart_plating(self.count * 2)]]
    def getByproduct(self):
        return [None]

class Petroleum_coke:
    def __init__(self, count) -> None:
        self.name = 'petroleum coke'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Heavy_oil_residue(self.count / 3)]]
    def getByproduct(self):
        return [None]

class Plastic:
    def __init__(self, count) -> None:
        self.name = 'plastic'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Crude_oil(self.count * 1.5)]
        recipe2 = [Polymer_resin(self.count * 3), Water(self.count)]
        recipe3 = [Rubber(self.count / 2), Fuel(self.count / 2)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [[Heavy_oil_residue(self.count / 2)], None, None]

class Polymer_resin:
    def __init__(self, count) -> None:
        self.name = 'polymer resin'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Crude_oil(self.count * 2)]
        recipe2 = [Crude_oil(self.count * 1.5)]
        recipe3 = [Crude_oil(self.count / 13 * 6)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [[Fuel(self.count * 4 / 3)],
         [Heavy_oil_residue(self.count * 2)], [Heavy_oil_residue(self.count / 13 * 2)]]

class Rubber:
    def __init__(self, count) -> None:
        self.name = 'rubber'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Crude_oil(self.count * 1.5)]
        recipe2 = [Polymer_resin(self.count * 2), Water(self.count * 2)]
        recipe3 = [Plastic(self.count / 2), Fuel(self.count / 2)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [[Heavy_oil_residue(self.count)], None, None]

class Alumina_solution:
    def __init__(self, count) -> None:
        self.name = 'alumina solution'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Bauxite(self.count * 7 / 8), Water(self.count * 1.25)]]
    def getByproduct(self):
        return [[Silica(self.count / 4)]]

class Alclad_aluminum_sheet:
    def __init__(self, count) -> None:
        self.name = 'alclad aluminum sheet'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Aluminum_ingot(self.count * 2), Copper_ingot(self.count * 0.75)]]
    def getByproduct(self):
        return [None]

class Aluminum_ingot:
    def __init__(self, count) -> None:
        self.name = 'aluminum ingot'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [[Aluminum_scrap(self.count * 3), Silica(self.count * 7 / 4)]]
        recipe2 = [Aluminum_scrap(self.count * 4)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Aluminum_scrap:
    def __init__(self, count) -> None:
        self.name = 'aluminum scrap'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Alumina_solution(self.count * 2 / 3), Petroleum_coke(self.count / 6)]
        recipe2 = [Alumina_solution(self.count / 5 * 3), Coal(self.count / 5)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [[Water(self.count / 6)], [Water(self.count / 5)]]

class Battery:
    def __init__(self, count) -> None:
        self.name = 'battery'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Alclad_aluminum_sheet(self.count * 8 / 3), Wire(self.count * 16 / 3), 
         Sulfur(self.count * 20 / 3), Plastic(self.count * 8 / 3)]]
    def getByproduct(self):
        return [None]

class Electromagnetic_control_rod:
    def __init__(self, count) -> None:
        self.name = 'electromagnetic control rod'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Stator(self.count * 1.5), AI_limiter(self.count)]
        recipe2 = [Stator(self.count), Highspeed_connector(self.count / 2)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Encased_uranium_cell:
    def __init__(self, count) -> None:
        self.name = 'encased uranium cell'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Uranium_pellet(self.count * 4), Concrete(self.count * 9 / 10)]
        recipe2 = [Uranium_pellet(self.count / 35 * 40), Sulfur(self.count / 35 * 45),
         Silica(self.count / 35 * 45), Quickwire(self.count / 35 * 75)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Heat_sink:
    def __init__(self, count) -> None:
        self.name = 'heat sink'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Alclad_aluminum_sheet(self.count * 4), Rubber(self.count * 7)]
        recipe2 = [Alclad_aluminum_sheet(self.count / 7 * 20), Copper_sheet(self.count / 7 * 30)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Beacon:
    def __init__(self, count) -> None:
        self.name = 'beacon'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Iron_plate(self.count * 3), Iron_rod(self.count),
         Wire(self.count * 15), Cable(self.count * 2)]
        recipe2 = [Steel_beam(self.count / 5),
         Steel_pipe(self.count / 5 * 4), Crystal_oscillator(self.count / 20)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Nuclear_fuel_rod:
    def __init__(self, count) -> None:
        self.name = 'nuclear fuel rod'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [[Encased_uranium_cell(self.count * 25),
         Encased_industrial_beam(self.count * 3), Electromagnetic_control_rod(self.count * 5)]]
        recipe2 = [Encased_uranium_cell(self.count / 3 * 50), Electromagnetic_control_rod(self.count / 3 * 10),
         Crystal_oscillator(self.count), Beacon(self.count * 2)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Nuclear_waste:
    def __init__(self, count) -> None:
        self.name = 'nuclear waste'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Nuclear_fuel_rod(self.count / 25)]]
    def getByproduct(self):
        return [None]

class Sulfuric_acid:
    def __init__(self, count) -> None:
        self.name = 'sulfuric acid'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [[Sulfur(self.count / 2), Water(self.count / 2)]]
        recipe2 = [Uranium(self.count * 2.5), Sulfuric_acid(self.count * 4)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, [Uranium_pellet(self.count * 2.5)]]

class Turbo_motor:
    def __init__(self, count) -> None:
        self.name = 'turbo motor'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Heat_sink(self.count * 4), Radio_control_unit(self.count * 2),
         Motor(self.count * 4), Rubber(self.count * 24)]
        recipe2 = [Motor(self.count / 3 * 7), Radio_control_unit(self.count / 3),
         AI_limiter(self.count * 3), Stator(self.count / 3 * 7)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Uranium_pellet:
    def __init__(self, count) -> None:
        self.name = 'uranium pellet'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Uranium(self.count), Sulfuric_acid(self.count * 8 / 5)]]
    def getByproduct(self):
        return [[Sulfuric_acid(self.count * 2 / 5)]]

class AI_limiter:
    def __init__(self, count) -> None:
        self.name = 'A.I. limiter'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Copper_sheet(self.count * 5), Quickwire(self.count * 20)]]
    def getByproduct(self):
        return [None]

class Black_powder:
    def __init__(self, count) -> None:
        self.name = 'black powder'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Coal(self.count), Sulfur(self.count * 2)]
        recipe2 = [Sulfur(self.count / 2), Compacted_coal(self.count / 4)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Caterium_ingot:
    def __init__(self, count) -> None:
        self.name = 'caterium ingot'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Caterium_ore(self.count * 3)]
        recipe2 = [Caterium_ore(self.count * 2), Water(self.count * 2)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Compacted_coal:
    def __init__(self, count) -> None:
        self.name = 'compacted coal'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Coal(self.count), Sulfur(self.count)]]
    def getByproduct(self):
        return [None]

class Fabric:
    def __init__(self, count) -> None:
        self.name = 'fabric'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Mycelia(self.count), Biomass(self.count * 5)]
        recipe2 = [Polymer_resin(self.count * 16), Water(self.count * 10)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Highspeed_connector:
    def __init__(self, count) -> None:
        self.name = 'high-speed connector'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Quickwire(self.count * 56),
         Cable(self.count * 10), Circuit_board(self.count)]
        recipe2 = [Quickwire(self.count * 30),
         Silica(self.count / 2 * 25), Circuit_board(self.count)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Quickwire:
    def __init__(self, count) -> None:
        self.name = 'quickwire'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Caterium_ingot(self.count / 5)]
        recipe2 = [Caterium_ingot(self.count / 12), Copper_ingot(self.count / 12 * 5)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Power_shard:
    def __init__(self, count) -> None:
        self.name = 'power shard'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Green_power_slug(self.count)],
         [Yellow_power_slug(self.count / 2)], [Purple_power_slug(self.count / 5)]]
    def getByproduct(self):
        return [None, None, None]

class Quartz_crystal:
    def __init__(self, count) -> None:
        self.name = 'quartz crystal'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Raw_quartz(self.count * 5 / 3)]
        recipe2 = [Raw_quartz(self.count / 7 * 9), Water(self.count / 7 * 5)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Silica:
    def __init__(self, count) -> None:
        self.name = 'silica'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Bauxite(self.count * 3.5), Water(self.count * 5)]
        recipe2 = [Raw_quartz(self.count * 3 / 5)]
        recipe3 = [Raw_quartz(self.count / 7 * 3), Limestone(self.count / 7 * 5)]
        return [recipe1, recipe2, recipe3]
    def getByproduct(self):
        return [Alumina_solution(self.count * 4) , None, None]

class Crystal_oscillator:
    def __init__(self, count) -> None:
        self.name = 'crystal oscillator'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Quartz_crystal(self.count * 18),
         Cable(self.count * 14), Reinforced_iron_plate(self.count * 2.5)]
        recipe2 = [Quartz_crystal(self.count * 10),
         Rubber(self.count * 7), AI_limiter(self.count)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Radio_control_unit:
    def __init__(self, count) -> None:
        self.name = 'radio control unit'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Heat_sink(self.count * 4), Rubber(self.count * 16),
         Crystal_oscillator(self.count), Computer(self.count)]
        recipe2 = [Heat_sink(self.count / 3 * 10),
         Supercomputer(self.count / 3), Quartz_crystal(self.count * 10)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Supercomputer:
    def __init__(self, count) -> None:
        self.name = 'supercomputer'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Computer(self.count * 2), AI_limiter(self.count * 2),
         Highspeed_connector(self.count * 3), Plastic(self.count * 28)]]
    def getByproduct(self):
        return [None]

class Turbofuel:
    def __init__(self, count) -> None:
        self.name = 'turbofuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        recipe1 = [Fuel(self.count / 5 * 6), Compacted_coal(self.count / 5 * 4)]
        recipe2 = [Heavy_oil_residue(self.count / 4 * 5), Compacted_coal(self.count)]
        return [recipe1, recipe2]
    def getByproduct(self):
        return [None, None]

class Packaged_turbofuel:
    def __init__(self, count) -> None:
        self.name = 'packaged turbofuel'
        self.count = count
        self.isRaw = False
    def getIngredient(self):
        return [[Empty_canister(self.count), Turbofuel(self.count)]]
    def getByproduct(self):
        return [None]

def getItem(name, count):
    n = int(count)

    if name == 'iron ore':
        return Iron_ore(n)
    elif name == 'bauxite':
        return Bauxite(n)
    elif name == 'caterium ore':
        return Caterium_ore(n)
    elif name == 'coal':
        return Coal(n)
    elif name == 'copper ore':
        return Copper_ore(n)
    elif name == 'crude oil':
        return Crude_oil(n)
    elif name == 'packaged oil':
        return Packaged_oil(n)
    elif name == 'limestone':
        return Limestone(n)
    elif name == 'raw quartz':
        return Raw_quartz(n)
    elif name == 'S.A.M. ore':
        return SAM_ore(n)
    elif name == 'sulfur':
        return Sulfur(n)
    elif name == 'uranium':
        return Uranium(n)
    elif name == 'water':
        return Water(n)
    elif name == 'packaged water':
        return Packaged_water(n)
    elif name == 'allen carapace':
        return Allen_carapace(n)
    elif name == 'allen organs':
        return Allen_organs(n)
    elif name == 'flower petals':
        return Flower_petals(n)
    elif name == 'leaves':
        return Leaves(n)
    elif name == 'mycelia':
        return Mycelia(n)
    elif name == 'green power slug':
        return Green_power_slug(n)
    elif name == 'yellow power slug':
        return Yellow_power_slug(n)
    elif name == 'purple power slug':
        return Purple_power_slug(n)
    elif name == 'wood':
        return Wood(n)
    elif name == 'bacon agaric':
        return Bacon_agaric(n)
    elif name == 'beryl nut':
        return Beryl_nut(n)
    elif name == 'paleberry':
        return Paleberry(n)
    elif name == 'medical inhaler':
        return Medical_inhaler(n)
    elif name == 'biomass':
        return Biomass(n)
    elif name == 'cable':
        return Cable(n)
    elif name == 'concrete':
        return Concrete(n)
    elif name == 'copper ingot':
        return Copper_ingot(n)
    elif name == 'iron ingot':
        return Iron_ingot(n)
    elif name == 'iron plate':
        return Iron_plate(n)
    elif name == 'iron rod':
        return Iron_rod(n)
    elif name == 'reinforced iron plate':
        return Reinforced_iron_plate(n)
    elif name == 'screw':
        return Screw(n)
    elif name == 'wire':
        return Wire(n)
    elif name == 'copper sheet':
        return Copper_sheet(n)
    elif name == 'solid biofuel':
        return Solid_biofuel(n)
    elif name == 'modular frame':
        return Modular_frame(n)
    elif name == 'rotor':
        return Rotor(n)
    elif name == 'smart plating':
        return Smart_plating(n)
    elif name == 'steel beam':
        return Steel_beam(n)
    elif name == 'steel ingot':
        return Steel_ingot(n)
    elif name == 'steel pipe':
        return Steel_pipe(n)
    elif name == 'versatile framework':
        return Versatile_framework(n)
    elif name == 'automated wiring':
        return Automated_wiring(n)
    elif name == 'encased industrial beam':
        return Encased_industrial_beam(n)
    elif name == 'heavy modular frame':
        return Heavy_modular_frame(n)
    elif name == 'motor':
        return Motor(n)
    elif name == 'stator':
        return Stator(n)
    elif name == 'adaptive control unit':
        return Adaptive_control_unit(n)
    elif name == 'circuit board':
        return Circuit_board(n)
    elif name == 'computer':
        return Computer(n)
    elif name == 'empty canister':
        return Empty_canister(n)
    elif name == 'fuel':
        return Fuel(n)
    elif name == 'packaged fuel':
        return Packaged_fuel(n)
    elif name == 'heavy oil residue':
        return Heavy_oil_residue(n)
    elif name == 'packaged oil residue':
        return Packaged_heavy_oil_residue(n)
    elif name == 'liquid biofuel':
        return Liquid_biofuel(n)
    elif name == 'packaged liquid biofuel':
        return Packaged_liquid_biofuel(n)
    elif name == 'modular engine':
        return Modular_engine(n)
    elif name == 'petroleum coke':
        return Petroleum_coke(n)
    elif name == 'plastic':
        return Plastic(n)
    elif name == 'polymer resin':
        return Polymer_resin(n)
    elif name == 'rubber':
        return Rubber(n)
    elif name == 'alumina solution':
        return Alumina_solution(n)
    elif name == 'alclad aluminum sheet':
        return Alclad_aluminum_sheet(n)
    elif name == 'aluminum ingot':
        return Aluminum_ingot(n)
    elif name == 'aluminum scrap':
        return Aluminum_scrap(n)
    elif name == 'battery':
        return Battery(n)
    elif name == 'electromagnetic control rod':
        return Electromagnetic_control_rod(n)
    elif name == 'encased uranium cell':
        return Encased_uranium_cell(n)
    elif name == 'heat sink':
        return Heat_sink(n)
    elif name == 'beacon':
        return Beacon(n)
    elif name == 'nuclear fuel rod':
        return Nuclear_fuel_rod(n)
    elif name == 'nuclear waste':
        return Nuclear_waste(n)
    elif name == 'sulfuric acid':
        return Sulfuric_acid(n)
    elif name == 'turbo motor':
        return Turbo_motor(n)
    elif name == 'uranium pellet':
        return Uranium_pellet(n)
    elif name == 'A.I. limiter':
        return AI_limiter(n)
    elif name == 'black powder':
        return Black_powder(n)
    elif name == 'caterium ingot':
        return Caterium_ingot(n)
    elif name == 'compacted coal':
        return Compacted_coal(n)
    elif name == 'fabric':
        return Fabric(n)
    elif name == 'high-speed connector':
        return Highspeed_connector(n)
    elif name == 'quickwire':
        return Quickwire(n)
    elif name == 'power shard':
        return Power_shard(n)
    elif name == 'quartz crystal':
        return Quartz_crystal(n)
    elif name == 'silica':
        return Silica(n)
    elif name == 'crystal oscillator':
        return Crystal_oscillator(n)
    elif name == 'radio control unit':
        return Radio_control_unit(n)
    elif name == 'supercomputer':
        return Supercomputer(n)
    elif name == 'turbofuel':
        return Turbofuel(n)
    elif name == 'packaged turbofuel':
        return Packaged_turbofuel(n)
    else:
        return None

def getItemList():
    result = ['                           ']
    result.append('iron ore')
    result.append('bauxite')
    result.append('caterium ore')
    result.append('coal')
    result.append('copper ore')
    result.append('crude oil')
    result.append('packaged oil')
    result.append('limestone')
    result.append('raw quartz')
    result.append('S.A.M. ore')
    result.append('sulfur')
    result.append('uranium')
    result.append('water')
    result.append('packaged water')
    result.append('allen carapace')
    result.append('allen organs')
    result.append('flower petals')
    result.append('leaves')
    result.append('mycelia')
    result.append('green power slug')
    result.append('yellow power slug')
    result.append('purple power slug')
    result.append('wood')
    result.append('bacon agaric')
    result.append('beryl nut')
    result.append('paleberry')
    result.append('medical inhaler')
    result.append('biomass')
    result.append('cable')
    result.append('concrete')
    result.append('copper ingot')
    result.append('iron ingot')
    result.append('iron plate')
    result.append('iron rod')
    result.append('reinforced iron plate')
    result.append('screw')
    result.append('wire')
    result.append('copper sheet')
    result.append('solid biofuel')
    result.append('modular frame')
    result.append('rotor')
    result.append('smart plating')
    result.append('steel beam')
    result.append('steel ingot')
    result.append('steel pipe')
    result.append('versatile framework')
    result.append('automated wiring')
    result.append('encased industrial beam')
    result.append('heavy modular frame')
    result.append('motor')
    result.append('stator')
    result.append('adaptive control unit')
    result.append('circuit board')
    result.append('computer')
    result.append('empty canister')
    result.append('fuel')
    result.append('packaged fuel')
    result.append('heavy oil residue')
    result.append('packaged oil residue')
    result.append('liquid biofuel')
    result.append('packaged liquid biofuel')
    result.append('modular engine')
    result.append('petroleum coke')
    result.append('plastic')
    result.append('polymer resin')
    result.append('rubber')
    result.append('alumina solution')
    result.append('alclad aluminum sheet')
    result.append('aluminum ingot')
    result.append('aluminum scrap')
    result.append('battery')
    result.append('electromagnetic control rod')
    result.append('encased uranium cell')
    result.append('heat sink')
    result.append('beacon')
    result.append('nuclear fuel rod')
    result.append('nuclear waste')
    result.append('sulfuric acid')
    result.append('turbo motor')
    result.append('uranium pellet')
    result.append('A.I. limiter')
    result.append('black powder')
    result.append('caterium ingot')
    result.append('compacted coal')
    result.append('fabric')
    result.append('high-speed connector')
    result.append('quickwire')
    result.append('power shard')
    result.append('quartz crystal')
    result.append('silica')
    result.append('crystal oscillator')
    result.append('radio control unit')
    result.append('supercomputer')
    result.append('turbofuel')
    result.append('packaged turbofuel')
    return result