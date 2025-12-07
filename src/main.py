from src.simulator import run_simulator

def main() -> None:
    """The start point of the program"""
    run_simulator(int(input("Сколько шагов симуляции прогнать? ")))

if __name__ == "__main__":
    main()
