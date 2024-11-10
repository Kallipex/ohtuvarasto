from varasto import Varasto

def eka(varasto1:Varasto, varasto2:Varasto):
    print("Luonnin jälkeen: Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.")
    print(f"Mehuvarasto: {varasto1}")
    print(f"Olutvarasto: {varasto2}")

    print("Olut getterit:")
    print(f"saldo = {varasto2.saldo}")
    print(f"tilavuus = {varasto2.tilavuus}")
    print(f"paljonko_mahtuu = {varasto2.paljonko_mahtuu()}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto1.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {varasto1}")
    print("Otetaan 3.14")
    varasto1.ota_varastosta(3.14)
    print(f"Mehuvarasto: {varasto1}")

def toka(varasto1:Varasto, varasto2:Varasto):
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    print(Varasto(-100.0))

    print("Varasto(100.0, -50.7)")
    print(Varasto(100.0, -50.7))

    print(f"Olutvarasto: {varasto2}")
    print("olutta.lisaa_varastoon(1000.0)")
    varasto2.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {varasto2}")

    print(f"Mehuvarasto: {varasto1}")
    print("mehua.lisaa_varastoon(-666.0)")
    varasto1.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {varasto1}")

def main():
    mehua, olutta = Varasto(100.0), Varasto(100.0, 20.2)

    eka(mehua, olutta)

    toka(mehua, olutta)

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
