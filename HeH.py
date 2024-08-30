from qiskit_ibm_runtime import Session
from scipy.optimize import minimize

def run_optimization():
    try:
        with Session(backend=backend) as session:
            estimator = Estimator(session=session)
            estimator.options.default_shots = 1000

            res = minimize(
                cost_func,
                x0,
                args=(ansatz_isa, hamiltonian_isa, estimator),
                method="cobyla",
            )
            return res
    except Exception as e:
        print(f"An error occurred: {e}")
        if "Session has been closed" in str(e):
            print("Restarting the session and retrying...")
            return run_optimization()

result = run_optimization()
