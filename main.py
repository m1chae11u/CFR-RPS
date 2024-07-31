# main.py

from RPS_Solver import RPS_Solver

if __name__ == "__main__":
    solver = RPS_Solver()
    solver.train(1000000)  # Train for 1,000,000 iterations
    print(solver.getAverageStrategy())
    print(f"[rock, paper, scissors]")