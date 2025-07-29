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
    import customtkinter as ctk
    from tkinter import filedialog, messagebox
    import sys
    import Spotpy_InVEST
    import threading

    # Configuración del tema y apariencia
    ctk.set_appearance_mode("light")  # Modo claro para estilo Notion
    ctk.set_default_color_theme("blue")

    # Colores personalizados estilo Notion con tonos pasteles sobrios
    COLORS = {
        'bg_primary': '#FAFAFA',      # Fondo principal muy suave
        'bg_secondary': '#F5F5F7',    # Fondo secundario
        'bg_card': '#FFFFFF',         # Fondo de tarjetas
        'accent_blue': '#4F46E5',     # Azul más vibrante
        'accent_green': '#059669',    # Verde más intenso
        'accent_purple': '#7C3AED',   # Púrpura más vibrante
        'text_primary': '#1F2937',    # Texto principal más oscuro
        'text_secondary': '#6B7280',  # Texto secundario
        'border': '#E5E7EB',         # Bordes suaves
        'hover': '#F3F4F6',          # Estado hover
        'button_text': '#FFFFFF',     # Texto de botones en blanco
        'console_bg': '#0F172A',      # Fondo terminal oscuro
        'console_text': '#E2E8F0',    # Texto principal terminal
        'console_success': '#10B981', # Verde para éxito
        'console_error': '#EF4444',   # Rojo para errores
        'console_warning': '#F59E0B', # Amarillo para advertencias
        'console_info': '#3B82F6',    # Azul para información
        'console_accent': '#8B5CF6'   # Púrpura para acentos
    }

    # Clase para redirigir stdout y stderr al widget Text con colores simulados
    class ConsoleOutput:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.configure(state="normal")

            # Como CTkTextbox no soporta colores nativamente, usamos emojis y formato
            formatted_message = self._format_message(message)
            self.text_widget.insert("end", formatted_message)
            self.text_widget.see("end")
            self.text_widget.configure(state="disabled")

        def _format_message(self, message):
            # Formatear mensajes con símbolos y estructura visual
            if "ERROR" in message.upper() or "Exception" in message or "❌" in message:
                return f"🔴 {message}"
            elif "WARNING" in message.upper() or "WARN" in message.upper() or "⚠️" in message:
                return f"🟡 {message}"
            elif "SUCCESS" in message.upper() or "✅" in message:
                return f"🟢 {message}"
            elif "INFO" in message.upper() or "ℹ️" in message or "📌" in message:
                return f"🔵 {message}"
            elif "━" in message or "=" in message:
                return f"🟣 {message}"
            else:
                return message

        def flush(self):
            pass

    # Función para crear directorio
    def create_folder(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    # Función para seleccionar directorio
    def select_folder(entry_field):
        filepath = filedialog.askdirectory()
        if filepath:
            entry_field.delete(0, "end")
            entry_field.insert(0, filepath)
        validate_inputs()

    # Función para seleccionar archivo
    def select_file(entry_field):
        filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if filepath:
            entry_field.delete(0, "end")
            entry_field.insert(0, filepath)
        validate_inputs()

    # Validar entradas y habilitar/deshabilitar botones
    def validate_inputs():
        if edit_projects_path.get() and main_file_path.get():
            button_run_cal.configure(state="normal")
            button_run_exe.configure(state="normal")
        else:
            button_run_cal.configure(state="disabled")
            button_run_exe.configure(state="disabled")

    # Validar cantidad de simulaciones
    def validate_simulations():
        try:
            value = int(nsim_entry.get())
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
            log_info("Starting calibration process...")
            log_info(f"Project path: {edit_projects_path.get()}")
            log_info(f"Configuration file: {main_file_path.get()}")
            log_info(f"Metric: {metric_combobox.get()}")
            log_info(f"Method: {method_combobox.get()}")
            log_info(f"Simulations: {nsim_entry.get()}")
            print("━" * 60)

            Spotpy_InVEST.RunCalInVEST(
                edit_projects_path.get(),
                main_file_path.get(),
                metric_combobox.get(),
                method_combobox.get(),
                nsim_entry.get()
            )
            print("━" * 60)
            log_success("Calibration completed successfully!")
        except Exception as e:
            print("━" * 60)
            log_error(f"Calibration failed: {str(e)}")
            print("━" * 60)

    # Función que inicia el hilo
    def start_calibration():
        if validate_simulations():
            thread = threading.Thread(target=run_calibration)
            thread.daemon = True
            thread.start()

    # Función para ejecutar el modelo en un hilo separado
    def run_execution():
        try:
            log_info("Starting execution process...")
            log_info(f"Project path: {edit_projects_path.get()}")
            log_info(f"Configuration file: {main_file_path.get()}")
            print("━" * 60)

            Spotpy_InVEST.RunInVEST(
                edit_projects_path.get(),
                main_file_path.get()
            )
            print("━" * 60)
            log_success("Execution completed successfully!")
        except Exception as e:
            print("━" * 60)
            log_error(f"Execution failed: {str(e)}")
            print("━" * 60)

    # Función que inicia el hilo
    def start_execution():
        if validate_simulations():
            thread = threading.Thread(target=run_execution)
            thread.daemon = True
            thread.start()

    # Crear la ventana principal
    app = ctk.CTk()
    app.title("InVEST Calibration Assistant")
    app.geometry("700x850")
    app.configure(fg_color=COLORS['bg_primary'])

    # Frame principal con scroll
    main_scroll = ctk.CTkScrollableFrame(
        app,
        fg_color=COLORS['bg_primary'],
        scrollbar_button_color=COLORS['accent_blue'],
        scrollbar_button_hover_color=COLORS['accent_purple']
    )
    main_scroll.pack(fill="both", expand=True, padx=15, pady=15)

    # Título principal con estilo elegante
    title_frame = ctk.CTkFrame(main_scroll, fg_color="transparent")
    title_frame.pack(fill="x", pady=(0, 15))

    title_label = ctk.CTkLabel(
        title_frame,
        text="🌊 InVEST Calibration Assistant",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color=COLORS['text_primary']
    )
    title_label.pack()

    subtitle_label = ctk.CTkLabel(
        title_frame,
        text="Nature For Water Facility - The Nature Conservancy",
        font=ctk.CTkFont(size=12),
        text_color=COLORS['text_secondary']
    )
    subtitle_label.pack(pady=(3, 0))

    # ----------------------------------------------------------------------------------------------------------------------
    # Módulo 1 - Select project path
    # ----------------------------------------------------------------------------------------------------------------------
    module1 = ctk.CTkFrame(
        main_scroll,
        fg_color=COLORS['bg_card'],
        border_width=1,
        border_color=COLORS['border'],
        corner_radius=12
    )
    module1.pack(fill="x", pady=(0, 12))

    module1_title = ctk.CTkLabel(
        module1,
        text="📁 Project Directory",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color=COLORS['text_primary']
    )
    module1_title.pack(anchor="w", padx=15, pady=(15, 8))

    path_frame = ctk.CTkFrame(module1, fg_color="transparent")
    path_frame.pack(fill="x", padx=15, pady=(0, 15))

    edit_projects_path = ctk.CTkEntry(
        path_frame,
        placeholder_text="Select your project directory...",
        height=35,
        font=ctk.CTkFont(size=11),
        fg_color=COLORS['bg_secondary'],
        border_color=COLORS['border'],
        corner_radius=6
    )
    edit_projects_path.pack(side="left", fill="x", expand=True, padx=(0, 8))

    button_open_path = ctk.CTkButton(
        path_frame,
        text="Browse",
        width=80,
        height=35,
        font=ctk.CTkFont(size=11, weight="bold"),
        fg_color=COLORS['accent_blue'],
        hover_color=COLORS['accent_purple'],
        text_color=COLORS['button_text'],
        corner_radius=6,
        command=lambda: select_folder(edit_projects_path)
    )
    button_open_path.pack(side="right")

    # ----------------------------------------------------------------------------------------------------------------------
    # Módulo 2 - Select InVEST Main File
    # ----------------------------------------------------------------------------------------------------------------------
    module2 = ctk.CTkFrame(
        main_scroll,
        fg_color=COLORS['bg_card'],
        border_width=1,
        border_color=COLORS['border'],
        corner_radius=12
    )
    module2.pack(fill="x", pady=(0, 12))

    module2_title = ctk.CTkLabel(
        module2,
        text="📊 InVEST Configuration File",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color=COLORS['text_primary']
    )
    module2_title.pack(anchor="w", padx=15, pady=(15, 8))

    file_frame = ctk.CTkFrame(module2, fg_color="transparent")
    file_frame.pack(fill="x", padx=15, pady=(0, 15))

    main_file_path = ctk.CTkEntry(
        file_frame,
        placeholder_text="Select your Excel configuration file (.xlsx)...",
        height=35,
        font=ctk.CTkFont(size=11),
        fg_color=COLORS['bg_secondary'],
        border_color=COLORS['border'],
        corner_radius=6
    )
    main_file_path.pack(side="left", fill="x", expand=True, padx=(0, 8))

    button_open_file = ctk.CTkButton(
        file_frame,
        text="Browse",
        width=80,
        height=35,
        font=ctk.CTkFont(size=11, weight="bold"),
        fg_color=COLORS['accent_blue'],
        hover_color=COLORS['accent_purple'],
        text_color=COLORS['button_text'],
        corner_radius=6,
        command=lambda: select_file(main_file_path)
    )
    button_open_file.pack(side="right")

    # ----------------------------------------------------------------------------------------------------------------------
    # Module 3 - Calibration Settings
    # ----------------------------------------------------------------------------------------------------------------------
    module3 = ctk.CTkFrame(
        main_scroll,
        fg_color=COLORS['bg_card'],
        border_width=1,
        border_color=COLORS['border'],
        corner_radius=12
    )
    module3.pack(fill="x", pady=(0, 12))

    module3_title = ctk.CTkLabel(
        module3,
        text="⚙️ Calibration Settings",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color=COLORS['text_primary']
    )
    module3_title.pack(anchor="w", padx=15, pady=(15, 10))

    # Grid para organizar los controles
    controls_frame = ctk.CTkFrame(module3, fg_color="transparent")
    controls_frame.pack(fill="x", padx=15, pady=(0, 15))

    # Metric selection
    metric_label = ctk.CTkLabel(
        controls_frame,
        text="Evaluation Metric",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=COLORS['text_primary']
    )
    metric_label.grid(row=0, column=0, sticky="w", padx=(0, 15), pady=(0, 4))

    metric_options = [
        "Mean Square Error (MSE)",
        "Mean Absolute Error (MAE)",
        "Root Mean Square Error (RMSE)",
        "Relative Root Mean Squared Error (RRMSE)"
    ]

    metric_combobox = ctk.CTkComboBox(
        controls_frame,
        values=metric_options,
        state="readonly",
        width=250,
        height=30,
        font=ctk.CTkFont(size=11),
        fg_color=COLORS['bg_secondary'],
        button_color=COLORS['accent_blue'],
        button_hover_color=COLORS['accent_purple'],
        dropdown_fg_color=COLORS['bg_card'],
        dropdown_hover_color=COLORS['hover'],
        dropdown_text_color=COLORS['text_primary'],
        text_color=COLORS['text_primary'],
        border_color=COLORS['border'],
        corner_radius=6
    )
    metric_combobox.grid(row=1, column=0, sticky="w", padx=(0, 15), pady=(0, 10))
    metric_combobox.set(metric_options[2])

    # Method selection
    method_label = ctk.CTkLabel(
        controls_frame,
        text="Optimization Method",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=COLORS['text_primary']
    )
    method_label.grid(row=0, column=1, sticky="w", pady=(0, 4))

    method_options = [
        "Dynamical dimensional search (DDS)",
        "Shuffled Complex Evolution (SCE-UA)",
        "Latin Hypercube Sampling (LHS)"
    ]

    method_combobox = ctk.CTkComboBox(
        controls_frame,
        values=method_options,
        state="readonly",
        width=250,
        height=30,
        font=ctk.CTkFont(size=11),
        fg_color=COLORS['bg_secondary'],
        button_color=COLORS['accent_blue'],
        button_hover_color=COLORS['accent_purple'],
        dropdown_fg_color=COLORS['bg_card'],
        dropdown_hover_color=COLORS['hover'],
        dropdown_text_color=COLORS['text_primary'],
        text_color=COLORS['text_primary'],
        border_color=COLORS['border'],
        corner_radius=6
    )
    method_combobox.grid(row=1, column=1, sticky="w", pady=(0, 10))
    method_combobox.set(method_options[2])

    # Configure grid weights
    controls_frame.grid_columnconfigure(0, weight=1)
    controls_frame.grid_columnconfigure(1, weight=1)

    # ----------------------------------------------------------------------------------------------------------------------
    # Module 4 - Execution Controls
    # ----------------------------------------------------------------------------------------------------------------------
    module4 = ctk.CTkFrame(
        main_scroll,
        fg_color=COLORS['bg_card'],
        border_width=1,
        border_color=COLORS['border'],
        corner_radius=12
    )
    module4.pack(fill="x", pady=(0, 12))

    module4_title = ctk.CTkLabel(
        module4,
        text="🚀 Execution Controls",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color=COLORS['text_primary']
    )
    module4_title.pack(anchor="w", padx=15, pady=(15, 10))

    execution_frame = ctk.CTkFrame(module4, fg_color="transparent")
    execution_frame.pack(fill="x", padx=15, pady=(0, 15))

    # Crear un frame horizontal para organizar entrada y botones
    horizontal_frame = ctk.CTkFrame(execution_frame, fg_color="transparent")
    horizontal_frame.pack(fill="x")

    # Simulation number
    sim_label = ctk.CTkLabel(
        horizontal_frame,
        text="Number of Simulations",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=COLORS['text_primary']
    )
    sim_label.pack(side="left", padx=(0, 10))

    nsim_entry = ctk.CTkEntry(
        horizontal_frame,
        placeholder_text="5",
        width=80,
        height=38,
        font=ctk.CTkFont(size=11),
        fg_color=COLORS['bg_secondary'],
        border_color=COLORS['border'],
        corner_radius=6
    )
    nsim_entry.pack(side="left", padx=(0, 20))
    nsim_entry.insert(0, "5")

    # Buttons en la misma línea
    button_run_cal = ctk.CTkButton(
        horizontal_frame,
        text="🔧 Start Calibration",
        width=140,
        height=38,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=COLORS['accent_green'],
        hover_color="#047857",
        text_color=COLORS['button_text'],
        corner_radius=6,
        state="disabled",
        command=start_calibration
    )
    button_run_cal.pack(side="left", padx=(0, 10))

    button_run_exe = ctk.CTkButton(
        horizontal_frame,
        text="▶️ Run Execution",
        width=140,
        height=38,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=COLORS['accent_purple'],
        hover_color="#6D28D9",
        text_color=COLORS['button_text'],
        corner_radius=6,
        state="disabled",
        command=start_execution
    )
    button_run_exe.pack(side="left")

    # ----------------------------------------------------------------------------------------------------------------------
    # Module 5 - Console Output
    # ----------------------------------------------------------------------------------------------------------------------
    module5 = ctk.CTkFrame(
        main_scroll,
        fg_color=COLORS['bg_card'],
        border_width=1,
        border_color=COLORS['border'],
        corner_radius=12
    )
    module5.pack(fill="both", expand=True)

    module5_title = ctk.CTkLabel(
        module5,
        text="📋 Console Output",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color=COLORS['text_primary']
    )
    module5_title.pack(anchor="w", padx=15, pady=(15, 8))

    console_text = ctk.CTkTextbox(
        module5,
        height=150,
        font=ctk.CTkFont(family="Consolas", size=10),
        fg_color=COLORS['console_bg'],
        text_color=COLORS['console_text'],
        corner_radius=6,
        scrollbar_button_color=COLORS['accent_blue']
    )
    console_text.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    # Redirigir stdout y stderr al widget Text
    sys.stdout = ConsoleOutput(console_text)
    sys.stderr = ConsoleOutput(console_text)

    # Función mejorada para logs con emojis y formato visual
    def log_info(message):
        print(f"ℹ️  INFO: {message}")

    def log_success(message):
        print(f"✅ SUCCESS: {message}")

    def log_warning(message):
        print(f"⚠️  WARNING: {message}")

    def log_error(message):
        print(f"❌ ERROR: {message}")

    # Mensaje inicial con estilo visual mejorado
    print("🌊 Welcome to the InVEST Calibration Assistant!")
    print("━" * 50)
    log_success("System initialized successfully")
    log_info("Please select your project directory and configuration file")
    print("")
    log_info("Console Legend:")
    print("   🔴 Errors  🟡 Warnings  🟢 Success  🔵 Info  🟣 Separators")
    print("━" * 50)

    # Validar inputs inicialmente
    validate_inputs()

    app.mainloop()

# === Bloque mágico para PyInstaller ===
if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()