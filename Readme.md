
# InVEST Calibration Assistant – User Guide

Welcome to the **InVEST Calibration Assistant**, a tool created to simplify the process of calibrating and validating hydrological and water quality models from the InVEST platform. Whether you're preparing your data for a single watershed or refining simulations across multiple catchments, this guide will walk you through every step to make the journey smooth, structured, and reproducible.

---

## 🌍 A Quick Overview

InVEST includes several environmental models, but the Calibration Assistant focuses on helping you configure and calibrate the following four (from version 3.15.1):

- Annual Water Yield (AWY)  
- Seasonal Water Yield (SWY)  
- Sediment Delivery Ratio (SDR)  
- Nutrient Delivery Ratio (NDR)  

Before going further: **only one model can be calibrated at a time**. Trying to activate multiple models will trigger an error—and no, it won’t explain itself nicely.

---

## 🚀 Two Ways to Use the Tool

### Option 1: Use the Precompiled `.exe`

No Python? No problem. For users who prefer to avoid setting up programming environments, a ready-to-use executable is included. Just double-click and follow the prompts—no installation needed.

### Option 2: Run the Python Source Code

For developers and advanced users, the assistant can be executed directly in Python. A Conda environment file is provided to simplify setup.

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) if you haven't yet.
2. Open a terminal and run:

```bash
conda env create -f Env_InVEST_Tool.yml
conda activate InVEST_Tool
```

You're now ready to explore or modify the source code as needed.

---

## 🗂️ Project Structure: Laying the Foundation

Every good model starts with organized data. Here’s how to structure your project:

- Create a main directory with all required input data.
- Refer to the `UserData` sheet in the Excel master file to see which files are needed for each model.
- For each model you want to calibrate, create a subfolder using the format: `Basin_Cal_[ModelName]` (e.g., `Basin_Cal_AWY`).
- In each folder, include a shapefile of your sub-watersheds, making sure it contains a field named `ws_id`.

This ID is essential. It links observed values to each sub-watershed during calibration.

---

## 🧾 Configuration File: The Control Center

Everything is managed from an Excel workbook. Here's how the sheets work:

### `UserData` Sheet

- Define the names of the required input files (no extensions).
- Fill in only the red-marked cells.
- Use `1` to activate calibration for a model, `0` to skip it.
- Reminder: only one model can be active per run.

### `Params` Sheet

- Set the minimum and maximum range for each parameter.
- To run a fixed-value simulation without calibration, fill in the `Value` column directly.
- After calibration, the assistant will overwrite this column with the optimized values.

### `Obs_Data` Sheet

- Add your observed data for each sub-watershed.
- Double-check that each `ws_id` matches what's in your shapefile.

---

## 🔬 Selective Calibration Using the Biophysical Table

Sometimes, not all land cover types should be adjusted equally. That’s where the `Status_` fields in the biophysical table come in.

Each column beginning with `Status_` followed by a parameter name (e.g., `Status_CN`) defines where calibration should apply:

- A value of `1` means the multiplier will be applied.
- A value of `0` leaves the parameter untouched.

This gives you the flexibility to calibrate only the land covers that matter most—like agriculture or grasslands—while excluding others like urban zones or water bodies.

---

## 🧪 Included Sample Dataset: Dummy_InVEST.zip

To help you get started, the repository includes a package named `Dummy_InVEST.zip`. This dataset contains:

- Raster files
- A pre-filled biophysical table
- Shapefiles with the required `ws_id` field
- A complete folder structure for each model
- A working Excel configuration file

Use it to explore how everything works, test the tool, or as a base for your own project setup.

---

## ⚙️ Practical Recommendations

- Use the same coordinate system across all shapefiles and raster layers.
- Choose a pixel size appropriate to your watershed size. Large basins = coarser pixels.
- Always close the Excel file before running the tool. An open file can silently block updates, leading to incomplete or lost outputs.

---

## 🧼 Recalibration & File Management

Each time you run a calibration, results are stored in the `PARAMETERS` and `EVALUATIONS` folders. These files accumulate over time.

Before starting a new calibration for the same model:

- Delete previous output files for that model.
- Failing to do so can mix old and new results, creating misleading outcomes and invalid parameter sets.

---

## 🧠 Additional Guidance

- **Plan Ahead**: Calibrations can take time. Allocate enough resources.
- **Check Everything**: Input completeness and format correctness are essential.
- **Version Control**: Keep backup copies of your original data and parameters.
- **Model Limits**: The tool is designed to work with the four listed models only.

---

## 🤝 Contributing

The InVEST Calibration Assistant is open for collaboration. Contributions, bug reports, and feature suggestions are welcome. Please use pull requests and issues to interact with the maintainers.

Make sure to document any code changes and test thoroughly before submitting.

---

This assistant was built to support reproducible, flexible, and efficient calibration workflows. Whether you're a modeler, researcher, or practitioner, the goal is to reduce manual overhead and improve the quality of your simulations.

Start simple. Build confidently. Calibrate wisely.
