"""
  Nature For Water Facility - The Nature Conservancy
  -------------------------------------------------------------------------
  Python 3.11
  -------------------------------------------------------------------------
                            BASIC INFORMATION
 --------------------------------------------------------------------------
  Author        : Jonathan Nogales Pimentel
  Email         : jonathan.nogales@tnc.org
  Date          : January, 2025
  InVEST - Version 3.15.1 (update July 2025)
"""

# ----------------------------------------------------------------------------------------------------------------------
# Load libraries
# ----------------------------------------------------------------------------------------------------------------------
def main():
    import os
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    import sys
    import Spotpy_InVEST
    import threading

    # Clase para redirigir stdout y stderr al widget Text
    class ConsoleOutput:
        def __init__(self, text_widget):
            self.text_widget = text_widget
            self.text_widget.configure(state="disabled")

        def write(self, message):
            self.text_widget.configure(state="normal")
            self.text_widget.insert(tk.END, message)
            self.text_widget.see(tk.END)  # Auto-scroll hacia abajo
            self.text_widget.configure(state="disabled")

        def flush(self):
            pass  # Necesario para compatibilidad con sys.stdout

    # Función para crear directorio
    def create_folder(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    # Función para seleccionar directorio
    def select_folder(entry_field):
        filepath = filedialog.askdirectory()
        if filepath:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, filepath)
        validate_inputs()

    # Función para seleccionar archivo
    def select_file(entry_field):
        filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if filepath:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, filepath)
        validate_inputs()

    # Validar entradas y habilitar/deshabilitar botones
    def validate_inputs():
        if Edit_ProjectsPath.get() and MainFilePath.get():
            Button_RunCal.config(state="normal")
            Button_RunExe.config(state="normal")
        else:
            Button_RunCal.config(state="disabled")
            Button_RunExe.config(state="disabled")

    # Validar cantidad de simulaciones
    def validate_simulations():
        try:
            value = int(Nsim.get())
            if value > 1:
                return True
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "The number of simulations must be an integer greater than 1.")
            return False

    # Función para ejecutar el modelo en un hilo separado
    def run_calibration():
        try:
            # Llamar a la función de calibración
            Spotpy_InVEST.RunCalInVEST(
                Edit_ProjectsPath.get(),
                MainFilePath.get(),
                metric_combobox.get(),
                method_combobox.get(),
                Nsim.get()
            )
        except Exception as e:
            print(f"Error during calibration: {e}")

    # Función que inicia el hilo
    def start_calibration():
        validate_simulations()

        thread = threading.Thread(target=run_calibration)
        thread.daemon = True  # Permite que el hilo se cierre al cerrar la aplicación
        thread.start()

    # Función para ejecutar el modelo en un hilo separado
    def run_execution():
        try:
            # Llamar a la función de calibración
            Spotpy_InVEST.RunInVEST(
                Edit_ProjectsPath.get(),
                MainFilePath.get()
            )
        except Exception as e:
            print(f"Error during execution: {e}")

    # Función que inicia el hilo
    def start_execution():
        validate_simulations()

        thread = threading.Thread(target=run_execution)
        thread.daemon = True  # Permite que el hilo se cierre al cerrar la aplicación
        thread.start()

    # Crear la ventana principal de aplicación
    App = tk.Tk()
    App.title("InVEST's automatic calibration assistant ")

    # ----------------------------------------------------------------------------------------------------------------------
    # Módulo 1 - Select project path
    # ----------------------------------------------------------------------------------------------------------------------
    module1 = tk.LabelFrame(App, text="Select project path ")
    module1.pack(fill="x", padx=10, pady=5)

    Edit_ProjectsPath = tk.Entry(module1, width=80)
    Edit_ProjectsPath.pack(side="left", padx=5, pady=5)

    Button_OpenPath = tk.Button(module1, text="Select", width=20, command=lambda: select_folder(Edit_ProjectsPath))
    Button_OpenPath.pack(side="left", padx=5, pady=5)

    # ----------------------------------------------------------------------------------------------------------------------
    # Módulo 2 - Select InVEST Main File
    # ----------------------------------------------------------------------------------------------------------------------
    module2 = tk.LabelFrame(App, text="Select InVEST Main File (.xlsx) ")
    module2.pack(fill="x", padx=10, pady=5)

    MainFilePath = tk.Entry(module2, width=80)
    MainFilePath.pack(side="left", padx=5, pady=5)

    Button_OpenFile = tk.Button(module2, text="Select", width=20, command=lambda: select_file(MainFilePath))
    Button_OpenFile.pack(side="left", padx=5, pady=5)

    # ----------------------------------------------------------------------------------------------------------------------
    # Module 3 - Calibration InVEST Models
    # ----------------------------------------------------------------------------------------------------------------------
    module3 = tk.LabelFrame(App, text="Calibration InVEST Models ")
    module3.pack(fill="x", padx=10, pady=5)

    # Lista desplegable para métricas
    metric_label = tk.Label(module3, text="Select Metric:")
    metric_label.pack(side="left", padx=5, pady=5)

    metric_options = [
        "Mean Square Error (MSE)",
        "Mean Absolute Error (MAE)",
        "Root Mean Square Error (RMSE)",
        "Relative Root Mean Squared Error (RRMSE)"
    ]

    metric_combobox = ttk.Combobox(module3, values=metric_options, state="readonly", width=35)
    metric_combobox.pack(side="left", padx=5, pady=5)
    metric_combobox.set(metric_options[2])

    # Lista desplegable para métodos
    method_label = tk.Label(module3, text="Select Method:")
    method_label.pack(side="left", padx=5, pady=5)

    method_options = [
        "Dynamical dimensional search (DDS)",
        "Shuffled Complex Evolution (SCE-UA)",
        "Latin Hypercube Sampling (LHS)"
    ]

    method_combobox = ttk.Combobox(module3, values=method_options, state="readonly", width=30)
    method_combobox.pack(side="left", padx=5, pady=5)
    method_combobox.set(method_options[2])

    # ----------------------------------------------------------------------------------------------------------------------
    # Module 4 - Execution InVEST Models
    # ----------------------------------------------------------------------------------------------------------------------
    module4 = tk.LabelFrame(App, text="Execution InVEST Models ")
    module4.pack(fill="x", padx=10, pady=5)

    # Entrada para cantidad de simulaciones
    sim_label = tk.Label(module4, text="Simulation number")
    sim_label.pack(side="left", padx=5, pady=5)

    Nsim = tk.Entry(module4, width=10)
    Nsim.pack(side="left", padx=5, pady=5)
    Nsim.insert(0, 5)

    Button_RunCal = tk.Button(module4, text=" Calibration ", state="disabled", command=start_calibration)
    Button_RunCal.pack(side="left", padx=5, pady=5)

    Button_RunExe = tk.Button(module4, text=" Execution ", state="disabled", command=start_execution)
    Button_RunExe.pack(side="left", padx=5, pady=5)

    # ----------------------------------------------------------------------------------------------------------------------
    # Module 5 - Console Output
    # ----------------------------------------------------------------------------------------------------------------------
    module5 = tk.LabelFrame(App, text="Console Output")
    module5.pack(fill="both", expand=True, padx=10, pady=5)

    console_text = tk.Text(module5, wrap="word", height=15, bg="black", fg="white")
    console_text.pack(fill="both", expand=True, padx=5, pady=5)

    # Redirigir stdout y stderr al widget Text
    sys.stdout = ConsoleOutput(console_text)
    sys.stderr = ConsoleOutput(console_text)

    # Mensaje inicial
    print("Welcome to the InVEST's calibration assistant!")
    print("Logs will appear here.")

    App.mainloop()

# === Aquí va el bloque mágico para PyInstaller ===
if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()